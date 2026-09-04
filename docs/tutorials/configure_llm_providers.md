# Configure LLM Service Providers

LLM service providers are configured in your Team settings under "LLM and Embedding Model Service Providers". Before configuring a provider, make sure you have an active account with the provider and its API key ready.

## Prerequisites

**API Key Required**: You cannot create a provider without a valid API key. The API key lets Open Chat Studio connect securely to your account with the provider. You must:

1. Have an active account with the provider (OpenAI, Anthropic, Google, etc.)
2. Generate an API key from your provider account
3. Have access to the specific models you want to use

## Adding a New Provider

1. Go to your team settings
2. Navigate to "LLM and Embedding Model Service Providers"
3. Click "Add Provider"
4. Select your provider from the dropdown (see [supported providers](../concepts/team/llm_providers.md) for the full list)
5. Enter your API key, plus any other details your provider needs — for example, a [LiteLLM](../concepts/team/llm_providers.md) provider also requires the **Base URL** of your proxy
6. Save the configuration

!!! tip "Base URL"

    You don't need to include the `/v1` suffix on a LiteLLM Base URL — Open Chat Studio appends it if it's missing, so `https://litellm.example.com` is saved as `https://litellm.example.com/v1`.

!!! note
    After saving, the provider page shows a **Models** tab listing the LLM models it supports, with filter chips to switch between chat and embedding models. Each model shows its [max token limit](../concepts/llm.md#max-token-limit) and pricing. A provider with no pre-configured models, such as LiteLLM, shows an empty list until you add a [custom model](../how-to/add_custom_llm_model.md).

## Verifying Your Credentials

Saving a provider checks its credentials against the provider's API, unless they're already [verified](../concepts/team/llm_providers.md#credential-verification). The save button tells you upfront whether saving will run this check.

The provider page then shows the standing result — **Verified**, **Never checked**, or **Rejected** with the provider's own error message — so you can always see where a provider's credentials stand, not just at the moment you save. See [Credential Verification](../concepts/team/llm_providers.md#credential-verification) for details.

## Testing Your Configuration

After adding a provider and models, it's recommended to:
1. Create a test chatbot
2. Configure it to use your new provider/model
3. Send a test message to verify everything works correctly

## Adding Custom LLM Models

If you need a model that isn't pre-configured in OCS, see [Add a Custom LLM Model](../how-to/add_custom_llm_model.md) for how to add one.
