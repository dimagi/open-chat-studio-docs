---
title: OpenAI Assistants (Removed)
---

# OpenAI Assistants (Removed)

!!! warning "OpenAI Assistants have been removed from Open Chat Studio"
    OpenAI retired the Assistants API on 26 August 2026. Open Chat Studio has removed the feature in two steps:

    - The Assistants pages were removed first — assistants can no longer be created, viewed, edited, or archived through the UI, and the Assistants entry no longer appears in the sidebar.
    - The assistant pipeline node and its runtime have now been removed too. A pipeline that still contains an assistant node opens in the pipeline editor, but the node renders as a **Removed Node** and the pipeline no longer builds — its chatbot cannot run until you replace that node.

    Your assistant records themselves are not deleted by this change — they are simply unreachable, since nothing in Open Chat Studio can use or display them any more. A later release will delete them for good.

    **What this means for you:**

    - If a pipeline still contains an assistant node, replace it with an [LLM node](pipelines/nodes.md#llm-node) before that chatbot can run again.
    - Open Chat Studio offers each of the assistant capabilities in another form — threads as [sessions](sessions.md), code interpreter as an LLM node builtin tool, and file search as an [indexed collection](collections/indexed.md).

    See the [migration guide](../how-to/assistants_migration.md) for step-by-step instructions on replacing an assistant node.
