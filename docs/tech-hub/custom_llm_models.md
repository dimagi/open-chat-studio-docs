# Custom LLM Models

Add a model to a provider that isn't already pre-configured, using the exact model name format each provider expects.

Before adding a custom model, make sure you understand [LLM Service Providers](../concepts/team/llm_providers.md) and have already [configured a provider](../tutorials/configure_llm_providers.md).

## Adding a custom model

Edit the provider and use the :material-plus-box: button in the "Custom LLM Models" section. Enter the model name using the exact format from the provider's API — see the naming conventions below.

## Model naming conventions

**Important**: Model names must match the exact format used by the provider's API. Use lowercase with hyphens as specified by the provider.

### OpenAI models

For OpenAI models, use the exact model names from their API documentation. Examples:

- `gpt-4o` (not `GPT-4o` or `gpt4o`)
- `gpt-5-nano-2025-08-07` (for specific snapshots)

Find current model names at: https://platform.openai.com/docs/models (check the "snapshots" section for each model)

### Anthropic models

For Anthropic (Claude) models, use the names from the "Claude API" column in their documentation. Examples:

- `claude-sonnet-4-6`
- `claude-opus-4-6`
- `claude-3-5-sonnet-20241022`
- `claude-3-haiku-20240307`

Find current model names at: https://docs.anthropic.com/en/docs/about-claude/models

### Google models

For Google (Gemini) models, use the names from the "Model Variant" column. Examples:

- `gemini-2.5-flash-exp`
- `gemini-1.5-pro`

Find current model names at: https://ai.google.dev/gemini-api/docs/models
