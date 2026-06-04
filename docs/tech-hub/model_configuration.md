---
title: Model Configuration Reference
---

# Model Configuration Reference

This page is a technical reference for the LLM model parameters available on [LLM nodes](../concepts/pipelines/nodes.md#llm-node) in Open Chat Studio. It is aimed at advanced users and developers who need to understand the precise behaviour of each parameter, LLM provider-level differences, and constraints.

For a conceptual introduction, see [Large Language Models](../concepts/llm.md). For step-by-step instructions on changing these settings in the UI, see [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md).

## Supported parameters

Different models expose different parameters. OCS shows only the parameters a selected model actually supports — unsupported fields are hidden to prevent silent misconfiguration.

### Temperature

| Value | Behaviour |
|-------|-----------|
| `0.0` | Fully deterministic (greedy decoding). |
| `0.1–0.4` | Low randomness. Consistent, predictable outputs. |
| `0.7` | Default. Balanced between coherence and variety. |
| `0.8–1.0` | High randomness. More varied and creative outputs. |

Applies to general-purpose models (GPT-4o, Claude Sonnet/Opus without thinking, Gemini, Groq, Perplexity, DeepSeek). Hidden on reasoning models — see [Effort](#effort-reasoning-effort) below.

### Effort (reasoning effort)

Controls the token budget for a reasoning model's internal chain-of-thought. Temperature is mutually exclusive with effort — OCS hides temperature on models that use effort (OpenAI GPT-5 series, Anthropic Claude Opus/Sonnet 4.6 with thinking enabled).

| Level    | What it does                                                                                        |
|----------|-----------------------------------------------------------------------------------------------------|
| `low`    | Fastest and cheapest. Short reasoning — good for routine questions.                                 |
| `medium` | Balanced default for most tasks.                                                                    |
| `high`   | More thorough reasoning — useful for complex analysis or multi-step problems.                       |
| `max`    | Maximum reasoning budget. Slowest and most expensive.                                               |

**Provider notes:** OpenAI exposes this as `reasoning_effort`. Anthropic's Claude 4.6 models use adaptive thinking, where the model self-allocates budget per turn within the effort level you set. Gemini 2.5+ exposes a thinking budget. OCS maps all of these to the same four levels.

### Max output tokens

Hard cap on generated output tokens only — does not affect input consumption. Truncates mid-sentence if reached and there can be no explicit error explaining this. OCS provides a default based on the LLM provider default (this varies by model and may be conservative).

Distinct from the model's [context window](../concepts/max_tokens.md), which limits combined input + output. Both limits apply simultaneously.

!!! warning "Reasoning models — shared budget"
    On reasoning models, thinking tokens and visible-reply tokens draw from the same max output tokens budget. If the thinking phase exhausts the budget, the model produces no visible output — silently.
    
    For `high` or `max` effort, a safe starting point is 2–4× your expected reply length.

## Adding custom models

If a model is available from a supported provider but is not listed in Open Chat Studio, you can add it as a [custom model](../concepts/team/llm_providers.md#adding-custom-llm-models). 

## Related pages

- [Large Language Models](../concepts/llm.md) — conceptual overview
- [Max Token Limit](../concepts/max_tokens.md) — understanding the model's context window
- [Choose an LLM Model](../how-to/choose_llm_model.md) — guidance for non-technical users
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — UI step-by-step guide
- [LLM Providers](../concepts/team/llm_providers.md) — configuring provider credentials
