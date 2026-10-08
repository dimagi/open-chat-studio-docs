---
title: Indexed Collections (for RAG applications)
---
# Indexed Collections (for RAG applications)

An indexed collection lets your chatbot search through your documents to find relevant information before responding. Instead of relying on the AI's built-in knowledge, the chatbot retrieves answers from files you upload — such as PDFs, reports, or wiki pages.

## When should I use this?
When you want your chatbot's responses to be grounded in your uploaded documents.

Common examples include:

- A **customer support chatbot** that answers questions from your product documentation or FAQs
- An **HR assistant** that looks up company policies from an internal wiki or handbook
- A **research tool** that searches across uploaded reports, studies, or reference materials
- An **onboarding guide** that walks new participants through your own uploaded training content

## How it works

To search documents by meaning, OCS uses an **embedding model**. Retrieving relevant passages and giving them to the AI model to answer from is called **Retrieval-Augmented Generation (RAG)**. See [Local Index Optimization](../../../tech-hub/collections/local-index-optimization.md) for a full explanation.

## Using it in a chatbot

Once your collection is created and populated with files, [link it to an LLM node](../index.md#adding-a-collection-to-a-chatbot). Linking the collection isn't enough on its own — add the `{collection_index_summaries}` [prompt variable](../../prompt_variables.md) to that node's prompt so the chatbot knows to search it.

### Limiting the search to matching metadata

If several chatbots share one collection, you can set **Metadata Filters** on the LLM node so each chatbot searches only rows whose metadata matches.
See [Filter Collection Search by Metadata](../../../how-to/filter_collection_search_by_metadata.md).

## Snapshots

A snapshot is a read-only copy of an indexed collection at a point in time.
It includes the collection's files, their indexed content, and its [document sources](./document_sources.md).
Use one to keep a reference copy before a large change, such as a big re-sync.

You create a snapshot from the **Snapshots** section at the bottom of the collection page.
Each snapshot is listed there with a version number and date, such as `v1`, and you can open it to see what it contains.
Creating one can take a while for large collections, and the page shows its progress.

Keep these limits in mind:

- You can't add or remove files in a snapshot.
- You can't restore, rename, or delete a snapshot.
- Auto Sync skips snapshots, so they stay as they were.
- Publishing a chatbot doesn't create a snapshot.
  See [Collections and published chatbots](../index.md#collections-and-published-chatbots) for how published chatbots use collections.

## See also

- [Local](./local_and_remote_indexes.md#local-index) or [Remote](./local_and_remote_indexes.md#remote-index) Indexes — choose where your files are indexed and how.
- [Document Sources](./document_sources.md) — sync files automatically from Confluence or GitHub.
- [Metadata Filters Reference](../../../tech-hub/collections/metadata-filters.md) — how filtered search behaves.
