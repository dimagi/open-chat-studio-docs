---
title: Adjust LLM Node Settings
---

# Adjust LLM Node Settings

This guide explains how to tune the key [LLM node](../concepts/pipelines/nodes.md#llm-node) settings — **Temperature**, **Effort**, and **Max Token Limit** — when configuring a chatbot [pipeline](../concepts/pipelines/index.md) in Open Chat Studio.

## Prerequisites

- You have added a LLM node to your chatbot pipeline.
- You have selected to edit the LLM Node advanced settings.
- You have selected the **LLM model** this node will use.

## LLM Model Parameters

Note that not all parameter settings are available for every model. Open Chat Studio shows only the parameters your selected model supports.

### Temperature

Temperature controls how creative or varied the model's responses are.

- Use a **low temperature** (closer to 0) for factual, consistent, or structured outputs.
- Use a **high temperature** (closer to 1) for creative, conversational, or generative outputs.
- The default of 0.7 balances coherence with natural variation and is a good starting point for most chatbots.

Temperature is available on general-purpose chat models. It is not available on reasoning models that use Effort instead.

**To adjust temperature:**

1. Open your chatbot or LLM node settings.
2. Locate the **Temperature** slider or input field.
3. Drag or type a value between 0 and 1.
4. Save your changes and test the output.

### Effort

Effort controls how much internal reasoning the model applies before producing a response. It is only available on reasoning models.

Use a **higher effort** level when accuracy and thoroughness matter more than speed — for example, for analysis, coding tasks, or complex multi-step questions. Use a **lower effort** level for simple or conversational tasks where speed and cost matter more.

| Level    | Best for                                                             |
|----------|----------------------------------------------------------------------|
| `low`    | Routine questions, simple lookups, conversational exchanges          |
| `medium` | General-purpose tasks — a good default                               |
| `high`   | Complex analysis, multi-step reasoning, careful code review          |
| `max`    | The most demanding tasks where quality outweighs cost and latency    |

**To adjust effort:**

1. Open your chatbot or LLM node settings.
2. If the **Effort** field appears (Temperature will be hidden), select a level from the dropdown.
3. Save your changes and test the output.

!!! note
    When Effort is set, Temperature is not available on the same model. Open Chat Studio hides the Temperature field automatically on reasoning models.

### Choosing Between Temperature and Effort

| If you want to…                                                  | Use…        |
|------------------------------------------------------------------|-------------|
| Make responses more or less creative or varied                   | Temperature |
| Make responses more or less rigorous or well-reasoned            | Effort      |
| Get natural-sounding phrasing in a conversational bot            | Temperature |
| Solve a hard problem (analysis, coding, multi-step reasoning)    | Effort      |
| Reduce hallucinations on a factual Q&A bot                       | Lower temperature, or switch to a reasoning model with low-to-medium effort |
| Make an extractor or classifier more deterministic               | Temperature → 0, or a reasoning model with low effort |
| Speed things up or reduce cost                                   | Lower effort (if set), or use a non-reasoning model |

**Quick decision guide:**

1. Is this a conversational, creative, or stylistic task? Use a general-purpose model and tune **Temperature**.
2. Is this a logic, analysis, math, or coding task? Use a reasoning model and tune **Effort**.
3. Not sure? Start with the default model and default settings. Adjust only if outputs are consistently too random, too bland, too shallow, or too slow.

### Max Token Limit

The max token limit sets the maximum number of tokens — input plus output — the model can process in a single interaction. Keeping this limit appropriate for your use case prevents responses from being cut off.

**To adjust the max token limit:**

1. Open your chatbot or LLM node settings.
2. Locate the **Max Token Limit** field.
3. Enter a value appropriate for your expected prompt length and response length.
4. Save your changes.

!!! warning "Reasoning models and token budgets"
    On reasoning models, the model's internal thinking tokens count toward the max output token budget. If you set Effort to `high` or `max` and the Max Token Limit is too low, the model may run out of space before producing a visible response. If you see truncated or empty responses from a high-effort run, raise the Max Token Limit.

### See Also

- [Large Language Models](../concepts/llm.md) — conceptual overview of LLMs, prompts, tokens, and parameters
- [LLM Node Advanced Settings](../tech-hub/llm_node_advanced_settings.md) — full technical parameter reference and provider-level details

## Other LLM Node Settings

- Node Name
- [Prompt](../concepts/llm.md#prompt)
- [LLM History Mode](../concepts/pipelines/history.md)
- [Max History Length](../concepts/pipelines/history.md#max-history-length)
- [Message Tag](../concepts/tags.md)
- [Tools](../concepts/tools/index.md)
