---
allowed-tools: Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*),WebFetch(domain:github.com,domain:raw.githubusercontent.com),Bash(uv run prek run markdownlint-cli2 --all-files),Bash(uv run zensical build --clean)
description: Review a pull request
---

# Review Pull Request Command

Review documentation and changelog PRs using the documentation-pr-reviewer subagent.

## Steps

Arguments: $ARGUMENTS contains `REPO` and `PR_NUMBER`. Pass both to every `gh` command as `<PR_NUMBER> --repo <REPO>`.

First, fetch the PR details to understand what files are being changed:
1. Use `gh pr view <PR_NUMBER> --repo <REPO>` to get PR overview
2. Use `gh pr diff <PR_NUMBER> --repo <REPO>` to see the actual changes

Then launch the documentation-pr-reviewer agent with context about:
- What files are being modified (README, CHANGELOG, docs/, etc.)
- The full diff content
- Any PR description or context

The agent will provide structured feedback following documentation best practices. Only post feedback that is noteworthy and actionable.

Use inline comments via `gh pr comment` for specific line issues.
Use top-level comments (`gh pr comment <PR_NUMBER> --repo <REPO>`) for overall observations.
Keep all feedback concise and constructive.

---
