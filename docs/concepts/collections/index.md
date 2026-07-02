# Collections

A collection is a group of files you can attach to a chatbot to give it access to content. There are two types of collections:

[Media collection](./media.md): Send files — such as images, PDFs, video, or audio — to participants during a conversation.
[Indexed collection](./indexed.md): Let your chatbot search your documents and ground its answers in that content (RAG).

## Adding a collection to a chatbot

Navigate to the **Collections** section in the sidebar and click "Add new". Once the collection is created, you will be able to upload files to it.

After your collection has been created and populated with files, you can link it to any [LLM node][llm_node].

## Collections and published chatbots

Collection content is a **live shared resource**: updates to your files in a collection reach your published chatbot automatically, without a republish. This applies whether you update a collection manually or via a scheduled [document-source](../../how-to/document_sources.md) sync:

- Adding or removing files from a [media collection](./media.md) takes effect for users immediately.
- Document-source syncs to an [indexed collection](./indexed.md#document-sources-for-indexed-collections) — for example, nightly Confluence or GitHub syncs — are applied to the published chatbot as each sync completes.

The collection *structure* of a published chatbot version — which collections are linked to which pipeline nodes — is still frozen at publish time. To change which collections a chatbot uses, you must publish a new version.

!!! note "What this means for drift detection"
    Because collection content is live, adding files to a collection or waiting for a document-source sync no longer marks your chatbot as having unpublished changes. Only changes to the chatbot's pipeline configuration and settings are tracked as pending changes.

!!! warning "Existing published bots"
    This live-collection behavior applies to chatbots republished after this change was introduced (2026-06-03). Bots that were published before retain their previous frozen collection snapshot until the next time they are republished.

For more detail on versioning in general, see [Versioning](../versioning.md).

[llm_node]: ../pipelines/nodes.md
