# Integrations

Every external service your team connects to — [LLM models](./llm_providers.md), [speech](./speech_providers.md), [messaging](./speech_providers.md), [authentication](./authentication_providers.md), and [tracing](../tracing.md) — is managed from one place: the **Integrations** table in Team Settings.

## The Integrations table

Depending on your permissions, each row also offers **Edit** and **Delete** actions. Deleting an integration warns you first, since it also removes the integration from anywhere it's currently being used.

### Filtering by category

Category filter pills above the table narrow it down to one category at a time. Each pill shows a live count of integrations in that category, including categories with none configured yet.

!!! note "MCP"
    An **MCP** category appears alongside the others once MCP servers are generally available. Until then it's only visible on teams with that feature enabled.

## Adding an integration

Click **Add integration** to open a single categorized dropdown. It's grouped, with each group expanding to the specific providers available in that category — for example, the **LLM & embedding** group lists OpenAI, Anthropic, Azure OpenAI, and the rest of the [supported LLM providers](llm_providers.md). Choosing an option takes you straight to that provider's configuration form.

This table and its single **Add integration** entry point replace the separate per-category pages OCS used to show. For provider-specific setup steps, supported services, models, and credential verification, see:

- [LLM Service Providers](llm_providers.md)
- [Speech Service Providers](speech_providers.md)
- [Messaging Providers](messaging_providers.md)
- [Authentication Providers](authentication_providers.md)
- [Tracing Providers](../tracing.md)

## See also

- [Team Settings](index.md)
- [Find Where a Provider Is Used](../../how-to/find_provider_usages.md)
