# GitHub Automation with Claude

For engineers responsible for extending, debugging, or operating the GitHub workflows. The main OCS project has similar workflows, see [the developer guide on GitHub automation with Claude](https://developers.openchatstudio.com/developer_guides/claude_github_automation/).

These workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to run [Claude Code inside GitHub Actions](https://code.claude.com/docs/en/github-actions). If you're writing or reviewing one of these workflows, start from [AGENTS.md](AGENTS.md) in this directory.

## GitHub workflows

Triggers, required secrets, and concurrency behavior are documented in each workflow's own header comment — this table is an index and a pointer to what each one delegates to, not the source of truth for how it runs.

Commands live in `.claude/commands/`, agents in `.claude/agents/` ([background](https://docs.anthropic.com/en/docs/claude-code/sub-agents)).

| File | Actions UI name | Purpose | Command / Instruction Spec | Subagent |
|---|---|---|---|---|
| `claude.yml` | Claude Code | Freeform `@claude` assistant for issue/PR conversations | none — freeform prompt taken from the mention itself | none |
| `claude-dependabot.yml` | Claude Dependabot PR Review | Flags breaking changes / build impact in Dependabot PRs | none — freeform inline prompt in the workflow | none |
| `claude-review.yml` | PR Review | Automated documentation review on PRs (skips Dependabot PRs and PRs labelled `automated`) | [`/review-pr`](../../.claude/commands/review-pr.md) | [`documentation-pr-reviewer`](../../.claude/agents/documentation-pr-reviewer.md) |
| `release.yml` | Weekly Release Summary | Drafts a GitHub release from the changelog | [`/create-release <tag> <title>`](../../.claude/commands/create-release.md) | none — the command does the work itself |
| `update-changelog.yml` | Update Changelog and Docs from OCS PR | Syncs changelog/docs from merged OCS PRs — see [README-changelog-automation.md](README-changelog-automation.md) | [`changelog-instructions.md`](../templates/changelog-instructions.md) rendered into the workflow's `prompt:` | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |
| *(manual only, no workflow)* | — | Ad-hoc docs writing outside any workflow | [`/write-docs`](../../.claude/commands/write-docs.md) | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |

## Security: Permissions & Tool Allowlists

These workflows use `permissions:` block, Claude's `--allowedTools`, and an installation access token for the `ocs-agent` GitHub App. See best practices for using them in [AGENTS.md](AGENTS.md) in this directory.

### Command and agent tool frontmatter

The commands and subagents in the table carry their own tool frontmatter in their `.md` files, and the two kinds behave differently:

- A Claude subagent's `tools:` ([reference](https://code.claude.com/docs/en/sub-agents)) is the flag for restricting tool availability. Omitting `tools:` inherits every tool available to subagents, so a subagent meant to be narrow has to list them explicitly.
- A Claude command's `allowed-tools:` ([reference](https://code.claude.com/docs/en/skills#frontmatter-reference)) lists tools that run without a permission prompt. It does not restrict which tools are available. Keep it no wider than the workflow grant to Claude via `claude_args`.

When adding or changing a command or agent, check that the workflow's `claude_args` still covers what it needs. A tool an agent's `tools:` names that neither the action's base set nor `claude_args` covers is dead on arrival, and shows up as a silently truncated result rather than an error — see [Troubleshooting](#troubleshooting).

## GitHub labels used by these workflows

The `automated` label exists so bot-authored docs PRs don't loop back into the AI review in `claude-review.yml`. It's applied by both `update-changelog.yml` and the unrelated, non-Claude `update-api-docs.yml` — removing the label from a PR created by either one makes it eligible for the AI review.

## Fork Limitations

Engineers contributing from a fork may trigger these workflows by opening a pull request (or commenting on one) against this repo.

GitHub gives a `pull_request` run from a fork no secrets and a read-only `permissions` block, whatever the workflow declares. So `ANTHROPIC_API_KEY` is empty and `id-token: write` is never granted — don't design a workflow around either being present on a fork PR.

- **`claude-review.yml`** is `pull_request`-triggered. A PR from a fork fails because the Claude Code Action cannot obtain an OIDC token.
- **`claude.yml`** is not `pull_request`-triggered (it fires on comments, reviews, and issues), but it fails via `claude-code-action`'s own actor check unless the user has write access to this repo.

`claude-dependabot.yml`, `release.yml`, and `update-changelog.yml` aren't meant to be reused on a forked repo — they're wired to this repo's own release process and to the OCS repo's changelog dispatch.

## Troubleshooting

Issues that can show up on any of these workflows. For workflow-specific troubleshooting, see that workflow's own doc (e.g. [README-changelog-automation.md](README-changelog-automation.md#troubleshooting) for `update-changelog.yml`).

- **Run fails immediately in the `claude-code-action` step for forked repos:** See [Fork Limitations](#fork-limitations) above.
- **Output looks incomplete, or a step Claude should have taken didn't happen:** A denied tool call doesn't fail the run — it's silently skipped and Claude continues without it. Check the run transcript for denied calls; that's the usual cause of a truncated-looking result.
- **Authentication or permission failures:** Verify `ANTHROPIC_API_KEY` is valid. If the workflow uses the `ocs-agent` GitHub App (check its header comment), also verify the GitHub app's private key matches `OCS_AGENT_PRIVATE_KEY` and the app is still installed on the relevant repo(s) — token minting fails if either repo is missing from the installation.
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant command or agent in `.claude/commands/` / `.claude/agents/` rather than correcting each PR manually.
