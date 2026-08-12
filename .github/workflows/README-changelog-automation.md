# Changelog and User Doc Automation with Claude

This page is for maintainers of the [user documentation and changelog process](https://developers.openchatstudio.com/developer_guides/user_docs/) that keeps user-facing documentation and changelog entries aligned after code PRs are merged in the main product repository.

GitHub workflows in this docs repository and in the [OCS repository](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together. The source workflow sends PR context to this docs repository, Claude updates changelog and writes user docs when needed. A docs PR is opened for human review.

## Maintenance Notes

Use this map to decide where to make updates:

- `.github/templates/`: Changelog section templates and `changelog-instructions.md`, the top-level instruction spec Claude receives — it orchestrates all three tasks, delegating documentation writing to the zensical-technical-writer agent.
- `.claude/agents/`: Agent definitions used by Claude across workflows. This workflow only uses `zensical-technical-writer`, which handles all documentation writing decisions; `documentation-pr-reviewer` (used by `claude-review.yml`) isn't part of this process.

> **Note on `.claude/commands/`:** The `/write-docs` slash command is a human-facing shortcut for interactive Claude Code sessions — it simply invokes the same `zensical-technical-writer` agent. The automated workflow calls the agent directly via the `Task` tool and does not use slash commands.

Keep in mind that behavior changes may require updates in both `.github/templates/` and `.claude/`.

### Repositories in Scope

Troubleshooting and process changes can involve both repositories:

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Required Secrets

- **`OCS_AGENT_PRIVATE_KEY`** (secret) and **`OCS_AGENT_APP_ID`** (variable): credentials for
  the `ocs-agent` GitHub App (org Settings → GitHub Apps). The app must be installed on both
  the OCS repo and this docs repo with contents, issues, and pull request write permissions.
  Workflows mint a short-lived installation token from these, so the PR itself and any
  `gh pr`/`gh issue` comments are attributed to `ocs-agent[bot]`. The git **commits** on
  the branch are attributed to `github-actions[bot]` instead — the workflow sets that
  identity via `git config` before Claude runs, and Claude's own commits inherit it too.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

- **Manual Trigger:** To run the workflow manually: open GitHub Actions, select `Update Changelog and Docs from OCS PR`, and enter the OCS PR number. It is safe to rerun this for a PR.
    - Note: this workflow requires repository secrets and will fail in forks unless those secrets are configured.
- **No PR created:** Check workflow runs in both repositories. If there was no docs/changelog change, no docs PR is expected.
- **Unexpected target branch or classification:** Check workflow logs in the source and receiving repos to verify how the PR was classified.
- **Authentication or permission failures:** Verify `ANTHROPIC_API_KEY` is valid, the `ocs-agent` app's private key matches `OCS_AGENT_PRIVATE_KEY`, and the app is still installed on both repos (token minting fails if either repo is missing from the installation).
- **widget-develop branch doesn't exist:** Create it: `git checkout -b widget-develop main && git push origin widget-develop`
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant agent in `.claude/agents/` rather than correcting each PR manually.

## Best Practices

1. [Developer guide with details on branching and app/widget release flow](https://developers.openchatstudio.com/developer_guides/user_docs/)
2. [Background to using Claude custom Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
