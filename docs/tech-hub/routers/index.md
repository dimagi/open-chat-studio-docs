# Router Nodes: Common Configuration

This page explains the technical setup shared by all router nodes. For a high-level explanation of how these nodes work, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Whether you are using an LLM Router (intent-based) or a Static Router (data-based), both use the same core configuration pattern to direct conversation flow. These settings are in the Advanced Settings of the node configuration.

For specific setup guides, see:

1. [LLM Router Configuration](llm_router.md)
2. [Static Router Configuration](static_router.md)


## The Default Output
Every router needs a "safety net" so the conversation never reaches a dead end. This is called the Default Output.

- The Indicator: The default output is marked with a blue asterisk (*) in the node configuration.
- The Logic: If the router cannot find a match for your configured outputs, or if a technical error occurs, the message is automatically directed to the downstream node connected to this Default Output.
- Customization: You can change the Default Output by clicking the blue * next to a different output keyword in your output list.

## Route Tagging & Tracing (Observability)
To understand how users move through your chatbot, you can enable Output Message Tagging. This is useful for debugging and analyzing routing performance.

- [Tagging](../../concepts/tags.md): Toggle the **Tag Output Message** flag within the Router node settings.
- [Tracing](../../concepts/tracing.md): Configure this for path-level analysis for debugging.

### Tag naming convention
To keep system tags organized, OCS follows this naming convention:
```
<node_name>:<route_name>
```
Example: If you have a Router node named `support_triage` and it selects the output keyword `BILLING`, the resulting tag is:
`support_triage:BILLING`

Ensure your `node_name` is descriptive (for example, `intent_classifier`) so tags are easy to interpret.

