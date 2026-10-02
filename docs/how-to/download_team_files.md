# Download Team Files

Team Admins can export every file belonging to a team as a single zip archive.
Use it as a backup, or to move the team's files as part of a migration.

## Prerequisites

- You need Team Admin access to the team.

## Download the team's files

1. Open **Team Settings** and go to the **Data & migration** section.
2. In the **Download team files** card, select **Download**.
3. Wait for the export to finish — a progress bar shows how far it's got.
4. Select **Download ZIP** to save the archive, then **Done**.

Once an export exists, the card shows **Download Export**, to fetch it again, and **Regenerate export**, to build a fresh one.
A line on the card shows when the export was created.

The export runs in the background, so it's safe to leave the page while it's running.
Reopening Team Settings picks up an export that's still in progress, instead of starting a second one.

### Example

Before migrating a team to another OCS instance, download its files so you can upload them to the target server's storage backend.
See [Migrate a Team to Another OCS Instance](../tech-hub/migrate_team.md) for the full procedure.

## Expected outcome

The zip contains every file belonging to the team, including archived files and older versions of files.
It does not contain chat history or provider credentials.
A file that can't be read is skipped, and the rest of the export still completes.

## Common issues

**The download link doesn't work.**
Each download link is valid for one hour. Select **Download Export** again for a fresh link.

**I can't find my export when I come back later.**
Exports are deleted 24 hours after they're created. Select **Regenerate export** to create a new one.

## See also

- [Data & Migration](../concepts/team/data_migration.md)
- [Migrate a Team to Another OCS Instance](../tech-hub/migrate_team.md)
