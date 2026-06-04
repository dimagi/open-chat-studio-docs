---
title: Choose an LLM Model
---

# Choose an LLM Model

Before you configure an [LLM node](../concepts/pipelines/nodes.md#llm-node), you need to choose a model. This guide helps you match your chatbot's purpose to the right type of model.

The key question to answer first is: **what does your chatbot need to do?**

## Two types of models

Open Chat Studio supports the two fundemental model types:

| Type | Best for |
|------|----------|
| **General-purpose** | Optimised for broad tasks - conversation, writing, summarising, Q&A, creative tasks | 
| **Reasoning** | Optimised for structured, multi-step thinking — analysis, coding, multi-step logic, structured problem-solving |

A reasoning model is not universally better — it is slower and costs more tokens. For most conversational chatbots, a general-purpose model is the right starting point.

## Match your use case

| If your chatbot needs to… | Use… |
|---------------------------|------|
| Hold natural, open-ended conversations | General-purpose |
| Answer factual questions from a defined knowledge base | General-purpose |
| Produce varied, creative, or personalised responses | General-purpose |
| Reason through complex or multi-step problems | Reasoning |
| Write, review, or explain code | Reasoning |
| Perform structured analysis or extract structured data | Reasoning |
| Reduce hallucinations on hard analytical tasks | Reasoning with low–medium effort |
| Prioritise speed and low cost | General-purpose, or reasoning with `low` effort |

!!! tip

    If you are unsure, start with a general-purpose model. You can always switch later.

## Provider choice

The same capability is available across multiple providers — for example, reasoning models are offered by OpenAI, Anthropic, and Google Gemini. You do not need to pick a specific provider to get a specific capability. Use whatever provider your team has already configured.

If your team has access to more than one provider, the choice often comes down to cost, latency, or organisational policy rather than capability. See [LLM Service Providers](../concepts/team/llm_providers.md) for a list of supported providers.

## Next step

Once you have chosen a model, configure its parameters:

- [Adjust LLM Node Model Parameters](adjust_llm_node_settings.md) — set Temperature, Effort, and Max Token Limit
