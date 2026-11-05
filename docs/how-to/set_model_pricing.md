# Review Models and Manage Pricing

The **Models** tab on an LLM provider's edit page lists the models the provider can run, with their prices and context sizes. Prices start from OCS's global rates. You can set a price for a model that has none, or override a global price with your team's own rate. An override applies only to your team.

## Prerequisites

- A [configured LLM provider](../tutorials/configure_llm_providers.md) in your team

## Review the models

1. Go to your team's **LLM and Embedding Model Service Providers** settings.
2. Edit the provider, then open the **Models** tab.

![Edit LLM Service Provider shows models with pricing](../assets/images/LLM_models_with_pricing.png)

- Prices are in dollars per 1M tokens. A chat model with no price shows **No pricing configured**, and embedding models show no price.
- **Context** is the model's [max token limit](../concepts/llm.md#max-token-limit).
- A **custom** badge marks a model your team added. It appears under both the **Chat** and **Custom** filters.
- Deprecated models are hidden until you tick **Show deprecated**. The filter counts then include them.
- If your team has several providers of the same type, such as two Anthropic providers, they share the same models and prices. A price you set on one applies to all of them.

## Set or override a price

1. On the model's row, click :material-pencil:. For a model showing **No pricing configured**, click **Set pricing** instead.
2. Enter at least one of **Input price**, **Output price** and **Cached input price**, in dollars per 1M tokens. A blank field keeps the global rate. Rates accept up to five decimal places.
3. Click **Save override**.

The row shows your rates with a **manual** badge, which marks a price your team entered. You can't set the cache write rate from this form.

For example, if your team has a discounted contract with its LLM vendor, override the model's input and output rates with your contracted ones.

## Revert to the global price

Click :material-undo: on the model's row and confirm. The row returns to the global rates.

The button appears only when the model has both a team override and a global rate. A custom model has no global rate, so it has no revert button.

## Delete a custom model

Click :material-delete: on a custom model's row and confirm. Built-in models can't be deleted.

## Common issues

- **A model has no pencil button.** Deprecated and embedding models can't be given prices.
- **A model is missing from the list.** Tick **Show deprecated** and check the filter. If it was never pre-configured, [add a custom model](add_custom_llm_model.md).

## See also

- [Choose an LLM Model for Your Chatbot](choose_llm_model.md) — pick a model once you've compared prices and context sizes
- [Add a Custom LLM Model](add_custom_llm_model.md)
