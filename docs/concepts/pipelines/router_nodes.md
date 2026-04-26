# Router Nodes

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for examples of complex pipelines using Routers.


## Routers

Router nodes are decision points in your pipeline. Instead of following one fixed path, a pipeline with a router can choose different paths based on what the user says or what your system already knows about the user.

In simple terms, a router checks the current conversation context and sends the input (user message plus available data) to the most relevant downstream node. This allows your chatbot to adapt in real time.

For example:

1. **User Status (Data-Based)**: You can route new users to a specialized onboarding flow while returning users are sent straight to the main menu.

2. **Topic Expertise (Intent-Based)**: You can detect when a user is asking about a complex technical issue and route that message to a specialist node instead of a general FAQ node.

## Useful Terms

1. **Linked Downstream Node**: Any node that appears after the current node in the pipeline flow.

2. **Conversation Context**: The total set of information available to the pipeline at that moment. This includes the user’s current message, their chat history, and known data (like whether they are a "new" or "returning" user).

3. **Default Path**: The "safety net" route (marked with a blue *). If the router cannot confidently decide where to send the user, it follows this path to prevent the conversation from breaking. [more](../../tech-hub/routers/index.md#the-default-output).

## Router Types
There are two distinct ways to route a conversation in OCS. The choice depends on whether you are routing based on what the user means or what the system knows.

### LLM Router Node
The LLM Router uses an AI model to read the incoming message and classify its intent.

- **How it works**: It acts as a classifier. You provide a prompt that tells the LLM how to categorize a message (for example, "If the user is angry, output `ESCALATE`").
- **Best for**: Handling unpredictable user text.
- You define output keywords for your downstream paths. If the LLM outputs `BILLING`, the conversation follows the path labeled `BILLING` to the next downstream node.

### Static Router Node
The Static Router does not use an AI model and does not read the user's message. Instead, it looks up a specific value stored in your [data source](../../tech-hub/routers/static_router.md).

- **How it works**: It checks a pre-existing key or tag, such as participant profile data or session information, and follows the matching path.
- **Best for**: Routing based on known attributes like preferred language, subscription tier, or VIP status.
- Example: If your data shows `subscription_tier = premium`, the Static Router immediately sends the user to the Priority Support Agent.


!!! tip "For technical configuration"

    See [Router Nodes on Tech Hub](../../tech-hub/routers/index.md) for configuration details and best practices.
