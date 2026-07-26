# Configure LLM Service Providers

LLM service providers are configured in your [Team](../concepts/team/index.md) settings under "LLM and Embedding Model Service Providers". Before configuring a provider, ensure that you have an active account at the provider and access to the necessary integration credentials.

## Prerequisites

**API Key Required**: You cannot create a provider without a valid API key. The API key is used for authentication between Open Chat Studio and the provider. You must:

1. Have an active account with the provider (OpenAI, Anthropic, Google, etc.)
2. Generate an API key from your provider account
3. Have access to the specific models you want to use

## Adding a New Provider

1. Go to your team settings
2. Navigate to "LLM and Embedding Model Service Providers"
3. Click "Add Provider"
4. Select your provider from the dropdown (see [supported providers](../concepts/team/llm_providers.md) for the full list)
5. Enter your API key
6. Save the configuration

!!! note  
    After saving, the provider page lists the LLM models it supports. Each model shows its [max token limit](../concepts/llm.md#max-token-limit).

## Testing Your Configuration

After adding a provider and models, it's recommended to:
1. Create a test chatbot
2. Configure it to use your new provider/model
3. Send a test message to verify everything works correctly

## Adding Custom LLM Models

If you need a model that isn't pre-configured, see [Custom LLM Models](../tech-hub/custom_llm_models.md) for how to add one and the exact naming format each provider requires.
