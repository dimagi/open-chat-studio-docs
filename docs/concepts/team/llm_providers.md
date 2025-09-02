# LLM Service Providers

Building chatbots in Open Chat Studio requires access to [LLMs](../llm.md). This requires providing Open Chat Studio with credentials needed to access the models provided by external services such as OpenAI, Anthropic, and Google.

Open Chat Studio currently supports the following providers:

* OpenAI
* Anthropic
* Google Gemini
* Azure OpenAI
* Groq
* Perplexity
* DeepSeek

## Models

Each service provider is pre-configured with the most common models for both AI inference and text embedding. Should the service provider configuration not include a model which is available via the provider, it may be added directly via the user interface. This is done by editing the provider and using the :material-plus-box: button in the 'Custom Models' section.
