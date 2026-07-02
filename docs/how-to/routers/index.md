# Configuration for Router Nodes

This page covers the configuration steps that apply to all router node types. For a conceptual overview of how routers work, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Both LLM Routers (intent-based) and Static Routers (data-based) share the same core configuration pattern for directing conversation flow. You find these settings in the Advanced Settings of the node.

For router-specific configuration, see:

1. [LLM Router Configuration](llm_router.md)
2. [Static Router Configuration](static_router.md)

## The Default Output
Every router needs a "safety net" so the conversation never reaches a dead end. This is called the Default Output.

- The Indicator: The default output is marked with a blue asterisk (*) in the node configuration.
- The Logic: If the router cannot find a match for your configured outputs, or if a technical error occurs, the message is automatically directed to the downstream node connected to this Default Output.
- Customization: You can change the Default Output by clicking the blue * next to a different output keyword in your output list.

<a id="route-tagging-observability"></a>

## Route Tagging & Tracing (Observability)
To understand how users move through your chatbot, you can enable Output Message Tagging. This is useful for debugging and analyzing routing performance.

- [Tagging](../../concepts/tags.md): Toggle the **Tag Output Message** flag within the Router node settings.
- [Tracing](../../concepts/tracing.md): Configure this for path-level analysis for debugging.

### Tag naming convention
To keep system tags organized, OCS follows this naming convention:

```text
<node_name>:<route_name>
```

Example: If you have a Router node named `support_triage` and it selects the output keyword `BILLING`, the resulting tag is:
`support_triage:BILLING`

Ensure your `node_name` is descriptive (for example, `intent_classifier`) so tags are easy to interpret.
