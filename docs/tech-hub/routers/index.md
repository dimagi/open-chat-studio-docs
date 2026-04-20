# Router Nodes Configuration

This page covers technical configuration details for Router nodes. For a conceptual overview, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Below is information about both types of routers and the details for each type: 

1. [LLM Router](llm_router.md) configuration details
2. [Static Router](static_router.md) configuration details

## Outputs

Each router node has one or more **outputs** — the connection points that link the router node to downstream nodes in the pipeline. The active output for a given input message is determined by matching the router's result against its configured **Output Keywords**.

### Output Keywords

Each output has a keyword. When the router runs, it compares its result against these keywords to select which output to activate.

Keywords must be unique.

#### Keyword Case Behaviour

- All **Output Keywords** are automatically converted to uppercase.
- When configuring outputs, use uppercase keywords to match this behaviour.
- Keyword matching itself is case-insensitive, so `HELP`, `Help`, and `help` will all match the same output.

### The default output

The **default** output is indicated by a blue `*` in the node configuration. This can be changed by clicking the blue `*` for another of the **Output Keywords**

If no keyword matches — or an error occurs — the message is routed along this default outputs downstream node .

## Route Tagging

Router nodes in OCS supports Output Message [tagging](../../concepts/tags.md) of output messages based on the routing decision, enabling tracking and analysis of conversation flow paths for debugging.

Toggle the **Tag Output Message** flag when configuring the node for this feature.  

Tags can be viewed in the session trace. See [Tracing](../../concepts/tracing.md) for more detail.


### The tag naming convention
```
<node_name>:<route_name>
```
For example, if a node named `intent_router` selects the route `HELP`, the tag will be `intent_router:HELP`.



