# Changelog and Documentation Automation with Claude

This automation keeps user documentation in sync after a PR is merged in the main product repo.

GitHub Action Workflows in this repo and in the [OCS repo](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together to process merged OCS PRs. The source workflow dispatches PR metadata to this repo, this workflow classifies the PR as widget or main app, generates changelog/docs updates with Claude, and opens a docs PR only when a real diff is produced.

## Overview

When a PR is merged in open-chat-studio:
1. **Dispatch workflow** detects if widget files (`components/`) changed for branch strategy
2. **Update Changlog workflow** in this repo uses Claude to:
   - Update the appropriate changelog page (widget or main)
   - Create/update User Documentation as needed
   - Create a PR with changes

## Widget Branching Strategy

**Detection:** PRs with changes in `components/` are classified as widget changes.

| Type         | Base Branch      | Changelog                       | Target Branch    |
|--------------|------------------|---------------------------------|------------------|
| **Widget**   | `widget-develop` | `docs/chat_widget/changelog.md` | `widget-develop` |
| **Main App** | `main`           | `docs/changelog.md`             | `main`           |

**Mixed Changes:** If a PR touches both widget and main app files, it's treated as a widget change and only the widget changelog is updated. Separate PRs are recommended.

## Manual Trigger

Run workflow manually: Actions → "Update Changelog and Docs from OCS PR" → Enter PR number

## Dependencies

Maintainers should consider that changes to any item may require updates in both repositories.

- **Source repo:** `dimagi/open-chat-studio` (with )
- **Receiving repo:** this docs repo

### Internal templates for Claude

Prompt building instruction templates for Claude in: `.github/templates/`.

Maintainers be aware that renaming variables requires coordinated changes in the workflow step that exports environment values


## Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with contents, issues, pull_request scope to both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

**No PR created:** Check workflow runs in both repos. Claude may have determined changes were internal-only.

**Wrong base branch:** Check dispatch workflow logs to see how PR was classified. Widget files must be in `components/`.

**widget-develop doesn't exist:** The workflow automatically creates `widget-develop` from `main` if it doesn't exist. If this still fails, check that `OCS_DOCS_PAT` has `contents: write` permission on this repo.

**Improve output:** Comment on generated PR with `@claude` to request changes.

## Best Practices

**For Better Results:**
- Write clear, descriptive PR titles
- Fill out "User Facing Changes" section thoroughly
- For widget releases: Include version number in PR description (e.g., "v0.4.9")
- Use `@claude` in generated PRs to request improvements

**Separate PRs:** Keep widget and main app changes in separate PRs to ensure both changelogs are updated.
