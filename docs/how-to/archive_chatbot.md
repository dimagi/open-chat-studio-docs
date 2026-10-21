# Archive and Un-archive a Chatbot

Archive a chatbot to retire it without losing it, and un-archive it later to bring it back.
This guide covers both tasks and explains what an un-archive restores and what it does not.

## Prerequisites

- You have permission to change chatbots.

## Archive a chatbot

1. Open the chatbot.
2. Go to **Settings**.
3. Click **Archive** and confirm.

Archiving releases the chatbot's channel identifiers, such as a Telegram bot token, so another chatbot can use them.
It also deletes the chatbot's scheduled messages.

## Un-archive a chatbot

1. Open the archived chatbot.
   The **Archived** badge appears on its detail page.
2. Click **Un-archive**, beside the **Archived** badge.
3. Read the dialog.
   It states that the chatbot and all its versions are restored.
   It also states that scheduled messages deleted at archive time cannot be restored.
4. Optionally, select the checkbox to reconnect the chatbot's channels.
   The checkbox is off by default.
5. Confirm.

## What the un-archive restores

| Item | Result |
|---|---|
| Chatbot | Restored. |
| Versions | All versions are restored. |
| Channels | Stay disconnected unless you select the checkbox. |
| Scheduled messages | Not restored. Archiving deleted them. |

## Reconnecting channels

When you select the checkbox, OCS checks each channel again.
Archiving released the channel identifiers, so another chatbot may now use one.

- A channel whose identifier is still free reconnects.
- A channel whose identifier another chatbot now uses is skipped.
  A warning message names each skipped channel.
- Slack channels are always skipped.
  Reconnect them by hand.
  See [Deploy chatbot to Slack](./deploy_slack_channel.md).

To reconnect a skipped channel, free its identifier on the other chatbot, then add the channel again.
See [Deploying your chatbot to different channels](./deploy_to_different_channels.md).

## Common issues

- **The Un-archive button is missing.** You may not have permission to change chatbots.
- **A channel is still disconnected after un-archiving.** You did not select the checkbox, the identifier is in use by another chatbot, or it is a Slack channel.
- **Scheduled messages are gone.** Archiving deletes them and un-archiving cannot bring them back.
  Create them again.
  See [Schedule Reminders](./reminders.md).

## See also

- [Deploying your chatbot to different channels](./deploy_to_different_channels.md)
- [Disable a channel](./disable_a_channel.md)
