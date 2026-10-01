---
title: Indexed Collection (for RAG applications)
---
# Indexed Collection (for RAG applications)

An indexed collection lets your chatbot search through your documents to find relevant information before responding. Instead of relying on the AI's built-in knowledge, the chatbot retrieves answers from files you upload — such as PDFs, reports, or wiki pages.

## When should I use this?
When you want your chatbot's responses to be grounded in your uploaded documents.

Common examples include:

- A **customer support chatbot** that answers questions from your product documentation or FAQs
- An **HR assistant** that looks up company policies from an internal wiki or handbook
- A **research tool** that searches across uploaded reports, studies, or reference materials
- An **onboarding guide** that walks new participants through your own uploaded training content

## How it works

To search documents by meaning, OCS uses an **embedding model** — this technique is called **Retrieval-Augmented Generation (RAG)**. See [Local Index Optimization](../../tech-hub/local-index-optimization.md) for a full explanation.

## Using it in a chatbot

Once your collection is created and populated with files, [link it to an LLM node](./index.md#adding-a-collection-to-a-chatbot). Linking the collection isn't enough on its own — add the `{collection_index_summaries}` [prompt variable](../prompt_variables.md) to that node's prompt so the chatbot knows to search it.

## Next steps

- [Local and Remote Indexes](./local_and_remote_indexes.md) — choose where your files are indexed and how.
- [Document Sources](./document_sources.md) — sync files automatically from Confluence or GitHub.
