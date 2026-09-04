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
* [LiteLLM](https://docs.litellm.ai/docs/simple_proxy) (bring your own proxy)

## LLM Models

Each provider comes with its most commonly used models already available in OCS — models that power chatbot conversations, and embedding models used for searching [knowledge bases](../collections/indexed.md).

On a provider's page, the **Models** tab lists every model it offers. Filter chips above the list let you switch between chat models and embedding models, and each chip shows how many models match — so the count always matches what's filtered below it.

If a model you need isn't pre-configured, see [Add a Custom LLM Model](../../how-to/add_custom_llm_model.md) for how to add one.

!!! note "LiteLLM has no pre-configured models"

    LiteLLM connects to a model gateway you run yourself, so Open Chat Studio has no way to know in advance which models it serves. After adding a LiteLLM provider, add every model you want to use as a [custom model](../../how-to/add_custom_llm_model.md).

## Credential Verification

Open Chat Studio checks your provider credentials against the provider's API and keeps showing the result on the provider's page, rather than as a one-off message. A provider's credentials show one of three states:

- **Verified**: the credentials were confirmed to work.
- **Never checked**: no successful check has run yet.
- **Rejected**: the last check failed. The page shows the provider's own error message, so you can see exactly why.

Verification runs automatically whenever you save a provider whose credentials haven't yet passed a check — including a provider stuck in the **Rejected** state, so saving again after fixing a key re-checks it. A provider whose credentials are already **Verified** isn't re-checked unless you change its credentials. The save button tells you upfront whether saving will trigger a check.

!!! note "Voyage AI is never verified"

    [Voyage AI](https://docs.voyageai.com/docs/embeddings) is an embeddings-only provider and is never offered credential verification.

## Model Lifecycle and Deprecation

LLM providers regularly update their model offerings. This means models available in Open Chat Studio may occasionally be deprecated or removed.

- **Deprecation**: When a model you are using is deprecated, you will receive an in-app notification recommending that you switch to a replacement model. Your team receives this notification only once per deprecated model, not on every subsequent release. Your chatbots and pipelines continue to work during this period, but you should update your chatbot configuration at your earliest convenience.
- **Removal**: When a model is fully removed from the platform, Open Chat Studio updates your chatbots and pipelines automatically. If a clear replacement model exists, it switches the chatbots to that model; otherwise, it clears the reference to the removed model. Either way, you'll receive an in-app notification confirming what changed.

!!! note

    No manual action is required when a model is removed — the platform handles the transition for you.

!!! note "The affected chatbots list is a snapshot"

    A deprecation notice lists the chatbots that were using the model at the time it was sent. If you point additional chatbots at the same deprecated model afterwards, they won't be added to that earlier notice.

## See also

- [Configure LLM Service Providers](../../tutorials/configure_llm_providers.md) — set up a provider to use in your chatbots
- [Finding where an LLM provider is used](index.md#finding-where-a-provider-is-used) — in your chatbots
- [Add a Custom LLM Model](../../how-to/add_custom_llm_model.md) — add a model that isn't pre-configured, including naming conventions per provider
- [Large Language Models (LLMs)](../llm.md) — key LLM concepts such as tokens and context window
