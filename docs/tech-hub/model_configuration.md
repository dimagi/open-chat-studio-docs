---
title: Model Configuration Reference
---

# Model Configuration Reference

This page is a technical reference for model configuration parameters in Open Chat Studio. It covers the full parameter details, provider-level behaviour differences, and the model lifecycle and deprecation process.

For a conceptual overview, see [Large Language Models](../concepts/llm.md). For step-by-step configuration instructions, see [Configure Model Parameters](../how-to/configure_model_parameters.md).

## Parameter Reference

Different models expose different parameters. When you select a model in Open Chat Studio, the configuration panel shows only the parameters that model supports — parameters with no effect on the selected model are hidden automatically.

### Temperature

Temperature controls the probability distribution over the model's next-token predictions. A value closer to 0 makes the distribution sharper (more deterministic); a value closer to 1 flattens it (more varied output).

- **Range:** 0.0–1.0 (exact range may vary by provider)
- **Default:** 0.7

| Value | Behaviour | Example output for "What's a dog?" |
|-------|-----------|-------------------------------------|
| Low (e.g. 0.1) | Deterministic, predictable | A dog is a domesticated animal. |
| High (e.g. 0.9) | Creative, varied | A dog is a loyal companion, a furry friend who fills your life with wagging tails and boundless joy. |

Temperature is supported by most general-purpose chat models including GPT-4o, Claude Sonnet/Opus without thinking enabled, Gemini, Groq, Perplexity, and Deepseek. It is not available on reasoning models that use Effort — see below.

### Effort

Effort (also called **reasoning effort**) controls the token budget allocated to the model's internal chain-of-thought before it produces the final visible response. It applies only to reasoning models.

| Level    | Behaviour                                                                                         |
|----------|---------------------------------------------------------------------------------------------------|
| `low`    | Minimal reasoning. Fastest and cheapest. Good for routine questions.                              |
| `medium` | Balanced default for most tasks.                                                                  |
| `high`   | More thorough reasoning — useful for complex analysis, multi-step problems, or code review.       |
| `max`    | Maximum reasoning budget. Slowest and most expensive; produces the most considered answers.       |

Higher effort levels generally improve answer quality on hard problems, at the cost of latency and token spend. For simple conversational tasks, `low` or `medium` is almost always sufficient.

#### When Effort is set, Temperature is ignored

OpenAI and Anthropic do not permit `temperature` or `top_p` to be set alongside reasoning effort — the reasoning loop manages output randomness internally. Open Chat Studio hides the Temperature field on these models automatically.

Models that use effort include OpenAI's GPT-5 / GPT-5.2 series and Anthropic's Claude Opus 4.6 and Sonnet 4.6 with thinking enabled.

### Reasoning and Adaptive Thinking

"Reasoning" is the broader concept underlying Effort: the model spends extra tokens thinking before it produces the answer the user sees. Each provider exposes this differently:

- **OpenAI** calls it `reasoning_effort` and uses the four-level system (`low`, `medium`, `high`, `max`).
- **Anthropic** offers **adaptive thinking** on Claude 4.6 models. Adaptive thinking lets the model decide how much to think on a per-message basis, guided by the effort level you set. Easier turns use less thinking budget; harder turns receive more.
- **Google Gemini** exposes a numeric thinking budget on Gemini 2.5+ models.

Open Chat Studio maps all of these to the same `low/medium/high/max` effort levels wherever the model supports them, so you do not need to manage provider-level API differences directly.

### Max Token Limit

The max token limit is the maximum number of tokens the model can process in a single interaction — input (prompt) plus output (response) combined.

For reasoning models, the model's internal thinking tokens count against the max output token budget. Setting Effort to `high` or `max` while keeping the Max Token Limit low can cause the model to exhaust its budget before generating any visible output. If you observe truncated or empty responses from a high-effort configuration, increase the Max Token Limit.

## Model Lifecycle and Deprecation

AI providers regularly update their model offerings. Models available in Open Chat Studio may be deprecated or removed over time.

### Deprecation

When a model you are using is deprecated, Open Chat Studio sends an in-app notification recommending that you switch to a replacement model. Your chatbots and pipelines continue to operate during the deprecation period, but you should update your configuration at your earliest convenience.

### Removal

When a model is fully removed from the platform:

- Open Chat Studio automatically removes all references to the model in your chatbots and pipelines.
- Where a clear replacement exists, Open Chat Studio migrates usages of the old model to the recommended replacement.
- You receive an in-app notification confirming the removal or migration.

No manual action is required when a model is removed — the platform handles the transition automatically.

## See Also

- [Large Language Models](../concepts/llm.md) — conceptual overview of LLMs, prompts, tokens, and parameters
- [Configure Model Parameters](../how-to/configure_model_parameters.md) — step-by-step instructions for tuning parameters in the UI
- [LLM Service Providers](../concepts/team/llm_providers.md) — setting up and managing provider credentials for your team
- [Configure LLM Providers](../tutorials/configure_providers.md) — adding providers and custom models to Open Chat Studio
