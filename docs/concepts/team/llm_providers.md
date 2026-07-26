# LLM Service Providers

Building chatbots in Open Chat Studio requires access to [LLMs](../llm.md). This requires configuring your [Teams](index.md) by providing credentials needed to access the LLM models provided by services such as OpenAI, Anthropic, and Google.

Open Chat Studio is developed to support a range of LLMs. The platform is designed to be flexible and can work with any
LLM that has an API. Open Chat Studio currently supports the following providers:

* [OpenAI](https://platform.openai.com/docs/models)
* [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models)
* [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure%2Cglobal-standard%2Cstandard-chat-completions)
* [Groq](https://console.groq.com/docs/models)
* [Perplexity](https://docs.perplexity.ai/guides/model-cards)
* [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)
* [Google Gemini](https://ai.google.dev/gemini-api/docs/models)
* [Voyage AI (embedding only)](https://docs.voyageai.com/docs/embeddings)

## LLM Models

Each service provider is pre-configured with the most common models for both AI inference and text embedding.

If a model you need isn't pre-configured, add it yourself: edit the provider and use the :material-plus-box: button in the "Custom LLM Models" section. See [Custom LLM Models](../../tech-hub/custom_llm_models.md) for step-by-step instructions and naming conventions.

## Model Lifecycle and Deprecation

AI providers regularly update their model offerings. This means models available in Open Chat Studio may occasionally be deprecated or removed.

- **Deprecation**: When a model you are using is deprecated, you will receive an in-app notification recommending that you switch to a replacement model. Your chatbots and pipelines continue to work during this period, but you should update your configuration at your earliest convenience.
- **Removal**: When a model is fully removed from the platform, Open Chat Studio automatically removes all references to it in your chatbots and pipelines. Where there is a clear replacement model, Open Chat Studio migrates usages of the old model to the recommended replacement. You will receive an in-app notification confirming that the removal or migration has taken place.

!!! note

    No manual action is required when a model is removed — the platform handles the transition for you.

## See also

- [Finding where a provider is used](index.md#finding-where-a-provider-is-used)
- [Configure LLM Service Providers](../../tutorials/configure_providers.md) — set up a provider
- [Custom LLM Models](../../tech-hub/custom_llm_models.md) — add a model that isn't pre-configured
- [Large Language Models (LLMs)](../llm.md) — key LLM concepts such as tokens and context window
