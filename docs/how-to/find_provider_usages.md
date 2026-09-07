# Find Where a Provider Is Used

Before rotating an API key, deprecating a provider, or triaging a potentially leaked credential, you need to know everywhere in your team that provider is referenced. Open Chat Studio surfaces this on the provider's own edit page, so you don't have to search chatbots, pipelines, and collections one by one.

## Prerequisites

- An existing [integration](../concepts/team/integrations.md) — an LLM, Speech, Messaging, Authentication, or Tracing provider — to look up.
- Access to view that provider's edit page in Team Settings.

## Steps

1. Go to **Team Settings → [Integrations](../concepts/team/integrations.md)**.
2. Select **Edit** on the provider you want to check.
3. Select the **Usages** tab.
4. Review the categories listed. What you see depends on what references the provider:
    - **Chatbots** — every chatbot that uses the provider, whether directly or through one of its pipelines or channels. Links go to the working version's edit page; references belonging to a published version are tagged with a version badge.
    - **Unlinked Pipelines** / **Unlinked Channels** — pipelines or channels that reference the provider but aren't attached to any chatbot, including archived pipelines. They can't be grouped under a chatbot row, so they get their own category instead.
    - **Collections** — collections whose document sources reference the provider, rolled up to the owning collection.
    - **Evaluators** — LLM evaluators that use the provider (LLM service providers only).

    Other object types that reference a provider can also appear, each as its own category named after that object type.

Resolving usages can take a few seconds on a busy team, since it looks across several tables.

## Example: rotating a leaked API key

Say a teammate accidentally commits an OpenAI API key to a public repository. Before rotating it:

1. Open the OpenAI provider's edit page and select **Usages**.
2. Note every chatbot, pipeline, and evaluator listed — these will need to keep working after the key changes, so this tells you what to test afterwards.
3. Rotate the key in OpenAI's dashboard, then update the provider's **API Key** field in OCS and save.
4. Open **Usages** again to confirm the same references are still there. Chatbots and pipelines point at the provider record, not the key itself, so they pick up the new key automatically — no need to update them individually.

## Common issues

- **A pipeline or channel I expect to see isn't listed under a chatbot.** Check the **Unlinked Pipelines** / **Unlinked Channels** categories — it's likely not attached to any chatbot (or was, and the chatbot has since been deleted).
- **The Usages tab is empty.** Nothing in your team currently references this provider, so it's safe to delete without affecting anything.

## See also

- [Team Settings](../concepts/team/index.md)
- [Integrations](../concepts/team/integrations.md)
