---
title: How to filter tables with natural language
---

# Filtering Tables with Natural Language

Open Chat Studio lets you filter data tables by typing a plain-English query instead of manually building filter rows. The platform converts your description into structured filters automatically.

Natural language filtering is available on the following tables:

- Sessions
- Messages
- Traces
- Participants
- Notifications

## How to use it

1. Open any supported table (for example, navigate to a chatbot's **Sessions** tab).
2. Locate the natural language input field at the top of the filter area.
3. Type a plain-English description of the records you want to see. For example:

    - `sessions from last week excluding WhatsApp`
    - `messages from participants in Ghana`
    - `failed traces from the past 3 days`

4. Click **✨ Generate**.

The platform sends your query to an AI model, which builds the corresponding filter rows and applies them to the table. You can review, adjust, or remove any generated filter row just as you would with manually created filters.

!!! tip
    Be as specific as you need to be. Mentioning a channel name, a date range, a status value, or a tag helps the generator produce more accurate filters.

## Date ranges

When you mention a relative date range in your query (such as "last week" or "past 3 days"), the filter is anchored to today's date at the moment you click **✨ Generate**.

The date range option **Last 14 Days** is available in the date filter picker when building or adjusting filters manually.

## Editing generated filters

After generation, each filter row behaves exactly like a manually created row. You can:

- Change a field, operator, or value using the dropdowns and inputs.
- Remove a row by clicking its delete button.
- Add additional rows manually to refine the result set.

Clicking **✨ Generate** again replaces all existing filter rows with a new set based on your updated query.

!!! warning
    Clicking **✨ Generate** clears any filters you have already built or edited. If you want to keep your current filters, adjust them manually instead of regenerating.

## Troubleshooting

**The generated filters do not match what I described.**
Try rephrasing your query with more specific field names or values. For example, instead of "recent sessions", write "sessions from the last 7 days".

**The ✨ Generate button is not visible.**
The natural language input appears only when a filter slug is present on the table. If you do not see it, check that you are on a supported table and that the page has fully loaded.
