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
- An **onboarding guide** that walks new users through your own uploaded training content

## How it works

To search documents by meaning, OCS uses an **embedding model** — this technique is called **Retrieval-Augmented Generation (RAG)**. See [Local Index Optimization](../../tech-hub/local-index-optimization.md) for a full explanation.

## Which should I use?

In OCS, there are two types of indexes:

- [Remote Index](#remote-index)
- [Local Index](#local-index)

| | Remote Index | Local Index |
|---|---|---|
| **Managed by** | Your LLM provider (e.g. OpenAI) | OCS |
| **Setup** | Simpler — the provider handles everything | More steps — you choose the embedding model |
| **Embedding model** | Selected by the provider | You choose |
| **Chunking** | Handled by provider, not configurable | Configurable per file set |
| **Collections per LLM node** | Max 2 (OpenAI limit) | Unlimited |
| **Best for** | Getting started quickly | More control, or more than 2 collections |

If you are new to indexed collections, start with a **Remote Index**. Switch to a Local Index if you need more than 2 collections or want to [choose a specific embedding model](../../tech-hub/local-index-optimization.md#choosing-an-embedding-model) for your content type.

## Remote Index
Remote indexes are hosted and managed by your LLM provider. Files are uploaded to the provider, which handles all indexing. The embedding model is chosen by the provider.

### Supported LLM providers
- OpenAI

!!! warning "OpenAI limit of 2 remote index collections"

    When using remote (OpenAI-hosted) indexed collections, you can select a **maximum of 2 collections** when configuring a LLM node.

    - **Local indexes** are NOT affected by this limit — it only applies to OpenAI-hosted remote indexes
    - This limit comes from OpenAI's API, although it's not specifically documented

### Supported file types
Supported files are determined by the selected provider:

- OpenAI - See the [OpenAI docs](https://platform.openai.com/docs/assistants/tools/file-search/supported-files#supported-files)

## Local Index

Local indexes are hosted and managed by OCS. When you create a local index, you choose which embedding model to use. Different models suit different types of content, so choosing the right one can improve retrieval accuracy. See [Local Index Optimization](../../tech-hub/local-index-optimization.md#choosing-an-embedding-model) for guidance.

### Indexing Options

- **Supported LLM providers**: OpenAI, Voyage AI, Google Gemini
- **Supported file types**: pdf, txt, csv, docx
- **Supported embedding models**: You can see the list of embedding models for the LLM provider you have selected.

### Chunking and Optimization

When you upload a document to a local index, OCS breaks it into smaller parts called **chunks** and stores them in the index. The default chunking settings work well for most use cases.

For advanced configuration — including chunk size, chunk overlap, and embedding model selection — see [Local Index Optimization](../../tech-hub/local-index-optimization.md).

## Document Sources for Indexed Collections

Instead of uploading files manually, you can connect OCS to an external document source — such as a Confluence space or GitHub repository — and have it fetch and index content automatically on a schedule. This keeps your OCS indexed collection (for both remote and local indexes) current without manual uploads.

!!! note "Document-source updates reach published chatbots automatically"
    When a document-source sync runs and updates the collection's content, those changes are applied to your published chatbot without requiring a republish. See [Collections and published chatbots](./index.md#collections-and-published-chatbots) for more detail.

Currently supported sources: **Confluence** and **GitHub**.

For configuration steps, authentication setup, and how to monitor sync status, see [Set Up Document Sources](../../how-to/document_sources.md).
