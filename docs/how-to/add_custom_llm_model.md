# Add a Custom LLM Model

If a model isn't pre-configured for your provider, add it yourself directly in Open Chat Studio.

## Prerequisites

- A [configured LLM provider](../tutorials/configure_llm_providers.md) in your team
- The exact model name, in the format required by the provider's API — see naming conventions below

## Steps

1. Go to your team's **LLM and Embedding Model Service Providers** settings
2. Edit the provider you want to add the model to
3. In the "Custom LLM Models" section, click :material-plus-box:
4. Enter the model name, using the exact format from the provider's API
5. Save the provider

The new model is now available when configuring chatbots and pipelines that use this provider.

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

## See also

- [LLM Service Providers](../concepts/team/llm_providers.md) — what LLM providers are and how models work in OCS
