# Configure Providers

Providers are configured in your team settings under "LLM and Embedding Model Service Providers". Before configuring a provider, ensure that you have an active account at the provider and access to the necessary integration credentials.

## Prerequisites

**API Key Required**: You cannot create a provider without a valid API key. The API key is used for authentication between Open Chat Studio and the provider. You must:

1. Have an active account with the provider (OpenAI, Anthropic, Google, etc.)
2. Generate an API key from your provider account
3. Have access to the specific models you want to use

## Adding a New Provider

1. Go to your team settings
2. Navigate to "LLM and Embedding Model Service Providers"
3. Click "Add Provider"
4. Select your provider from the dropdown
5. Enter your API key
6. Save the configuration

## Adding Custom Models

If your provider doesn't have a pre-configured model you want to use, you can add it under the "Custom LLM Models" section.

### Model Naming Conventions

**Important**: Model names must match the exact format used by the provider's API. Use lowercase with hyphens as specified by the provider.

#### OpenAI Models
For OpenAI models, use the exact model names from their API documentation. Examples:
- `gpt-4o` (not `GPT-4o` or `gpt4o`)
- `gpt-5-nano-2025-08-07` (for specific snapshots)

Find current model names at: https://platform.openai.com/docs/models (check the "snapshots" section for each model)

#### Anthropic Models
For Anthropic (Claude) models, use the names from the "Claude API" column in their documentation. Examples:
- `claude-opus-4-6` (latest flagship model with adaptive thinking)
- `claude-3-5-sonnet-20241022`
- `claude-3-haiku-20240307`

Find current model names at: https://docs.anthropic.com/en/docs/about-claude/models

!!! info "Claude Opus 4.6 Features"
    Claude Opus 4.6 supports adaptive thinking with configurable effort levels (low, medium, high, max). This feature allows the model to engage in extended reasoning for complex tasks. See the [LLM documentation](../concepts/llm.md#claude-opus-46-anthropic) for detailed information about this capability.

#### Google Models
For Google (Gemini) models, use the names from the "Model Variant" column. Examples:
- `gemini-2.5-flash-exp`
- `gemini-1.5-pro`

Find current model names at: https://ai.google.dev/gemini-api/docs/models

## Testing Your Configuration

After adding a provider and models, it's recommended to:
1. Create a test bot
2. Configure it to use your new provider/model
3. Send a test message to verify everything works correctly
