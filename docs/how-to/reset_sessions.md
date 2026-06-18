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
    Resetting a session clears the conversation history — the bot will have no memory of previous exchanges. Participant data is not removed.

## User-Initiated manual reset of a session

### Reset manually from chat channel

1. As a participant, view the conversation in the chatbot channel
2. Send `/reset` (case-insensitive) as a text command
3. Continue chatting to start a fresh session.

This command is available on all channels except **Web Chat Widget** and **Slack**.

### Reset manually from the web UI

This allows users to customize how the transition between sessions occurs.

1. As a participant, view the chat widget on the web chat interface.
2. Click the "End chat" button.
3. Choose whether to trigger [end conversation events](../concepts/events.md) or skip them
4. Enter a chat message for the new session.

If your chatbot has been configured with a seed message, this is pre-filled and then can be edited by the user.

### Reset manually from the OCS Admin UI

When viewing the session detail, the "End Session" button ends the current session.
- For more on ending sessions see [Session Status](../concepts/session_status.md#pending_review)

## Reset sessions automatically

For details on how to end sessions from a chatbot see [Session Status](../concepts/session_status.md#ending-sessions-from-a-chatbot)

### Reset automatically via API

Use this when your integration controls when conversations should restart.

 - When using the [Trigger Bot Message](https://openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) API, you can set `"start_new_session": true`, which will end the current session and start a new one before messaging the user.

## Related concepts

- [Chat Sessions](../concepts/sessions.md)
- [Session Status](../concepts/session_status.md#pending_review)
