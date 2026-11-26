# Langfuse Tracing

[Langfuse][langfuse] is an optional external tracing provider.
Connect it when you need more detail than the [builtin trace](tracing.md) gives, such as each LLM call inside a conversation turn.

## What Langfuse Adds

[Builtin tracing](tracing.md) stops at the turn level.
Langfuse also records each step inside a turn, called a span.
A span is one LLM call, tool call, or retrieval step.

When Langfuse is configured for a chatbot, Open Chat Studio sends detailed trace data to Langfuse and adds span-level information to the trace detail page.
Choosing the trace provider is a chatbot setting, so it takes effect for participants only after you publish a version that includes it.
Editing the provider itself, such as its team-wide sample rate, applies to new conversation turns straight away.

## Spans on the Trace Detail Page

With Langfuse configured, the trace detail page adds a **Langfuse Trace** panel and a **View in Langfuse** link to the same trace in Langfuse.
The panel lists every span in the turn on the left.
Select a span to see its input and output on the right, as readable text or raw JSON.
It opens on the first span with an error, or on the first span if none has an error, so the likely cause is visible first.

If a trace has no Langfuse data, or Langfuse can't be reached, the page says so and the rest of the page still works.

## Trace Sampling

A high-traffic chatbot can send a lot of trace volume to Langfuse.
Trace sampling sends only a fraction of turns, set as a sample rate from `0.0` to `1.0`.
For example, `0.1` sends roughly 1 in 10 turns.
Set a team-wide rate on the Langfuse provider (**Sample Rate**), and override it for one chatbot in its settings (**Trace sample rate**).
A blank chatbot rate inherits the provider's rate, and `0.0` turns off Langfuse for that chatbot.
Builtin tracing still records every turn, because sampling only affects what is sent to Langfuse.

For the steps, see [Configure Langfuse Trace Sampling](../how-to/configure_langfuse_trace_sampling.md).

## See also

- [Tracing](tracing.md)
- [Configure Langfuse Trace Sampling](../how-to/configure_langfuse_trace_sampling.md)
- [Integrations](team/integrations.md)

[langfuse]: https://langfuse.com/docs
