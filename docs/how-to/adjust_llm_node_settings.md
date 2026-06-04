---
title: Adjust LLM Node Model Settings
---

# Adjust LLM Node Model Settings

This guide steps you through adjusting the LLM model parameters on an [LLM node](../concepts/pipelines/nodes.md#llm-node) in your chatbot [pipeline](../concepts/pipelines/index.md).
!!! note "Before you start"
    Choose your LLM model first — see [Choose an LLM Model](choose_llm_model.md). The parameters available in the settings panel depend on the model you select.

## LLM model parameters

### Temperature

See [Temperature](../concepts/llm.md#temperature) for a conceptual overview.

- **Range:** 0.0–1.0 (exact range may vary by provider)
- **Default:** 0.7 (to provide responses that are both varied and interesting, while still being coherent)

**Example**:

- Low temperature: What's a dog? → A dog is a domesticated animal.
- High temperature: What's a dog? → A dog is a loyal companion, a furry friend who fills your life with wagging tails and boundless joy.

Temperature is supported by most general-purpose chat models including GPT-4o, Claude Sonnet/Opus without thinking enabled, Gemini, Groq, Perplexity, and Deepseek. 

It is **not** available on reasoning models that use Effort — see below.

### Effort

See [Effort](../concepts/llm.md#effort) for a conceptual overview. Effort applies only to reasoning models.

| Level    | Behaviour                                                                                         |
|----------|---------------------------------------------------------------------------------------------------|
| `low`    | Minimal reasoning. Fastest and cheapest. Good for routine questions.                              |
| `medium` | Balanced default for most tasks.                                                                  |
| `high`   | More thorough reasoning — useful for complex analysis, multi-step problems, or code review.       |
| `max`    | Maximum reasoning budget. Slowest and most expensive; produces the most considered answers.       |

Higher effort levels generally produce better answers on hard problems but cost more (both in tokens and latency). For simple conversational tasks, low or medium is almost always enough — turning the knob up doesn't make a friendly chitchat bot friendlier, just slower.

Models that use effort include OpenAI's GPT-5 / GPT-5.2 series and Anthropic's Claude Opus 4.6 and Sonnet 4.6 with [thinking enabled](../tech-hub/llm_model_parameters.md#reasoning-and-adaptive-thinking).


## Choosing Between Temperature and Effort

These two knobs do very different things, so it's worth being clear about when each one helps

[Temperature](../concepts/llm.md#temperature) and [Effort](../concepts/llm.md#effort) are mutually exclusive — only one will be available depending on your selected model.

| If you want to…                                                  | Use…        |
|------------------------------------------------------------------|-------------|
| Make responses more or less creative, varied or unpredictable    | Temperature |
| Make responses more or less rigorous or well-reasoned            | Effort      |
| Get natural-sounding phrasing in a conversational bot            | Temperature |
| Solve a hard problem (analysis, coding, multi-step reasoning)    | Effort      |
| Reduce hallucinations on a factual Q&A bot                       | Lower temperature, or switch to a reasoning model and raise effort |
| Make an extractor or classifier more deterministic               | Temperature → 0, or a reasoning model with low effort |
| Speed things up or reduce cost on an over-engineered setup       | Lower effort (if set), or use a non-reasoning model |



## Other LLM Node Settings

- Node Name
- [Prompt](../concepts/llm.md#prompt)
- [LLM History Mode](../concepts/pipelines/history.md)
- [Max History Length](../concepts/pipelines/history.md#max-history-length)
- [Max Token Limit](../concepts/max_token_limit.md)
- [Message Tag](../concepts/tags.md)
- [Tools](../concepts/tools/index.md)