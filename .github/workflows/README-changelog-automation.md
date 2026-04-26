# Changelog and Documentation Automation with Claude

This automation keeps user documentation in sync after a PR is merged in the main product repo.

GitHub Actions workflows in this repo and in the [OCS repo](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together to process merged OCS PRs. The source workflow dispatches PR metadata to this repo; this workflow classifies the PR as widget or main app, generates changelog/docs updates with Claude, and opens a docs PR only when a real diff is produced.

1. Read the [developer guide](https://github.com/lisa-jwayela/open-chat-studio/blob/Dev-Docs/docs/developer_guides/user_docs.md) for an overview, guidelines, and process details.
2. The notes below are for workflow maintainers; implementation details live in templates, commands, and agent files

## Widget Branching Strategy

For background on handling [widget vs main app changes](https://github.com/lisa-jwayela/open-chat-studio/blob/Dev-Docs/docs/developer_guides/user_docs.md), see the widget branching strategy documentation.

## Manual Trigger

To run the workflow manually, open GitHub Actions, select ‘Update Changelog and Docs from OCS PR,’ and enter the OCS PR number.

## Maintenance Notes

### Dependencies

Maintainers should consider that changes to any item may require updates in both repositories.

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Internal templates for Claude

- Claude prompt templates are stored in: `.github/templates/`.
- Maintainers should be aware that renaming variables requires coordinated changes in the workflow step that exports environment values.


### Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with scopes for contents, issues, and pull requests in both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

### Troubleshooting

- **No PR created:** Check the GitHub workflow runs in both repos. Claude may have determined changes were internal-only.
- **Wrong base branch:** Check dispatch workflow logs to see how PR was classified. Widget files must be in `components/`.
- **widget-develop doesn't exist:** The workflow automatically creates `widget-develop` from `main` if it doesn't exist. If this still fails, check that `OCS_DOCS_PAT` has `contents: write` permission on this repo.
- **Improve output:** Comment on generated PR with `@claude` to request changes.

## Best Practices

1. [Contribution Guides for Creating Good PRs](https://github.com/lisa-jwayela/open-chat-studio/blob/Dev-Docs/docs/contributing/pull_requests.md)
2. [User docs and changelog process](https://github.com/lisa-jwayela/open-chat-studio/blob/Dev-Docs/docs/developer_guides/user_docs.md)

