---
title: Indexed Collection (for RAG applications)
---

An indexed collection lets your chatbot search through your documents to find relevant information before responding. Instead of relying on the AI's built-in knowledge, the chatbot retrieves answers from files you upload — such as PDFs, reports, or wiki pages.

## When should I use this?
When you want your chatbot's responses to be grounded in your uploaded documents.

Common examples include:

- A **customer support chatbot** that answers questions from your product documentation or FAQs
- An **HR assistant** that looks up company policies from an internal wiki or handbook
- A **research tool** that searches across uploaded reports, studies, or reference materials
- An **onboarding guide** that walks new users through your own uploaded training content

!!! note "Definition"
    **Retrieval-Augmented Generation** (RAG) is a technique where a language model retrieves relevant information from a set of documents to ground its answers in real data. Instead of relying solely on its built-in knowledge, the model uses indexes—specialized databases that store document content as vectors (numerical representations of meaning). This makes it easy for the model to find and use the most relevant parts of your uploaded files when answering questions.

!!! warning "Indexed collections will replace OpenAI Assistants' file search functionality in the future"

    Consult the [migration guide][migration-guide] if you have assistants that you want to replace with indexed collections.

If you’ve used the OpenAI Assistants’ [file search][file-search] capability in OCS, you’ve already interacted with an index behind the scenes.

To search documents by meaning, OCS uses an **embedding model** — a component that converts text into a mathematical form so the chatbot can find conceptually related content even when the exact words don't match. For example, a user asking "how do I cancel?" can match a document that says "terminating your subscription."

In OCS, there are two types of indexes:

- Remote Index
- Local Index

### Which should I use?

| | Remote Index | Local Index |
|---|---|---|
| **Managed by** | Your LLM provider (e.g. OpenAI) | OCS |
| **Setup** | Simpler — the provider handles everything | More steps — you choose the embedding model |
| **Embedding model** | Selected by the provider | You choose |
| **Collections per LLM node** | Max 2 (OpenAI limit) | Unlimited |
| **Best for** | Getting started quickly | More control, or more than 2 collections |

If you are new to indexed collections, start with a **Remote Index**. Switch to a Local Index if you need to use more than 2 collections, or want to choose a specific embedding model for your content type.

## Remote Index
Remote indexes are hosted and managed by an LLM provider. Files and index configuration are uploaded to the provider, which maintains and manages the index. The embedding model used to create file embeddings is selected by the provider.

### Supported providers
- OpenAI (using the [responses API](https://platform.openai.com/docs/api-reference/responses))

!!! warning "OpenAI Remote Collection Limit"

    When using OpenAI as your LLM provider with remote (OpenAI-hosted) indexed collections, you can select a **maximum of 2 collections per LLM node**. This is a limitation imposed by OpenAI's API, not Open Chat Studio.

    - **Local indexes** are NOT affected by this limit
    - **Non-OpenAI providers** are NOT affected by this limit
    - If you attempt to select more than 2 remote collections with OpenAI, you will receive a validation error

    If you need to use more than 2 collections, consider using local indexes instead.

### Supported file types
Supported files are determined by the selected provider:

- OpenAI - See the [OpenAI docs](https://platform.openai.com/docs/assistants/tools/file-search/supported-files#supported-files)

## Local Index
!!! info "Local indexes are a new feature in OCS. We are actively working to support additional file types and embedding models, allowing you to better customize your index with models that suit your needs."

Local indexes are hosted and managed by OCS. When you create a local index, you choose which embedding model to use. Different models suit different content types for a chatbot, so choosing the right one can improve retrieval accuracy. See [RAG Index Optimization](../../tech-hub/local-index-optimization.md#choosing-an-embedding-model-local-indexes) for guidance.

### Supported providers
- OpenAI
- Voyage AI

### Supported file types
- pdf
- txt
- csv
- docx

### Supported embedding models
You can see the supported embedding models for each provider when creating or editing the provider in your team settings.

## Chunking and Optimization
When you upload a document, OCS breaks it into smaller parts called **chunks** and stores them in the index. The default chunking settings work well for most use cases.

For advanced configuration — including chunk size, chunk overlap, and embedding model selection — see [RAG Index Optimization](../../tech-hub/local-index-optimization.md).

[file-search]: ../experiment/index.md#file-search
[migration-guide]: ../../how-to/assistants_migration.md

## Document Sources

In addition to manually uploading documents to a collection, you can also configure document sources from which Open Chat Studio will automatically load and index documents.

The primary advantage of document sources over manual uploads is that Open Chat Studio can check for updates periodically, which eliminates the need for manual updates.

!!! note "Document-source updates reach published chatbots automatically"
    When a document-source sync runs and updates the collection's content, those changes are applied to your published chatbot without requiring a republish. See [Collections and published bots](./index.md#collections-and-published-bots) for more detail.

The following document source types are currently supported:

### :simple-confluence: Confluence

Load pages from a Confluence site. Pages can be filtered using the space key, label, CQL, or individual page IDs.

**Authentication**

Use a [Basic Auth](../team/authentication_providers.md#basic-auth) authentication provider with your Atlassian username and use your API Key as the password.

**Configuration**

| Field     | Description                                                               |
|-----------|---------------------------------------------------------------------------|
| Site URL  | The URL of the Confluence site (e.g. https://yoursite.atlassian.net/wiki) |
| Max Pages | The maximum number of pages to load                                       |
| Space Key | Load pages from this space                                                |
| Label     | Load pages with this label                                                |
| CQL       | CQL query to use to search for pages to load                              |
| Page IDs  | Load only these specific pages                                            |

!!! note

    Only one of the `Space Key`, `Label`, `CQL` and `Page IDs` fields can be used at a time.

### :simple-github: GitHub

Load pages from a GitHub repository. Files can be filtered by path and by matching patterns against the filenames.

**Authentication**

Use a [Bearer Token](../team/authentication_providers.md#bearer-token) authentication provider.

**Configuration**

| Field          | Description                                                          |
|----------------|----------------------------------------------------------------------|
| Repository URL | GitHub repository URL (e.g. https://github.com/user/repo)            |
| Branch         | Git branch to sync from                                              |
| File Pattern   | File patterns to include. Prefix with '!' to exclude matching files. |
| Path Filter    | Optional path prefix to filter files (e.g., docs/)                   |

## Monitoring Sync Status

Open Chat Studio tracks the history of every sync run for each document source. Use the sync logs to confirm that syncs are completing successfully and to diagnose problems when they are not.

### Status indicator

Each document source header displays a status indicator reflecting the outcome of the most recent sync:

- **Error** – the last sync encountered a problem. The indicator is shown in red.
- **Success** – the last sync completed without errors.
- **In progress** – a sync is currently running. The indicator animates to show activity.
