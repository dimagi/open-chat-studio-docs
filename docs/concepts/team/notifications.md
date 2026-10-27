# Notifications

The **Notifications** section of Team Settings is where Team Admins set up [notification channels](#notification-channels), so the team's Open Chat Studio (OCS) [notifications](../notifications.md) are posted to Slack.
Slack posts are sent in addition to in-app and email notifications, which are still delivered if a Slack post fails.

Use it when people on your team need to see important events, such as errors, without opening OCS or checking their email.
Notification channels belong to the team, not to a user, so one setup serves everyone on the team.
Team Admins can manage them by default; other members need permission through a [User Group](groups.md).

## Notification channels

A notification channel connects one Slack channel in one of the team's [Slack workspaces](messaging_providers.md#slack-providers-and-team-notifications) to a minimum [severity level](../notifications.md#severity-levels).
OCS posts each notification at or above that level to the channel.
Your team needs a Slack messaging provider before you can add a channel.

You can use several channels at different levels to send notifications to the right audience.
For example, Error notifications can go to `#alerts` for the people who fix problems, and Info notifications to `#updates` for everyone else.

See [Send Notifications to Slack](../../how-to/send_notifications_to_slack.md) to connect a workspace and add a channel.

## Members' personal settings

Slack posting does not depend on any team member's settings.
Members' [notification preferences](../../how-to/manage_notifications.md#set-your-notification-preferences) and [Do Not Disturb](../../how-to/manage_notifications.md#turn-on-do-not-disturb) control only what each member sees in OCS and receives by email.
They do not change what the team's Slack channels receive, so you do not need to ask members to adjust their settings for Slack posting to work.

## See also

- [Team Settings](index.md)
- [Notifications](../notifications.md)
- [Send Notifications to Slack](../../how-to/send_notifications_to_slack.md)
- [Manage Notifications](../../how-to/manage_notifications.md)
- [Messaging Providers](messaging_providers.md)
- [User Groups](groups.md)
