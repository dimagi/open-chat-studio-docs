# Review Chatbot Adoption with the Engagement Dashboard

The Engagement dashboard shows how many people use your team's chatbots and how often they return.
Use it to review adoption over the last several months.
It is separate from the team dashboard and uses a fixed monthly window instead of a date-range picker.

!!! note
    The Engagement dashboard is behind the `flag_engagement_dashboard` feature flag.
    The flag is off for every team by default.

## Prerequisites

- The `flag_engagement_dashboard` feature flag is enabled for your team.
  Self-hosted operators and admins enable it per team from the admin feature-flags page.
- At least one chatbot with participant messages.

## Steps

1. In the left navigation, select **Dashboard → Engagement**.
2. Review the three headline stat tiles: Monthly Active Users, Core Users Rate, and Average Session Duration.
3. Review the charts below the tiles: Weekly Active Users Trend and New vs. Returning Users.
4. Review the ranked breakdowns by chatbot and by channel.
   Select a row's link to open that chatbot or its sessions.
5. To narrow the data, filter by chatbot, channel, participant, or tag.

## Time window

The window is fixed.
It covers the last six complete months plus the current partial month.
You cannot change the date range or granularity, and you cannot save filters.

Because of this, totals differ from the date-filtered totals on the team dashboard.
This is expected.

## Metrics

| Metric | Meaning |
|---|---|
| Monthly Active Users | Distinct participants who sent a message in the month. |
| Core Users Rate | The share of active participants who were active in two or more separate weeks of the month. Use it as a signal of repeat use. |
| Average Session Duration | The average length of a session. |
| Weekly Active Users Trend | Participants grouped by the number of weeks they were active in the month: 1, 2, 3, or 4+. |
| New vs. Returning Users | Weekly counts. New participants are those whose participant record was created in that week (first contact). Returning participants were seen before. |
| Breakdown by chatbot and channel | Ranked rows showing each item's share, last month's figure, and a link to the chatbot or its sessions. |

### Stat tiles

Each headline tile shows a sparkline covering seven months and the span the figure covers.

While the current month is still in progress, the tile names its cutoff, for example "Sep 1-24".
It does not show the month-over-month change.
Comparing a partial month with a complete one would show a decline that has not happened.

### How activity is counted

- Evaluation activity and setup-session activity are excluded.
- Only conversation turns are counted.
- A week belongs to the month that contains its Monday.
- Series are zero-filled, so quiet periods show as zero.

## Example

You launched a WhatsApp chatbot three months ago and want to know whether users come back.
Open the Engagement dashboard and filter by the chatbot.
A rising Core Users Rate and a growing share of participants in the 3 and 4+ weekly buckets show repeat use.
The channel breakdown shows whether WhatsApp or another channel drives the activity.

## Common issues

- **The Engagement item is missing from the Dashboard menu.** The feature flag is not enabled for your team. Ask your operator or admin to enable it.
- **A tile has no month-over-month change.** The current month is incomplete. The change appears after the month ends.
- **Totals differ from the team dashboard.** The team dashboard uses the date range you pick. This page uses a fixed monthly window.

## See also

- [Feature Flags](../concepts/team/feature_flags.md)
- [Sessions](../concepts/sessions.md)
- [Tags](../concepts/tags.md)
- [Channels](../concepts/channels.md)
