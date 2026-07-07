---
title: How to track chatbot costs on the Dashboard
---

# Tracking Chatbot Costs on the Dashboard

The Dashboard gives you a team-wide view of chatbot usage and spend. This guide covers the **Cost Tracking panel**, which shows how much your chatbots are costing you and flags any usage data that could make those numbers incomplete.

## Before you begin

- You need access to your team's Dashboard to follow these steps.
- Cost tracking is enabled per team. If your team doesn't have it enabled, the cost chart and the **Cost** / **Cost per session** columns won't appear — contact your administrator or Dimagi support to have it turned on.
- Cost figures depend on your [LLM providers](../concepts/team/llm_providers.md) and the models your chatbots use. A chatbot that hasn't sent or received any messages in the selected period has no cost data to show.

## Orient yourself: Dashboard filters

The Dashboard applies a shared set of filters across its panels, including Cost Tracking:

- **Date range** — the period the numbers cover.
- **Chatbot** — restrict the view to one or more chatbots.
- **Participant** — restrict the view to one or more participants.
- **Channel** — restrict the view to one or more [channels](../concepts/channels.md).

!!! note "Filters now apply to Cost Tracking"
    Previously, the Cost Tracking panel only responded to the date range filter. It now respects the chatbot, participant, and channel filters too, so the costs you see always match the rest of the Dashboard.

## View daily spend

1. From the main navigation, open **Dashboard**.
2. Locate the **Cost Tracking** panel.
3. Set the filters (date range, chatbot, participant, channel) to the scope you want to review.
4. Review the daily-spend chart, which plots your spend for each day in the selected period.

Use the daily-spend chart to spot spikes or trends in spend before they show up as a surprise on your bill, and to see whether a change to a chatbot's model or prompt affected cost.

<!-- TODO: screenshot of the Cost Tracking panel, including the daily-spend chart -->

## Review cost per bot

The Dashboard's **Bot Performance** table lists usage metrics for each chatbot in the current filter scope. It now includes two cost columns:

| Column | Description |
|---|---|
| **Cost** | Total spend attributed to the chatbot for the selected period. |
| **Cost per session** | The chatbot's total cost divided by its number of sessions in the period. |

Use **Cost per session** to compare chatbots of different sizes on a level footing — a chatbot with more sessions will usually have a higher total **Cost**, but that doesn't necessarily mean it's less efficient per conversation.

## Understand coverage-gap warnings

Cost figures can only be as complete as the data behind them. When the Cost Tracking panel can't fully price your usage, it shows a coverage-gap warning above the chart.

To see which models are affected:

1. Locate the coverage-gap warning in the Cost Tracking panel.
2. Click the warning to expand it.
3. Review the list of affected models, grouped by reason:
    - **Unpriced models** — models with no cost data configured, so their usage can't be converted to a dollar amount.
    - **Missing usage data** — models with no token or usage records for the period, so there's nothing to price.

A model can appear in one of these lists even if the chatbots using it still respond normally — the warning only affects the accuracy of the cost figures, not chatbot behavior.

## Troubleshooting

**I see a coverage-gap warning and don't know why.**
Expand the warning to see the specific models involved, then check each one:

- If a model is listed as **unpriced**, confirm it's not a [custom LLM model](../concepts/team/llm_providers.md#adding-custom-llm-models) added without cost information.
- If a model is listed as **missing usage data**, check whether the affected chatbots were actually used during the selected date range.

**My totals changed after I adjusted a filter.**
This is expected. The Cost Tracking panel now recalculates using the same chatbot, participant, channel, and date range filters as the rest of the Dashboard. Narrowing a filter narrows the cost totals to match.

**A chatbot I expect to see is missing from Bot Performance.**
Check that it isn't excluded by the current chatbot, participant, or channel filter, and that it had activity within the selected date range.

## Related concepts

- [Large Language Models (LLMs)](../concepts/llm.md) — how tokens and models relate to cost.
- [LLM Service Providers](../concepts/team/llm_providers.md) — how models are configured for your team, including custom models.
- [Channels](../concepts/channels.md) — how a chatbot's channel is determined for filtering.
