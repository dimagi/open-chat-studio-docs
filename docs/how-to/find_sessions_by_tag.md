# Find Sessions by Tag

This guide shows you how to find the sessions that carry a tag, and how to see which message carries it.
It applies to [session tags and message tags](../concepts/tags.md#types-of-tags).

For example, a `billing` tag is on the replies of your billing LLM node.
Filtering by `billing` lists every session that included a billing reply, so you can review them together.

## Prerequisites

- A chatbot with tagged sessions or messages.
  See [Tags](../concepts/tags.md) for the ways tags are added.

## Filter the sessions by tag

1. Select **All sessions** in the left menu.
2. Use the **Tags** filter to select the tag, for example `billing`.

The list shows the sessions that carry the tag on the session itself or on any of its messages.
The **Tags** column shows session tags only.

Tags come from people, pipeline nodes and [tag rules](../concepts/evaluations/tag_rules.md).
For example, filter by a `goal-not-met` tag to review only the sessions an evaluation flagged, instead of reading every result.

## Find the tagged message

The **All Sessions** screen does not show which message carries the tag.

1. Click the **Session Details** button in a session's row in the filtered list.
   The **Session Transcript** opens.
2. Find the tag on the message.
   Session tags appear in the **Tags** bar at the top instead.

## Common issues

- **The tag does not appear in the Tags column.**
  The tag is on a message.
  Follow the steps in [Find the tagged message](#find-the-tagged-message).

## See also

- [Find and Review Sessions](all_sessions.md)
- [Tags](../concepts/tags.md)
- [Tag Rules](../concepts/evaluations/tag_rules.md)
