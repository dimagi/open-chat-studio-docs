# Data & Migration

The **Data & migration** section of Team Settings is where Team Admins [export the team's files](#downloading-team-files), prepare a [migration to another OCS instance](#migrating-to-another-instance), and [delete the team](#deleting-a-team).

## Downloading team files

Use this feature to back up the team's files into a single zip archive, or before moving them to another OCS instance as part of a migration.
See [Download Team Files](../../how-to/download_team_files.md) for how to start an export and what it contains.

## Migrating to another instance

Team Admins can migrate a team's chatbots, configuration, and chat history to another OCS instance — for example, moving to a self-hosted server.

The **Migration public key** and **Migration mode** controls in this section are part of that process.
See [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md) for the full procedure.

## Deleting a team

Team Admins can permanently delete a team from the **Danger Zone** card, which contains the **Delete Team** action.
Deletion is a cascade delete: removing the team also removes everything that belongs to it.

To prevent accidental deletion, OCS asks the Team Admin to confirm by typing the team's name (not its slug).
The Team Admin also chooses an email address to notify when deletion finishes.
Deletion runs in the background, so this email is the only indication that it has completed.

!!! warning
    Deleting a team cannot be undone.
    To keep a copy of the team's files, [download them](#downloading-team-files) before deleting.

## See also

- [Team Settings](index.md)
- [Download Team Files](../../how-to/download_team_files.md)
- [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md)
