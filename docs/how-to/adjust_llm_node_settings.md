---
title: Adjust LLM Node Model Settings
---

# Adjust LLM Node Model Settings

This guide helps you choose the right model settings for the [LLM node](../concepts/pipelines/nodes.md#llm-node) in your chatbot [pipeline](../concepts/pipelines/index.md). For an explanation of what each parameter does, see [Large Language Models](../concepts/llm.md).

## Prerequisites

- You have added a LLM node to your chatbot pipeline.
- You have selected to edit the LLM Node advanced settings.
- You have selected the **LLM model** this node will use.

!!! note
    Different models expose different knobs for shaping their behaviour. The most common are temperature, effort, and reasoning / adaptive thinking. 
    
    Not every model supports every parameter — when you select a model in Open Chat Studio, the configuration panel only shows the parameters that model actually supports, so you won't accidentally set one that has no effect.

## LLM model parameters

### Temperature

See [Temperature](../concepts/llm.md#temperature-parameter) for a conceptual overview.

- **Range:** 0.0–1.0 (exact range may vary by provider)
- **Default:** 0.7 (to provide responses that are both varied and interesting, while still being coherent)

**Example**:

- Low temperature: What's a dog? → A dog is a domesticated animal.
- High temperature: What's a dog? → A dog is a loyal companion, a furry friend who fills your life with wagging tails and boundless joy.

Temperature is supported by most general-purpose chat models including GPT-4o, Claude Sonnet/Opus without thinking enabled, Gemini, Groq, Perplexity, and Deepseek. 

It is **not** available on reasoning models that use Effort — see below.

### Effort

See [Effort](../concepts/llm.md#effort-parameter) for a conceptual overview. Effort applies only to reasoning models.

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

[Temperature](../concepts/llm.md#temperature-parameter) and [Effort](../concepts/llm.md#effort-parameter) are mutually exclusive — only one will be available depending on your selected model.

| If you want to…                                                  | Use…        |
|------------------------------------------------------------------|-------------|
| Make responses more or less creative, varied or unpredictable    | Temperature |
| Make responses more or less rigorous or well-reasoned            | Effort      |
| Get natural-sounding phrasing in a conversational bot            | Temperature |
| Solve a hard problem (analysis, coding, multi-step reasoning)    | Effort      |
| Reduce hallucinations on a factual Q&A bot                       | Lower temperature, or switch to a reasoning model and raise effort |
| Make an extractor or classifier more deterministic               | Temperature → 0, or a reasoning model with low effort |
| Speed things up or reduce cost on an over-engineered setup       | Lower effort (if set), or use a non-reasoning model |

**Quick decision guide:**

1. Is this a conversational, creative, or stylistic task? Use a general-purpose model and tune **Temperature**.
2. Is this a logic, analysis, math, or coding task? Use a reasoning model and tune **Effort**.
3. Not sure? Start with the default model and default settings. Adjust only if outputs are consistently too random, too bland, too shallow, or too slow.

## Max Token Limit

See [Max Token Limit](../concepts/llm.md#max-token-limit) for an explanation of what this setting does.

!!! warning "Reasoning models and token budgets"
    On [reasoning models](../tech-hub/llm_model_parameters.md#reasoning-and-adaptive-thinking), internal thinking tokens count toward the max output token budget. If you set Effort to `high` or `max` and the Max Token Limit is too low, the model may run out of space before producing a visible response. 
    
    If you see truncated or empty responses from a high-effort run, raise the Max Token Limit.

## Other LLM Node Settings

- Node Name
- [Prompt](../concepts/llm.md#prompt)
- [LLM History Mode](../concepts/pipelines/history.md)
- [Max History Length](../concepts/pipelines/history.md#max-history-length)
- [Message Tag](../concepts/tags.md)
- [Tools](../concepts/tools/index.md)