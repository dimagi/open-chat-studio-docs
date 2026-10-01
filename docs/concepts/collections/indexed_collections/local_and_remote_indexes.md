---
title: Local and Remote Indexes
---
# Local and Remote Indexes

An [indexed collection](./index.md) stores its files in an index that the chatbot searches. In OCS, there are two types of indexes:

- [Remote Index](#remote-index)
- [Local Index](#local-index)

## Which should I use?

| | Remote Index | Local Index |
|---|---|---|
| **Managed by** | Your [LLM provider](../../team/llm_providers.md) (e.g. OpenAI) | OCS |
| **Setup** | Simpler — the provider handles everything | More steps — you choose the embedding model |
| **Embedding model** | Selected by the provider | You choose |
| **Chunking** | Handled by provider, not configurable | Configurable per file set |
| **Collections per LLM node** | Max 2 (OpenAI limit) | Unlimited |
| **Best for** | Getting started quickly | More control, or more than 2 collections |

!!! tip "Start with a Remote Index"
    If you are new to indexed collections, start with a **Remote Index**. Switch to a Local Index if you need more than 2 collections or want to [choose a specific embedding model](../../../tech-hub/local-index-optimization.md#choosing-an-embedding-model) for your content type.

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

### Checking why a file failed to index

If a file fails to index, its entry in the collection's file list shows a red status badge.
Hover over the badge to see why it failed — for example, a rejected API key, an exceeded quota, or a dropped connection.
This message comes directly from your LLM provider.

!!! note "Provider error messages are shown as-is"
    OCS doesn't filter or mask the provider's error message.
    Some providers redact sensitive details automatically — OpenAI, for example, masks your API key in its own error message — but not every provider does.

## Local Index

Local indexes are hosted and managed by OCS. When you create a local index, you choose which embedding model to use. Different models suit different types of content, so choosing the right one can improve retrieval accuracy. See [Local Index Optimization](../../../tech-hub/local-index-optimization.md#choosing-an-embedding-model) for guidance.

### Indexing Options

- **Supported LLM providers**: OpenAI, Voyage AI, Google Gemini
- **Supported file types**: pdf, txt, csv, docx
- **Supported embedding models**: You can see the list of embedding models for the LLM provider you have selected.

### Chunking and Optimization

When you upload a document to a local index, OCS breaks it into smaller parts called **chunks** and stores them in the index. The default chunking settings work well for most use cases.

For advanced configuration — including chunk size, chunk overlap, and embedding model selection — see [Local Index Optimization](../../../tech-hub/local-index-optimization.md).
