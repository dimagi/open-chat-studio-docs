---
title: LLM Model Parameters
---

# LLM Model Parameters
This page provides a more in-depth technical reference of model parameters as OCS UI hides the complexity of the different LLM providers. Advanced users can use this to map OCS terminology to industry-standard AI terminology.


## Which models support which parameters

Temperature is supported by most general-purpose chat models including GPT-4o, Claude Sonnet/Opus without thinking enabled, Gemini, Groq, Perplexity, and Deepseek. 

It is **not** available on reasoning models that use Effort — see below.

Models that use effort include OpenAI's GPT-5 / GPT-5.2 series and Anthropic's Claude Opus 4.6 and Sonnet 4.6 with [thinking enabled](../tech-hub/llm_model_parameters.md#reasoning-and-adaptive-thinking).

### When Effort is set, Temperature is ignored

For models that use reasoning effort, `temperature` and `top_p` cannot be set at the same time — the reasoning loop manages output randomness internally. This applies to reasoning-capable models from OpenAI and Anthropic (exact models vary by API version and release). Open Chat Studio hides the Temperature field automatically based on the selected model's capabilities.

### Reasoning and Adaptive Thinking

"Reasoning" is the broader name for the same idea as effort: letting the model spend extra tokens *thinking* before it produces the answer the user sees. Different providers expose this slightly differently:

- **OpenAI** calls it `reasoning_effort` and uses the four-level system (`low`, `medium`, `high`, `max`).
- **Anthropic** offers **adaptive thinking** on its Claude 4.6 models. Adaptive thinking
  lets the model decide how much to think on a per-message basis, guided by the effort
  level you set. Easy turns finish quickly; hard turns get more thinking budget.
- **Google Gemini** exposes a thinking budget on some Gemini 2.5+ models.

You normally don't need to think about these provider-level differences — Open Chat Studio abstracts them into the same effort levels (`low/medium/high/max`) wherever the model supports them.

## See Also

- [Large Language Models](../concepts/llm.md) — conceptual overview of LLMs, prompts, tokens, and parameters
- [Max Token Limit](../concepts/max_token_limit.md) — how the context window is shared between input and output, and reasoning model caveats
- [Adjust LLM Node Settings](../how-to/adjust_llm_node_settings.md) — guidance on choosing the right settings
