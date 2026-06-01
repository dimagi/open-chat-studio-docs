---
title: LLM Model Parameters
---

# LLM Model Parameters

This page is a technical reference for the model parameters available in Open Chat Studio. It covers parameter details and provider-level behaviour differences.

For a conceptual overview, see [Large Language Models](../concepts/llm.md). For guidance on choosing the right settings, see [Adjust LLM Node Settings](../how-to/adjust_llm_node_settings.md).

## Parameter Reference

Different models expose different parameters. When you select a model in Open Chat Studio, the configuration panel shows only the parameters that model supports — parameters with no effect on the selected model are hidden automatically.

### When Effort is set, Temperature is ignored

For models that use reasoning effort, `temperature` and `top_p` cannot be set at the same time — the reasoning loop manages output randomness internally. This applies to reasoning-capable models from OpenAI and Anthropic (exact models vary by API version and release). Open Chat Studio hides the Temperature field automatically based on the selected model's capabilities.

### Reasoning and Adaptive Thinking

"Reasoning" is the broader concept underlying Effort: the model spends extra tokens thinking before it produces the answer the user sees. Each provider exposes this differently:

- **OpenAI** calls it `reasoning_effort` and uses the four-level system (`low`, `medium`, `high`, `max`).
- **Anthropic** offers **adaptive thinking** on Claude 4.6 models. Adaptive thinking lets the model decide how much to think on a per-message basis, guided by the effort level you set. Easier turns use less thinking budget; harder turns receive more.
- **Google Gemini** exposes a numeric thinking budget on Gemini 2.5+ models.

You normally don't need to think about these provider-level differences — Open Chat Studio abstracts them into the same effort levels (`low/medium/high/max`) wherever the model supports them.

## See Also

- [Large Language Models](../concepts/llm.md) — conceptual overview of LLMs, prompts, tokens, and parameters
- [Adjust LLM Node Settings](../how-to/adjust_llm_node_settings.md) — guidance on choosing the right settings
