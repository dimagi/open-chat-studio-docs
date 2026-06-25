---
title: RAG Index Optimization
---

This page covers advanced configuration options for indexed collections. For a conceptual overview of how indexed collections work, see [Indexed Collection for RAG](../concepts/collections/indexed.md).

## Choosing an Embedding Model (Local Indexes)

When you create a local index, you select which embedding model converts your documents into vectors. The model you choose affects how well the chatbot retrieves relevant content.

Different embedding models have different strengths:

- Some perform better on short, conversational text (FAQs, chat logs).
- Others are optimised for long, technical documents (reports, manuals, legal text).
- Models trained on domain-specific data (medical, legal, code) can outperform general-purpose models in those domains.

You can view the available embedding models for each provider when creating or editing the [LLM provider in your team](../concepts/team/llm_providers.md) settings. If you are unsure which model to choose, start with the default offered by your LLM provider — it is optimised for general-purpose retrieval.

!!! info "Local indexes are a new feature in OCS. We are actively working to support additional embedding models."

## Chunking and Optimization

When you upload a document to an index, OCS breaks it into smaller parts called **chunks**. Each chunk is converted into a vector and stored in the index. The chunking strategy affects how accurately the chatbot retrieves relevant content.

In most cases the default chunking strategy works well. You can customise it per set of uploaded files if needed:

| Setting       | What it controls                                        | When to adjust                                                  |
|---------------|---------------------------------------------------------|-----------------------------------------------------------------|
| Chunk size    | How large each chunk is, measured in tokens             | Increase for long, dense documents; decrease for short snippets |
| Chunk overlap | How much each chunk overlaps with the next              | Increase to preserve context across chunk boundaries            |

### Guidelines

- **Short documents or FAQs**: Use smaller chunks (e.g. 256–512 tokens) with low overlap. Each answer fits in one chunk, so large chunks add noise.
- **Long technical documents or reports**: Use larger chunks (e.g. 512–1024 tokens) with moderate overlap (10–20%) to preserve context across sections.
- **Structured data (tables, forms)**: Experiment with overlap settings — tables often lose meaning when split mid-row.

!!! warning "Changing the chunking strategy after upload requires re-indexing your files."
