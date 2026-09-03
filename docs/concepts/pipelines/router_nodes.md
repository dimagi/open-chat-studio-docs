# Router Nodes

## Routers

Router nodes are decision points in your pipeline. Instead of following one fixed path, a pipeline with a router can choose different paths based on what the participant says or what your system already knows about the participant.

In simple terms, a router evaluates a condition, chooses one of its configured paths, and passes the input through unchanged to the node on that path. This allows your chatbot to adapt in real time. What the router evaluates depends on its type — see [Router Types](#router-types) below.

For example:

1. **Participant Status (Data-Based)**: You can route new participants to a specialized onboarding flow while returning participants are sent straight to the main menu.

2. **Topic Expertise (Intent-Based)**: You can detect when a participant is asking about a complex technical issue and route that message to a specialist node instead of a general FAQ node.

## Useful Terms

1. **Linked Downstream Node**: Any node that appears after the current node in the pipeline flow.

2. **Conversation Context**: The information a router evaluates to make its decision. For an [LLM Router](#llm-router-node), this is the participant's current message plus its own [History setting](history.md). A [Static Router](#static-router-node) does not evaluate the message or history at all — it looks up a value already stored as data (see [Router Types](#router-types)).

3. **Default Path**: The "safety net" route (marked with a blue *). If the router cannot confidently decide where to send the participant, it follows this path to prevent the conversation from breaking. [Read more about the default output](../../how-to/routers/index.md#the-default-output).

## Router Types
There are two distinct ways to route a conversation in OCS. The choice depends on whether you are routing based on what the participant means or what the system knows.

### LLM Router Node
The LLM Router uses an AI model to read the incoming message and classify its intent.

- **How it works**: It acts as a classifier. You provide a prompt that tells the LLM how to categorize a message (for example, "If the participant is angry, output `ESCALATE`").
- **Best for**: Handling unpredictable participant text.
- You define output keywords for your downstream paths. If the LLM outputs `BILLING`, the conversation follows the path labeled `BILLING` to the next downstream node.

!!! tip "For configuration steps"

    See [Router Nodes in How-to Guides](../../how-to/routers/index.md) for configuration details and best practices.

See a working example in the [Chatbot Workflow Cookbook](../../how-to/workflow_cookbook.md#split-a-chatbot-into-multiple-smaller-chatbots), where an LLM Router classifies input into `GENERAL`, `ROLEPLAY`, and `QUIZ` paths.

### Static Router Node
The Static Router does not use an AI model and does not read the participant's message. Instead, it looks up a specific value stored in your [data source](../../how-to/routers/static_router.md#supported-data-sources).

- **How it works**: It checks a pre-existing key or tag, such as participant profile data or session information, and follows the matching path.
- **Best for**: Routing based on known attributes like preferred language, subscription tier, or VIP status.
- Example: If your data shows `subscription_tier = premium`, the Static Router immediately sends the participant to the Priority Support Agent.

!!! tip "For configuration steps"

    See [Router Nodes in How-to Guides](../../how-to/routers/index.md) for configuration details and best practices.
