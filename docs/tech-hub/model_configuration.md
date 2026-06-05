---
title: Model Configuration Reference
---

# Model Configuration Reference

This page is a technical reference for the LLM model parameters available on [LLM nodes](../concepts/pipelines/nodes.md#llm-node) in Open Chat Studio. It is aimed at advanced users and developers who need to understand the precise behaviour of each parameter, LLM provider-level differences, and constraints.

For a conceptual introduction, see [LLM Model Parameters](../concepts/llm.md#model-parameters-temperature-and-effort). For step-by-step instructions on changing these settings in the UI, see [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md).

## Supported parameters

Different models expose different parameters. OCS shows only the parameters a selected model actually supports — unsupported settings are not shown in the UI so you won't accidentally set one that has no effect.

### Temperature

| Value | Behaviour |
|-------|-----------|
| `0.0` | Fully deterministic. |
| `0.1–0.4` | Low randomness. Consistent, predictable outputs. |
| `0.7` | Default. Balanced between coherence and variety. |
| `0.8–1.0` | High randomness. More varied and creative outputs. |

**Provider notes:** Temperature is supported by most ["general-purpose"](../how-to/choose_llm_model.md#two-model-types) chat models (GPT-4o, Claude Sonnet/Opus without thinking, Gemini, Groq, Perplexity, DeepSeek). It is usually not supported on [reasoning models](../how-to/choose_llm_model.md#two-model-types), but there are a few exceptions like Claude Opus 4.6.

### Effort (reasoning effort)

| Level    | What it does                                                                                        |
|----------|-----------------------------------------------------------------------------------------------------|
| `low`    | Fastest and cheapest. Short reasoning — good for routine questions.                                 |
| `medium` | Balanced default for most tasks.                                                                    |
| `high`   | More thorough reasoning — useful for complex analysis or multi-step problems.                       |
| `max`    | Maximum reasoning budget. Slowest and most expensive.                                               |

Set effort level to guide how much the model reasons; set Max output tokens to enforce a hard token cap.

**Provider notes:** Different providers expose this slightly differently. OpenAI exposes this as `reasoning_effort`. Anthropic's Claude models use [adaptive thinking](#adaptive-thinking). Gemini's thinking-capable models expose a thinking budget. 

OCS maps all of these to the same four effort levels.

### Max output tokens

!!! note "Distinct from the max token limit"
    It is a different limit from the model's [max token limit](../concepts/llm.md#max-token-limit). Both limits apply simultaneously.

This is a hard cap on generated **output** tokens only — it does not affect input consumption. If reached, output truncates mid-sentence and OCS may not display an explicit error. 

OCS provides a default based on the LLM provider default (this varies by model and may be conservative).

!!! warning "Reasoning models — shared budget"
    On reasoning models, thinking tokens and visible-reply tokens draw from the same max output tokens budget. If the thinking phase exhausts the budget, the model produces no visible output — silently.
    
    For `high` or `max` effort level, a safe starting point is 2–4× your expected reply length.

### Adaptive thinking

When enabled, the model dynamically allocates its reasoning budget per message rather than spending a fixed amount every time — guided by the [effort level](#effort-reasoning-effort) you set. Easy turns finish quickly; complex ones get more thinking tokens.

Only available on supported Claude models.

## Adding custom models

If a model is available from a supported provider but is not listed in Open Chat Studio, you can add it as a [custom model](../concepts/team/llm_providers.md#adding-custom-llm-models). 

## Related pages

- [Large Language Models](../concepts/llm.md) — conceptual overview
- [Choose an LLM Model](../how-to/choose_llm_model.md) — guidance for non-technical users
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — UI step-by-step guide
- [LLM Providers](../concepts/team/llm_providers.md) — configuring provider credentials
