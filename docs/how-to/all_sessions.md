# Find and Review Sessions

This guide shows you how to use the **All Sessions** screen to find [sessions](../concepts/sessions.md) and open them for review.

For example, after you change a chatbot's prompt, filter the list by that chatbot and the last seven days.
You can then open each session and read how the chatbot answered after the change.

## Prerequisites

- A chatbot with at least one session.

## Read the session list

Select **All sessions** in the left menu.
The list has one row per session, with these columns:

- **Chatbot**: the chatbot that handled the session.
- **Participant**: the person chatting with the chatbot.
- **Message Count**: how many messages the session has.
- **Last activity**: how long ago the participant last sent a message.
  Sort by this column to see the most recent conversations first.
- **Tags**: the tags on the session.
  See [Find Sessions by Tag](find_sessions_by_tag.md).
- **Annotation Queues**: the queues the session is in, and its review status in each.
  See [Filter by annotation queue](#filter-by-annotation-queue).
- **Versions**: the published chatbot versions used in the session.
  It is empty if the session only used the working version.
- **State**: how far the session has progressed, for example **Active** or **Complete**.
  See [Session Status](../concepts/session_status.md).
- **Remote Id**: the remote ID stored for the participant.
  Filter by it to find all sessions of one person when you know their remote ID.
- **Actions**: the **Session Details** button, which opens the session transcript.
  Some sessions also show a chat icon (:fontawesome-solid-comments:), the **Continue Chat** button.
  See [Continue a chat](#continue-a-chat).

## Open a session transcript

1. Find the session in the list.
   To narrow the list, see [Filter the list](#filter-the-list).
2. Click the **Session Details** button in the session's row.
   You can also click a plain table cell, such as **Message Count**.
   Hold **Ctrl** while clicking to open the transcript in a new tab.

The **Session Transcript** opens.
It shows the session's messages, the session tags in the **Tags** bar at the top, and the tags on each message.

## Continue a chat

To reply in a session yourself, click the chat icon (:fontawesome-solid-comments:), the **Continue Chat** button, in the session's **Actions** column.
The session opens in the chat widget in a popup on the page.
If a session has no chat icon, open its transcript instead.

## Filter the list

You can filter on any column.
Add filter rows by hand, or describe the sessions you want in plain English.
See [Filter Tables with Natural Language](nl_filter.md).
To filter by tag, see [Find Sessions by Tag](find_sessions_by_tag.md).

### Filter by annotation queue

The **Annotation Queues** column shows which [annotation queues](../concepts/annotations/queues.md) a session is in, so you don't need to open the session.
Each badge has the format `Queue · Status`.

To filter by membership, use the **Annotation Queue** filter:

- Select one or more queues to show sessions in any of them.
- Select **Not in any queue**, the first value in the list, to show sessions that are in no queue.
  This finds sessions nobody has reviewed yet.
- Select **Not in any queue** together with queue names to combine them.
  For example, **Not in any queue** and **Safety QA** shows unreviewed sessions plus the sessions already in Safety QA.
- Use the **excludes** operator to show the sessions that do not match the selection.

The same filter is available in the dataset session pickers and the queue's **Add Sessions** picker.

The column and filter appear only for teams with the human annotations feature flag.
The column is not shown in the sessions table on the participant details page or on the Session Analysis page.

The sessions CSV export has a matching **Annotation Queues** column after **Session Tags**, for example `Safety QA (Completed), Tone (Pending)`.
Columns after it move one position to the right.
The header is always present, but the cells are empty without the flag.

## Common issues

- **The Annotation Queues column or filter is missing.**
  Your team does not have the human annotations feature flag, or you are on a page that does not show the column.

## See also

- [Chat Sessions](../concepts/sessions.md)
- [Session Status](../concepts/session_status.md)
- [Tags](../concepts/tags.md)
- [Find Sessions by Tag](find_sessions_by_tag.md)
- [Annotation Queues](../concepts/annotations/queues.md)
- [Filter Tables with Natural Language](nl_filter.md)
