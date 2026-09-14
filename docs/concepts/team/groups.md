# User Groups on OCS

Users can be assigned to specific groups upon invitation to the OCS platform enabling tailored access to features and resources based on their role or requirements. Users can be put in one or multiple groups.

!!! warning "Assistant Admin role removed"
    The **Assistant Admin** role has been removed — it can no longer be granted to a team member or attached to an invitation, and existing memberships in it are gone.
    It was the only role granting full file management (add, change, delete); the other roles that reach files, such as **Chat Viewer**, are view-only.
    If someone on your team relied on **Assistant Admin** for file management, assign them another role that covers what they need.
    See [OpenAI Assistants (Removed)](../assistants.md) for why this role existed.

## Permissions Table

| Permission                                       | Super Admin         | Team Admin | Experiment Admin | Chat Viewer | Analysis Admin | Analysis User | Event Admin | Pipeline Admin | Annotation Reviewer |
|-------------------------------------------------|--------------------|------------|-----------------|-------------|---------------|--------------|-------------|---------------|---------------------|
| **Can See Experiments**                         | ✅                 | ❌         | ✅              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Can View Safety Layers, Source Material, Consent Forms** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Can See Tags**                                 | ✅                 | ❌         | ✅              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Can Access Prompt Builder**                   | ✅                 | ✅         | ✅              | ✅          | ✅            | ✅           | ✅          | ✅            | ❌                  |
| **Can View Graphs/Download Files**              | ✅                 | ❌         | ❌              | ✅          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Can Invite Participants**                     | ✅                 | ❌         | ✅              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Can Export Chat Transcripts**                 | ✅                 | ❌         | ✅              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Can Manage Files**                            | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Create and Manage Experiment Events**         | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ✅          | ❌            | ❌                  |
| **Create and Manage Pipelines**                 | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ✅            | ❌                  |
| **Can View Assigned Annotation Queues**         | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ✅                  |
| **Can View and Change Annotation Queue Items**  | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ✅                  |
| **Can Add Annotations**                         | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ✅                  |
| **Can View Annotation Aggregate Results**       | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ✅                  |
| **Can Manage Annotation Queues**                | ✅                 | ❌         | ❌              | ❌          | ❌            | ❌           | ❌          | ❌            | ❌                  |
| **Additional Notes**                         | **Full Access, Default Role** | - | **Cannot see sessions** | **View-only access to files** | - | - | - | - | **Annotation queues only; cannot manage queues, add sessions, export results, or access other app areas** |

**Can Manage Files** covers adding, changing, and deleting files — for example, in [collections](../collections/index.md) — and only **Super Admin** grants it.
A role with view-only file access, such as **Chat Viewer**, can see and download files but not add, change, or delete them.
