# Custom Action

Custom Actions let your chatbot connect to other systems so it can retrieve information or complete tasks.

For example, your chatbot can:

- look up an order status
- create a support ticket
- get participant details from another system

Use a Custom Action when you want your chatbot to work with another service in a reusable, managed way.

## What happens when you add one?

Open Chat Studio includes built-in [tools](./tools/index.md) and also lets you add your own external services as Custom Actions, which then appear as "Custom Actions" in your chatbot's configuration.

When you [create a Custom Action](./team/custom_actions.md), your chatbot can use it to call approved external services. This lets the chatbot send data to the connected service and use the response to help the user.

## Health Status Monitoring

Open Chat Studio monitors these external service connections so you can quickly see whether there are technical issues. It regularly checks whether each Custom Action is available and displays its status.

For details on health status monitoring, see the Custom Action [Health Checks Tech Hub Guide](../tech-hub/custom_action/health_custom_action.md).
