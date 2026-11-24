# Tracing

Tracing records what a chatbot did on each conversation turn.
Chatbot developers use traces to find out why a chatbot gave a particular answer and to debug turns that went wrong.

Open Chat Studio (OCS) records a trace for every turn, with no setup.
These docs call this builtin tracing; it is not a setting you turn on.

For more detail inside a turn, you can also connect an external provider (see [Langfuse External Tracing](#langfuse-external-tracing)).

## Builtin Tracing

A trace is recorded automatically for every conversation turn.
Each trace captures:

- Input and Output — the participant's message and the chatbot's reply
- Duration — how long the turn took
- Session data and Participant data — the state of each at the time of the turn
- Participant data changes — what the turn added, removed, or modified
- Performance metrics — LLM usage for the turn
- [Custom Action requests](#custom-action-requests) — the HTTP requests a Custom Action made

### Traces List

**Traces**, listed under **Chatbots** in the navigation menu, opens a list of every trace recorded for your team.
Use it to find a conversation turn that went wrong, or to compare how a chatbot, session, or participant behaved across turns.
Filters narrow the list.
You can also describe a filter in plain English (see [Filtering Tables with Natural Language](../how-to/nl_filter.md)).

You can reach a single trace or a filtered list from several places:

- The **View Traces** button on a session's transcript page opens the list already filtered to that session.
- On a session's **Messages** tab, hover over a message and select its trace icon to open that message's trace.
  The icon is greyed out when no trace was recorded for the message.
- On the chatbot list, select a chatbot's **Trends (last 24h)** chart to open the list filtered to that chatbot.
- The trace detail page has links to the session's, chatbot's, and participant's traces.

Trace links appear only for users with permission to view traces.

### Trace Detail Page

The top of the trace detail page shows summary cards with the resource usage of the turn:

- **Total latency**: how long the turn took, with the trace status.
- **Tokens**: total tokens used, split into input (prompt) and output (completion), with a breakdown per model.
- **LLM turns**: the number of LLM calls made during the turn.
- **Tool calls**: the number of tool invocations, each counted separately.

Metrics cover all [LLM nodes](pipelines/nodes.md#llm-node) and [LLM router nodes](pipelines/router_nodes.md#llm-router-node) in the [pipeline](pipelines/index.md).
A pipeline with neither shows "—" for all metrics.
Token counts come from the model provider, so a turn that fails partway may show partial or empty values.

Below the participant data, a **Changes during this trace** section shows what the turn changed.
Green marks data that was added, red data that was removed, and yellow data that was modified.
The section is hidden when nothing changed.

### Custom Action Requests

The trace detail page lists the HTTP requests a [Custom Action](../tech-hub/custom_action/index.md) made, so you can debug one that returns errors or unexpected data.
See [Custom Action Tracing](../tech-hub/custom_action/tracing.md).

## Langfuse External Tracing

Builtin tracing records top-level information and Custom Action requests only.
It does not include individual LLM calls, other tool calls, or retrieval steps.
Each of those steps is a span, one step within a trace.

[Langfuse][langfuse] is an optional external tracing provider that records spans.
When Langfuse is configured for a chatbot, OCS sends detailed trace data to Langfuse and adds span-level information to the trace detail page.

Tracing begins automatically with the next conversation after you configure a Langfuse provider.

### Spans on the trace detail page

With Langfuse configured, the trace detail page adds a **Langfuse Trace** panel and a **View in Langfuse** link to the same trace in Langfuse.
The panel lists every span in the turn on the left.
Select a span to see its input and output on the right, as readable text or raw JSON.
It opens on the first span with an error, or on the first span if none has an error, so the likely cause is visible first.

If a trace has no Langfuse data, or Langfuse can't be reached, the page says so and the rest of the page still works.

### Trace Sampling

A high-traffic chatbot can send a lot of trace volume to Langfuse.
Trace sampling sends only a fraction of turns, set as a sample rate from `0.0` to `1.0`.
For example, `0.1` sends roughly 1 in 10 turns.
Set a team-wide rate on the Langfuse provider (**Sample Rate**), and override it for one chatbot in its settings (**Trace sample rate**).
Builtin tracing still records every turn, because sampling only affects what is sent to Langfuse.

For the steps, see [Configure Langfuse Trace Sampling](../how-to/configure_langfuse_trace_sampling.md).

## See also

- [Configure Langfuse Trace Sampling](../how-to/configure_langfuse_trace_sampling.md)
- [Sessions](sessions.md)
- [Participant Data](participant_data.md)
- [Notifications](notifications.md)

[langfuse]: https://langfuse.com/docs
