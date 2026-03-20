# Custom Action

Custom Actions enable bots to communicate with external services. 
This feature allows you to extend the functionality of your LLM node by integrating it with other third-party APIs.

This feature is analogous to the OpenAI's [GPT Actions](https://platform.openai.com/docs/actions/introduction) feature.

## Custom Action or Python Node
- Choose a Custom Action if you want your [LLM nodes](./pipelines/nodes.md) to call an API (with an OpenAPI schema) through a managed, reusable integration with health monitoring and notifications.
- Choose to add an  [HTTP client](./pipelines/http_client.md) to a [Python node](./pipelines/python_node.md) if you have simple API calls and the API you are calling does not have an OpenAPI schema.

## How Custom Actions Work

When you [create a new Custom Action](./team/custom_actions.md), each API endpoint in the OpenAPI schema will be available as a separate action listed in the ChatBot configuration. This makes it easy to select actions, and gives you full control over which actions are available to your bot.

When you add a Custom Action to your ChatBot, the bot will be able to make HTTP requests to the external service
using the API endpoints you have configured. The bot will send the request and receive the response from the external
service, which it can then use to generate a response to the user.


## Health Status Monitoring

Open Chat Studio automatically monitors the health of your custom actions to help you ensure your external services are available when your bot needs them. This feature provides visibility into the operational status of your integrations and helps you quickly identify connection issues.

### How Health Checks Work

The system automatically queries the health check endpoint of each custom action every 5 minutes. This periodic check verifies that the target server is reachable and responding correctly. The health status is determined by whether the server responds successfully to these automated checks.

!!! note "Health Check Endpoint"
    The health check queries the base URL of your custom action. Ensure your external service has a health check endpoint configured at the base URL or root path.

### Viewing Health Status

You can view the health status of your custom actions in two places:

1. **Custom Actions Table**: The health status is displayed as a column in the table showing all your custom actions. This gives you an at-a-glance view of which services are operational.

2. **Edit Custom Action Page**: When editing a custom action, the current health status is displayed, allowing you to verify connectivity while configuring your integration.

### Manual Health Checks

In addition to automatic monitoring, you can manually trigger a health check at any time. This is useful when:

- You've just configured a new custom action and want to verify connectivity immediately
- You've made changes to your external service and want to confirm it's still reachable
- The automatic check shows a service is down and you want to verify it's back online

Manual health checks are performed synchronously, giving you immediate feedback on the service status.

### Health Status Values

The health status can be one of the following:

- **Up**: The external service is reachable and responding correctly to health checks
- **Down**: The external service is not responding or is returning errors
- **Unknown**: A health check has never been performed. This can occur when:
    - A health check endpoint has not been configured for the custom action
    - The custom action was recently created and the automatic health check task has not yet run

!!! tip "Troubleshooting"
    If a custom action shows as "Down," verify that:

    - The base URL is correct and accessible
    - Your authentication provider credentials are valid
    - The external service is running and accepting connections
    - Any firewall or network rules allow connections from Open Chat Studio
