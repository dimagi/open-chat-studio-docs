# Add a Custom LLM Model

If a model isn't pre-configured for your provider, add it yourself directly in Open Chat Studio.

## Prerequisites

- A [configured LLM provider](../tutorials/configure_llm_providers.md) in your team
- The exact model name, in the format required by the provider's API — see naming conventions below

## Steps

1. Go to your team's **LLM and Embedding Model Service Providers** settings
2. Edit the provider you want to add the model to
3. On the **Models** tab, click :material-plus-box: to add a custom model
4. Enter the model name, using the exact format from the provider's API
5. Save the provider

The new model is now available when configuring chatbots and pipelines that use this provider. It appears alongside the provider's built-in models on the [Models tab](../concepts/team/llm_providers.md#llm-models), filtered by the same chat/embedding role.

## Model naming conventions

**Important**: Model names must match the exact format used by the provider's API. Use lowercase with hyphens as specified by the provider.

### OpenAI models

For OpenAI models, use the exact model name from their API documentation — for example, `gpt-4o` (not `GPT-4o` or `gpt4o`), and `gpt-5-nano-2025-08-07` (for specific snapshots).

Find current model names in [OpenAI's model documentation](https://platform.openai.com/docs/models).

### Anthropic models

For Anthropic (Claude) models, use the exact name from the "Claude API" column in their documentation — for example, `claude-sonnet-4-6`,`claude-3-5-sonnet-20241022`.

Find current model names in [Anthropic's model documentation](https://docs.anthropic.com/en/docs/about-claude/models).

### Google models

For Google (Gemini) models, use the name from the "Model Variant" column — for example, `gemini-3.5-flash-lite`.

Find current model names in [Google's Gemini model documentation](https://ai.google.dev/gemini-api/docs/models).

### LiteLLM models

A [LiteLLM](../concepts/team/llm_providers.md) provider ships with no pre-configured models, so you must add every model it should offer. Use the exact name your proxy is configured to serve it under — for example, `gpt-4o` or `claude-sonnet-4-6` — depending on the backend models your proxy exposes. Check your proxy's configuration to confirm the exact names.

## See also

- [LLM Service Providers](../concepts/team/llm_providers.md) — what LLM providers are and how models work in OCS
