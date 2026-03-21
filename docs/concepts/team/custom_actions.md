# Custom Actions Team Settings

Use this page to set up Custom Actions in Team Settings.

To learn what Custom Actions are and how they work in chats, see [Custom Action](../llm_custom_action.md).
For technical setup details and troubleshooting, see the [Custom Action Developer Guide](../../dev_guides/tech_custom_action.md).


## Team setup steps

### 1) Set up an Authentication Provider

Before creating a Custom Action, create an Authentication Provider if your external service requires authentication.

Go to [Authentication Providers][auth_providers] in Team Settings and create a provider.

[auth_providers]: authentication_providers.md

### 2) Create a new Custom Action
Add a Custom Action in Team Settings.

### 3) Enable actions for your chatbot

After creating the Custom Action, choose which actions your [LLM Node](../pipelines/nodes.md) is allowed to use.

## Where to manage Custom Actions

In Team Settings, you can:

- create new Custom Actions
- edit existing Custom Actions
- run a manual health check

For field-level technical requirements (Base URL, OpenAPI schema format, and health check behavior), see the [Custom Action Developer Guide](../../dev_guides/tech_custom_action.md).

## Related docs

- [Custom Action overview](../llm_custom_action.md)
- [Custom Action Developer Guide](../../dev_guides/tech_custom_action.md)
