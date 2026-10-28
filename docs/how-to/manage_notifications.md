# Manage Notifications

[Notifications](../concepts/notifications.md) are the alerts Open Chat Studio sends when something needs your
attention across your chatbots. This guide covers finding and reading them, pausing them with Do Not Disturb,
and setting your notification preferences.

## Find and read your notifications

1. Look in the sidebar under **My Account** for the bell icon labeled **Notifications**.
   If you have unread notifications, a small badge shows how many.
2. Click **Notifications** to open the notifications list.
   It shows notifications from every team you belong to.
3. Use the filters at the top of the page to narrow the list —
   by team, severity level, or read/unread status.
   Toggle buttons for level, and for team if you belong to fewer than three teams, sit next to the filter panel for quick access.
4. Click any notification to open it.
   This shows the full detail, including any links to the affected chatbot or session, and automatically marks it as read.
   The breadcrumb at the top names the team the notification belongs to, since the list mixes all of your teams together.
5. Back on the list, click **Mark all read** to mark every notification currently matching your filters as read.

A notification row shows a count, like `×3`, once that same issue has
[recurred](../concepts/notifications.md#what-triggers-a-notification) more than once.

!!! tip "Reduce noise from one notification"
    If a notification keeps repeating for an issue you're already tracking, click **Mute** next to it and choose how long to silence it for —
    anywhere from a few hours to a month, or indefinitely.

## Turn on Do Not Disturb

If you know a team's chatbots are about to get noisy —
during planned maintenance, for example —
you can silence all of that team's notifications for a while:

1. On the notifications page, find the **Do Not Disturb** widget.
   It lists which of your teams are currently silenced.
2. Choose the team (or teams) to silence and how long to silence them for.
   To end it early, use the cancel option on the same widget.

Do Not Disturb only affects your own notifications, not your teammates'.

## Set your notification preferences

1. Open your profile page from the sidebar under **My Account**.
2. Find the **Notification Preferences** section.
3. Under **In-App Notifications**, toggle notifications on or off and choose the minimum severity level you want to see in the list.
4. Under **Email Notifications**, toggle email on or off and choose the minimum severity level for emails.
5. Click **Save Preferences**.

For example, you could keep in-app notifications on for everything, but only enable email for Error-level issues so you're not emailed about routine information.

## Post notifications to Slack

Team admins can send the team's notifications to a Slack channel.
See [Slack notification channels](../concepts/notifications.md#slack-notification-channels) for how this works.

**Prerequisites:**

- A Slack messaging provider connected to your team through Slack OAuth.
  If your team has none, the Notifications section shows the message "No Slack workspace is linked to this team yet."
  Click **Connect a Slack workspace** to add one.
  This link appears only if you can add messaging providers.
- The Open Chat Studio Slack app installed in your Slack workspace.
- Permission to view, add, change, and delete notification channels.
  Team admins have these permissions by default.
- Self-hosted only: your administrator has configured Slack for the OCS instance.
  Without this configuration, no messages are posted.

**Add a channel:**

1. Open **Team settings** (Manage Team) and find the **Notifications** section.
   It lists your team's notification channels.
2. Click **Add channel**.
   The button is disabled until a Slack workspace is linked.
3. In **Slack workspace**, choose one of your team's Slack messaging providers.
4. In **Channel name**, enter the Slack channel to post to, such as `#alerts`.
   The `#` is optional.
5. In **Level**, choose **Info**, **Warning**, or **Error**.
   OCS posts only notifications at or above this level.
6. Leave **Enabled** selected to start posting, or clear it to save the channel without posting.
7. Save the channel.

OCS looks up the Slack channel ID for the name when you save.
If Slack can't resolve the name, OCS stores it as you entered it.

To change or remove a channel, use the edit and delete actions in the channel table.
To pause posting without deleting a channel, clear **Enabled**.

**Example:** Create one **Error** channel that posts to `#alerts` and one **Info** channel that posts to `#updates`.
The on-call team sees only critical issues in `#alerts`, while `#updates` receives everything.

**Common issues:**

- **"This Slack workspace already has a notification channel at this level."** Edit the existing channel, or choose a different level.
- **Nothing appears in Slack.** Check that **Enabled** is selected, the Slack app is installed in the workspace, and the channel name is correct.
  On a self-hosted instance, confirm that Slack is configured.
- **The Notifications section is missing.** You need permission to view notification channels. Ask a team admin.

## See also

To learn more about how notifications are grouped, scoped, and delivered, see the [Notifications](../concepts/notifications.md) concept page.
