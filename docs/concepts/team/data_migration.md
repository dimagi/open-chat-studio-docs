# Team Settings: Data & Migration

In the **Data & migration** section of Team Settings, Team Admins [export the team's files](#downloading-team-files), prepare a [migration](#migrating-to-another-instance), and [delete the team](#deleting-a-team).

## Downloading team files

Use this feature to back up the team's files into a single zip archive.
You can also use it before moving them to another OCS instance as part of a migration.
See [Download Team Files](../../how-to/download_team_files.md) for how to start an export and what it contains.

## Migrating to another instance

Team Admins can migrate a team's chatbots, configuration, and chat history to another OCS instance — for example, moving to a self-hosted server.

The **Migration public key** and **Migration mode** controls in this section are part of that process.
See [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md) for the full procedure.

## Deleting a team

Team Admins can delete a team from the **Danger Zone** card, which contains the **Delete Team** action.
The team is disabled immediately and permanently deleted after a 30-day grace period.
Permanent deletion removes everything that belongs to the team, including its traces, evaluation messages, event actions, and its remote OpenAI vector stores and uploaded files (best effort).

To prevent accidental deletion, OCS asks the Team Admin to confirm by typing the team's name (not its slug).
The Team Admin also chooses an email address to notify.
That address receives an email when the deletion is scheduled and another when it completes.

### While deletion is pending

- **Pages:** Team members see a "scheduled for deletion" page.
  People outside the team see the team as nonexistent.
- **Chatbots:** Chatbots stop responding on every channel and send no reply, even if the channel has a "disabled" message configured.
- **API:** Every API request for the team, including the export API, is refused with a 403 error.
- **Background work:** Scheduled messages, evaluations, dataset auto-population, document sync, and custom action health checks are paused.
- **Team switcher:** The team appears as "(pending deletion)".
- **Invitations and OAuth:** Invitations to the team return a 404 error, and the OAuth authorize page does not offer the team.

### Cancel a deletion

A Team Admin or superuser can cancel the deletion during the grace period.
On the pending deletion page, select **Cancel deletion and restore team**.
OCS restores the team as it was before deletion was scheduled.

!!! warning
    After the grace period ends, deletion cannot be undone.
    To keep a copy of the team's files, [download them](#downloading-team-files) before deleting the team. Exports are not available while deletion is pending.

!!! note "Self-hosted operators"
    Set the grace period with the `TEAM_DELETION_GRACE_PERIOD_DAYS` setting (default 30).
    A daily Celery beat task performs the final deletion, so Celery beat must be running for deletions to complete.

## See also

- [Team Settings](index.md)
- [Download Team Files](../../how-to/download_team_files.md)
- [Migrate a Team to Another OCS Instance](../../tech-hub/migrate_team.md)
