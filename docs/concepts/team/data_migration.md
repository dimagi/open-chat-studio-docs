# Data & Migration

The **Data & migration** section of Team Settings is where Team Admins export the team's files, prepare a migration to another OCS instance, and delete the team.

## Downloading team files

The **Download team files** card is subtitled "A zip archive of every file belonging to this team."
Select **Download** to start the export.

The export runs as a background job, so leaving the page is safe.
Reopening Team Settings reattaches to a running export instead of losing track of it.
Starting a new export while one is running resumes it, rather than starting a duplicate.
While it runs, the card shows a progress bar.
When the export finishes, select **Download ZIP** to fetch the file.

Once an export exists, the card also shows a "Last export created …" line, along with **Download Export**, to fetch that export again, and **Regenerate export**, to build a fresh one.

- The zip contains every file belonging to the team, including archived files and older versions of files.
- It does not contain chat history or provider credentials.
- Files that cannot be read are skipped; the zip is still produced with everything else.

!!! note
    An export is deleted 24 hours after it is created, and each download link is valid for one hour.
    Select **Regenerate export** to replace a stale one.

## Migration public key and migration mode

The **Migration public key** card is subtitled "Seals secret data exported from this team during a migration."
A **Set** or **Not set** badge shows whether a key is registered.
Paste your public key, in PEM format, into the **Public Key** field, described as "Public key used to seal data exported from this team."

The same card has a **Migration mode** checkbox: "While enabled, scheduled messages and event triggers (including timeout triggers) for this team are paused and will not fire."
The key and the checkbox are one form, saved together with **Save key**.

Turning on migration mode pauses scheduled messages, event triggers, timeout triggers, and scheduled triggers.
They stop firing until you turn migration mode off again.
Live chat keeps working as normal throughout.
While migration mode is on, every page in the team shows a banner: "This team is undergoing a migration. Do not create or edit chatbots until the migration is complete."

For the full migration procedure — generating a key pair, exporting files, and running the sync command — see [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md).

## Deleting a team

The **Danger Zone** card holds a single **Delete Team** button, which opens a "Really delete team?" modal.

- Type the team's name, not its slug, into the field labelled `Type <team name> to confirm`.
- Choose who gets emailed once deletion finishes: **Send email notification to myself** (preselected), **Send email notification to admins**, or **Send email notification to all members of the team**.
- Select **Delete team** to confirm, or **Cancel** to back out.

!!! warning
    Deleting a team cannot be undone.
    It is a cascade delete: removing the team removes everything that belongs to it.
    Deletion runs in the background — the email you chose is the only signal that it has finished.

## See also

- [Team Settings](index.md)
- [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md)
