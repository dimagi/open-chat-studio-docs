---
title: Indexed Collection (for RAG applications)
---

## When should I use this?
When you want your bot's responses to be grounded in your uploaded documents.

!!! note "Definition"
    **Retrieval-Augmented Generation** (RAG) is a technique where a language model retrieves relevant information from a set of documents to ground its answers in real data. Instead of relying solely on its built-in knowledge, the model uses indexes—specialized databases that store document content as vectors (numerical representations of meaning). This makes it easy for the model to find and use the most relevant parts of your uploaded files when answering questions.

!!! warning "Indexed collections will replace OpenAI Assistants' file search functionality in the future"

If you’ve used the OpenAI Assistants’ [file search][file-search] capability in OCS, you’ve already interacted with an index behind the scenes.

!!! tip "TIP: You can create an indexed collection from an OpenAI assistant that uses file search by clicking the `Create from assistant` button"

In OCS, there are two types of indexes:

- Remote Index
- Local Index

## Remote Index
Remote indexes are hosted and managed by an LLM provider. Files and index configuration are uploaded to the provider, which maintains and manages the index. The embedding model used to create file embeddings is selected by the provider.

### Supported providers
- OpenAI

### Supported file types
Supported files are determined by the selected provider:

- OpenAI - See the [OpenAI docs](https://platform.openai.com/docs/assistants/tools/file-search/supported-files#supported-files)



## Local Index
!!! info "Local indexes are a new feature in OCS. We are actively working to support additional file types and embedding models, allowing you to better customize your index with models that suit your needs."

Local indexes are hosted and managed by OCS. When you create a local index, you can select which embedding model to use for generating file embeddings. Embedding models are provided by LLM providers. Just as different LLM models have varying strengths and weaknesses, different embedding models also have their own strengths and weaknesses. Thus, choosing the right embedding model is important to ensure the best performance for your specific use case.

### Supported providers
- OpenAI

### Supported file types
- pdf
- txt
- csv
- docx

### Supported embedding models
You can see the supported embedding models for each provider when creating or editing the provider in your team settings.


## Chunking and Optimization
When you upload a document to an index, it’s broken up into smaller parts called chunks. These chunks are then converted into vectors and stored in the index. Chunking is a key part of how RAG works, as it affects how accurately the model can retrieve relevant information.

In most cases, it will not be necessary to change the default chunking strategy, but you’ll have the option to customize the chunking strategy for each set of uploaded files:

- Chunk size – how large each chunk is (in tokens)
- Chunk overlap – how much each chunk overlaps with the next, to preserve context

Choosing the right chunking strategy can improve retrieval accuracy, especially for technical documents.

!!! info "This flexibility helps tailor the index to your use case—whether it’s short notes or long, complex reports."


[file-search]: ../experiment/index.md#file-search
