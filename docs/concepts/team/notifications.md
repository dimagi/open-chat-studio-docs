# Notifications

The **Notifications** section of Team Settings lets a team post its Open Chat Studio (OCS) [notifications](../notifications.md) to Slack channels.
Slack posts are sent in addition to in-app and email notifications.

Notification channels belong to the team, not to a user.
One setup serves everyone on the team.

To find the section, open **Manage Team** and select **Notifications** (bell icon).
It lists the team's notification channels.

## Notification channels

A notification channel connects one Slack channel, such as `#alerts`, in one of the team's [Slack workspaces](messaging_providers.md) to a minimum [severity level](../notifications.md#severity-levels).
OCS posts each notification at or above that level to the channel:

| Channel level | Notifications posted    |
|---------------|-------------------------|
| Info          | Info, Warning and Error |
| Warning       | Warning and Error       |
| Error         | Error only              |

A team can have only one channel for each Slack workspace and level.
It can have several channels in the same workspace at different levels.
For example, Error notifications can go to `#alerts` for the people who fix problems, and Info notifications to `#updates` for everyone else.

You can disable a channel to stop posting without deleting it.

## What a Slack message contains

Each notification is posted as a Slack message containing:

- The notification title, as the message header
- The team name
- The level
- Any links attached to the notification
- A **View in OCS** link to the notification page

## How Slack posting relates to your personal settings

Slack posting does not depend on any team member's settings.
Your [notification preferences](../../how-to/manage_notifications.md#set-your-notification-preferences) and [Do Not Disturb](../../how-to/manage_notifications.md#turn-on-do-not-disturb) control only what you see in OCS and receive by email.
They do not change what the team's Slack channels receive.

If a message fails to post to Slack, the in-app and email notifications are still delivered.

To set up a channel, see [Send Notifications to Slack](../../how-to/send_notifications_to_slack.md).

## See also

- [Notifications](../notifications.md)
- [Send Notifications to Slack](../../how-to/send_notifications_to_slack.md)
- [Manage Notifications](../../how-to/manage_notifications.md)
- [Messaging Providers](messaging_providers.md)
- [Team Settings](index.md)
