# GitHub Automation with Claude

For engineers responsible for extending, debugging, or operating the GitHub workflows on this user documentation repo. The main OCS project has similar workflows, see [the developer guide on GitHub automation with Claude](https://developers.openchatstudio.com/developer_guides/claude_github_automation/).

These workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to run Claude Code inside GitHub Actions.

## GitHub workflows

| File | Actions UI name | Trigger |
|---|---|---|
| `claude.yml` | Claude Code | `@claude` mention in an issue/PR comment or review; issue opened or assigned with `@claude` in the title or body |
| `claude-dependabot.yml` | Claude Dependabot PR Review | Dependabot PR opened or updated, or manual dispatch |
| `claude-review.yml` | PR Review | PR opened, marked ready for review, or reopened (skips Dependabot PRs and [PRs labelled `automated`)](#labels) |
| `release.yml` | Weekly Release Summary | Weekly schedule (Mondays 9am UTC), or manual dispatch with `release_tag`/`release_name` inputs |
| `update-changelog.yml`| Update Changelog and Docs from OCS PR | See [README-changelog-automation.md](README-changelog-automation.md) |

## Pipelines

End-to-end view of what each workflow actually does: which Claude command or instruction spec it
invokes, whether that delegates to a subagent, and what comes out the other end.

Commands live in `.claude/commands/`, agents in `.claude/agents/` ([background](https://docs.anthropic.com/en/docs/claude-code/sub-agents)).

| Workflow | Command / Instruction Spec | Subagent | Outcome |
|---|---|---|---|
| `claude.yml` | none — freeform prompt taken from the `@claude` mention itself | none | Whatever the mention asks, using the allowlisted tools (edit, build, push, open PR, etc.) |
| `claude-dependabot.yml` | none — freeform inline prompt in the workflow | none | Adds a PR comment on the dependabot PR analyzing the dependency bump and flagging breaking changes |
| `claude-review.yml` | [`/review-pr`](../../.claude/commands/review-pr.md) | [`documentation-pr-reviewer`](../../.claude/agents/documentation-pr-reviewer.md) | Adds PR comments: Approve / Request Changes / Comment |
| `release.yml` | [`/create-release <tag> <title>`](../../.claude/commands/create-release.md) | none — the command does the work itself | Creates a draft GitHub release summarizing the changelog diff for the week |
| `update-changelog.yml` | [`changelog-instructions.md`](../templates/changelog-instructions.md) rendered into the workflow's `prompt:` | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) | Creates PR with doc updates — see [README-changelog-automation.md](README-changelog-automation.md) |
| *(manual only, no workflow)* | [`/write-docs`](../../.claude/commands/write-docs.md) | [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) | Docs content written or updated |

## Setup

Secrets and variables are configured under **Settings > Secrets and variables > Actions**:
`ANTHROPIC_API_KEY` (every workflow), plus `OCS_AGENT_APP_ID` / `OCS_AGENT_PRIVATE_KEY` for
`claude.yml` and `update-changelog.yml`, which push branches and open PRs as the `ocs-agent`
bot. See each workflow file for exactly how they're used.

## Forked Repos

A PR from a forked repo runs its `pull_request`-triggered workflows with a read-only `GITHUB_TOKEN` and no access to this repo's Actions secrets.

Any workflow here triggered by `pull_request` (check the code) is affected: the job still starts, but fails inside the `claude-code-action` step once it tries to authenticate — it isn't skipped. Workflows triggered by comment/review events instead are unaffected — those always run in the base repo's context with full secrets access, regardless of the underlying PR's origin.

## Tool Allowlist

The explicit per-run tool allowlist is the main safeguard against a compromised or malicious prompt (e.g. a hostile issue/PR body) taking unintended action.

Every workflow passes `--allowedTools` in `claude_args` directly — that's what's enforced. Some workflows invoke a command with its own `allowed-tools:` frontmatter (e.g. `.claude/commands/create-release.md`), and some of those commands launch a subagent via `Task` with its own `tools:` frontmatter (e.g. `documentation-pr-reviewer`).

None of these further declarations expand what's enforced — only the workflow's `--allowedTools` does — so a tool named further down the chain but missing from the workflow's list is simply unusable there, no matter what the command or agent frontmatter claims. Keep all of these in sync: right now `documentation-pr-reviewer`'s `tools:` includes `WebFetch`/`WebSearch` for link-checking, but neither `claude-review.yml` nor `review-pr.md` grants them, so that capability is currently dead when the agent runs through this pipeline. The command frontmatter is also what governs if a command is ever run manually/interactively outside its workflow.

> [!WARNING]
> If Claude tries to use a tool that isn't permitted, that call is denied and it continues without it — **the run won't fail**. A missing tool usually surfaces as an **incomplete result rather than an error**, so check the run transcript for denied tool calls if the output looks truncated.

## Labels

The `automated` label `claude-review.yml` skips is applied by the bot-PR-creating workflows
themselves, not by Claude: `update-changelog.yml` (`--label "automated"`) and the unrelated,
non-Claude `update-api-docs.yml` (`labels: automated`). Removing the label from either kind of
PR makes it eligible for the AI review above.

## Concurrency

`claude-review.yml` groups runs by PR number with `cancel-in-progress: true`. Note this only cancels on reopen / ready-for-review, not on push — the workflow doesn't listen for `synchronize`, so pushing to an open PR neither starts a new review nor cancels a running one.

`update-changelog.yml` also sets concurrency, grouped by PR number but with `cancel-in-progress: false`, so an in-flight changelog run finishes rather than being superseded.

## Troubleshooting

Issues that can show up on any of these workflows. For workflow-specific troubleshooting, see that workflow's own doc (e.g. [README-changelog-automation.md](README-changelog-automation.md#troubleshooting) for `update-changelog.yml`).

- **Run fails immediately in the `claude-code-action` step on a `pull_request`-triggered workflow:** Expected if the PR is from a forked repo — see Forked Repos above.
- **Output looks incomplete, or a step Claude should have taken didn't happen:** Check the run transcript for denied tool calls — see Tool Allowlist above.
- **Authentication or permission failures:** Verify `ANTHROPIC_API_KEY` is valid. For `claude.yml` and `update-changelog.yml` (which use the `ocs-agent` app), also verify the app's private key matches `OCS_AGENT_PRIVATE_KEY` and the app is still installed on the relevant repo(s).
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant command or agent in `.claude/commands/` / `.claude/agents/` rather than correcting each PR manually.
