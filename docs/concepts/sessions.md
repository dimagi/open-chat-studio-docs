# Chat Sessions

## Overview

Chat sessions in Open Chat Studio define the scope of conversations between a user and a chatbot within a specific channel. Sessions are isolated, ensuring data privacy and contextual continuity for the duration of an interaction.

## Session Scope

A session is uniquely defined by:

- **User**: The individual engaging with the chatbot.
- **Channel**: The platform through which the chat occurs (e.g., WhatsApp, Telegram, Web, Slack). See [channels](channels.md).
- **Chatbot**: The specific chatbot handling the conversation.

Each session is independent, meaning:

- The session's data is bound to that session only and is not shared with other sessions.
- When a user interacts with a chatbot, the bot receives the session's history to maintain context.
- **Multi-Session Channels**: Channels such as **Web**, **API**, and **Slack** allow multiple active sessions per user, enabling parallel conversations.
- **Single-Session Channels**: Platforms like **WhatsApp**, **Telegram**, and **SureAdhere** support only one active session per user at a time.

## History Management

- As conversations progress, all previous messages within a session are stored as `history`.
- If the session history exceeds a predefined maximum length, it is **summarized**, and the bot will only receive:
  - A summary of older interactions.
  - The most recent exchanges to maintain context.

## Participant Data

Aside from session-specific data, Open Chat Studio maintains [participant data](participant_data.md), which:

- Persists across sessions.
- Is tied to the same `User, Channel, Chatbot` scope.
- Helps retain long-term user preferences and contextual information beyond a single session.

## Anonymous Sessions

On the **Web** channel, users can have **anonymous sessions**, where:

- Participant data is only available for the duration of the session.
- Since user identity cannot be verified, data cannot persist beyond the session.

## Resetting Sessions

For **Single-Session Channels** like **WhatsApp** and **Telegram**, the current session continues indefinitely. However, sessions can be reset either manually by the user or automatically using [Events](events.md) or the API. When a session is reset:

- The current session is marked as completed.
- A new session is started with a fresh history.

This means that, aside from participant data, the bot loses all information about the previous conversation — including the fact that it even took place.

### Manual resets

The chat user can manually reset the session (start a new session) by sending the `/reset` command. This command is available on all channels except **Web** and **Slack**.

### Automatic resets

There are two ways to automatically reset a session:

- **Events**: You can configure an event to end the current session when the event is triggered. This will not create a new session automatically however if the user sends a message after the session is ended, a new session will be created. See [Events](events.md).
- **API**: When using the [Trigger Bot Message](https://chatbots.dimagi.com/api/docs/#tag/Channels/operation/trigger_bot_message) API you can set `"start_new_session": true` which will end the current session and start a new one before messaging the user.

By structuring sessions in this way, Open Chat Studio ensures privacy-conscious, context-aware, and seamless interactions across different communication channels.
