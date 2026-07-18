# Collections

Give your chatbot access to your files — grouped into a **collection** — whether that's sending them to users during a conversation, or letting the chatbot search them to answer questions. There are two types of collections, depending on what you want to do:

- **Want to send files to users in a conversation?** Use a **[Media collection](./media.md)** — share images, PDFs, video, or audio directly in the chat.
- **Want your chatbot to answer questions using your documents?** Use an **[Indexed collection](./indexed.md)** — it searches your files and grounds its answers in that content (RAG).

## Adding a collection to a chatbot

1. Navigate to the **Collections** section in the sidebar, click "Add new", and choose a collection type: [Media Collection](./media.md) or [Indexed Collection (RAG)](./indexed.md).
2. Once the collection is created, you will be able to upload files to it.
3. For indexed collections, you'll also need to choose between a Remote and a Local index before uploading — see [Which should I use?](./indexed.md#which-should-i-use).
4. After your collection has been created, you can link it to any [LLM node][llm_node]. To actually access the collection's content, add the matching [prompt variable](../prompt_variables.md) to the node's prompt — `{media}` for media collections, or `{collection_index_summaries}` for indexed collections.

## Collections and published chatbots

Collection content is a **live shared resource**: updates to your files in a collection reach your published chatbot automatically, without a republish. This applies whether you update a collection manually or via a scheduled [document-source](../../how-to/document_sources.md) sync.

- Adding or removing files from a [media collection](./media.md) takes effect for users immediately.
- Document-source syncs to an [indexed collection](./indexed.md#document-sources-for-indexed-collections) — for example, nightly Confluence or GitHub syncs — are applied to the published chatbot as each sync completes.

The collection *structure* of a published chatbot version — which collections are linked to which pipeline nodes — is still frozen at publish time. To change which collections a chatbot uses, you must publish a new version.

!!! note "What this means for drift detection"
    Because collection content is live, adding files to a collection or waiting for a document-source sync no longer marks your chatbot as having unpublished changes. Only changes to the chatbot's pipeline configuration and settings are tracked as pending changes.

!!! warning "Existing published chatbots"
    This live-collection behavior applies to chatbots republished after this change was introduced (2026-06-03). Chatbots that were published before retain their previous frozen collection snapshot until the next time they are republished.

For more detail on versioning in general, see [Versioning](../versioning.md).

[llm_node]: ../pipelines/nodes.md#llm-node
