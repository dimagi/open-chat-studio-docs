# Custom Action

Custom Actions let your chatbot connect to another system so it can get information or complete tasks.

For example, your chatbot can:

- look up an order status
- create a support ticket
- get participant details from another tool

Use a Custom Action when you want your chatbot to work with another service in a reusable, managed way.

## What happens when you add one?

When you [create a new Custom Action](./team/custom_actions.md), you can choose which actions your chatbot is allowed to use.

When needed, your chatbot can send information to the connected service and use the result to help answer the user.


## Health Status Monitoring

Open Chat Studio regularly checks whether your Custom Action is available so you can see if the connection is working.

### How Health Checks Work

Automatic checks run every 5 minutes.

### Viewing Health Status

You can view the health status of your custom actions in two places:

1. **Custom Actions Table**: This gives you a quick view of which services are available.

2. **Edit Custom Action Page**: This lets you check status while updating your configuration.

### Manual Health Checks

In addition to automatic monitoring, you can manually trigger a health check at any time. This is useful when:

- You've just configured a new custom action and want to verify connectivity immediately
- You've made changes to your external service and want to confirm it's still reachable
- The automatic check shows a service is down and you want to verify it's back online

When you run a manual check, you see the result right away.

### Health Status Values

The health status can be one of the following:

- **Up**: The connected service is available.
- **Down**: The connected service is not available or is returning an error.
- **Unknown**: A health check has not completed yet.

!!! tip "Troubleshooting"
    If a custom action shows as "Down," verify that:

    - The service address is correct
    - The external service is running
    - The service can be reached from Open Chat Studio

For advanced setup and technical troubleshooting, see the [Custom Action Developer Guide](../tech-hub/tech_custom_action.md).
