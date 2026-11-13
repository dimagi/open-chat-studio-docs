# User Groups on OCS

Users can be assigned to specific groups when they are invited to the OCS platform.
Groups give each user access to the features and resources their role requires.
Users can be put in one or multiple groups.

!!! warning "Assistant Admin role removed"
    The **Assistant Admin** role has been removed.
    It can no longer be granted to a team member or attached to an invitation, and existing memberships in it are gone.
    It was the only role granting full file management (add, change, delete); the other roles that reach files, such as **Chat Viewer**, are view-only.
    If someone on your team relied on **Assistant Admin** for file management, assign them another role that covers what they need.
    See [OpenAI Assistants (Removed)](../assistants.md) for why this role existed.

## Permissions Table

| Permission | Super Admin | Team Admin | Chatbot Admin | Chat Viewer | Event Admin | Evaluation Admin | Annotation Reviewer |
|---|---|---|---|---|---|---|---|
| **Can See Chatbots** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Can View Sessions and Transcripts** | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Can View Source Material and Consent Forms** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Can See Tags** | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Can Access Prompt Builder** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Can View and Download Files** | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Can Invite Participants** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Can Export Chat Transcripts** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Can Manage Files** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Create and Manage Chatbot Events** | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Create and Manage Pipelines** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Create and Manage Evaluations** | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Can View Assigned Annotation Queues** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Can View and Change Annotation Queue Items** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Can Add Annotations** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Can View Annotation Aggregate Results** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Can Manage Annotation Queues** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Manage Team Members and Settings** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Manage Custom Actions** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Manage Service Providers** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Manage OAuth Applications and Notification Channels** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Additional Notes** | **Full Access, Default Role** | - | - | **View-only access to sessions and files** | - | - | **Annotation queues plus Chat Viewer access; cannot manage queues, add sessions, or export results** |

**Can Manage Files** covers adding, changing, and deleting files — for example, in [collections](../collections/index.md) — and only **Super Admin** grants it.
A role with view-only file access, such as **Chat Viewer**, can see and download files but not add, change, or delete them.
Every team member can open the dashboard.

## See also

- [Members & access](members.md)
- [Team Settings](index.md)
