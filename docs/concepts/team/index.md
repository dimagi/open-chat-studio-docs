---
hide:
  - toc
---
# Team Settings

Open Chat Studio supports multiple organizations/departments working in the same system while keeping their data completely separate. Each organization is called a **Team**. Teams have their own settings, private data, and chatbots.

As an OCS user, you can belong to several teams at once, with different roles in each — for example, an Admin on one team and a Viewer on another. Roles are managed with [User Groups](groups.md).

## Team configuration

Global settings are managed at the Team level, from the [Integrations](integrations.md) page. It lists every external service provider your team has connected, as rows in a single table you can filter by category:

- LLM & embedding
- Speech
- Messaging
- Authentication
- Tracing
- MCP (only visible on teams with that feature enabled)

A single **Add integration** button connects a new provider in any category.

## Finding where a provider is used

Every provider's edit page has a **Usages** tab. Opening it lists everything in your team that references that provider.

- **Chatbots** — links go to the working version's edit page; references belonging to a published version are tagged with a version badge.
- **Pipelines** — rolled up to their owning chatbot. Archived pipelines are included.
- **Channels** — rolled up to their owning chatbot.
- **Collections** — rolled up to the owning collection.
- **Evaluators** — LLM evaluators that use the provider, for LLM service providers.

This is most useful before rotating an API key, deprecating a provider, or triaging a potentially leaked credential — it gives you an immediate picture of what would be affected.

## Managing members

The [Members & access](members.md) section lists everyone with access to your team, active members and pending invitations together in one table.
Team Admins invite people, assign them roles, and remove access from there.

## Extending and integrating with your chatbots

The [Developers](developer.md) section groups the tools for extending Open Chat Studio: [Custom Actions](custom_actions.md), which let a chatbot call an external HTTP service, and OAuth applications, which let external systems read or write your team's data through the API.

## Moving a team to another instance

To move a team — its chatbots, configuration, and chat history — to a different OCS server, see [Migrate a Team to Another Instance](../../tech-hub/migrate_team.md).

## See also

- [Integrations](integrations.md)
- [Members & Access](members.md)
- [Developers](developer.md) — Custom Actions and OAuth applications
- [User Groups](groups.md)
