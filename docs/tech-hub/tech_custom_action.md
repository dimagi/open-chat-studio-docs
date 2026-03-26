# Custom Actions

Custom Actions let chatbots call external services through a managed integration based on an OpenAPI schema.

Use this guide if you are configuring or troubleshooting a Custom Action. For a non-technical overview, see [Custom Action](../concepts/llm_custom_action.md).

This feature is broadly similar to OpenAI [GPT Actions](https://platform.openai.com/docs/actions/introduction), but is configured within Open Chat Studio and exposed as tools your chatbot can use.

## When to use a Custom Action

Choose a Custom Action when:

- the external service provides a usable OpenAPI schema
- you want API operations to appear as selectable tools in chatbot configuration
- you want a managed integration with health monitoring
- you want to reuse the same integration across multiple chatbots

Use a [Python node](../how-to/external_api_calls.md) instead when:

- the external service does not provide a suitable OpenAPI schema
- you need custom request logic that is easier to express in code
- you only need a small number of direct HTTP calls inside a pipeline

## Prerequisites

Before creating a Custom Action, make sure you have:

1. an HTTPS base URL for the external service
2. an OpenAPI schema in JSON or YAML format
3. an [Authentication Provider](../concepts/team/authentication_providers.md), if the API requires authentication

You can create the integration in [Custom Actions team settings](../concepts/team/custom_actions.md).

## Team settings fields

### Base URL

The Base URL is the HTTPS URL of the external service you want to call.

Example: `https://www.example.com`

Only HTTPS URLs are supported.

### API Schema

The API Schema is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

The schema should come from the external service you are integrating with. For example, for many FastAPI services the default schema path is `/openapi.json`.

## How Custom Actions work

When you create a Custom Action, Open Chat Studio parses the supplied OpenAPI schema, validates it, and extracts supported API operations.

Each extracted operation becomes an action that can be enabled for a chatbot. This gives you control over which external operations the chatbot is allowed to use.

When the chatbot invokes one of those actions, Open Chat Studio sends the HTTP request to the external service, applies any configured authentication, and passes the response back to the model for use in the conversation.

## Health checks

Open Chat Studio monitors Custom Actions by checking the configured service automatically every 5 minutes.

!!! note "Health Check Endpoint"
    The health check is made against the base URL of the Custom Action. To support this, the external service should respond successfully at the configured base URL or root path.

You can also trigger a manual health check from the UI. Manual checks run immediately and return the current status without waiting for the scheduled check.

## Health status values

A Custom Action can report one of the following states:

- **Up**: the external service is reachable and has responded successfully to the health check
- **Down**: the external service could not be reached or returned an error
- **Unknown**: no health check has completed yet. This can occur when:
    - the health check endpoint has not been configured for the custom action
    - the custom action was recently created and the automatic health check task has not yet run

!!! tip "Troubleshooting"
    If a custom action shows as "Down" or is not behaving as expected, verify that:

    - The base URL is correct and accessible
    - Your Authentication Provider credentials are valid
    - The OpenAPI schema matches the deployed API
    - The external service is running and accepting connections
    - Any firewall or network rules allow connections from Open Chat Studio


## Related docs

- [Custom Action overview](../concepts/llm_custom_action.md)
- [Custom Actions team settings](../concepts/team/custom_actions.md)
- [Authentication Providers](../concepts/team/authentication_providers.md)
- [How to call external APIs with a Python node](../how-to/external_api_calls.md)