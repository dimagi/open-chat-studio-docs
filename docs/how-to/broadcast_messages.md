# Broadcast a Message to Participants

A broadcast message is a one-off message sent to every participant of a chatbot, on the channels you choose. Use it for things like announcing planned downtime, sharing an update, or letting participants know about a change to the service — without waiting for them to message the bot first.

## Before you begin

!!! note "Who can send a broadcast"
    The **Broadcast message** button is only available to team members with permission to invite participants (the `experiments.invite_participants` permission). See the [permissions table](../concepts/team/groups.md#permissions-table) for which roles include it.

- Make sure the chatbot already has at least one [channel](../concepts/channels.md) linked — see [Deploy your chatbot to different channels](deploy_to_different_channels.md) if it doesn't yet.

!!! warning "Participants must have messaged the bot before on that channel"
    A broadcast reaches a participant on a given channel only if they've already had at least one conversation with the chatbot on that channel. If someone has never messaged the bot on, say, WhatsApp, a WhatsApp broadcast can't reach them there — even if they're an active participant elsewhere.

## Broadcasting a message

1. Navigate to the chatbot's home page — the page you land on when you open the chatbot.
2. Click **Broadcast message**.
3. In the **Channels** field, select one or more of the chatbot's linked channels to send on.

    !!! info "Only the chatbot's own, active channels are listed"
        The picker only shows channels linked to this specific chatbot. It leaves out:

        - Team-wide platforms such as API, Web, and Evaluations, which don't have individual participants to broadcast to.
        - Any channel that's currently [disabled](disable_a_channel.md), since a disabled channel drops bot-initiated messages. See [Disabling a channel](../concepts/channels.md#disabling-a-channel) for what that means. Re-enable the channel first if you need to include it.

4. Enter your message. A character counter shows how much room you have left.

    !!! info "One length limit applies to every channel"
        The message is capped at the character limit WhatsApp enforces for template messages, no matter which channels you've selected. This guarantees the same message can be delivered in full on every channel you pick, rather than being truncated or split on one of them.

5. If you've selected a WhatsApp channel, the modal shows a warning that your WhatsApp provider needs a `new_bot_message` template configured. Broadcasts are sent outside WhatsApp's 24-hour customer service window, so WhatsApp requires a pre-approved template for this kind of provider-initiated message. Set the template up first if you haven't already — see [Set Up WhatsApp with Meta Cloud API](whatsapp_meta_cloud_api.md#out-of-service-window-template-messages) or [Set Up WhatsApp with Turn.io](turnio_whatsapp.md), depending on your provider.
6. Click **Send**. This button stays disabled until you've selected at least one channel and entered a message.

## What happens after you send

Sending queues a background job rather than delivering messages immediately, so a broadcast to a large audience takes some time to reach everyone and the UI doesn't show a live delivery progress count.

## Troubleshooting

**I don't see the Broadcast message button.** You need the permission to invite participants — ask a team admin to check your role against the [permissions table](../concepts/team/groups.md#permissions-table).

**A channel I expected isn't in the list.** Check whether it's [disabled](disable_a_channel.md) — disabled channels are excluded because they can't receive bot-initiated messages. Team-wide platforms (API, Web, Evaluations) never appear here, since they aren't per-participant channels.

**A participant didn't receive the broadcast.** Confirm they've messaged the chatbot on that channel before — broadcasts can only reach participants with an existing conversation on the selected channel.

## See also

- [Channels](../concepts/channels.md)
- [Disable a channel](disable_a_channel.md)
- [Deploy your chatbot to different channels](deploy_to_different_channels.md)
- [Set Up WhatsApp with Meta Cloud API](whatsapp_meta_cloud_api.md)
- [Set Up WhatsApp with Turn.io](turnio_whatsapp.md)
- [User Groups on OCS](../concepts/team/groups.md)
