#### Widget Changelog (This PR)

Since this PR modifies widget files, update the **widget changelog** at `${WIDGET_CHANGELOG}`.

**Steps:**

1. If the PR has no effect on participants or on people who embed or style the widget, skip the rest of Task 1.  
2. Read the entries under `## Changelog` in the file, starting with the most recent versions. Sections are versions with a release date, and entries have no type prefixes.
3. Choose the section: the latest version, unless the PR description names a new version. Leave the date of an existing section unchanged.
   - For a new version, add a section at the top in the same heading format.
   - If a new version is being released, check the PR description for version info.
   - Use the PR's merged date as the release date, written as `YYYY-MM-DD` (for example, `### v0.14.0 (2026-09-16)`).
4. Focus on changes visible to people who embed or style the widget. Leave out internal implementation details unless they affect integrators.
5. Write one entry for this PR the way the existing entries are written: same structure, length, tone and links.
6. Add it as a bullet in that section.

Whether or not you skipped, continue to Task 2.
