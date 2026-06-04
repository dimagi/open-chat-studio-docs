---
title: Max Token Limit
---

# Max Token Limit

Every AI model has a maximum token limit — also called its **context window**. This is a fixed property of the model itself that you cannot change.

The context window is the total number of tokens the model can work with in one turn: your prompt, the conversation history, and the model's reply all share the same budget. When the budget runs out, the request may be truncated or fail.

If your chatbot uses long prompts or extended conversations, choose a model with a larger context window. Context window size is listed alongside the model name when selecting a model in OCS.

For guidance on picking the right model, see [Choose an LLM Model](../how-to/choose_llm_model.md).

## Related pages

- [Large Language Models](llm.md) — foundational concepts including prompts and tokens
- [Model Configuration Reference](../tech-hub/model_configuration.md#max-output-tokens) — how to control how long the model's reply can be
- [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md) — how to change model settings in the UI
