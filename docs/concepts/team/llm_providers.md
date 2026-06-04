# LLM Service Providers

Building chatbots in Open Chat Studio requires access to [LLMs](../llm.md). This requires configuring your [Teams](index.md) by providing credentials needed to access the LLM models provided by services such as OpenAI, Anthropic, and Google.

Open Chat Studio currently supports the following providers:

* OpenAI
* Anthropic
* Google Gemini
* Azure OpenAI
* Groq
* Perplexity
* DeepSeek
* Voyage AI (embedding only)

## LLM Models

Each service provider is pre-configured with the most common models for both AI inference and text embedding. 

Should the service provider configuration not include a model which is available via the provider, it may be added directly via the user interface. This is done by editing the provider and using the :material-plus-box: button in the 'Custom Models' section.

### Adding Custom LLM Models

If your LLM provider list doesn't have a pre-configured model you want to use, you can add it under the "Custom LLM Models" section.

See the [How to guide for adding custom LLM models](../../tutorials/configure_providers.md)

## Model Lifecycle and Deprecation

AI providers regularly update their model offerings. This means models available in Open Chat Studio may occasionally be deprecated or removed.

- **Deprecation**: When a model you are using is deprecated, you will receive an in-app notification recommending that you switch to a replacement model. Your chatbots and pipelines continue to work during this period, but you should update your configuration at your earliest convenience.
- **Removal**: When a model is fully removed from the platform, Open Chat Studio automatically removes all references to it in your chatbots and pipelines. Where there is a clear replacement model, Open Chat Studio migrates usages of the old model to the recommended replacement. You will receive an in-app notification confirming that the removal or migration has taken place.

No manual action is required when a model is removed — the platform handles the transition for you.