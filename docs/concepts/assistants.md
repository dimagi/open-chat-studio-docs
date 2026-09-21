---
title: OpenAI Assistants (Removed)
---

# OpenAI Assistants (Removed)

!!! warning "OpenAI Assistants have been removed from Open Chat Studio"
    OpenAI retired the Assistants API on 26 August 2026. Open Chat Studio has removed the feature in three steps:

    - The Assistants pages were removed first — assistants can no longer be created, viewed, edited, or archived through the UI, and the Assistants entry no longer appears in the sidebar.
    - The assistant pipeline node and its runtime were removed next. A pipeline that still contains an assistant node opens in the pipeline editor, but the node renders as a **Removed Node** and the pipeline no longer builds — its chatbot cannot run until you replace that node.
    - All stored assistant records have now been deleted permanently and irreversibly, along with their tool resources and any custom action operation that was attached to an assistant. Custom actions themselves, and operations attached to pipeline nodes, are not affected. The audit log retains a history of the deleted records, but the data itself cannot be recovered.

    **What this means for you:**

    - If a pipeline still contains an assistant node, replace it with an [LLM node](pipelines/nodes.md#llm-node) before that chatbot can run again.
    - Open Chat Studio offers each of the assistant capabilities in another form — threads as [sessions](sessions.md), code interpreter as an LLM node builtin tool, and file search as an [indexed collection](collections/indexed.md).
    - The **Assistant Admin** [team role](team/groups.md) has also been removed — it can no longer be granted to a member or attached to an invitation.
      It was the only role granting full file management (add, change, delete), so anyone who relied on it for that needs another role.

    See the [migration guide](../how-to/assistants_migration.md) for step-by-step instructions on replacing an assistant node.
