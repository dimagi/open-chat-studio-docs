---
allowed-tools: Bash(gh release:*),Bash(git:*),Read,AskUserQuestion
description: Create a new release with changelog
argument-hint: [release-tag] [release-title]
---

Create a new GitHub release by comparing the current changelog with the previous release.

## Release Configuration

- **Tag**: $1
- **Name**: $2
- **Target Branch**: 'main'

## Steps to follow:

1. **Find the most recent non-draft release:**
   - Run `gh release list --limit 1 --exclude-drafts` to get the latest release
   - Extract the tag name (3rd column in the output)

2. **Get changelog changes since last release:**
   - Run `git diff <previous-tag> HEAD -- docs/changelog.md` to get only the new entries
   - Lines starting with `+` are new additions since the previous release

3. **Generate a well-formatted release summary:**
   - Start with an overall summary of the release
   - Organize changes into sections:
     * **New Features** (entries tagged with **NEW** in the changelog)
     * **Improvements** (entries tagged with **CHANGE** in the changelog)
     * **Bug Fixes** (entries tagged with **BUG** in the changelog)
   - Use markdown formatting for the release notes
   - Keep the summary concise but comprehensive
   - Focus on user-facing changes

4. **Create the GitHub release:**
   - Use `gh release create --draft` with tag: $1
   - Title: $2
   - Target: 'main'
   - Use your generated summary as the release notes
   - Example: `gh release create $1 --title "..." --notes "..." --target main --draft`

5. **Confirm completion:**
   - Output the URL of the created release
   - Summarize what was included in the release notes

## Important notes:
- Only include changelog entries that are NEW since the last release
- Keep the release notes concise and well-formatted
- Use markdown formatting consistently
- Focus on user-facing changes and their impact
