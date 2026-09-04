# Send a broadcast message

A broadcast is a one-off message you send to every participant of a chatbot, on
one or more of its channels, without waiting for them to message the bot first.
Use it to share an announcement, a service update, or a reminder.

## Prerequisites

- You need the **Can Invite Participants** permission on the team — see the
  [permissions table][groups] for which roles have it.
- The chatbot needs at least one participant-facing channel connected — for
  example Telegram, WhatsApp, Slack, or Email.

## Send a broadcast

1. Open the chatbot.
2. Click **Broadcast message**.
3. In the dialog, tick the checkbox for each channel you want to send on. You
   can select more than one.
4. Type your message in the text box. The counter below it shows how many
   characters you have left.
5. Click **Send**.

Sending queues the broadcast for delivery in the background, so it may take a
short while to reach everyone after you click **Send**.

## Which channels you can choose

The dialog only lists the chatbot's own messaging channels — the platforms
your participants message the bot on, such as Telegram, WhatsApp, or Email.

- The chatbot's API, Web, and Evaluations platforms do not support broadcast messages.
- Disabled channels are left out too.

!!! note "A broadcast only reaches participants who have messaged the bot before"
    On each channel you select, the broadcast is delivered to participants
    using the address from their most recent conversation with the bot on
    that channel. If someone has never messaged the bot on a particular
    channel, OCS has no address to deliver to, so the broadcast can't reach
    them there — even if they've messaged the bot on a different channel.

## Message length and formatting

The message box enforces a character limit — the same limit WhatsApp message
templates use — shown by the live counter in the dialog.

If one of your channels is WhatsApp, then OCS collapses line breaks and repeated spaces in your
message down to single spaces, so the broadcast always arrives as a single
paragraph. This happens because WhatsApp message templates reject messages
that contain line breaks, and the same message needs to go out over every
channel you picked. The dialog warns you about this before you send.

## Sending to WhatsApp

If you tick a WhatsApp channel, the dialog shows a warning that your
WhatsApp provider needs a `new_bot_message` message template configured in
Meta. This is because a broadcast isn't a reply — it can go out at any time,
including outside WhatsApp's 24-hour customer-service window, and WhatsApp
only allows messages outside that window if they use an approved template.

See [Out-of-service-window template messages][whatsapp-template] for how to
create and approve the `new_bot_message` template in Meta Business Manager.
Without it, broadcasts sent to participants who are outside the service
window will fail to deliver.

## See also

- [Channels][channels-concept] — what channels are and how disabling one works
- [Disable a channel][disable]
- [Deploying your chatbot to different channels][deploy]
- [Set Up WhatsApp with Meta Cloud API][whatsapp-meta]

[groups]: ../concepts/team/groups.md
[deploy]: ./deploy_to_different_channels.md
[disable]: ./disable_a_channel.md
[disabling-concept]: ../concepts/channels.md#disabling-a-channel
[channels-concept]: ../concepts/channels.md
[whatsapp-meta]: ./whatsapp_meta_cloud_api.md
[whatsapp-template]: ./whatsapp_meta_cloud_api.md#out-of-service-window-template-messages
