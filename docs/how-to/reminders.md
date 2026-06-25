# Schedule Reminders

Reminder tools let your chatbot schedule messages that OCS delivers to participants at a future time — even after the conversation ends. For an overview of the four tools, see [Reminders](../concepts/tools/index.md#reminders).

## Prerequisites

- An existing chatbot connected to at least one channel (WhatsApp, Telegram, web widget, etc.).

## Step 1: Enable the reminder tools

1. Open your chatbot's node settings.
2. In the **Tools** section, enable the reminder tools your chatbot needs.

!!! tip
    Only enable what the chatbot needs — a shorter tool list helps the LLM stay focused.

## Step 2: Guide the LLM in your system prompt

Add instructions to your system prompt that name the tools explicitly:

```text
When the participant asks to be reminded once, use the `one-off-reminder` tool.
When the participant asks to be recurrently reminded about something, use the `recurring-reminder` tool.
When they ask to cancel a reminder, use the `delete-reminder` tool.
When they ask to change the time, use the `move-scheduled-message-date` tool.
```

Also describe the tone for reminder messages:

```text
Write reminder messages in a warm, encouraging tone.
For example: "Good morning! Time to take your medication."
```

## Step 3: Handle timezones

The tools handle timezones differently:

- `one-off-reminder` and `recurring-reminder` store ISO 8601 datetime strings, which can carry a timezone offset. The LLM does not need to convert to UTC for these tools.
- `move-scheduled-message-date` takes an `hour` value in UTC. The LLM must convert the participant's local time to UTC when calling this tool.

If the channel is the web chat widget, the participant's timezone is available as [participant data](../concepts/participant_data.md#participant-timezone-for-web-channel). For other channels, include the timezone in your system prompt:

```text
Participants are in Cape Town, South Africa (UTC+2). When calling move-scheduled-message-date, convert their requested local time to UTC.
```

## Step 4: Verify reminders for a participant

To confirm a reminder was scheduled or troubleshoot a missed message, open the participant's chatbot **Session details** screen. It shows both the participant's data and their **participant schedules** — all active reminders and scheduled messages — in one place.

See [Participant data](../concepts/participant_data.md) for details on how to use participant data.
