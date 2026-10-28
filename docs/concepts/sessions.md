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

Every session has a status that tracks the progress of the conversation. See [Session Status](session_status.md).

## History Management

- As conversations progress, all previous messages within a session are stored as `history`, regardless of how the [pipeline](pipelines/index.md) is configured.
- What subset of that stored history reaches an [LLM node](pipelines/nodes.md#llm-node), and whether it is summarized or trimmed as it grows, is controlled per node. See [Conversation History](pipelines/history.md) for how this works.

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

## Annotation Queues on the Sessions List

The sessions list shows which [annotation queues](annotations/queues.md) each session is in, so you don't need to open the session.
The **Annotation Queues** column shows one badge per queue, in the format `Queue · Status`, where the status is the session's item status in that queue.
Queues of every status appear, and only session-level items count.

To filter by membership, use the **Annotation Queue** filter:

- Select one or more queues to show sessions in any of them.
- Select **Not in any queue**, the first value in the list, to show sessions that are in no queue.
- Select **Not in any queue** together with queue names to combine them with OR.
  For example, **Not in any queue** and **Safety QA** shows unreviewed sessions plus the sessions already in Safety QA.
- Use the **excludes** operator to get the complement of the selection.

The filter stores queue IDs, so saved filters keep working after you rename a queue.
The same filter is available in the dataset session pickers, the participants page and the queue's **Add Sessions** picker.

!!! note
    The column and filter appear only for teams with the human annotations feature flag.
    The column is not shown in the sessions table on the participant details page or on the Session Analysis page.
    The per-chatbot sessions page shows it.

The sessions CSV export has a matching **Annotation Queues** column after **Session Tags**, for example `Safety QA (Completed), Tone (Pending)`.
Columns after it move one position to the right.
The header is always present so the layout is stable, but cells are empty for teams without the feature flag.

## Tags on the Sessions List

The **Tags** column shows only [tags](tags.md) applied to the session itself, followed by a tag icon (:fontawesome-solid-tags:).
A session whose tags are all on individual messages shows just the icon.
Open the session to see the tags on its messages.

To find sessions by tag, use the **Tags** filter.
It matches sessions that carry the tag on the session itself or on any of the messages in the session.

ags come from people, pipeline nodes and [tag rules](evaluations/tag_rules.md), which tag sessions or messages automatically when an LLM evaluator's output meets a condition.
For example, filter by a `goal-not-met` tag to review only the sessions an evaluation flagged, instead of reading every result.

## See also

- [Session Status](session_status.md)
- [Tags](tags.md)
- [Participant Data](participant_data.md)
- [Channels](channels.md)
- [Conversation History](pipelines/history.md)
- [Annotation Queues](annotations/queues.md)
