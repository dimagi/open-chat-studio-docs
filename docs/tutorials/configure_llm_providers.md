# Configure LLM Service Providers

This tutorial shows how to connect an [LLM provider](../concepts/team/llm_providers.md), such as OpenAI or Anthropic, to your team.
Your chatbots need a provider to get AI models that generate replies.
You configure providers from **Team Settings → [Integrations](../concepts/team/integrations.md)**, filtered to the **LLM & embedding** category.

## Prerequisites

**API Key Required**: You cannot create a provider without a valid API key.
The API key lets Open Chat Studio connect securely to your account with the provider.
You must:

1. Have an active account with the provider (OpenAI, Anthropic, Google, etc.)
2. Generate an API key from your provider account
3. Have access to the specific models you want to use

## Adding a New Provider

1. Go to **Team Settings → [Integrations](../concepts/team/integrations.md)**.
2. Click **Add integration**, then choose your provider from the **LLM & embedding** group.
   See [supported providers](../concepts/team/llm_providers.md) for the full list.
3. Enter your API key, plus any other details your provider needs.
   For example, a [LiteLLM](../concepts/team/llm_providers.md) provider also requires the **Base URL** of your proxy.
4. Save the configuration.

!!! tip "Base URL"

    You don't need to include the `/v1` suffix on a LiteLLM **Base URL**.
    Open Chat Studio appends it if it's missing, so `https://litellm.example.com` is saved as `https://litellm.example.com/v1`.

After saving, the provider page shows a **Models** tab listing the models it supports.
See [LLM Models](../concepts/team/llm_providers.md#llm-models) for how to filter the list.
If your provider, such as LiteLLM, has no pre-configured models, [add a custom model](../how-to/add_custom_llm_model.md).

## Verifying Your Credentials

Saving a provider checks its credentials against the provider's API, unless they're already [verified](../concepts/team/llm_providers.md#credential-verification).
The save button tells you upfront whether saving will run this check.

The provider page then shows the result: **Verified**, **Not checked**, or **Check failed**.
See [Credential Verification](../concepts/team/llm_providers.md#credential-verification) for what each state means.

## Testing Your Configuration

After adding a provider and models, it's recommended to:

1. Create a test chatbot
2. Configure it to use your new provider/model
3. Send a test message to verify everything works correctly

## Next steps

Configure the basics for your [LLM Node](configure_llm_node.md).

## See also

- [Add a Custom LLM Model](../how-to/add_custom_llm_model.md) if you need a model that isn't pre-configured in OCS.
- [Choose an LLM Model](../how-to/choose_llm_model.md)
