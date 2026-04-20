# Router Nodes

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for example usage of pipelines using Routers in complex bots.

## Routers

Router nodes direct the conversation to different paths based on context. Rather than following a single fixed flow, a pipeline with routers can behave differently depending on what the user says or what is known about them.

For example, you might route new users to an onboarding flow while returning users go straight to the main menu, or send a message to a specialist node if the user asks about a particular topic.

There are two types of Router Nodes:

1. **LLM Router** — uses an AI model to classify the input and choose a route
2. **Static Router** — chooses a route based on a stored data value


### LLM Router Node

The LLM Router uses an AI model to classify incoming messages into one of your defined categories. Each category corresponds to a different node output path.

You define the categories (called **outputs**) in the [router node settings](../../tech-hub/routers/llm_router.md#outputs-and-default-route). 

The model will pick the closest match. If the model cannot confidently match any category, the message is sent along the **default** route — marked with a blue `*` in the interface.
!!! tip "For technical configuration tips"

    See [Router Node — Technical Reference](../../tech-hub/routers/index.md) for best practices around output categories, history mode and output formatting.

### Static Router Node

The Static Router routes the conversation based on a value stored in your data — such as a participant's profile or session information. It does not use an AI model; it simply looks up a key and follows the matching route.

This is useful for directing users based on known attributes, such as their preferred language, their subscription tier, or a flag set earlier in the conversation.

If the key is not found in the data, the message is sent along the default (first linked) route.

!!! tip "For technical configuration"

    See [Router Node — Technical Reference](../../tech-hub/routers/index.md) for details on supported data sources and key syntax.
