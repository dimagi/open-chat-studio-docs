# Send Notifications to Slack

This guide shows how to post your team's [notifications](../concepts/notifications.md) to a Slack channel.
For how notification channels and levels work, see [Team Settings: Notifications](../concepts/team/notifications.md).

## Prerequisites

- A Slack [messaging provider](../concepts/team/messaging_providers.md) connected to your team through Slack OAuth.
  See [Connect a Slack workspace](#connect-a-slack-workspace) if your team doesn't have one.
- The Open Chat Studio Slack app installed in that Slack workspace.
- Permission to manage notification channels:

    | Action                         | Permission required          |
    |--------------------------------|------------------------------|
    | View the Notifications section | `view_notificationchannel`   |
    | Add a channel                  | `add_notificationchannel`    |
    | Edit a channel                 | `change_notificationchannel` |
    | Delete a channel               | `delete_notificationchannel` |

    Team admins have these permissions by default. See [User Groups](../concepts/team/groups.md).

!!! note "Self-hosted instances"

    Whoever runs the instance must configure Slack first, or nothing is posted to Slack.
    See [Configure Slack for Notifications on a Self-Hosted Instance](../tech-hub/slack_notifications_self_hosted.md).

## Connect a Slack workspace

If your team has no Slack workspace, the **Notifications** section shows this notice above the channel table:
"No Slack workspace is linked to this team yet. Notification channels need one to post messages."
The **Add channel** button is disabled until a workspace is linked.

1. Click **Connect a Slack workspace** in the notice.
   This link appears only if you have permission to add messaging providers and Slack is configured on the instance.
   If you don't see it, your [User Group](../concepts/team/groups.md) may not include that permission.
   On a self-hosted instance, check that [Slack is configured](../tech-hub/slack_notifications_self_hosted.md).
2. Follow the Slack OAuth flow to add a Slack messaging provider.
   See [Configure a messaging provider](../tutorials/configure_msg_providers.md).
3. Return to **Manage Team** > **Notifications**.
   The **Add channel** button is now available.

## Add a channel

1. Open **Manage Team** and select **Notifications** (bell icon).
2. Click **Add channel**.
3. In **Slack workspace**, choose one of your team's Slack messaging providers.
4. In **Channel name**, enter the Slack channel to post to, such as `#alerts`.
   The `#` is optional.
5. In **Level**, choose **Info**, **Warning** or **Error**.
   OCS posts only notifications at or above this level.
6. Leave **Enabled** selected to start posting, or clear it to save the channel without posting.
7. Save the channel.

When you save, OCS checks the channel name with Slack.
If Slack can't find the channel, OCS still saves the name as you entered it.

To send different levels to different audiences, add one channel for each level.
See [Notification channels](../concepts/team/notifications.md#notification-channels) for an example.

## Edit, disable or delete a channel

Use the actions in the channel table:

- To change the workspace, channel name or level, edit the channel.
- To stop posting but keep the channel, edit it and clear **Enabled**.
- To remove the channel, delete it.

## What a Slack message contains

Each notification is posted as a Slack message containing:

- The notification title, as the message header
- The team name
- The level
- The notification message, under **Details**
- Any links attached to the notification
- A **View in OCS** link to the notification page

## Troubleshooting

- **"This Slack workspace already has a notification channel at this level."**
  A team can have only one channel for each workspace and level.
  Edit the existing channel, or choose a different level.
- **Nothing appears in Slack.**
  Check that **Enabled** is selected, the channel name is correct, and the Open Chat Studio Slack app is installed in the workspace.
  Check that the notification's level is at or above the channel's level.
  On a self-hosted instance, check that [Slack is configured](../tech-hub/slack_notifications_self_hosted.md).
- **The Add channel button is disabled.**
  Your team has no Slack workspace linked. See [Connect a Slack workspace](#connect-a-slack-workspace).
- **The Notifications section is missing.**
  Your [User Group](../concepts/team/groups.md) needs the `view_notificationchannel` permission.

## See also

- [Team Settings: Notifications](../concepts/team/notifications.md)
- [Manage Notifications](manage_notifications.md): your personal notification settings
- [Notifications](../concepts/notifications.md)
- [Messaging Providers](../concepts/team/messaging_providers.md)
