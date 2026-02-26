# Tracing Providers

LLM tracing involves capturing a model's output and decision-making process. Tracing providers offer platforms to visualize and analyze these traces, aiding bot developers in understanding their chatbot's behavior.

Open Chat Studio (OCS) has built-in support for the following providers:

- [LangFuse][langfuse]
- [LangSmith][langsmith]


Tracing will automatically begin with the next conversation after configuring a tracing provider.

## Langfuse Trace Detail

When Langfuse is configured, the trace detail page in Open Chat Studio includes a **span tree panel** that lets you inspect exactly what happened inside a single trace.

The panel is split into two panes:

- **Left pane** — the full Langfuse observation tree, with colored status dots and latency badges for each span.
- **Right pane** — the input and output for the selected span, shown as readable text by default, with a "Show raw JSON" toggle for the underlying Langfuse data.

When the panel loads, it automatically selects the first span that has an error status, or the first span overall if no errors are present. This makes it easy to jump straight to the root cause of a problem.

!!! note
    The span tree panel only appears when a Langfuse tracing provider is configured for your team. If no provider is configured, no trace information exists for the session, or the Langfuse API returns an error, the panel is hidden and the rest of the page is unaffected.

## See also
- [Configure a provider](../../how-to/configure_providers.md)


[langfuse]: https://langfuse.com/docs
[langsmith]: https://www.langchain.com/langsmith
