#### Main Changelog (This PR)

Since this PR modifies main app files, update the **main changelog** at `${MAIN_CHANGELOG}`.

**Main Changelog Structure:**
- The main changelog is organized by **dates** (e.g., "Oct 22, 2025")
- Entries use TYPE prefixes: **NEW**, **CHANGE**, **BUG**, **MIGRATION**
- Format: * **[TYPE]** [Description]

**Steps for Main Changelog:**
1. Read `${MAIN_CHANGELOG}` to understand the current structure
2. Analyze the PR title, description, and labels to understand what changed
3. Determine the appropriate changelog type:
   - **NEW**: New features or functionality
   - **CHANGE**: Modifications to existing features
   - **BUG**: Bug fixes
   - **MIGRATION**: Migration-related changes or breaking changes
4. Write a clear, concise changelog entry (1-2 sentences max)
5. Add the entry to the changelog under the appropriate date section
6. Format the merged date as "MMM D, YYYY" (e.g., "Oct 22, 2025")
7. If a section for that date already exists, add to it; otherwise create a new date section

**Main Changelog Format:**
```markdown
## Oct 22, 2025
* **NEW** Added support for parallel pipeline execution.
* **BUG** Fixed issue with session timeout handling.
```
