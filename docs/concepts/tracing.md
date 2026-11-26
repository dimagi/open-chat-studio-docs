# Tracing

Tracing records what a chatbot did on each conversation turn.
Chatbot developers use traces to find out why a chatbot gave a particular answer and to debug turns that went wrong.

Open Chat Studio records a trace for every turn, with no setup.
These docs call this builtin tracing; it is not a setting you turn on.

## Builtin Tracing

A trace is recorded automatically for every conversation turn.
A trace's detail page shows:

- Input and output — the participant's message and the chatbot's reply, so you can see what the chatbot was asked and what it said.
- Latency — how long the turn took, so you can spot slow turns.
- Token usage and cost, LLM calls, and tool calls — what the turn used and where, so you can find expensive or looping turns.
- Session and participant data — their state at the time of the turn, so you can see what the chatbot knew when it answered.
- Changes — what the turn added, removed, or modified in the data, so you can find unexpected updates.
- [Custom Action requests](../tech-hub/custom_action/tracing.md) — the HTTP requests a Custom Action made, so you can debug one that returns errors or unexpected data.

Usage figures cover all [LLM nodes](pipelines/nodes.md#llm-node) and [LLM router nodes](pipelines/router_nodes.md#llm-router-node) in the [pipeline](pipelines/index.md).
A pipeline with neither shows "—" for all of them.
Token counts come from the model provider, so a turn that fails partway may show partial or empty values.

Builtin tracing does not record the detail of individual LLM calls, tool calls, or retrieval steps.  
To see those, use [Langfuse Tracing](langfuse_tracing.md).

### Traces List

**:fontawesome-solid-magnifying-glass-location: Traces**, listed under **:fontawesome-solid-comments: Chatbots** in the navigation menu, opens a list of every trace recorded for your team.
Use it to find a conversation turn that went wrong, or to compare how a chatbot, session, or participant behaved across turns.
Filters narrow the list.
You can also describe a filter in plain English (see [Filtering Tables with Natural Language](../how-to/nl_filter.md)).

You can reach a single trace or a filtered list from several places:

- The **:fontawesome-solid-bars-staggered: View Traces** button on a session's transcript page opens the list already filtered to that session.
- On a session's **Messages** tab, hover over a message and select its Open Chat Studio trace icon (:fontawesome-solid-diagram-project:) to open that message's trace.
  The icon is greyed out when no trace was recorded for the message.
- On the chatbot list, select a chatbot's **Trends (last 24h)** chart to open the list filtered to that chatbot.
- The trace detail page has links to the session's, chatbot's, and participant's traces.

The **:fontawesome-solid-bars-staggered: View Traces** button and the message trace icons (:fontawesome-solid-diagram-project:) appear only for users with permission to view traces.

## See also

- [Langfuse Tracing](langfuse_tracing.md)
- [Configure Langfuse Trace Sampling](../how-to/configure_langfuse_trace_sampling.md)
- [Sessions](sessions.md)
- [Participant Data](participant_data.md)
