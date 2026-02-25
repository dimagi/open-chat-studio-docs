---
title: How to filter sessions and messages
---
# Filtering Sessions and Messages

Open Chat Studio provides a filter panel on the Sessions and Messages tables that lets you narrow down the data you see. You can build filters manually by adding filter rows, or use the **natural language filter** to describe what you want in plain English and have the system generate the filter rows for you.

!!! note "Availability"

    The Sessions and Messages tables are available within each chatbot or experiment. Other tables (traces, participants, notifications) do not have this filter panel.

## Natural Language Filter

!!! note "Beta Feature"

    The natural language filter is currently in **beta**. A team admin must enable it before it appears in the UI.

The natural language filter lets you describe what you want to find using a plain-English sentence. The system interprets your description and automatically populates the filter rows, which are applied immediately to the table.

### Enabling the Feature

Before you can use the natural language filter, a team admin must turn it on for your team.

1. Sign in with a team admin account.
2. Navigate to your team settings and open the **Team Feature Flags** page.
3. Enable the **Natural Language Filter** flag.

Once enabled, the natural language input field appears at the top of the filter panel on the Sessions and Messages tables for all members of your team.

### Using the Natural Language Filter

1. Open the **Sessions** table for a chatbot (or the **Messages** table within a session).
2. Click the filter panel to expand it. The natural language input field appears at the top.
3. Type a plain-English description of the data you want to find. For example:

    - `sessions from last week excluding WhatsApp`
    - `messages that contain an error`
    - `sessions started in January 2026 on Telegram`

4. Click **Generate** (or press **Enter**).
5. The system converts your description into structured filter rows and applies them to the table immediately.

!!! tip

    You can review and adjust the generated filter rows after they are created. The natural language input is a starting point; you can always fine-tune individual filter values manually.

### Supported Tables

| Table | Natural Language Filter Available |
|---|---|
| Sessions (chatbot/experiment) | Yes |
| Messages | Yes |
| Traces | No |
| Participants | No |
| Notifications | No |

### Tips for Writing Effective Queries

- **Be specific about time ranges**: Use phrases like "last week", "in January 2026", or "in the past 30 days".
- **Name channels explicitly**: Use channel names as they appear in the UI, such as "WhatsApp", "Telegram", or "Web".
- **Combine conditions naturally**: Join multiple criteria with "and" or "excluding" to refine results (for example, "sessions from this month on WhatsApp excluding completed sessions").
- **Keep it concise**: Short, direct descriptions produce more accurate filters than long, complex sentences.

### Troubleshooting

**The natural language input field does not appear.**

The feature may not be enabled for your team. Ask a team admin to enable it from the **Team Feature Flags** page.

**The generated filters do not match what I expected.**

Review the generated filter rows and adjust any individual values manually. You can also try rephrasing your query to be more specific.

**The filter returns no results.**

Check that the generated filter values are correct. For example, verify that channel names and date ranges match the data in your table.
