---
hide:
  - toc
---
# Teams

Open Chat Studio is designed for multiple companies or groups to work securely within the same system while keeping their data completely separate. Technically this is known as a [multitenant](https://en.wikipedia.org/wiki/Multitenancy) platform.

In OCS, these private spaces/tenants are called "Teams". Multiple teams can be set up, each with its own members. Each team has its own settings, private data, and chatbots.

As a user, you can belong to several Teams at once with different roles/permissions in each—like being an "Admin" for your support Chatbot but a "Viewer" for the knowledge base team. Roles are managed with [User Groups](groups.md)

## Team configuration

Global settings are managed at the Team level. This includes:

- [LLM Service Providers](llm_providers.md)
- [Speech Service Providers](speech_providers.md)
- [Messaging Providers](messaging_providers.md)
- [Authentication Providers](authentication_providers.md)
- [Custom Actions](custom_actions.md)
- [Tracing providers](../tracing.md)
- [User Management](groups.md)

## Finding where a provider is used

Every service-provider edit page has a **Show usages** button. Clicking it lists everything in your team that references that provider:

- **Chatbots and assistants** — links go to the working version's edit page; references belonging to a published version are tagged with a version badge.
- **Pipelines** — rolled up to their owning chatbot.
- **Collections and document sources** — rolled up to the owning collection.
- **Channels** — rolled up to their owning chatbot.

This is most useful before rotating an API key, deprecating a provider, or triaging a potentially leaked credential — it gives you an immediate picture of what would be affected.

<!--- TODO: user management -->
