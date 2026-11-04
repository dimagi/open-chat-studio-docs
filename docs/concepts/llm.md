---
title: Large Language Model
---

# Large Language Models (LLMs)

!!! note "Definition"
    A Large Language Model (or LLM) is a type of artificial intelligence (or AI) software that is trained on a vast amount of text data.
    Its primary function is to understand, interpret, and generate human language.
    This training allows it to produce text-based responses, answer questions, translate between languages, and perform various other language-related tasks.

    The term "large" in its name refers to the extensive volume of data it has been trained on and the complexity of its design, enabling it to handle complex language tasks.

<small>The definition above was authored by the famous LLM that powers ChatGPT: GPT-4 developed by OpenAI.</small>

When building chatbots, an LLM powers the chatbot's ability to understand and respond to participant inputs, effectively acting as the brain behind the chatbot.

## Prompt

A prompt is the input or instructions given to the LLM to guide its response.
It sets the context for the chatbot.
Prompts can be as simple as a single question or as detailed as a conversation framework or role-play setup.
Use [prompt variables](prompt_variables.md) to insert dynamic values into a prompt.

**Example:** "You are a helpful assistant. Answer questions clearly and concisely."

## Tokens

Tokens are the units of text that the LLM processes.
A token might be a word, part of a word, or even just punctuation.

**Example:** The sentence *"Chatbots are cool."* is broken into 4 tokens:
`Chatbots | are | cool | .`

Tokens are important because they determine the cost and the processing complexity of an LLM's response.

## Max Token Limit

Every AI model has a maximum token limit — also called its **context window**.
Max Token Limit is a fixed property of the model.
It is listed next to each model name on the [team's LLM providers](team/llm_providers.md) page.

The context window is the total number of tokens the model can work with in one turn.
Your prompt, the conversation history, and the model's reply all share the same budget.
When the budget runs out, the request may be truncated or fail.
See [Conversation History](pipelines/history.md) for how nodes limit the history they send.

## Model Parameters: Temperature and Effort

Open Chat Studio exposes two main parameters that change how a model responds: **temperature** and **effort**.
Which one is available depends on the model you choose.

**Temperature** controls how creative or varied the responses are.
A low temperature produces consistent, predictable answers.
A high temperature produces more varied and imaginative ones.

**Effort** controls how much internal reasoning the model does before answering.
It is used by [reasoning models](../how-to/choose_llm_model.md) that work through problems step-by-step.
You set it as a level: `low`, `medium`, `high`, or `max`.

These two parameters serve different purposes: temperature changes how varied the wording is, and effort changes how much reasoning goes into the answer.

## See also

- [Configure an LLM Provider](../tutorials/configure_llm_providers.md) — set up a provider so your chatbot can use its models
- [Choose an LLM Model](../how-to/choose_llm_model.md) — helps you pick the right model for your use case
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — step-by-step instructions for changing these settings
- [Conversation History](pipelines/history.md) — how nodes control the history sent to the model
- [Prompt Variables](prompt_variables.md) — insert dynamic values into prompts
