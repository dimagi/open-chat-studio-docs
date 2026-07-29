# LLM Service Providers

An **LLM provider** is the company that hosts the AI models powering your chatbot — for example OpenAI, Anthropic, or Google. Building chatbots in Open Chat Studio requires access to [Large Language Models (LLMs)](../llm.md). You'll need an account with at least one provider. Enter its credentials in your Team settings so Open Chat Studio chatbots can access its models.

Open Chat Studio is designed to be flexible, and can connect to any LLM provider that offers an API. It has built-in support for the following providers, each offering a range of models:

* [OpenAI](https://platform.openai.com/docs/models)
* [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models)
* [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure%2Cglobal-standard%2Cstandard-chat-completions)
* [Groq](https://console.groq.com/docs/models)
* [Perplexity](https://docs.perplexity.ai/guides/model-cards)
* [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)
* [Google Gemini](https://ai.google.dev/gemini-api/docs/models)
* [MiniMax](https://platform.minimax.io)
* [Voyage AI (embedding only)](https://docs.voyageai.com/docs/embeddings)

## LLM Models

Each provider comes with its most commonly used models already available in OCS — models that power chatbot conversations, and embedding models used for searching [knowledge bases](../collections/indexed.md).

If a model you need isn't pre-configured, see [Add a Custom LLM Model](../../how-to/add_custom_llm_model.md) for how to add one.

## Model Lifecycle and Deprecation

LLM providers regularly update their model offerings. This means models available in Open Chat Studio may occasionally be deprecated or removed.

- **Deprecation**: When a model you are using is deprecated, you will receive an in-app notification recommending that you switch to a replacement model. Your chatbots and pipelines continue to work during this period, but you should update your chatbot configuration at your earliest convenience.
- **Removal**: When a model is fully removed from the platform, Open Chat Studio updates your chatbots and pipelines automatically. If a clear replacement model exists, it switches the chatbots to that model; otherwise, it clears the reference to the removed model. Either way, you'll receive an in-app notification confirming what changed.

!!! note

    No manual action is required when a model is removed — the platform handles the transition for you.

## See also

- [Configure LLM Service Providers](../../tutorials/configure_llm_providers.md) — set up a provider to use in your chatbots
- [Finding where an LLM provider is used](index.md#finding-where-a-provider-is-used) — in your chatbots
- [Add a Custom LLM Model](../../how-to/add_custom_llm_model.md) — add a model that isn't pre-configured, including naming conventions per provider
- [Large Language Models (LLMs)](../llm.md) — key LLM concepts such as tokens and context window
