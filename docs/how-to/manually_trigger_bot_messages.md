---
title: Manually Trigger Bot Messages
description: Learn how to manually send bot-initiated messages to participants
---

# Manually Trigger Bot Messages

The manual bot trigger feature allows you to proactively send bot-initiated messages to participants from the participant management interface. This is useful for scenarios where you want to initiate a conversation or send a message to a participant without waiting for them to message the bot first.

## When to Use Manual Bot Triggers

Manual bot triggers are particularly useful for:

- **Proactive engagement**: Starting conversations with participants on channels like WhatsApp, Telegram, or SMS
- **Follow-up messages**: Sending reminders or follow-ups to participants
- **Re-engagement**: Reaching out to participants who haven't interacted with the bot recently
- **Testing**: Testing bot behavior by manually initiating conversations

!!! note "Alternative Methods"
    Open Chat Studio provides other ways to trigger bot messages automatically:

    - **[Events](../concepts/events.md)**: Configure events to automatically trigger bot messages based on specific conditions or timeouts
    - **[API](../api/index.md)**: Use the [Trigger Bot Message API](https://openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) to programmatically send messages to participants

## Accessing the Manual Bot Trigger

To manually trigger a bot message for a participant:

1. Navigate to the **Chatbot** you want to work with
2. Go to the **Participants** tab or list page
3. Click on a specific participant to view their details
4. On the participant details page, you'll find the **Trigger Bot Message** option

## Sending a Manual Trigger

Once you've accessed the manual bot trigger interface:

1. Review the participant's information to ensure you're triggering the message for the correct participant
2. Select the appropriate channel if the participant has multiple active channels
3. Click the **Trigger Bot Message** button
4. The bot will initiate a message to the participant based on your chatbot's configuration

The message content and behavior will follow your chatbot's configured prompts and pipeline logic, just as if the participant had initiated the conversation.

## Important Limitations

### Web Channel Restriction

!!! warning "Web Channel Not Supported"
    You cannot manually trigger bot messages for participants on the **Web channel**. This limitation exists because:

    - Users may have closed their browser session, making it impossible to deliver the message
    - Starting new web sessions doesn't make sense since participants won't have a way to access the new session without a specific link

    For web-based participants, consider using other communication channels or encourage users to initiate conversations themselves.

### Channel Requirements

- The participant must have an active channel configuration (e.g., WhatsApp, Telegram, SMS)
- The messaging provider for the channel must be properly configured
- The participant must be reachable on the selected channel

## Supported Channels

Manual bot triggers work with the following channels:

- **WhatsApp**: Participants will receive a message through WhatsApp
- **Telegram**: Messages are sent via Telegram
- **SMS/SureAdhere**: Text messages are delivered to the participant's phone number
- **Facebook Messenger**: Messages are sent through Facebook Messenger
- **Slack**: Messages are delivered in the configured Slack channel

For more information about channels, see [Channels](../concepts/channels.md) and [Deploy to Different Channels](deploy_to_different_channels.md).

## Understanding Sessions

When you manually trigger a bot message:

- If the participant has an existing active session on a single-session channel (like WhatsApp or Telegram), the message will be sent within that session
- If no active session exists, a new session will be created
- For multi-session channels, a new session is always created

For more details about how sessions work, see [Chat Sessions](../concepts/sessions.md).

## Troubleshooting

### Message Not Delivered

If a manually triggered message doesn't reach the participant:

1. **Check channel configuration**: Ensure the messaging provider is properly configured in Team Settings
2. **Verify participant identifier**: Confirm the participant's phone number or platform identifier is correct
3. **Review channel status**: Check if the channel is active and not blocked by the messaging platform
4. **Check bot configuration**: Ensure your chatbot has appropriate prompts and pipeline logic configured

### Unable to Trigger on Web Channel

If you see an error when trying to trigger a message for a web channel participant, this is expected behavior. Switch to using an alternative channel or communication method.

## Best Practices

1. **Use sparingly**: Manual triggers are useful but shouldn't replace well-designed conversation flows
2. **Respect user preferences**: Ensure participants have opted in to receive proactive messages
3. **Test thoroughly**: Test manual triggers in a development environment before using in production
4. **Monitor responses**: Track how participants respond to manually triggered messages to optimize engagement
5. **Consider automation**: For recurring scenarios, use [Events](../concepts/events.md) or the [API](../api/index.md) instead of manual triggers

## Related Documentation

- [Participant Data](../concepts/participant_data.md): Learn about managing participant information
- [Chat Sessions](../concepts/sessions.md): Understand how sessions work across different channels
- [Events](../concepts/events.md): Automate bot message triggers based on conditions
- [Channels](../concepts/channels.md): Learn about different communication channels
- [API Documentation](../api/index.md): Use the API to trigger messages programmatically
