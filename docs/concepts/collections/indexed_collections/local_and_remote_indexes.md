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
| **Chunking** | Done by the provider, using the chunk size and overlap you set in OCS | Done by OCS, using the chunk size and overlap you set |
| **Collections per LLM node** | Max 2 (OpenAI limit) | Unlimited |
| **Best for** | Getting started quickly | More control, or more than 2 collections |

!!! tip "Start with a Remote Index"
    If you are new to indexed collections, start with a **Remote Index**. Switch to a Local Index if you need more than 2 collections or want to [choose a specific embedding model](../../../tech-hub/collections/local-index-optimization.md#choosing-an-embedding-model) for your content type.

## Remote Index
Remote indexes are hosted and managed by your LLM provider, which indexes your uploaded files and chooses the embedding model.

### Supported LLM providers
- OpenAI

!!! warning "OpenAI limit of 2 remote index collections"

    When using remote (OpenAI-hosted) indexed collections, you can select a **maximum of 2 collections** when configuring a LLM node.

    The limit comes from OpenAI's API, although it's not specifically documented. Local indexes are not affected.

### Supported file types
Remote indexes accept the same file types as [local indexes](#indexing-options).

### Checking why a file failed to index

If a file fails to index, its entry in the collection's file list shows a red status badge.
Hover over the badge to see why it failed — for example, a rejected API key, an exceeded quota, or a dropped connection.
This message comes directly from your LLM provider.

!!! note "Provider error messages are shown as-is"
    OCS doesn't filter or mask the provider's error message.
    Some providers redact sensitive details automatically — OpenAI, for example, masks your API key in its own error message — but not every provider does.

## Local Index

Local indexes are hosted and managed by OCS. When you create one, you choose the embedding model. See [Local Index Optimization](../../../tech-hub/collections/local-index-optimization.md#choosing-an-embedding-model) for guidance.

### Indexing Options

- **Supported LLM providers**: OpenAI, Voyage AI, Google Gemini
- **Supported file types**: txt, md, pdf, doc, docx, pptx, html, json, and common code files (c, cs, cpp, java, php, py, rb, tex, css, js, sh, ts)
- **Supported embedding models**: The embedding models available for the LLM provider you select.

`.csv` and `.tsv` files are not accepted through regular file upload. Add them through [Importing CSV/TSV rows](#importing-csvtsv-rows) instead.

### Chunking and Optimization

OCS breaks uploaded documents into smaller parts called **chunks**. The default settings work well for most use cases.
For chunk size, chunk overlap and embedding model selection, see [Local Index Optimization](../../../tech-hub/collections/local-index-optimization.md).

### Importing CSV/TSV rows

You can import a `.csv` or `.tsv` file so each row becomes its own searchable record.
Use **Add Files → Import CSV/TSV rows** on a local-index collection.
This is the only way to add a CSV or TSV file to an indexed collection, because regular file upload doesn't accept them.

Each row is indexed as one chunk.
The chunk text is the file name followed by one `column: value` line for every column in the row.
The columns you tick are also stored as metadata on the row's chunk.
When a chatbot searches the collection, each matching row comes back with its row number and its metadata.

!!! note "Local indexes only"
    Row import works for local indexes only.
    Remote (OpenAI) indexes don't offer the **Import CSV/TSV rows** option.

See [Import CSV/TSV Rows into a Collection](../../../how-to/import_csv_tsv_rows.md) for step-by-step instructions.
