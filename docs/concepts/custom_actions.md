# Custom Actions

Custom Actions enable bots to communicate with external services via HTTP API calls. 
This feature allows you to extend the functionality of your bot by integrating it with other services.

This feature is analogous to the OpenAI's [GPT Actions](https://platform.openai.com/docs/actions/introduction) feature.

## Custom Action Fields

### Authentication Provider

Before you create a Custom Action will need to create an Authentication Provider for your action to use (unless the API
you are using does not require authentication). You can do this by navigating to the [Authentication Providers][auth_providers] section
in Team Settings and creating a new Authentication Provider.

[auth_providers]: team/authentication_providers.md

### Base URL

This is the URL of the external service you want to communicate with. For example: `https://www.example.com`. Only HTTPS URLs
are supported.

### API Schema

This is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

You should be able to get this from the service you want to connect to. For example, the default location for the schema for [FastAPI](https://fastapi.tiangolo.com/) services is `/openapi.json` (https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema).

## How Custom Actions work

When you create a custom action, each API endpoint in the OpenAPI schema will be available as a separate action in the
Experiment configuration. This gives you full control over which actions are available to your bot.

When you add a Custom Action to your Experiment, the bot will be able to make HTTP requests to the external service
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
