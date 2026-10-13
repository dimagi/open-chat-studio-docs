# Custom Actions

Custom Actions let chatbots call external services. This feature is similar to OpenAI [GPT Actions](https://platform.openai.com/docs/actions/introduction), but it is configured within Open Chat Studio, and each enabled operation appears as a selectable "Custom Action" in your chatbot's configuration.

Use this guide if you are configuring or troubleshooting a Custom Action. For a non-technical overview, see [Custom Action](../../concepts/llm_custom_action.md).

## When to use a Custom Action

Choose a Custom Action when:

- the external service provides a usable [OpenAPI Schema](https://swagger.io/specification/)
- you want API operations to appear as a list of selectable actions in chatbot configuration
- you want a managed integration with [health monitoring](./health_custom_action.md)
- you want to reuse the same integration across multiple chatbots

Use a [Python node](../python_node.md) instead when:

- the external service does not provide a suitable OpenAPI schema
- you need custom request logic that is easier to express in code
- you only need a small number of direct HTTP calls within a pipeline

## How Custom Actions work

For the end-to-end flow, see [Custom Action](../../concepts/llm_custom_action.md#how-it-works).
Two details matter when you configure one:

- When you save a Custom Action, Open Chat Studio validates the OpenAPI schema and extracts the supported API operations. Each operation becomes an action you can allow.
- When the chatbot invokes an action, Open Chat Studio sends the HTTP request to the external service and applies the configured authentication.

## Prerequisites

Before creating a Custom Action, make sure you have:

1. an HTTPS base URL for the external service
2. an [OpenAPI Schema](https://swagger.io/specification/) in JSON or YAML format
3. an [Authentication Provider](../../concepts/team/authentication_providers.md), if the API requires authentication — create one from **Integrations** in Team Settings

Once you have this information, go to the **Developers** section of [Team Settings](../../concepts/team/developer.md), select **Add action** under **Custom actions**, and enter the details described below.

## Team Settings fields

Use the following fields to configure the integration.

**Base URL** is the HTTPS URL of the external service you want to call.

- Example: `https://www.example.com`
- Only HTTPS URLs are supported.

**Health Check Path** is an optional path appended to the Base URL when Open Chat Studio runs a health check.

- If you configure a path, the external service should respond successfully at that endpoint.
- If you leave it blank, Open Chat Studio looks in the API schema for a `GET` operation at `/health`, `/healthz`, `/healthcheck`, `/api/health`, `/status` or `/_health` and uses the first one it finds.
- If the schema has none of these, no health checks run for the Custom Action and no health status is shown.

**API Schema** is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

- The schema should come from the external service you are integrating with.
- For many FastAPI services, the default schema path is `/openapi.json`.

**Allowed Operations** selects which actions from the external service your chatbot is allowed to use.

- This field appears only when you edit a saved Custom Action, because the operations come from the saved API schema.
- Save the Custom Action, then reopen it to choose the operations.

## Enabling actions for a chatbot

After you save the Custom Action, its actions appear in the advanced settings for the [LLM node](../../concepts/pipelines/nodes.md). Select the actions you want to enable for the chatbot — once enabled, the LLM can call those actions when they are relevant to the conversation.

To confirm an enabled action works, see [Custom Action Testing](./test_custom_action.md).

## Failure notifications

When a chatbot calls a Custom Action during a conversation and the call fails, Open Chat Studio creates an **Error** [notification](../../concepts/notifications.md):

- **Custom Action '*name*' failed** means the request to the external service failed, for example because it returned an error status or could not be reached.
- **Custom Action '*name*' encountered an error** means something else went wrong while running the action.

The notification names the HTTP method and operation, includes the error message, and links to the Custom Action. It goes to team members who can view Custom Actions, and repeated failures are grouped into one thread.

Failure notifications report calls made by chatbots. To monitor whether the service is reachable, see [Health checks](#health-checks).

## Health checks

Open Chat Studio checks Custom Actions every hour, and you can run a check on demand. See [Custom Action Health Monitoring](./health_custom_action.md) for health statuses, manual checks and troubleshooting.
