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

## Prompt

A prompt is the input or instructions given to the LLM to guide its response. It sets the context for the chatbot. Prompts can be as simple as a user question or as detailed as a conversation framework or role-play setup.

**Example:**

```
You are a helpful assistant. Answer questions clearly and concisely.
```

## Tokens

Tokens are the building blocks of text that the LLM processes. A token might be a word, part of a word, or even just punctuation.

**Example:** The sentence *"Chatbots are cool."* is broken into 4 tokens:
`Chatbots | are | cool | .`

Tokens are important because they determine the cost and the processing complexity of an LLM's response. For more on how token limits affect your chatbot, see [Max Token Limit](max_tokens.md).

## Model Parameters: Temperature and Effort

Open Chat Studio exposes two main knobs for shaping how a model responds: **temperature** and **effort**. Which one is available depends on the model you choose.

**Temperature** controls how creative or varied the responses are. A low temperature produces consistent, predictable answers. A high temperature produces more varied and imaginative ones.

**Effort** controls how much internal reasoning the model does before answering. It is used by reasoning models that work through problems step-by-step. You set it as a level: `low`, `medium`, `high`, or `max`.

These two parameters serve different purposes: temperature shapes *style*, effort shapes *substance*.

For guidance on which model type to choose and when to use each parameter, see:

- [Choose an LLM Model](../how-to/choose_llm_model.md) — helps you pick the right model for your use case
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — step-by-step instructions for changing these settings
- [Model Configuration Reference](../tech-hub/model_configuration.md) — full parameter details for advanced users
