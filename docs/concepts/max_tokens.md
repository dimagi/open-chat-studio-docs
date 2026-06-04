---
title: Max Token Limit
---

# Max Token Limit

Every LLM has a maximum number of [tokens](llm.md#tokens) it can handle in a single interaction. This limit covers both the input (your prompt and the conversation history) and the output (the model's response) combined.

## Why it matters

When the total token count for a request approaches the limit, the model has less room to generate a full response. A very long prompt leaves fewer tokens available for the answer. If the limit is reached, the response may be cut short.

Understanding the token limit helps you write effective prompts and configure your chatbot so responses are never unexpectedly truncated.

**Example:** If the max token limit is 4 096 tokens and your prompt uses 2 000 tokens, up to 2 096 tokens remain for the model's response.

## Reasoning models and token budgets

Reasoning models (those that use an [effort](llm.md#model-parameters-temperature-and-effort) setting) consume tokens differently. Before producing a visible answer, these models spend tokens on internal "thinking". Those thinking tokens count toward the same output token budget.

If you set effort to `high` or `max` on a complex task but keep the max output token limit low, the model may exhaust its budget on thinking before it produces any visible response. The result is a truncated or empty reply.

If you see empty or cut-off responses from a high-effort run, raise the max output token limit in your node settings.

## Related pages

- [Large Language Models](llm.md) — foundational concepts including prompts and tokens
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — how to change the max output token setting
- [Model Configuration Reference](../tech-hub/model_configuration.md) — full parameter details for advanced users
