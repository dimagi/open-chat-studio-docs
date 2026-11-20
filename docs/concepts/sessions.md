# Sessions

## Overview

In OCS, a session is a conversation thread between a participant and your chatbot on a specific channel.
Sessions are isolated, which keeps data private and preserves context for the duration of a conversation.

## Session Scope

A session is uniquely defined by:

- **Participant**: The individual engaging with the chatbot.
- **Channel**: The platform through which the chat occurs (e.g., WhatsApp, Telegram, Web, Slack).
  See [channels](channels.md).
- **Chatbot**: The specific chatbot handling the conversation.

Each session is independent, meaning:

- The session's data is bound to that session only and is not shared with other sessions.
- When a participant interacts with a chatbot, the chatbot receives the session's history to maintain context.
- **Multi-Session Channels**: Channels such as **Web**, **API**, and **Slack** allow multiple active sessions per participant, enabling parallel conversations.
- **Single-Session Channels**: Platforms like **WhatsApp**, **Telegram**, and **SureAdhere** support only one active session per participant at a time.

Every session has a status that tracks the progress of the conversation.
See [Session Status](session_status.md).

## Messages

A **message** is one piece of content within a [session](#overview): a human message from the participant, or an AI message from the chatbot.

## History Management

- As conversations progress, all previous messages within a session are stored as `history`, regardless of how the [pipeline](pipelines/index.md) is configured.
- What subset of that stored history reaches an [LLM node](pipelines/nodes.md#llm-node), and whether it is summarized or trimmed as it grows, is controlled per node.
  See [Conversation History](pipelines/history.md) for how this works.

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

## Reviewing Sessions

Each session records its participant, chatbot and messages.
A session and its messages can carry [tags](tags.md), and a session can be added to [annotation queues](annotations/queues.md) for human review.
To find sessions and open them, see [Find and Review Sessions](../how-to/all_sessions.md).

## See also

- [Find and Review Sessions](../how-to/all_sessions.md)
- [Session Status](session_status.md)
- [Tags](tags.md)
- [Participant Data](participant_data.md)
- [Channels](channels.md)
- [Conversation History](pipelines/history.md)
- [Annotation Queues](annotations/queues.md)
