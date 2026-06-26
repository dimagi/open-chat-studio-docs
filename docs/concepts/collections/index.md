# Collections

A collection in OCS refers to a collection of files. There are two types of collections:

- [Media collection](./media.md)
- [Indexed Collection (for RAG applications)](./indexed.md)

## Adding a collection to a chatbot

Navigate to the **Collections** section in the sidebar and click "Add new". Once the collection is created, you will be able to upload files to it.

After your collection has been created and populated with files, you can link it to any [LLM node][llm_node].

## Collections and published chatbots

Collection content is a **live shared resource**. When you update the files in a collection — either manually or through a scheduled document-source sync — those changes are reflected in your published chatbot automatically. You do not need to republish to pick up new or updated files.

This means:

- Adding or removing files from a media collection takes effect for users immediately.
- Document-source syncs to a RAG index collection (for example, nightly Confluence or GitHub syncs) are applied to the published chatbot as each sync completes.

The *structure* of a published version — which collections are linked to which pipeline nodes — is still frozen at publish time. To change which collections a chatbot uses, you must publish a new version.

For more detail on how versioning interacts with collections, see [Versioning](../versioning.md#what-is-frozen-and-what-is-live).

[llm_node]: ../pipelines/nodes.md
