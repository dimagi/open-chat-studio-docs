# Changelog and Documentation Automation with Claude

This process keeps user-facing documentation and changelog entries aligned after PRs are merged in the main product repository.

Workflows in this repository and in the [OCS repository](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together. The source workflow sends PR context to this docs repository, Claude updates changelog and docs when needed, and a docs PR is opened only when there is a meaningful content change.

This page is for maintainers of the changelog automation process. It explains how the system is organized and where to make updates.

For broader process guidance and details about main app vs chat widget, see the [developer guide](https://developers.openchatstudio.com/developer_guides/user_docs/).

## Maintenance Notes

Use this map to decide where to make updates:

- `.github/templates/`: Change automation decisions, such as when changelog or docs updates are required.
- `.claude/agents/`: Change writing and review standards used by Claude.
- `.claude/commands/`: Change reusable command workflows.

Keep in mind that behavior changes may require updates in both `.github/templates/` and `.claude/`.
Use AI assistants to understand key files and their responsibility.

### Repositories in Scope

Troubleshooting and process changes can involve both repositories:

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with scopes for contents, issues, and pull requests in both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

- **Manual Trigger** To run the workflow manually, open GitHub Actions, select ‘Update Changelog and Docs from OCS PR,’ and enter the OCS PR number.
- **No PR created:** Check workflow runs in both repositories. If there was no meaningful docs/changelog change, no docs PR is expected.
- **Unexpected target branch or classification:** Check workflow logs in the source and receiving repos to verify how the PR was classified.
- **Authentication or permission failures:** Verify `OCS_DOCS_PAT` and `ANTHROPIC_API_KEY` are set correctly and still valid.
- **Output quality needs improvement:** Comment on the generated PR with `@claude` and specify what to revise.
- **For systemic quality issues** Update the relevant agent in agents rather than correcting each PR manually.

## Best Practices

1. [Contribution Guides for Creating Good PRs](https://developers.openchatstudio.com/contributing/pull_requests/)
2. [User docs and changelog process](https://developers.openchatstudio.com/developer_guides/user_docs/)
3. [Claude custom Subagents](https://code.claude.com/docs/en/sub-agents#create-custom-subagents)

