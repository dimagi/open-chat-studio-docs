---
hide:
  - toc
---
# Team Settings

Open Chat Studio (OCS) supports multiple organizations/departments working in the same system while keeping their data completely separate. Each organization is called a **Team**. Teams have their own settings, private data, and chatbots.

As an OCS user, you can belong to several teams at once, with different roles in each — for example, an Admin on one team and a Viewer on another. Roles are managed with [User Groups](groups.md).

Team Settings is organized into sections:

- **[Integrations](integrations.md)** — configure and manage the external services your chatbots use: LLM & embedding, Speech, Messaging, Authentication, and Tracing providers.
- **[Members](members.md)** — invite people to the team, and manage their roles and access.
- **[Developers](developer.md)** — manage Custom Actions and OAuth applications for extending and integrating with your chatbots.
- **[Data](data_migration.md)** — export your team's files, and migrate the team to another OCS instance.
- **[Feature Flags](feature_flags.md)** — where Team Admins turn experimental features on or off for the team.

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

The [Developers](developer.md) section groups the tools for extending OCS: [Custom Actions](../../tech-hub/custom_action/index.md), which let a chatbot call an external HTTP service, and OAuth applications, which let external systems read or write your team's data through the API.

## Data & Migration

The [Data & Migration](data_migration.md) section lets Team Admins export the team's files, register a migration public key, and delete the team.
This section is only visible to Team Admins.
See [Migrate a Team to Another Instance](../../tech-hub/migrate_team.md) for the full walkthrough of moving a team — its chatbots, configuration, and chat history — to a different OCS server.

## See also

- [Integrations](integrations.md)
- [Members & access](members.md)
- [Developers](developer.md) — Custom Actions and OAuth applications
- [Data & Migration](data_migration.md) — export team files and migrate to another instance
- [Feature Flags](feature_flags.md) — experimental features your team can turn on
- [User Groups](groups.md)
