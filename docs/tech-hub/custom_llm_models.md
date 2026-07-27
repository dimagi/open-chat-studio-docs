# Custom LLM Models

Add a model to a provider that isn't already pre-configured, using the exact model name format each provider expects.

Before adding a custom model, make sure you understand [LLM Service Providers](../concepts/team/llm_providers.md) and have already [configured a provider](../tutorials/configure_llm_providers.md).

## Adding a custom model

Edit the provider and use the :material-plus-box: button in the "Custom LLM Models" section. Enter the model name using the exact format from the provider's API — see the naming conventions below.

## Model naming conventions

**Important**: Model names must match the exact format used by the provider's API. Use lowercase with hyphens as specified by the provider.

### OpenAI models

For OpenAI models, use the exact model name from their API documentation — for example, `gpt-4o` (not `GPT-4o` or `gpt4o`).

Find current model names in [OpenAI's model documentation](https://platform.openai.com/docs/models).

### Anthropic models

For Anthropic (Claude) models, use the exact name from the "Claude API" column in their documentation — for example, `claude-3-5-sonnet-20241022`.

Find current model names in [Anthropic's model documentation](https://docs.anthropic.com/en/docs/about-claude/models).

### Google models

For Google (Gemini) models, use the name from the "Model Variant" column — for example, `gemini-1.5-pro`.

Find current model names in [Google's Gemini model documentation](https://ai.google.dev/gemini-api/docs/models).
