---
title: How to reset sessions
---

# How to reset sessions

Use this guide to end a current [session](../concepts/sessions.md) and start a new one. Resets can be done [manually](#user-initiated-manual-reset-of-a-session) or [automatically](#reset-sessions-automatically).

## Before you begin

- Confirm which [channel](../concepts/channels.md) your chatbot uses.
- For **Web Chat Widget** and **Slack**, use the session reset button in the UI.
- For messaging channels (such as WhatsApp and Telegram), use `/reset` or an automatic method.

!!! note
    Resetting a session ends the current conversation history. Participant data is not removed.

## User-Initiated Manual Reset of a session

### Reset manually from chat channel

1. As a participant, view the conversation in the chatbot channel
2. Send `/reset` (case-insensitive) as a text command
3. Continue chatting to start a fresh session.

This command is available on channels except **Web Chat Widget** and **Slack**.

### Reset manually from the web UI

The "New Chat" button provides more control over the session reset process compared to the `/reset` command, allowing users to customize how the transition between sessions occurs.

1. As a participant, view the chat widget on the web interface.
2. Click the session reset button.
3. Choose whether to trigger [end conversation events](../concepts/events.md) or skip them
4. Enter a chat message for the new session.

If your chatbot has been configured with a seed message, this is pre-filled and then can be edited by the user.

### Reset manually from the Admin UI

When viewing the "Chatbot Review" screen, the "End Session" button ends the current session and creates a new one for the same participant and channel.

## Reset sessions automatically
There are two ways to automatically reset a session:

### Reset automatically with Events

Use this when session resets should happen based on lifecycle conditions.

- You can configure an event to end the current session when the event is triggered. This will not automatically create a new session; however, if the user sends a message after the session is ended, a new session will be created.
- When this event fires, the current session ends. A new session starts when the participant sends the next message.
- For more on event types and actions, see [Events](../concepts/events.md).

### Reset automatically via API

Use this when your integration controls when conversations should restart.

 - When using the [Trigger Bot Message](https://openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) API, you can set `"start_new_session": true`, which will end the current session and start a new one before messaging the user.

## Related concepts

- [Chat Sessions](../concepts/sessions.md)
- [Session Status](../concepts/session_status.md)
