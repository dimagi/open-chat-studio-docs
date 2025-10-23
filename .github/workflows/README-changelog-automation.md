# Changelog and Documentation Automation

GitHub Actions workflows that use Claude AI to automatically generate changelog entries and update documentation from merged PRs in open-chat-studio.

## Overview

When a PR is merged in open-chat-studio:
1. **Dispatch workflow** detects if widget files (`components/`) changed
2. **Update workflow** in this repo uses Claude to:
   - Update the appropriate changelog (widget or main)
   - Create/update documentation as needed
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

## Required Secrets

- **`OCS_DOCS_PAT`**: GitHub PAT with contents, issues, pull_request scope to both the OCS repo and the OCS docs repo.
- **`ANTHROPIC_API_KEY`**: Claude API key.

## Troubleshooting

**No PR created:** Check workflow runs in both repos. Claude may have determined changes were internal-only.

**Wrong base branch:** Check dispatch workflow logs to see how PR was classified. Widget files must be in `components/`.

**widget-develop doesn't exist:** Create it: `git checkout -b widget-develop main && git push origin widget-develop`

**Improve output:** Comment on generated PR with `@claude` to request changes.

## Best Practices

**For Better Results:**
- Write clear, descriptive PR titles
- Fill out "User Facing Changes" section thoroughly
- For widget releases: Include version number in PR description (e.g., "v0.4.9")
- Use `@claude` in generated PRs to request improvements

**Separate PRs:** Keep widget and main app changes in separate PRs to ensure both changelogs are updated.
