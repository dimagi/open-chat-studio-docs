# GitHub Automation with Claude

For engineers responsible for extending, debugging, or operating the GitHub workflows on this user documentation repo. The main OCS project has similar workflows, see [the developer guide on GitHub automation with Claude](https://developers.openchatstudio.com/developer_guides/claude_github_automation/).

These workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to run Claude Code inside GitHub Actions. Each run gives Claude access to the repository, a shell, and the GitHub CLI.

## GitHub workflows

Triggers, required secrets, and concurrency/permission behavior are documented in each
workflow's own header comment — this table is an index and a pointer to what each one
delegates to, not the source of truth for how it runs.

Commands live in `.claude/commands/`, agents in `.claude/agents/` ([background](https://docs.anthropic.com/en/docs/claude-code/sub-agents)).

| File | Actions UI name | Purpose | Command / Instruction Spec | Subagent |
|---|---|---|---|---|
| `claude.yml` | Claude Code | Freeform `@claude` assistant for issue/PR conversations | none — freeform prompt taken from the mention itself | none |
| `claude-dependabot.yml` | Claude Dependabot PR Review | Flags breaking changes / build impact in Dependabot PRs | none — freeform inline prompt in the workflow | none |
| `claude-review.yml` | PR Review | Automated documentation review on PRs (skips Dependabot PRs and PRs labelled `automated`) | [`/review-pr`](../../.claude/commands/review-pr.md) | [`documentation-pr-reviewer`](../../.claude/agents/documentation-pr-reviewer.md) |
| `release.yml` | Weekly Release Summary | Drafts a GitHub release from the changelog | [`/create-release <tag> <title>`](../../.claude/commands/create-release.md) | none — the command does the work itself |
| `update-changelog.yml` | Update Changelog and Docs from OCS PR | Syncs changelog/docs from merged OCS PRs — see [README-changelog-automation.md](README-changelog-automation.md) | [`changelog-instructions.md`](../templates/changelog-instructions.md) rendered into the workflow's `prompt:` | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |
| *(manual only, no workflow)* | — | Ad-hoc docs writing outside any workflow | [`/write-docs`](../../.claude/commands/write-docs.md) | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |

## Secrets

Requirements differ per workflow. Check the `Requirements:` line in each workflow file's header comment.

## Security: Permissions & Tool Allowlists

Two independent mechanisms combine to shape a workflow's run:

- `--allowedTools` in `claude_args`, which controls what Claude itself will attempt to invoke.
- The `permissions:` block, which controls what the job's `GITHUB_TOKEN` can actually reach on GitHub — including when Claude's own `gh`/git calls use it.

### How it works

**`permissions:`** These can be **bypassed** in a workflow when the `ocs-agent` GitHub App (check each workflow's header for which ones) mints a short-lived installation token. That token's write capabilities come from the App's own permission grant (org Settings → GitHub Apps), **not** from the workflow's `permissions:` block. So any action that uses the `ocs-agent` will have the PRs and comments attributed to `ocs-agent[bot]`.

**`--allowedTools`** — Claude Code itself is only launched with the `--allowedTools` value set in the workflow's `claude_args`; that's what's enforced at run time. Commands (`.claude/commands/`) and agents (`.claude/agents/`) can declare their own `allowed-tools:` / `tools:` frontmatter, but that never expands what Claude is actually allowed to use: a tool missing from the workflow's `claude_args` stays unusable no matter what a command or agent claims to need. (That frontmatter still governs what's available if the command is ever run manually, outside its workflow.)

See [claude-code-action's security docs](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) and the [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) for how these actually behave.

### Gotchas & checklist

Getting either mechanism wrong is the main way a compromised or malicious prompt (for example, a hostile issue or PR body) could take unintended action — treat changes to permissions and tool allowlists as security-sensitive.

- **Adding or changing a command/agent?** Check that the `--allowedTools` set in the workflow's `claude_args` still covers what it actually needs. For example, `documentation-pr-reviewer`'s `tools:` frontmatter lists `WebFetch`/`WebSearch` for link-checking, but neither `claude-review.yml` nor `review-pr.md` grants them — so that capability is currently dead in that pipeline.
- **Adding or changing a `permissions:` block?** Trace whether each scope is actually consumed by the default `GITHUB_TOKEN` — don't assume it is. A step that passes its own `token:`/`github_token:`/`GH_TOKEN:` (e.g. the `ocs-agent` app token) never touches the job's `permissions:`-governed default token for that call. `token:` is easy to miss: it's the key `actions/checkout` and `peter-evans/create-pull-request` use.
- **Output looks incomplete, or a step Claude should have taken didn't happen?** A denied tool call doesn't fail the run — it's silently skipped and Claude continues without it. Check the run transcript for denied tool calls; that's the usual cause of a truncated-looking result.

## GitHub labels used by these workflows

The `automated` label exists so bot-authored docs PRs don't loop back into the AI review in `claude-review.yml`. It's applied by both `update-changelog.yml` and the unrelated, non-Claude `update-api-docs.yml` — removing the label from a PR created by either one makes it eligible for the AI review.

## Fork Limitations

Engineers contributing from a fork may trigger these workflows by opening a pull request (or commenting on one) against this repo.

- **`claude-review.yml`** is `pull_request`-triggered. A PR from a fork fails because the Claude Code Action cannot obtain an OIDC token.
- **`claude.yml`** While this is not `pull_request`-triggered (it fires on comments, reviews, and issues), it fails via `claude-code-action`'s own actor check unless the user has write access to this repo.

`claude-dependabot.yml`, `release.yml`, and `update-changelog.yml` aren't meant to be reused on a forked repo — they're wired to this repo's own release process and to the OCS repo's changelog dispatch.

## Troubleshooting

Issues that can show up on any of these workflows. For workflow-specific troubleshooting, see that workflow's own doc (e.g. [README-changelog-automation.md](README-changelog-automation.md#troubleshooting) for `update-changelog.yml`).

- **Run fails immediately in the `claude-code-action` step for forked repos:** See [Fork Limitations](#fork-limitations) above.
- **Output looks incomplete, or a step Claude should have taken didn't happen:** Check the run transcript for denied tool calls — see [Gotchas & checklist](#gotchas--checklist).
- **Authentication or permission failures:** Verify `ANTHROPIC_API_KEY` is valid. If the workflow uses the `ocs-agent` app (check its header comment), also verify the GitHub app's private key matches `OCS_AGENT_PRIVATE_KEY` and the app is still installed on the relevant repo(s) — token minting fails if either repo is missing from the installation.
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant command or agent in `.claude/commands/` / `.claude/agents/` rather than correcting each PR manually.
