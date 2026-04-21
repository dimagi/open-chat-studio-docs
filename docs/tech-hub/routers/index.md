# Router Nodes: Common Configuration

This page details the technical setup shared by all Router nodes. For a high-level explanation of how these nodes function, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Regardless of whether you are using an LLM Router (intent-based) or a Static Router (data-based), both utilize the same underlying mechanics to direct conversation flow. These settings are found in the Advanced section of the node configuration.

For specific setup guides, see:

1. [LLM Router Configuration](llm_router.md)
2. [Static Router Configuration](static_router.md)


### The Default Output
Every Router requires a "safety net" to ensure the conversation never hits a dead end. This is known as the Default Output.

- The Indicator: The default output is marked with a blue asterisk (*) in the node configuration.
- The Logic: If the Router cannot find a confident match for any of your configured Keywords—or if a technical error occurs—the message is automatically directed to the linked downstream node connected to this default path.
- Customization: You can change which path is the default by clicking the blue * next to a different Keyword in your output list.

## Route Tagging (Observability)
To understand how users are moving through your chatbot, you can enable Output Message Tagging. This is a critical feature for debugging and analyzing the performance of your routing logic.

- How to Enable: Toggle the **Tag Output Message** flag within the Router node settings.
- Viewing Data: Once enabled, these tags are recorded in the session logs. You can review them in real-time using the Tracing tool to see exactly which path was chosen and why.
- Router nodes support [tagging](../../concepts/tags.md), enabling [tracing](../../concepts/tracing.md) and analysis of conversation flow paths for debugging.

### Tag naming convention
To keep your system tags organized, OCS follows a strict naming convention for these tags:
```
<node_name>:<route_name>
```
Example: If you have a Route node named `support_triage` and it selects the **Output Keyword** BILLING, the resulting tag will be:
`support_triage:BILLING`

Ensure your node_name is descriptive (e.g., intent_classifier) to make the tags meaningful.

