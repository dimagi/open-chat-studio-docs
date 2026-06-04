---
title: Model Configuration Reference
---

# Model Configuration Reference

This page is a technical reference for the model configuration parameters available on LLM nodes in Open Chat Studio. It is aimed at advanced users and developers who need to understand the precise behaviour of each parameter, provider-level differences, and constraints.

For a conceptual introduction, see [Large Language Models](../concepts/llm.md). For step-by-step instructions on changing these settings in the UI, see [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md).

## Supported parameters

Different models expose different parameters. Open Chat Studio shows only the parameters a selected model actually supports — unsupported fields are hidden to prevent silent misconfiguration.

### Temperature

Temperature is a floating-point value that controls the probability distribution over the model's next-token predictions.

| Value | Behaviour |
|-------|-----------|
| `0.0` | Fully deterministic (greedy decoding). The highest-probability token is always chosen. |
| `0.1–0.4` | Low randomness. Consistent, predictable outputs. Good for classifiers and factual Q&A. |
| `0.7` | Default. Balanced between coherence and variety. |
| `0.8–1.0` | High randomness. More varied and creative outputs. May produce less coherent answers on factual tasks. |

**Applicable models:** General-purpose chat models including GPT-4o, Claude Sonnet/Opus without thinking enabled, Gemini, Groq, Perplexity, and DeepSeek.

**Not applicable:** Reasoning models that use effort (see below). On these models, the provider controls internal sampling; Open Chat Studio hides the temperature field.

### Effort (reasoning effort)

Effort is a discrete level that controls the token budget allocated to a reasoning model's internal chain-of-thought before it produces a visible response.

| Level    | What it does                                                                                          |
|----------|-------------------------------------------------------------------------------------------------------|
| `low`    | Fastest and cheapest. Short reasoning before answering — good for routine questions.                  |
| `medium` | A balanced default for most tasks.                                                                    |
| `high`   | More thorough reasoning — useful for complex analysis, multi-step problems, or careful code review.   |
| `max`    | Maximum reasoning budget. Slowest and most expensive, but produces the most considered answers.       |

Higher effort levels generally produce better answers on hard problems but cost more (both in tokens and latency). For simple conversational tasks, low or medium is almost always enough — turning the knob up doesn't make a friendly chitchat bot friendlier, just
slower.

#### When effort is set, temperature is ignored

On models that use effort, OpenAI and Anthropic do not allow temperature or `top_p` to be
configured at the same time — the reasoning loop manages randomness internally. Open Chat
Studio reflects this by hiding the temperature field on these models so you don't have to
think about it.

Models that use effort include OpenAI's GPT-5 / GPT-5.2 series and Anthropic's Claude Opus
4.6 and Sonnet 4.6 with thinking enabled.

### Reasoning and adaptive thinking
"Reasoning" is the broader name for the same idea as effort: letting the model spend extra
tokens *thinking* before it produces the answer the user sees. Different providers expose
this slightly differently:

- **OpenAI** calls it `reasoning_effort` and uses the level system above.
- **Anthropic** offers **adaptive thinking** on its Claude 4.6 models. Adaptive thinking
  lets the model decide how much to think on a per-message basis, guided by the effort
  level you set. Easy turns finish quickly; hard turns get more thinking budget.
- **Google Gemini** exposes a thinking budget on some Gemini 2.5+ models.

You normally don't need to think about these provider-level differences — Open Chat Studio
abstracts them into the same effort levels (low/medium/high/max) wherever the model supports
them.

## Adding custom models

If a model is available from a supported provider but is not listed in Open Chat Studio, you can add it as a [custom model](../concepts/team/llm_providers.md#adding-custom-llm-models). 

## Related pages

- [Large Language Models](../concepts/llm.md) — conceptual overview
- [Max Token Limit](../concepts/max_tokens.md) — token budget concepts
- [Choose an LLM Model](../how-to/choose_llm_model.md) — guidance for non-technical users
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — UI step-by-step guide
- [LLM Providers](../concepts/team/llm_providers.md) — configuring provider credentials
