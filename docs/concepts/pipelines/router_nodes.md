# Router Nodes

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for example usage of Routers in complex bots. 

## Routers

Router nodes allow you to route the input to one of the linked nodes. It selects an output path based on conversation context.

This is useful if you want your bot to behave differently depending on the input or some persistent context. For example, you might want to route the input to a different node if the user is asking for help with a specific topic.

There are 2 types of Router Nodes:
1. LLM Router Nodes
2. Static Router Nodes

Router nodes share some common configuration such as the list of route options. Router nodes can also be configured to
tag the output message with the selected route. This is useful for debugging and for tracking the flow of messages through the pipeline.
The format of the tag is `<node_name>:<route_name>` where `<route_name>` is the name of the route selected by the router node.

!!! info "Router Keywords Are Uppercase"

    All router keywords are automatically converted to uppercase. When configuring router outputs, use uppercase keywords to match this behavior. Keyword matching is case-insensitive, so "HELP", "Help", and "help" will all match the same route.

### LLM Router Node
Routes the input to one of the linked nodes using an LLM. In this case, the LLM acts as a classifier using the prompt provided to classify an incoming message into a set of discrete categories that allow messages to be routed.

The `outputs` listed by the node are the available classification labels. These should match the classification categories specified in your prompt. They can be adjusted through the `Advanced` settings for the node. The top output, which is prepended by a blue `*` is the default label. In the event that the LLM generates a response outside of the specified `outputs`, the route with the default label will be taken.

!!! info "Best practices for configuring a LLM Router"

    It is advisable to use the [Node history mode](history.md#node) for an LLM Router to avoid unintentionally supplying few-shot examples to the node with an incorrect output format.

### Static Router Node
The Static Router node allows you to route the input to one of the linked nodes based on the value of a specific key in the data source. This is useful if you want your bot to behave differently depending on the value of a specific key in the data source.

The data source can be any of the following:

* [Participant Data](../participant_data.md)
* [Session State](../../tech-hub/python_node.md#session-state)
* [Temporary State](../../tech-hub/python_node.md#temporary-state)

The key should be a name of a field in the data source and supports selecting nested fields via the `<field>.<subfield>` syntax. For example, if the data source is a JSON object with the following structure:

```json
{
    "user": {
        "name": "John",
        "age": 30
    }
}
```

You can select the `name` field using the key `user.name` and the `age` field using the key `user.age`.

If the field is not present in the data source, the router will route the input to the default (first linked) node.
