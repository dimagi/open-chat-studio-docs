# Changelog and Documentation Automation with Claude

This process keeps user-facing documentation and changelog entries aligned after PRs are merged in the main product repository.


This page is for maintainers of this process. It explains how the system is organized, where to make updates and troubleshooting

Workflows in this repository and in the [OCS repository](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together. The source workflow sends PR context to this docs repository, Claude updates changelog and docs when needed, and a docs PR is opened only when there is a meaningful content change.

## Maintenance Notes

Use this map to decide where to make updates:

- `.github/templates/`: 1) Changelog section templates and 2) Instruction file for **decisions** on if changelog or docs updates are required.
- `.claude/agents/`: Change writing and review standards used by Claude.
- `.claude/commands/`: Change reusable command workflows.

Keep in mind that behavior changes may require updates in both `.github/templates/` and `.claude/`.
Use AI assistants to understand key files and their responsibilities.

### Repositories in Scope

Troubleshooting and process changes can involve both repositories:

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with scopes for contents, issues, and pull requests in both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

- **Manual Trigger:** To test, run the workflow manually, open GitHub Actions, select `Update Changelog and Docs from OCS PR`, and enter the OCS PR number. There is no risk to rerunning this for a PR. 
    - Note: workflows will fail if running from a fork
- **No PR created:** Check workflow runs in both repositories. If there was no meaningful docs/changelog change, no docs PR is expected.
- **Unexpected target branch or classification:** Check workflow logs in the source and receiving repos to verify how the PR was classified.
- **Authentication or permission failures:** Verify `OCS_DOCS_PAT` and `ANTHROPIC_API_KEY` are set correctly and still valid.
- **widget-develop branch doesn't exist:** Create it: `git checkout -b widget-develop main && git push origin widget-develop`
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues:** Update the relevant agent in agents rather than correcting each PR manually.

## Best Practices

1. [User docs and changelog process](https://developers.openchatstudio.com/developer_guides/user_docs/)
2. [Developer guide with details on the main app vs chat widget](https://developers.openchatstudio.com/developer_guides/user_docs/).
3. [Background to using Claude custom Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

