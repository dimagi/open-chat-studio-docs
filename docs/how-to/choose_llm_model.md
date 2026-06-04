---
title: Choose an LLM Model
---

# Choose an LLM Model

Open Chat Studio supports a range of AI models from providers such as OpenAI, Anthropic, Google, and others. Each model has different strengths. This guide helps you pick the right one for your chatbot without needing a deep technical background.

## Two model types

All models in Open Chat Studio fall into one of two categories.

**General-purpose models** are designed for everyday conversation. They respond quickly, handle a wide range of topics, and let you tune how creative or consistent their answers are using a setting called *temperature*. Examples include GPT-4o, Claude Sonnet (without thinking), and Gemini.

**Reasoning models** are designed for tasks that require careful, step-by-step thinking — such as analysis, coding assistance, or complex decision-making. Before producing a final answer, these models work through the problem internally. You control how much thinking they do using a setting called *effort*. Examples include OpenAI's GPT-5 series and Anthropic's Claude Opus with thinking enabled.

!!! note
    You do not need to configure both settings. Each model type uses one or the other — Open Chat Studio only shows the settings that apply to the model you have selected.

## Match your use case

Use this table as a starting point when choosing a model type.

| Your chatbot does…                                       | Model type to consider    |
|----------------------------------------------------------|---------------------------|
| Answer general questions and have conversations          | General-purpose           |
| Provide friendly support or onboarding                   | General-purpose           |
| Classify or route incoming messages                      | General-purpose           |
| Summarise documents or rewrite content                   | General-purpose           |
| Analyse data, reason through a problem, or write code    | Reasoning                 |
| Handle multi-step workflows requiring careful logic      | Reasoning                 |
| Produce highly accurate factual answers                  | Reasoning (with effort raised) |

If you are unsure, start with a general-purpose model and the default settings. You can always switch later — your chatbot configuration is easy to update.

## Provider choice

The model you choose determines which AI provider is used. Open Chat Studio supports the following providers:

- [OpenAI](https://platform.openai.com/docs/models)
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)
- [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models)
- [Google Gemini](https://ai.google.dev/gemini-api/docs/models)
- [Groq](https://console.groq.com/docs/models)
- [Perplexity](https://docs.perplexity.ai/guides/model-cards)
- [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)

Your team must have credentials configured for a provider before you can use its models. If the model you want is not listed, check with your team administrator or see the guide for [configuring LLM providers](../tutorials/configure_providers.md).

Different providers may offer the same underlying model type but with different pricing, speed, and availability. If your preferred model is unavailable or too slow, try the equivalent model from another provider.

## Next steps

- [Adjust LLM Node Model Parameters](adjust_llm_node_model_parameters.md) — once you have chosen a model, learn how to fine-tune its settings
- [LLM Providers](../concepts/team/llm_providers.md) — understand how providers are configured in your team
- [Large Language Models](../concepts/llm.md) — a conceptual overview of how LLMs work
