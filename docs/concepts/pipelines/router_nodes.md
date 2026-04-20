# Router Nodes

## Routers

Router nodes direct the conversation to different paths. Rather than following a single fixed workflow, a pipeline with routers can behave differently depending on what the user says or what is known about them.

Router nodes are essentially decision points as they branch the pipeline workflow along different paths based on logic.

For example, you might route new users to an onboarding flow while returning users go straight to the main menu, or send a message to a specialist node if the user asks about a particular topic.

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for example usage of pipelines using Routers in complex bots.

There are two types of Router Nodes:

1. **LLM Router** — uses an AI model to classify the input and choose a route
2. **Static Router** — chooses a workflow path based on a stored data value


### LLM Router Node

This uses an AI model to classify incoming messages into one of your defined **outputs**. Each output connects to a different downstream node.

You define **outputs** in the [router node settings](../../tech-hub/routers/llm_router.md#outputs-and-default-route).

The model will pick the closest match. If the LLM cannot confidently match to any of the configured **outputs**, the router choses the **default** output — marked with a blue `*` in the interface.
!!! tip "For technical configuration tips"

    See [Router Node — Technical Reference](../../tech-hub/routers/index.md) for best practices around output keywords, history mode and tagging.

### Static Router Node

The Static Router routes the conversation based on a value stored in your data — such as a participant's profile or session information. It does not use an AI model; it simply looks up a key and follows the matching output.

This is useful for directing users based on known attributes, such as their preferred language, their subscription tier, or a flag set earlier in the conversation.

If the key is not found in the data, the message is sent along the **default** output.

!!! tip "For technical configuration"

    See [Router Node — Technical Reference](../../tech-hub/routers/index.md) for details on supported data sources and key syntax.
