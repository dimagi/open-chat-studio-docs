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

To search documents by meaning, OCS uses an **embedding model** — this technique is called **Retrieval-Augmented Generation (RAG)**. See [Local Index Optimization](../../../tech-hub/local-index-optimization.md) for a full explanation.

## Using it in a chatbot

Once your collection is created and populated with files, [link it to an LLM node](../index.md#adding-a-collection-to-a-chatbot). Linking the collection isn't enough on its own — add the `{collection_index_summaries}` [prompt variable](../../prompt_variables.md) to that node's prompt so the chatbot knows to search it.

## Snapshots

A snapshot is a read-only copy of an indexed collection at a point in time.
It includes the collection's files, their indexed content, and its [document sources](./document_sources.md).
Use one to keep a reference copy before a large change, such as a big re-sync.

To create a snapshot, click **Create snapshot** in the **Snapshots** section at the bottom of the collection page.
OCS shows **Creating snapshot** while it works, which can take a while for large collections.
Each snapshot is listed with a version number and date, such as `v1`. Click **View** to open it.

Keep these limits in mind:

- You can't add or remove files in a snapshot.
- You can't restore, rename, or delete a snapshot.
- Auto Sync skips snapshots, so they stay as they were.
- Publishing a chatbot doesn't create a snapshot.
  See [Collections and published chatbots](../index.md#collections-and-published-chatbots) for how published chatbots use collections.

## See also

- [Local](./local_and_remote_indexes.md#local-index) or [Remote](./local_and_remote_indexes.md#remote-index) Indexes — choose where your files are indexed and how.
- [Document Sources](./document_sources.md) — sync files automatically from Confluence or GitHub.
