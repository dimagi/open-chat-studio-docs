# Maintaining Claude Code Agent Workflows

For engineers responsible for extending, debugging, or operating the GitHub workflows. For day-to-day usage of similar workflows on the main project, see [docs/developer_guides/claude_code_agent.md](https://developers.openchatstudio.com/developer_guides/claude_code_agent).

These workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to run Claude Code inside GitHub Actions. Each run gives Claude access to the repository, a shell, and the GitHub CLI. Claude autonomously reads code, writes changes, runs tests, and opens PRs based on its instructions.

## Setup

The `ANTHROPIC_API_KEY` secret must be set under **Settings > Secrets and variables > Actions** in the repository. All Claude workflows require it.

## Workflow files

| File | Actions UI name | Trigger |
|---|---|---|
| `.github/workflows/claude.yml` | Claude Code | `@claude` mention in an issue/PR comment or review; issue opened or assigned with `@claude` in the title or body |
| `.github/workflows/claude-dependabot.yml` | Claude Dependabot PR Review | Dependabot PR opened or updated, manual dispatch |
| `.github/workflows/claude-review.yml` | PR Review | PR opened, marked ready for review, or reopened (skips Dependabot PRs and PRs labelled `automated`) |

## Forked PRs
Fork PRs run with restricted permissions and no access to secrets. This specifically affects `claude-review.yml`, which triggers directly on `pull_request` — reviews do **not** run on fork PRs. `claude.yml` is unaffected: it triggers on comment/review events (`issue_comment`, `pull_request_review_comment`, `pull_request_review`, `issues`), which run in the base repo's context with full token access regardless of whether the underlying PR is from a fork.

## Tool allowlist

Each run is restricted to an explicit allowlist of tools defined in the `claude_args` field of the workflow file. Claude cannot call anything outside that list. If it needs a tool that isn't permitted, the run fails rather than silently taking an unintended action.

For more information on `claude_args`, see [GitHub for claude-code-action usage guide](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md).

## Custom commands and agents

`claude-review.yml` doesn't use any external plugin or marketplace. Its prompt invokes `/review-pr`, a local slash command defined at `.claude/commands/review-pr.md`, which launches the local `documentation-pr-reviewer` subagent (`.claude/agents/documentation-pr-reviewer.md`).

## Concurrency

`claude.yml` has no `concurrency:` block, so it has no built-in queuing or cancellation — multiple triggers for the same issue or PR (e.g. several `@claude` mentions in quick succession) can run simultaneously.

`claude-review.yml` is the one workflow that defines concurrency: it groups runs by PR number and sets `cancel-in-progress: true`, so a new push to a PR cancels any in-progress review of that PR, since a review of stale code is wasted spend.

## Branch and label conventions

- **Branches** — all Claude-created branches are namespaced under `claude/` (e.g. `claude/123-20240518-143022` — issue number, date, time). Easy to target with branch protection rules. (This naming comes from `claude-code-action`'s own defaults — it isn't configured anywhere in this repo's workflow files.)
