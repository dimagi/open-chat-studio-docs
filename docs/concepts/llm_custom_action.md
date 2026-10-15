# Custom Action

A Custom Action lets your chatbot use another service during a conversation, so it can look up information or complete a task for the participant.

For example, a chatbot can:

- look up an order status
- create a support ticket
- get participant details from another system

## How it works

1. A Team Admin connects an external service to your team by adding it as a Custom Action.
2. Open Chat Studio lists the actions the service offers, such as "get order status".
3. The Team Admin chooses which of those actions your chatbots may use.
4. When you build a chatbot, you turn on only the actions it needs in its [LLM node](pipelines/nodes.md#llm-node).
5. During a conversation, the chatbot decides when an action is useful.
   It sends the request to the service and uses the response in its reply.

## When to use a Custom Action

Use a Custom Action for connections you want to set up once and reuse across chatbots.

Open Chat Studio also includes built-in [tools](./tools/index.md) for common tasks.
To check whether it suits your service, see [When to use a Custom Action](../tech-hub/custom_action/index.md#when-to-use-a-custom-action) in the Tech Hub guide.

## Keeping track of problems

Open Chat Studio checks each Custom Action regularly and shows whether the service is available.
It also sends a [notification](notifications.md) when the service goes down or when a call fails during a conversation.

## Next steps

[Set up a Custom Action](../tech-hub/custom_action/index.md) covers the fields to fill in and how to enable actions on a chatbot.

## See also

- [Custom Action health checks](../tech-hub/custom_action/health_custom_action.md)
- [Team Settings: Developers](team/developer.md)
