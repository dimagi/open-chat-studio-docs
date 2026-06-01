# Changelog and User Doc Automation with Claude

This process keeps user-facing documentation and changelog entries aligned after PRs are merged in the main product repository.

Workflows in this docs repository and in the [OCS repository](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together. The source workflow sends PR context to this docs repository, Claude updates changelog and docs when needed, and a docs PR is opened only when there is a meaningful content change.

This page is for maintainers of this [process](https://developers.openchatstudio.com/developer_guides/user_docs/). It explains how the workflow is organized, where to make updates, and how to troubleshoot issues.

## Maintenance Notes

Use this map to decide where to make updates:

- `.github/templates/`: Changelog section templates and the (`changelog-instructions.md`) which is the top-level instruction spec Claude receives — it orchestrates all three tasks, delegating documentation writing to the zensical-technical-writer agent.
- `.claude/agents/`: Writing and PR review standards used by Claude. The `zensical-technical-writer` agent handles all documentation writing decisions for this workflow.

> **Note on `.claude/commands/`:** The `/write-docs` slash command is a human-facing shortcut for interactive Claude Code sessions — it simply invokes the same `zensical-technical-writer` agent. The automated workflow calls the agent directly via the `Task` tool and does not use slash commands.

Keep in mind that behavior changes may require updates in both `.github/templates/` and `.claude/`.

### Repositories in Scope

Troubleshooting and process changes can involve both repositories:

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with scopes for contents, issues, and pull requests in both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

- **Manual Trigger:** To run the workflow manually: open GitHub Actions, select `Update Changelog and Docs from OCS PR`, and enter the OCS PR number. It is safe to rerun this for a PR.
    - Note: this workflow requires repository secrets and will fail in forks unless those secrets are configured.
- **No PR created:** Check workflow runs in both repositories. If there was no meaningful docs/changelog change, no docs PR is expected.
- **Unexpected target branch or classification:** Check workflow logs in the source and receiving repos to verify how the PR was classified.
- **Authentication or permission failures:** Verify `OCS_DOCS_PAT` and `ANTHROPIC_API_KEY` are set correctly and still valid.
- **widget-develop branch doesn't exist:** Create it: `git checkout -b widget-develop main && git push origin widget-develop`
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant agent in `.claude/agents/` rather than correcting each PR manually.

## Best Practices

1. [Developer guide on docs branching and app/widget release flow](https://developers.openchatstudio.com/developer_guides/user_docs/)
2. [Background to using Claude custom Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

