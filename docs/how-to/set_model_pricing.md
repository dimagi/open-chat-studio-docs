# Set or Override Model Pricing

The **Models** tab shows a price for each chat model. Prices start from OCS's global rates. You can set a price for a model that has none, or override a global price with your team's own rate. An override applies only to your team.

## Prerequisites

- A [configured LLM provider](../tutorials/configure_llm_providers.md) in your team
- Permission to change LLM provider models

## Steps

1. Go to your team's **LLM and Embedding Model Service Providers** settings.
2. Edit the provider, then open the **Models** tab.
3. On the model's row, click :material-pencil: to override the price. For a model showing **No pricing configured**, click **Set pricing** instead.
4. Enter one or more rates in dollars per 1M tokens:
    - **Input price**
    - **Output price**
    - **Cached input price**
5. Click **Save override**.

Enter at least one rate. Rates accept up to five decimal places. A blank field keeps the global rate for that item.

The row now shows your rates, with a badge naming the source. The **manual** badge, or a tooltip reading "Custom pricing override set for this team", marks a price your team entered.

!!! note "Cache write rates"

    A model's cache write rate appears on its row when one exists, but you can't set or override it from this form.

## Revert to the global price

To remove your override, click :material-undo: on the model's row and confirm. The row returns to the global rates.

This button appears only on a model that has both a team override and a global rate. A custom model has no global rate, so it has no revert button. To remove its price, [delete the model](#delete-a-custom-model) and add it again.

## Delete a custom model

Click :material-delete: on a custom model's row and confirm. Built-in models can't be deleted.

## Limits

- Deprecated models show their price but have no override, **Set pricing**, or revert buttons.
- Embedding models show no price.
- Every provider of the same type in your team shows the same model list, so an override on one applies to all of them.

## See also

- [LLM Service Providers](../concepts/team/llm_providers.md#llm-models) — how the Models tab works
- [Add a Custom LLM Model](add_custom_llm_model.md)
