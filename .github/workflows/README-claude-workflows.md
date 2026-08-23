# GitHub Automation with Claude

For engineers responsible for extending, debugging, or operating the GitHub workflows on this user documentation repo. The main OCS project has similar workflows, see [the developer guide on GitHub automation with Claude]](https://developers.openchatstudio.com/developer_guides/claude_github_automation/).

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
| `claude-review.yml` | PR Review | Automated documentation review on every PR | [`/review-pr`](../../.claude/commands/review-pr.md) | [`documentation-pr-reviewer`](../../.claude/agents/documentation-pr-reviewer.md) |
| `release.yml` | Weekly Release Summary | Drafts a GitHub release from the changelog | [`/create-release <tag> <title>`](../../.claude/commands/create-release.md) | none — the command does the work itself |
| `update-changelog.yml` | Update Changelog and Docs from OCS PR | Syncs changelog/docs from merged OCS PRs — see [README-changelog-automation.md](README-changelog-automation.md) | [`changelog-instructions.md`](../templates/changelog-instructions.md) rendered into the workflow's `prompt:` | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |
| *(manual only, no workflow)* | — | Ad-hoc docs writing outside any workflow | [`/write-docs`](../../.claude/commands/write-docs.md) | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) |

## Required secrets and permissions

Secret requirements differ per workflow — check the Requirements: line in each workflow file's header comment.

- **`OCS_AGENT_PRIVATE_KEY`** (secret) and **`OCS_AGENT_APP_ID`** (variable): credentials for
  the `ocs-agent` GitHub App (org Settings → GitHub Apps). The GitHub app must be installed on the repo with contents, issues, and pull request write permissions.
- Workflows mint a short-lived installation token from these, so the PR itself and any
  `gh pr`/`gh issue` comments are attributed to `ocs-agent[bot]`.
- The token's actual write capabilities come from the GitHub App's own permission grant, not from any workflow's `permissions:` block — which only governs the default `GITHUB_TOKEN` and is bypassed wherever the app token is used instead.

Two independent mechanisms scope what Claude can do in every run: the `permissions:` block (what the `GITHUB_TOKEN` can access) and `--allowedTools` in `claude_args` (which tools **run without a prompt for permission**). Getting either wrong is the main way a compromised or malicious prompt — e.g. a hostile issue/PR body — could take unintended action, so treat changes to them as security-sensitive. See [claude-code-action's security docs](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) and the [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) for how they actually behave.

Every workflow passes `--allowedTools` in `claude_args` directly — that's what's enforced. Some workflows invoke a command with its own `allowed-tools:` frontmatter (e.g. `.claude/commands/create-release.md`), and some of those commands launch a subagent via `Task` with its own `tools:` frontmatter (e.g. `documentation-pr-reviewer`).

None of these further declarations expand what's enforced — only the workflow's `--allowedTools` does — so a tool named further down the chain but missing from the workflow's list is simply unusable there, no matter what the command or agent frontmatter claims. Keep all of these in sync: right now `documentation-pr-reviewer`'s `tools:` includes `WebFetch`/`WebSearch` for link-checking, but neither `claude-review.yml` nor `review-pr.md` grants them, so that capability is currently dead when the agent runs through this pipeline. The command frontmatter is also what governs if a command is ever run manually/interactively outside its workflow.

> [!WARNING]
> If Claude tries to use a tool that isn't permitted, that call is denied and it continues without it — **the run won't fail**. A missing tool usually surfaces as an **incomplete result rather than an error**, so check the run transcript for denied tool calls if the output looks truncated.

## GitHub labels used by these workflows

The `automated` label exists so bot-authored docs PRs don't loop back into the AI review in `claude-review.yml`. It's applied by the workflow that opens each such PR, not by Claude, and removing the label makes that PR eligible for review again.

See the relevant workflow's header comment for exactly how and when it sets the label.

## Forked Repos

A PR from a forked repo runs its `pull_request`-triggered workflows with a read-only `GITHUB_TOKEN` and no access to this repo's Actions secrets.

Of the workflows above, `claude-dependabot.yml` and `claude-review.yml` are `pull_request`-triggered and therefore affected: the job still starts, but fails inside the `claude-code-action` step once it tries to authenticate — it isn't skipped. The comment/review/issue-triggered `claude.yml`, and the schedule/dispatch-triggered `release.yml` and `update-changelog.yml`, are unaffected — those always run in the base repo's context with full secrets access, regardless of any PR's origin.

## Troubleshooting

Issues that can show up on any of these workflows. For workflow-specific troubleshooting, see that workflow's own doc (e.g. [README-changelog-automation.md](README-changelog-automation.md#troubleshooting) for `update-changelog.yml`).

- **Run fails immediately in the `claude-code-action` step on a `pull_request`-triggered workflow:** Expected if the PR is from a forked repo — see Forked Repos above.
- **Output looks incomplete, or a step Claude should have taken didn't happen:** Check the run transcript for denied tool calls — see Tool Allowlist above.
- **Authentication or permission failures:** Verify `ANTHROPIC_API_KEY` is valid. For `claude.yml` and `update-changelog.yml` (which use the `ocs-agent` app), also verify the app's private key matches `OCS_AGENT_PRIVATE_KEY` and the app is still installed on the relevant repo(s).
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant command or agent in `.claude/commands/` / `.claude/agents/` rather than correcting each PR manually.

## Best Practices

1. [Background to using Claude custom Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
