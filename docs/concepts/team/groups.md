# User Groups on OCS

Users can be assigned to specific groups upon invitation to the OCS platform, giving them tailored access based on their role.
Users can be put in one or multiple groups.

!!! note "Where roles appear in the UI"
    Each group a person belongs to is shown as a **Roles** badge on their row in the [Members & access](members.md) table in Team Settings.

## Permissions table

| Capability                                                          | Super Admin | Team Admin | Chatbot Admin | Chat Viewer | Assistant Admin | Event Admin | Evaluation Admin | Annotation Reviewer |
|----------------------------------------------------------------------|:-----------:|:----------:|:--------------:|:------------:|:-----------------:|:--------------:|:-------------------:|:----------------------:|
| Manage team settings, members & invitations, custom actions, integrations & OAuth applications | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Create, edit & delete chatbots, pipelines, bot channels & collections   | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Invite chatbot participants & export chat transcripts                  | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage annotation queues & comments, and apply tags                    | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| View annotation queues, review items & add annotations                 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| View chat transcripts and sessions (read-only)                         | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Manage assistants and their files                                      | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Manage events, triggers & scheduled messages                           | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Manage evaluations, evaluators & datasets                              | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |

### Notes

- **Super Admin** grants full access to every team resource and is assigned by default to whoever creates a team.
- **Chatbot Admin** already has full access to a chatbot's sessions as part of managing it, so the read-only "View chat transcripts and sessions" row above mainly applies to **Chat Viewer** and **Annotation Reviewer**.
- **Annotation Reviewer** access is limited to annotation queues and chat transcripts — it doesn't include managing queues, chatbots, or other app areas.
- A team must always keep at least one **Team Admin** (or Super Admin); OCS blocks removing the last one.

## See also

- [Members & Access](members.md)
- [Team Settings](index.md)
