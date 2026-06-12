---
title: Adjust LLM Node Model Parameters
---

# Adjust LLM Node Model Parameters

This guide steps you through adjusting the LLM model parameters on an [LLM node](../concepts/pipelines/nodes.md#llm-node) in your chatbot [pipeline](../concepts/pipelines/index.md). It assumes you already have a chatbot or pipeline open for editing.

!!! note "Before you start"
    Choose your LLM model first — see [Choose an LLM Model](choose_llm_model.md). The parameters available in the settings panel depend on the model you select.

## Step 1 — Open the node settings

1. Open your pipeline or chatbot for editing.
2. Click the LLM node you want to configure.
3. Select "Advanced" to expand the settings panel.

## Step 2 — Select a model

1. In the node settings, locate the **LLM Model** dropdown.
2. Select the model you want to use.

## Step 3 — Adjust temperature or effort

Once you select an LLM model, Open Chat Studio shows only the parameter settings that apply to it. This can be one or more parameters.

### If the model shows a Temperature setting

Temperature controls how creative or varied the responses are.

- Slide toward **0** for more consistent, predictable answers (good for factual Q&A or classification).
- Slide toward **1** for more varied, creative answers (good for creative writing or friendly conversation).
- The default value of **0.7** is a reasonable starting point for most chatbots.

### If the model shows an Effort setting

Effort (or Reasoning Effort) controls how much internal reasoning the model does before answering. It is available on [reasoning models](choose_llm_model.md#two-model-types).

Select a level from the dropdown:

| Level    | When to use it                                                       |
|----------|----------------------------------------------------------------------|
| `low`    | Routine questions where speed matters more than depth                |
| `medium` | Most tasks — a good default                                          |
| `high`   | Complex analysis, multi-step problems, or tasks needing careful logic|
| `max`    | The hardest problems where accuracy is more important than speed     |

!!! tip
    Higher effort levels cost more tokens (see below) and take longer to respond. Start with `medium` and only raise it if answers are not thorough enough.

## Step 4 — Adjust max output tokens (if shown)

The **Max output tokens** field caps how long the model's response can be. Leave it at the default unless you have a specific reason to limit response length.

!!! note "Distinct from the max token limit"
    It is a different limit from the model's [context window](../concepts/llm.md#max-token-limit) (i.e., the max token limit), which limits combined input + output. Both limits apply simultaneously.

!!! warning "Reasoning models"
    If you are using a reasoning model (one that shows an Effort setting), set this value higher than you would for a standard model. A value that is too low can result in no visible output at all. See [Max output tokens](#max-output-tokens) in the parameter reference below.

## Step 5 — Configure adaptive thinking (if shown)

See [Adaptive thinking](#adaptive-thinking) in the parameter reference below for details.

## Step 6 — Save your changes

1. Click outside the edit settings dialog to save.
2. Test your chatbot to confirm the output looks as expected.

## Troubleshooting

**The model I want does not appear in the list.**
Your team may not have that provider configured. Ask your team administrator or see [LLM Providers](../concepts/team/llm_providers.md).

**Responses are being cut off.**
The max output token limit may be too low. Raise it in the node settings. If you are using a [reasoning model](../how-to/choose_llm_model.md#two-model-types), this is especially common — see [Max output tokens](#max-output-tokens) in the parameter reference below.

## Related pages

- [Choose an LLM Model](choose_llm_model.md) — guidance on picking the right model for your use case
- [Large Language Models](../concepts/llm.md) — conceptual overview of temperature and effort
- [LLM Providers](../concepts/team/llm_providers.md) — configuring provider credentials

---

## Parameter reference

This section covers the precise behaviour of each parameter and LLM provider-level differences. It is intended for advanced users.

### Temperature

| Value | Behaviour |
|-------|-----------|
| `0.0` | Fully deterministic. |
| `0.1–0.4` | Low randomness. Consistent, predictable outputs. |
| `0.7` | Default. Balanced between coherence and variety. |
| `0.8–1.0` | High randomness. More varied and creative outputs. |

**Provider notes:** Temperature is supported by most ["general-purpose"](choose_llm_model.md#two-model-types) chat models (GPT-4o, Claude Sonnet/Opus without thinking, Gemini, Groq, Perplexity, DeepSeek). It is usually not supported on [reasoning models](choose_llm_model.md#two-model-types), but there are a few exceptions like Claude Opus 4.6.

### Effort (reasoning effort)

| Level    | What it does                                                                                        |
|----------|-----------------------------------------------------------------------------------------------------|
| `low`    | Fastest and cheapest. Short reasoning — good for routine questions.                                 |
| `medium` | Balanced default for most tasks.                                                                    |
| `high`   | More thorough reasoning — useful for complex analysis or multi-step problems.                       |
| `max`    | Maximum reasoning budget. Slowest and most expensive.                                               |

Set the effort level to guide how much the model reasons; set Max output tokens to enforce a hard token cap.

**Provider notes:** Different providers expose this slightly differently. OpenAI exposes this as `reasoning_effort`. Anthropic's Claude models use [adaptive thinking](#adaptive-thinking). Gemini's thinking-capable models expose a thinking budget. OCS maps all of these to the same four effort levels.

### Max output tokens

!!! note "Distinct from the max token limit"
    This is a different limit from the model's [max token limit](../concepts/llm.md#max-token-limit). Both limits apply simultaneously.

This is a hard cap on generated **output** tokens only — it does not affect input consumption. If reached, output truncates mid-sentence and OCS may not display an explicit error.

OCS provides a default based on the LLM provider default (this varies by model and may be conservative).

!!! warning "Reasoning models — shared budget"
    On reasoning models, thinking tokens and visible-reply tokens draw from the same max output tokens budget. If the thinking phase exhausts the budget, the model produces no visible output — silently.

    For `high` or `max` effort level, a safe starting point is 2–4× your expected reply length.

### Adaptive thinking

When enabled, the model dynamically allocates its reasoning budget per message rather than spending a fixed amount every time — guided by the [effort level](#effort-reasoning-effort) you set. Easy turns finish quickly; complex ones get more thinking tokens.

Only available on supported Claude models.
