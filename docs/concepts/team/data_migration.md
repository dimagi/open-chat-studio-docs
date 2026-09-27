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
- [Download Team Files](../../how-to/download_team_files.md)
- [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md)
