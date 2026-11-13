#### Widget Changelog (This PR)

Since this PR modifies widget files, update the **widget changelog** at `${WIDGET_CHANGELOG}`.

**Widget Changelog Structure:**
- The widget changelog is organized by **version numbers** (e.g., v0.4.8, v0.4.7)
- NO date-based sections
- NO TYPE prefixes (NEW, CHANGE, BUG)

**Steps:**

1. Read the file and its most recent entries.
2. If the PR has no effect on people who embed or style the widget, skip the rest of this task.
3. Choose the section: the latest version, unless the PR description names a new version. For a new version, add a section at the top in the same heading format.
4. Focus on changes visible to people who embed or style the widget. Leave out internal implementation details unless they affect integrators.
5. Write one entry for this PR the way the existing entries are written: same structure, length, tone and links.
6. Add it as a bullet in that section.

Whether or not you skipped, continue to Task 2.
