---
title: Max Token Limit
---

# Max Token Limit

The max token limit is the maximum number of tokens an LLM can handle in a single interaction — covering both the input (your prompt and conversation history) and the output (the model's response) combined.

## How it works

Every LLM has a fixed context window: a ceiling on the total number of tokens it can process at once. Within that window, tokens are shared between:

- **Input tokens** — your prompt, system instructions, and conversation history
- **Output tokens** — the model's response

If the input alone is too long, the model cannot process the request. If there is not enough space left for output, the response may be cut short.

**Example:** If the max token limit is 4096 tokens, a prompt using 2000 tokens leaves 2096 tokens available for the response.

## Relationship to History Mode

The Max Token Limit interacts directly with [History Mode](pipelines/history.md). When history is enabled, prior conversation turns accumulate as input tokens. A low token limit combined with a long conversation history leaves little room for the model's response.

## Default behaviour

If you do not set a Max Token Limit in OCS, the system uses the default for the selected LLM model. You only need to configure this explicitly if:

- You are seeing truncated or empty responses
- You are using a reasoning model with high effort (see below)

## Reasoning models and token budgets

On [reasoning models](../tech-hub/llm_model_parameters.md#reasoning-and-adaptive-thinking), internal thinking tokens count toward the max output token budget. With Effort set to `high` or `max`, the model spends more tokens on internal reasoning before producing a visible response — leaving fewer tokens available for that response.

If you see truncated or empty responses from a high-effort run, raise the Max Token Limit.

## Going Further

- [Adjust the Max Token Limit](../how-to/adjust_llm_node_settings.md#max-token-limit) — step-by-step instructions
- [LLM Model Parameters](../tech-hub/llm_model_parameters.md#reasoning-and-adaptive-thinking) — provider-level detail on reasoning and thinking budgets
- [History Mode](pipelines/history.md) — how conversation history affects token usage
