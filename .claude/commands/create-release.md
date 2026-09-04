---
allowed-tools: Bash(gh release list:*),Bash(gh release create:*),Bash(git diff:*),Read
description: Create a new draft GitHub release from the changelog
argument-hint: [release-tag] [release-title]
---

# Create Release Command

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

     Remove before publishing:
     - diff link: https://github.com/dimagi/open-chat-studio-docs/compare/<previous-tag>...HEAD
   ```

   - Only include sections that have entries. If a section has no entries, omit it entirely.
   - Do not add any other sections or headers to the release notes.
   - Focus on user-facing changes
   - Where possible include links to the documentation
       - The documentation and changelog are hosted at https://docs.openchatstudio.com/
       - Only include links that already appear in the changelog diff. Do not
         invent, guess, or fetch documentation URLs; if you're not sure a
         link from the diff is correct, leave it out.
       - Convert relative paths to absolute URLs using that base. The site serves clean
         directory URLs, not raw markdown files. Apply these checks in order and stop
         at the first one that applies:
         1. If the link is already an absolute URL (starts with `http://`, `https://`,
            or another scheme like `mailto:`), leave it exactly as it is.
         2. If the link is only an `#anchor` with no path, it points at the changelog
            page itself — prefix it with `https://docs.openchatstudio.com/changelog/`.
         3. Otherwise, convert the relative path:
            a. Split off any `#anchor` from the rest of the link.
            b. Strip a leading `./` or `/` from the remaining path.
            c. If the filename is `index.md`, drop it, keeping the parent directory
               path; otherwise strip just the `.md` extension.
            d. Ensure the path ends in exactly one trailing slash, then re-append
               the `#anchor` from step (a) if there was one.
         Example: `./tech-hub/tools.md#set-session-state-key` →
         `https://docs.openchatstudio.com/tech-hub/tools/#set-session-state-key`
         Example: `./chat_widget/index.md` →
         `https://docs.openchatstudio.com/chat_widget/`
         Example: `concepts/sessions.md` →
         `https://docs.openchatstudio.com/concepts/sessions/`

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
