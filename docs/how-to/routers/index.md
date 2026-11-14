# Configuration for Router Nodes

This page covers the configuration steps that apply to all router node types.
For a conceptual overview of how routers work, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Both LLM Routers (intent-based) and Static Routers (data-based) share the same core configuration pattern for directing conversation flow.
You find these settings in the Advanced Settings of the node.

For router-specific configuration, see:

1. [LLM Router Configuration](llm_router.md)
2. [Static Router Configuration](static_router.md)

## The Default Output

Every router needs a fallback output so the conversation always continues.
This is called the Default Output.

- The Indicator: The default output is marked with a blue asterisk (*) in the node configuration.
- The Logic: If the router cannot find a match for your configured outputs, or if a technical error occurs, the message goes to the Default Output.
  The message is automatically directed to the downstream node connected to it.
  This includes when an LLM Router's model returns no classification at all.
- Customization: You can change the Default Output by clicking the blue * next to a different output keyword in your output list.

<a id="route-tagging-observability"></a>

## Route Tagging & Tracing (Observability)

To understand how participants move through your chatbot, you can enable Output Message Tagging.
This is useful for debugging and analyzing routing performance.

- [Tagging](tag_router_routes.md): Toggle the **Tag Output Message** flag within the Router node settings.
  The guide covers the tag naming rules, including the `:default` suffix.
- [Tracing](../../concepts/tracing.md): Configure this for path-level analysis for debugging.
