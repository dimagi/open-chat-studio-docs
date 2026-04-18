# Custom Actions

Custom Actions let chatbots call external services through a managed integration based on an [OpenAPI Schema](https://swagger.io/specification/). This feature is similar to OpenAI [GPT Actions](https://platform.openai.com/docs/actions/introduction), but it is configured within Open Chat Studio and exposed as tools that your chatbot can use.

Use this guide if you are configuring or troubleshooting a Custom Action. For a non-technical overview, see [Custom Action](../../concepts/llm_custom_action.md).

## When to use a Custom Action

Choose a Custom Action when:

- the external service provides a usable [OpenAPI Schema](https://swagger.io/specification/)
- you want API operations to appear as selectable [tools](../../concepts/tools/index.md) in chatbot configuration
- you want a managed integration with [health monitoring](./health_custom_action.md)
- you want to reuse the same integration across multiple chatbots

Use a [Python node](../python_node.md) instead when:

- the external service does not provide a suitable OpenAPI schema
- you need custom request logic that is easier to express in code
- you only need a small number of direct HTTP calls within a pipeline

## How Custom Actions work

When you create a Custom Action, Open Chat Studio parses the supplied OpenAPI schema, validates it, and extracts the supported API operations.

Each extracted operation becomes an action that can be enabled for a chatbot. This gives you control over which external operations the chatbot is allowed to use.

When the chatbot invokes one of those actions, Open Chat Studio sends the HTTP request to the external service, applies any configured authentication, and passes the response back to the model for use in the conversation.

## Prerequisites

Before creating a Custom Action, make sure you have:

1. an HTTPS base URL for the external service
2. an [OpenAPI Schema](https://swagger.io/specification/) in JSON or YAML format
3. an [Authentication Provider](../../concepts/team/authentication_providers.md), if the API requires authentication

Once you have this information, go to [Team Settings](../../concepts/team/custom_actions.md) and enter the details described below.

## Team Settings fields

Use the following fields to configure the integration.

**Base URL** is the HTTPS URL of the external service you want to call.

- Example: `https://www.example.com`
- Only HTTPS URLs are supported.

**Health Check Path** is an optional path appended to the Base URL when Open Chat Studio runs a health check.

- If you configure a path, the external service should respond successfully at that endpoint.
- If you do not configure a path, the health check uses the base URL or root path.

**API Schema** is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

- The schema should come from the external service you are integrating with.
- For many FastAPI services, the default schema path is `/openapi.json`.

Use **Allowed Operations** to select which actions from the external service your chatbot is allowed to use.

## Health checks

Open Chat Studio monitors Custom Actions by automatically checking the configured service every 5 minutes.

- You can also trigger a [manual health check](./health_custom_action.md#manual-health-checks) from the UI. Manual checks run immediately and return the current status without waiting for the scheduled check.
- If the [health status](./health_custom_action.md#health-status-values) indicates that the service is not **Up**, follow the troubleshooting guidance on that page.


