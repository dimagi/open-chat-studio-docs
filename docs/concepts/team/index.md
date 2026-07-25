---
hide:
  - toc
---
# Teams

Open Chat Studio supports multiple organizations/departments working in the same system while keeping their data completely separate. Each organization is called a **Team**. Teams have their own settings, private data, and chatbots.

You can belong to several teams at once, with different roles in each — for example, an Admin on one team and a Viewer on another. Roles are managed with [User Groups](groups.md).

## Team configuration

Global settings are managed at the Team level. This includes:

- [LLM Service Providers](llm_providers.md)
- [Speech Service Providers](speech_providers.md)
- [Messaging Providers](messaging_providers.md)
- [Authentication Providers](authentication_providers.md)
- [Custom Actions](custom_actions.md)
- [Tracing Providers](../tracing.md)
- [User Management](groups.md)

## Finding where a provider is used

Every service-provider edit page has a **Show usages** button. Clicking it lists everything in your team that references that provider:

- **Chatbots and assistants** — links go to the working version's edit page; references belonging to a published version are tagged with a version badge.
- **Pipelines** — rolled up to their owning chatbot.
- **Collections and document sources** — rolled up to the owning collection.
- **Channels** — rolled up to their owning chatbot.

This is most useful before rotating an API key, deprecating a provider, or triaging a potentially leaked credential — it gives you an immediate picture of what would be affected.

## Moving a team to another instance

To move a team — its chatbots, configuration, and chat history — to a different OCS server, see [Migrate a Team to Another Instance](../../tech-hub/migrate_team.md).

<!--- TODO: user management -->
