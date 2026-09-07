---
hide:
  - toc
---
# Team Settings

Open Chat Studio supports multiple organizations/departments working in the same system while keeping their data completely separate. Each organization is called a **Team**. Teams have their own settings, private data, and chatbots.

As an OCS user, you can belong to several teams at once, with different roles in each — for example, an Admin on one team and a Viewer on another. Roles are managed with [User Groups](groups.md).

Team Settings is organized into four sections:

- **[Integrations](integrations.md)** — configure and manage the external services your chatbots use: LLM & embedding, Speech, Messaging, Authentication, and Tracing providers.
- **[Members](members.md)** — invite people to the team, and manage their roles and access.
- **[Developers](developer.md)** — manage Custom Actions and OAuth applications for extending and integrating with your chatbots.
- **Data** — export your team's files, and migrate the team to another OCS instance.

## Integrations

Global settings are managed at the Team level, from the [Integrations](integrations.md) page. It lists every external service provider your team has connected, as rows in a single table you can filter by category:

- LLM & embedding
- Speech
- Messaging
- Authentication
- Tracing
- MCP (only visible on teams with that feature enabled)

A single **Add integration** button connects a new provider in any category.

Every provider's edit page also has a **Usages** tab, showing everywhere in your team that provider is referenced — see [Find Where a Provider Is Used](../../how-to/find_provider_usages.md).

## Members

The [Members & access](members.md) section lists everyone with access to your team, active members and pending invitations together in one table.
Team Admins invite people, assign them roles, and remove access from there.

## Developers

The [Developers](developer.md) section groups the tools for extending Open Chat Studio: [Custom Actions](custom_actions.md), which let a chatbot call an external HTTP service, and OAuth applications, which let external systems read or write your team's data through the API.

## Data

Team Admins can also manage the team's data from Team Settings:

- **Download team files** — export a zip archive of every file belonging to the team.
- **Migration public key** — register the public key OCS uses to seal secrets when migrating the team to another instance, and turn on migration mode to pause scheduled messages and event triggers while a migration is in progress.
- **Danger Zone** — permanently delete the team.

This section is only visible to Team Admins. See [Migrate a Team to Another Instance](../../tech-hub/migrate_team.md) for the full walkthrough of moving a team — its chatbots, configuration, and chat history — to a different OCS server.

## See also

- [Integrations](integrations.md)
- [Members & Access](members.md)
- [Developers](developer.md) — Custom Actions and OAuth applications
- [User Groups](groups.md)
