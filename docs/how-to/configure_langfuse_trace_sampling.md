---
title: Configure Langfuse Trace Sampling
---

# Configure Langfuse Trace Sampling

This guide walks you through reducing how much [Langfuse trace](../concepts/tracing.md#langfuse-external-tracing) data a chatbot sends, by setting a sample rate — either as a team-wide default or as a per-chatbot override. This is useful for high-traffic chatbots where sending every turn to Langfuse creates more trace volume than you need.

!!! note "Before you start"
    You need a Langfuse tracing provider already configured for your team. See [Langfuse External Tracing](../concepts/tracing.md#langfuse-external-tracing) for what it does, and open your Team settings' **Tracing Providers** page to add or edit one.

## Set a team-wide default sample rate

Use this when you want every chatbot on the team to send a reduced, consistent fraction of traces to Langfuse by default.

1. Go to your Team settings and open **Tracing Providers**.
2. Select the Langfuse provider you want to update.
3. Set the **Sample rate** field to a decimal between `0.0` and `1.0`.
4. Save the provider.

If no rate is set at either level, every turn is sent to Langfuse, the same as before this feature existed.

## Override the sample rate for one chatbot

Use this when a single chatbot needs a different rate than the team default — for example, a high-traffic chatbot that should send fewer traces than the rest of the team.

1. Open the chatbot for editing.
2. Go to the chatbot's settings.
3. Set the **Trace sample rate** field to a decimal between `0.0` and `1.0`.
4. Save.

Leave **Trace sample rate** blank to inherit the team-wide **Sample rate** from the chatbot's [trace provider](../concepts/team/index.md#team-configuration).

!!! tip "Turning off Langfuse tracing for one chatbot"
    Setting **Trace sample rate** to exactly `0.0` stops Langfuse traces for that chatbot completely, without removing the provider or affecting other chatbots. Builtin tracing keeps recording every turn for that chatbot as usual.

### Example

A chatbot handles 100,000 conversation turns a day, and the team's Langfuse plan is priced by trace volume. Setting that chatbot's **Trace sample rate** to `0.1` sends detailed span data to Langfuse for roughly 1 in 10 turns — cutting Langfuse volume by 90% — while every turn still appears in the Open Chat Studio [trace table](../concepts/tracing.md#trace-table) through builtin tracing.

## Expected outcome

New conversation turns immediately follow the updated rate — there's no delay before it takes effect. Turns that aren't sampled still appear in the builtin [trace table](../concepts/tracing.md#trace-table); they just won't have Langfuse span data or a "View in Langfuse" link on their trace detail page.

## Common issues

**I don't see a span tree panel on some trace detail pages, but the provider is configured.**
Those turns probably weren't sampled. Check whether the chatbot has a **Trace sample rate** override set lower than you expected, and raise the rate if you need more turns captured.

**Changing the rate didn't add span data to older traces.**
Sampling only affects new turns. Traces recorded before the change keep whatever data they already have.

## Related pages

- [Tracing](../concepts/tracing.md) — how builtin and Langfuse tracing work
- [Teams](../concepts/team/index.md) — team-level configuration, including tracing providers
- [Chatbots API (v2)](../api/v2/index.md) — the `trace_sample_rate` field is also available when creating or updating a chatbot through the API
