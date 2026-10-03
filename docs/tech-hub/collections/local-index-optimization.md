---
title: Local Index Optimization
---
# Local Index Optimization

This page covers advanced configuration options for [indexed collections](../../concepts/collections/indexed_collections/index.md).

## Choosing an Embedding Model

An embedding model converts your documents into a numeric form so the chatbot can search by *meaning* instead of exact keywords. It finds related content even when a participant uses different words.
You choose the model when you create a local index, and it affects how relevant the retrieved content is.

Different embedding models have different strengths:

- Some perform better on short, conversational text (FAQs, chat logs).
- Others are optimised for long, technical documents (reports, manuals, legal text).
- Models trained on domain-specific data (medical, legal, code) can outperform general-purpose models in those domains.

To see a provider's embedding models, open the **Models** tab of its page in your [team's LLM provider](../../concepts/team/llm_providers.md) settings and filter for embedding models.
If you are unsure which to choose, use the provider's default, which suits general-purpose retrieval.

## Chunking and Optimization

!!! info
    Chunking is configured in OCS for local indexes only. For remote indexes, the provider (e.g. OpenAI) handles chunking internally and it cannot be configured.

OCS breaks each document uploaded to a local index into smaller parts called **chunks**, converts each chunk into a vector and stores it in the index.
The default chunking strategy works well in most cases.
If needed, you can customise it per set of uploaded files:

| Setting       | What it controls                                        | When to adjust                                                  |
|---------------|---------------------------------------------------------|-----------------------------------------------------------------|
| Chunk size    | How large each chunk is, measured in tokens             | Increase for long, dense documents; decrease for short snippets |
| Chunk overlap | How much each chunk overlaps with the next              | Increase to preserve context across chunk boundaries            |

Files synced by a [document source](document_sources.md) always use a chunk size of 800 tokens and an overlap of 400 tokens.
You can't change these values per source.

### Guidelines

- **Short documents or FAQs**: Use smaller chunks (e.g. 256–512 tokens) with low overlap. Each answer fits in one chunk, so large chunks add noise.
- **Long technical documents or reports**: Use larger chunks (e.g. 512–1024 tokens) with moderate overlap (10–20%) to preserve context across sections.
- **Structured data (tables, forms)**: Experiment with overlap settings — tables often lose meaning when split mid-row.

!!! warning "Changing the chunking strategy after upload requires re-indexing your files."
