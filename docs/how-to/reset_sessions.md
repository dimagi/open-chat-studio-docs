---
title: How to reset sessions
---

# How to reset sessions

Use this guide to end a current [session](../concepts/sessions.md) and start a new one.

## Before you begin

- Confirm which [channel](../concepts/channels.md) your chatbot uses.
- Resets can be done [manually](#manual-reset-of-a-session) or [automatically](#reset-sessions-automatically).

!!! note

    Resetting a session clears the conversation history — the bot will have no memory of previous exchanges. Participant data is not removed.

## Manual reset of a session

### Participant reset manually from chat channel

1. As a participant, view the conversation in the chatbot channel
2. Send `/reset` (case-insensitive) as a text command
3. Continue chatting to start a fresh session.

This command is available on all channels except **Web Chat Widget** and **Slack**.

### Participant reset manually from the Web Chat Widget

This allows participants to customize how the transition between sessions occurs.

1. As a participant, view the chat widget on the web chat interface.
2. Click the "End chat" button.
3. Enter a chat message for the new session.

### OCS User reset manually from the OCS Admin UI

When viewing the session detail on the Chatbot Review page, an OCS user with permission to manage sessions has two options:

- **End Session** — ends the current session. This does not start a new one.
- **New Session** — ends the current session and starts a new one. This option is only available for non-Web channels.

## Reset sessions automatically

For details on how to end sessions from a chatbot see [Session Status](../concepts/session_status.md#ending-sessions-from-a-chatbot)

### Reset automatically via API

Use this when your integration controls when conversations should restart.

 - When using the [Trigger Bot Message](https://openchatstudio.com/api/v1/docs/#tag/Channels/operation/trigger_bot_message) API, you can set `"start_new_session": true`, which will end the current session and start a new one before messaging the participant.

## Related concepts

- [Chat Sessions](../concepts/sessions.md)
- [Session Status](../concepts/session_status.md#pending_review)
