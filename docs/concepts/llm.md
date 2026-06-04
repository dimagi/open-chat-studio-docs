---
title: Large Language Model
---

# Large Language Models (LLMs)

!!! note "Definition"
    A Large Language Model (or LLM) is a type of artificial intelligence software that is trained on a vast amount of text data. Its
    primary function is to understand, interpret, and generate human language. This training allows it to produce text-based
    responses, answer questions, translate between languages, and perform various other language-related tasks.

    The term "large" in its name refers to the extensive volume of data it has been trained on and the complexity of its design, enabling it to handle complex language tasks.

<small>The definition above was authored by the famous LLM that powers ChatGPT: GPT-4 developed by OpenAI.</small>

When building chatbots, an LLM powers the chatbot's ability to understand and respond to user inputs, effectively acting as the brain behind the chatbot.

## Which LLMs are supported by Open Chat Studio?

Open Chat Studio is developed to support a range of LLMs. The platform is designed to be flexible and can work with any
LLM that has an API. The platform currently supports all the models provided by the following APIs:

* [OpenAI](https://platform.openai.com/docs/models)
* [Azure OpenAi](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure%2Cglobal-standard%2Cstandard-chat-completions)
* [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models_)
* [Groq](https://console.groq.com/docs/models)
* [Perplexity](https://docs.perplexity.ai/guides/model-cards)
* [Deepseek](https://api-docs.deepseek.com/quick_start/pricing)

## Key Concepts of LLMs

### Prompt

A prompt is the input or instructions given to the LLM to guide its response. It sets the context for the chatbot. Prompts can be as simple as a user question or as detailed as a conversation framework or role-play setup.

**Example:** `You are a helpful assistant. Answer questions clearly and concisely.`

### Tokens

Tokens are the building blocks of text that the LLM processes. A token might be a word, a part of a word, or even just punctuation.

**Example:** The sentence *"Chatbots are cool."* is broken into 4 tokens: `Chatbots | are | cool | .`

Tokens are important because they determine the cost and the processing complexity of an LLM's response.

### Max Token Limit

See [Max Token Limit](max_token_limit.md) for a full explanation of how the context window is shared between input and output tokens.

### LLM Model Parameters
#### Temperature

Temperature controls the creativity or randomness of a model's responses.

- A **low temperature** produces more predictable, consistent answers — useful for factual or structured tasks.
- A **high temperature** produces more varied, creative answers — useful for conversational or generative tasks.

A simple rule of thumb: **temperature is for style**.

#### Effort

Effort (sometimes called **reasoning effort**) controls how much internal reasoning a model applies before answering. It is used by reasoning models — models designed to think through problems step-by-step before producing a response.

- A **lower effort** level is faster and more economical — suitable for straightforward tasks.
- A **higher effort** level produces more considered answers — suitable for complex analysis or multi-step problems.

A simple rule of thumb: **effort is for substance**.

## Going Further

!!! tip "Using an LLM in a chatbot"
    First do the tutorial on [creating your first chatbot](../tutorials/first_chatbot.md) and then see more about using the [LLM Node](../concepts/pipelines/nodes.md#llm-node) in a chatbot.

!!! tip "Choose an LLM model"
    For guidance on matching your chatbot's purpose to the right model type, see [Choose an LLM Model](../how-to/choose_llm_model.md).

!!! tip "Adjust LLM behavior"
    For step-by-step guidance on tuning **temperature, effort, and token limits** for a LLM, see the [Adjust LLM Model Parameters](../how-to/adjust_llm_node_settings.md) how-to guide.

