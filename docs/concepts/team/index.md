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
- [Tracing providers](../tracing.md)
- [User Management](groups.md)

## Finding where a provider is used

Every service-provider edit page has a **Show usages** button. Clicking it lists everything in your team that references that provider:

- **Chatbots and assistants** — links go to the working version's edit page; references belonging to a published version are tagged with a version badge.
- **Pipelines** — rolled up to their owning chatbot.
- **Collections and document sources** — rolled up to the owning collection.
- **Channels** — rolled up to their owning chatbot.

This is most useful before rotating an API key, deprecating a provider, or triaging a potentially leaked credential — it gives you an immediate picture of what would be affected.

## Exporting team files

From the Team Settings page, a **Team Admin** can download a zip archive of all the files currently in use across the team's chatbots, assistants, and collections.

To start an export:

1. Go to Team Settings.
2. Select **Download team files**. This button is only visible to Team Admins.
3. A progress bar appears and tracks the export while it runs in the background.
4. When the export finishes, a download link to the generated archive appears on the page.

A few things to know about exports:

- Only **current** files are included. Archived files and older versioned copies of a file are excluded.
- If an export is already running for your team — for example, another admin started one, or you reload the page — Team Settings resumes tracking that existing job instead of starting a duplicate export.
- The generated archive is available for **24 hours** after it's created. After that, the download link no longer works and you'll need to start a new export.

## Deleting a team

Team Admins can delete a team from Team Settings.

!!! warning "Team deletion is permanent"
    Deleting a team removes it and its data. This action cannot be undone.

To confirm a deletion, type the team's exact name into the confirmation modal. The **Delete** button stays disabled until the name you type matches the team's name.

<!--- TODO: user management -->
