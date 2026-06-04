---
title: Adjust LLM Node Model Parameters
---

# Adjust LLM Node Model Parameters

This guide steps you through adjusting the LLM model parameters on an [LLM node](../concepts/pipelines/nodes.md#llm-node) in your chatbot [pipeline](../concepts/pipelines/index.md). It assumes you already have a chatbot or pipeline open for editing.

!!! note "Before you start"
    Choose your LLM model first — see [Choose an LLM Model](choose_llm_model.md). The parameters available in the settings panel depend on the model you select.

## Step 1 — Open the node settings

1. Open your pipeline or chatbot for editing.
2. Click the LLM node you want to configure.
3. Select "Advanced" to open up the settings panel

## Step 2 — Select a model

1. In the node settings, locate the **LLM Model** dropdown.
2. Select the model you want to use.

## Step 3 — Adjust temperature or effort

Once you select an LLM model, Open Chat Studio shows only the settings that apply to it.

### If the model shows a Temperature setting

Temperature controls how creative or varied the responses are.

- Slide toward **0** for more consistent, predictable answers (good for factual Q&A or classification).
- Slide toward **1** for more varied, creative answers (good for creative writing or friendly conversation).
- The default value of **0.7** is a reasonable starting point for most chatbots.

### If the model shows an Effort setting

Effort (or Reasoning Effort) controls how much internal reasoning the model does before answering. It is available on reasoning models.

Select a level from the dropdown:

| Level    | When to use it                                                       |
|----------|----------------------------------------------------------------------|
| `low`    | Routine questions where speed matters more than depth                |
| `medium` | Most tasks — a good default                                          |
| `high`   | Complex analysis, multi-step problems, or tasks needing careful logic|
| `max`    | The hardest problems where accuracy is more important than speed     |

!!! tip
    Higher effort levels cost more tokens and take longer to respond. Start with `medium` and only raise it if answers are not thorough enough.

## Step 4 — Adjust max output tokens (if shown)

The **Max output tokens** field caps how long the model's response can be. Leave it at the default unless you have a specific reason to limit response length.

!!! warning "Reasoning models"
    If you are using a reasoning model (one that shows an Effort setting), set this value higher than you would for a standard model. A value that is too low can result in no visible output at all. See [Max Output Tokens](../tech-hub/model_configuration.md#max-output-tokens) for details.

## Step 5 — Save your changes

1. Click off the edit settings dialog to save
2. Test your chatbot to confirm the output looks as expected.

## Troubleshooting

**The model I want does not appear in the list.**
Your team may not have that provider configured. Ask your team administrator or see [LLM Providers](../concepts/team/llm_providers.md).

**Responses are being cut off.**
The max output token limit may be too low. Raise it in the node settings. If you are using a [reasoning model](../tech-hub/model_configuration.md), this is especially common — see [Model Configuration Reference](../tech-hub/model_configuration.md#max-output-tokens) for details.

**I changed temperature but the answers feel the same.**
Check that you are not using a reasoning model — those use effort instead of temperature. OCS hides the temperature setting on reasoning models.

## Related pages

- [Choose an LLM Model](choose_llm_model.md) — guidance on picking the right model for your use case
- [Large Language Models](../concepts/llm.md) — conceptual overview of temperature and effort
- [Model Configuration Reference](../tech-hub/model_configuration.md) — full parameter details including max output tokens
