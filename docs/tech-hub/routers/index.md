# Router Nodes Configuration

This page covers technical configuration details for Router nodes. For a conceptual overview, see [Router Nodes in Pipelines](../../concepts/pipelines/router_nodes.md).

Below is information about both types of routers and the details for each type: 

1. [LLM Router](llm_router.md) configuration details
2. [Static Router](static_router.md) configuration details

## Route Tagging

Router nodes in Open Chat Studio support automatic tagging of output messages based on the routing decision, enabling tracking and analysis of conversation flow paths.

Router nodes can be configured to tag each output message with the route that was selected. This is useful for debugging and for tracking message flow through a pipeline. Tags can be viewed in the session trace. See [Tracing](../../concepts/tracing.md) for more detail.

!!! tip "Tip"

    Use this tagging feature to make it easy to review how messages are flowing through your pipeline. 

### The tag naming convention
```
<node_name>:<route_name>
```
For example, if a node named `intent_router` selects the route `HELP`, the tag will be `intent_router:HELP`.


## Keyword Case Behaviour

- All router keywords are automatically converted to uppercase internally. 
- When configuring router outputs, use uppercase keywords to match this behaviour. 
- Keyword matching itself is case-insensitive, so `HELP`, `Help`, and `help` will all match the same route.

---