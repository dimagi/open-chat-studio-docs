#### Widget Changelog (This PR)

Since this PR modifies widget files, update the **widget changelog** at `${WIDGET_CHANGELOG}`.

**Widget Changelog Structure:**
- The widget changelog is organized by **version numbers** (e.g., v0.4.8, v0.4.7)
- Entries are bullet points under each version
- NO date-based sections
- NO TYPE prefixes (NEW, CHANGE, BUG)
- Read the existing widget changelog to understand the format

**Steps for Widget Changelog:**
1. Read `${WIDGET_CHANGELOG}` to understand the current structure
2. Find the latest version section (e.g., v0.4.8)
3. Add your entry as a new bullet point under that version
4. If a new version is being released, check the PR description for version info
5. Follow the existing style: concise bullet points describing changes

**Widget Changelog Format:**
```markdown
### v0.4.8

* Fix horizontal scrollbar styling.
* Improve scrolling behavior for new messages.
* Your new entry here.
```
