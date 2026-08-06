# Chat Sessions

## Overview

Chat sessions in Open Chat Studio define the scope of conversations between a participant and a chatbot within a specific channel. Sessions are isolated, ensuring data privacy and contextual continuity for the duration of an interaction.

## Session Scope

A session is uniquely defined by:

- **Participant**: The individual engaging with the chatbot.
- **Channel**: The platform through which the chat occurs (e.g., WhatsApp, Telegram, Web, Slack). See [channels](channels.md).
- **Chatbot**: The specific chatbot handling the conversation.

Each session is independent, meaning:

- The session's data is bound to that session only and is not shared with other sessions.
- When a participant interacts with a chatbot, the chatbot receives the session's history to maintain context.
- **Multi-Session Channels**: Channels such as **Web**, **API**, and **Slack** allow multiple active sessions per participant, enabling parallel conversations.
- **Single-Session Channels**: Platforms like **WhatsApp**, **Telegram**, and **SureAdhere** support only one active session per participant at a time.

Every session has a status that tracks where the participant is in their chat journey. See [Session Status](session_status.md).

## History Management

- As conversations progress, all previous messages within a session are stored as `history`, regardless of how the pipeline is configured.
- What subset of that stored history reaches an LLM node, and whether it gets summarized or trimmed as it grows, is controlled per node. See [Conversation History](pipelines/history.md) for how this works.

## Participant Data

Aside from session-specific data, Open Chat Studio maintains [participant data](participant_data.md), which:

- Persists across sessions.
- Is tied to the same `Participant, Channel, Chatbot` scope.
- Helps retain long-term participant preferences and contextual information beyond a single session.

## Anonymous Sessions

On the **Web** channel, participants can have **anonymous sessions**, where:

- Participant data is only available for the duration of the session.
- Since participant identity cannot be verified, data cannot persist beyond the session.

## Resetting Sessions

For **Single-Session Channels** like **WhatsApp** and **Telegram**, the current session continues until it is explicitly ended.

Sessions can be reset either [manually](../how-to/reset_sessions.md#manual-reset-of-a-session) by the participant or [automatically](../how-to/reset_sessions.md#reset-sessions-automatically).

For task-focused details, see [How to reset sessions](../how-to/reset_sessions.md).
