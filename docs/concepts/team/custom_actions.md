# Custom Actions

Use Team Settings to create and manage Custom Actions for your team.

To learn what Custom Actions are and how they work in chats, see [Custom Action](../llm_custom_action.md). For technical setup details and troubleshooting, see the [Custom Action Tech Hub Guide](../../tech-hub/tech_custom_action.md).

## What you can do in Team Settings

In Team Settings, you can:

- create a new Custom Action
- edit an existing Custom Action
- run a [manual health check](../../tech-hub/health_custom_action.md#manual-health-checks) for a Custom Action

## Configuration steps

### 1) Create an Authentication Provider (if required)

If your external service requires authentication, first create an Authentication Provider in Team Settings.

Go to [Authentication Providers][auth_providers] in Team Settings to create a provider.

### 2) Add the Custom Action

Go to Team Settings, scroll to the **Custom Actions** section, and select **Add new**.

For field-level technical requirements, including the Base URL, OpenAPI schema format, and health check behavior, see the [Custom Action Tech Hub Guide](../../tech-hub/tech_custom_action.md#team-settings-fields).

### 3) Enable actions for your chatbot

After you save the Custom Action, its actions appear in the advanced settings for an [LLM node](../pipelines/nodes.md). Select the actions you want to enable for the chatbot.

Once enabled, the LLM can call those actions when they are relevant to the conversation.

[auth_providers]: authentication_providers.md