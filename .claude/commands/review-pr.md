---
allowed-tools: Task,Read,Grep,Glob,mcp__github_inline_comment__create_inline_comment,Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*)
description: Review a pull request
---

Review documentation and changelog PRs using the doc-pr-reviewer subagent.

First, fetch the PR details to understand what files are being changed:
1. Use `gh pr view` to get PR overview
2. Use `gh pr diff` to see the actual changes

Then launch the documentation-pr-reviewer agent with context about:
- What files are being modified (README, CHANGELOG, docs/, etc.)
- The full diff content
- Any PR description or context

The agent will provide structured feedback following documentation best practices. Only post feedback that is noteworthy and actionable.

Use `mcp__github_inline_comment__create_inline_comment` for feedback tied to a specific file/line.
Use `gh pr comment` for a top-level summary comment covering overall observations.
Keep all feedback concise and constructive.

---
