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

## LLM Models

Each service provider is pre-configured with the most common models for both AI inference and text embedding. 

Should the service provider configuration not include a model which is available via the provider, it may be added directly via the user interface. This is done by editing the provider and using the :material-plus-box: button in the 'Custom Models' section.

### Adding Custom LLM Models

If your LLM provider list doesn't have a pre-configured model you want to use, you can add it under the "Custom LLM Models" section.

See the [How to guide for adding custom LLM models](../../how-to/configure_providers.md)