---
allowed-tools: Bash(gh release:*),Bash(git:*),Read
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
   - Run `git diff <previous-tag> HEAD -- docs/changelog.md` to the diff from the previous release.
   - Use the diff to determine what has changed.

3. **Generate a well-formatted release summary:**
   - Use markdown formatting for the release notes
   - Use the following template:

     ```markdown
     ### New Features
     - Itemized list of **NEW** entries
     ### Improvements
     - Itemized list of **CHANGE** entries
     ### Bug Fixes
     - Itemized list of **BUG** entries
     ### Migrations
     - Itemized list of **MIGRATION** entries
     ```
   - Only include sections that have entries. If a section has no entries, omit it entirely.
   - Do not add any other sections or headers to the release notes.
   - Focus on user-facing changes

4. **Create the GitHub release:**
   - Use `gh release create --draft` with tag: $1
   - Title: $2
   - Target: 'main'
   - Use your generated summary as the release notes
   - Example: `gh release create $1 --title "$2" --notes "..." --target main --draft`

5. **Confirm completion:**
   - Output the URL of the created release
   - Summarize what was included in the release notes

## Important notes:
- Only include changelog entries that are NEW since the last release
- Keep the release notes concise and well-formatted
- Use markdown formatting consistently
- Focus on user-facing changes and their impact
- If no changes found in changelog diff, warn user and don't create empty release
