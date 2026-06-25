# Tools Reference

This page is a full technical reference for the built-in tools available in Open Chat Studio.

For a plain-English overview of what each tool does and when to use it, see [Tools](../concepts/tools/index.md).

## Quick reference

To instruct the model to use a specific tool, refer to it by its tool name in your system prompt. For example:

> When the user asks to be reminded, use the `recurring-reminder` tool.

### User-configurable tools

| Tool | Name | Description |
|------|------|-------------|
| [Calculator](#calculator) | `calculator` | Performs mathematical calculations |
| [Recurring reminders](#recurring-reminders) | `recurring-reminder` | Schedules a repeating reminder |
| [One-off reminder](#one-off-reminder) | `one-off-reminder` | Schedules a single reminder |
| [Delete reminder](#delete-reminder) | `delete-reminder` | Cancels an existing reminder |
| [Move reminder date](#move-reminder-date) | `move-scheduled-message-date` | Reschedules an existing reminder |
| [Update participant data](#update-participant-data) | `update-user-data` | Writes a value to participant data |
| [Append to participant data](#append-to-participant-data) | `append-to-participant-data` | Appends a value to a list in participant data |
| [Increment counter](#increment-counter) | `increment-counter` | Increments a counter in participant data |
| [Set session state key](#set-session-state-key) | `set-session-state-key` | Stores a key-value pair in session state |
| [Get session state key](#get-session-state-key) | `get-session-state` | Retrieves a value from session state |
| [Append to session state](#append-to-session-state) | `append-to-session-state` | Appends a value to a list in session state |
| [Increment session state counter](#increment-session-state-counter) | `increment-session-state-counter` | Increments a counter in session state |
| [End session](#end-session) | `end-session` | Marks the current session as complete |

### LLM provider tools

| Provider | Tool | Supported |
|----------|------|-----------|
| OpenAI | [Web Search](#openai-web-search) | :material-check-circle-outline:{ .green } Yes |
| OpenAI | [Code Interpreter](#openai-code-interpreter) | :material-check-circle-outline:{ .green } Yes |
| Anthropic | [Web Search](#anthropic-web-search) | :material-check-circle-outline:{ .green } Yes |
| Anthropic | [Code Execution](#anthropic-code-execution) | :octicons-x-circle-24:{ .red } No |
| Gemini | [Grounding with Search](#gemini-grounding-with-search) | :octicons-x-circle-24:{ .red } No |
| Gemini | [Code Execution](#gemini-code-execution) | :octicons-x-circle-24:{ .red } No |

## User-configurable tools

### Calculator

Allows the bot to perform mathematical calculations reliably.

- Name: `calculator`
- Arguments:
    - `expression`: The mathematical expression to evaluate.

### Recurring reminders

Allows the bot to schedule recurring reminders for the participant.

- Name: `recurring-reminder`
- Arguments:
    - `datetime_due`: The first (or only) reminder start date in ISO 8601 format.
    - `every`: Number of 'periods' to wait between reminders.
    - `period`: The time period used in conjunction with `every`. One of `minutes`, `hours`, `days`, `weeks`, `months`.
    - `message`: The reminder message.
    - `schedule_name`: The name for this reminder.
    - `datetime_end`: The date of the last reminder in ISO 8601 format (optional).
    - `repetitions`: The number of messages to send before stopping (optional).

### One-off reminder

Allows the bot to schedule a once-off reminder for the participant.

- Name: `one-off-reminder`
- Arguments:
    - `datetime_due`: The datetime that the reminder is due in ISO 8601 format.
    - `message`: The reminder message.
    - `schedule_name`: The name for this reminder.

### Delete reminder

Allows the bot to delete an existing reminder (either once-off or recurring).

- Name: `delete-reminder`
- Arguments:
    - `message_id`: The ID of the scheduled message to delete.

### Move reminder date

Allows the bot to update the date or time of an existing reminder.

- Name: `move-scheduled-message-date`
- Arguments:
    - `message_id`: The ID of the scheduled message to update.
    - `weekday`: The new day of the week (1–7, where 1 = Monday).
    - `hour`: The new hour of the day, in UTC.
    - `minute`: The new minute of the hour.
    - `specified_date`: A specific date to reschedule the message for in ISO 8601 format.

### Update participant data

Allows the bot to write a value to [participant data](../concepts/participant_data.md) at a specific key.

- Name: `update-user-data`
- Arguments:
    - `key`: The key in the participant data to update.
    - `value`: The new value to store.

### Append to participant data

Appends a value to [participant data](../concepts/participant_data.md) at a specific key. Converts any existing value to a list and appends the new value to the end.

- Name: `append-to-participant-data`
- Arguments:
    - `key`: The key in the participant data to append to.
    - `value`: The value to append.

### Increment counter

Increments a numeric counter stored in [participant data](../concepts/participant_data.md). The counter is stored under the key `_counter_{counter_name}`.

- Name: `increment-counter`
- Arguments:
    - `counter`: The name of the counter to increment.
    - `value`: Integer value to increment the counter by (defaults to 1).

### Set session state key

Allows the bot to set a key-value pair in the [session state](../concepts/sessions.md). Session state persists for the duration of the session and is useful in pipeline configurations for passing data across conversation turns.

- Name: `set-session-state-key`
- Arguments:
    - `key`: The key in the session state to set.
    - `value`: The value to store at the specified key.

### Get session state key

Allows the bot to retrieve a value from the [session state](../concepts/sessions.md).

- Name: `get-session-state`
- Arguments:
    - `key`: The key in the session state to retrieve.

### Append to session state

Appends a value to [session state](../concepts/sessions.md) at a specific key. Converts any existing value to a list and appends the new value to the end.

- Name: `append-to-session-state`
- Arguments:
    - `key`: The key in the session state to append to.
    - `value`: The value to append.

### Increment session state counter

Increments a numeric counter stored in [session state](../concepts/sessions.md). The counter is stored under the key `_counter_{counter_name}`.

- Name: `increment-session-state-counter`
- Arguments:
    - `counter`: The name of the counter to increment.
    - `value`: Integer value to increment the counter by (defaults to 1).

### End session

Ends the current chat [session](../concepts/sessions.md). The session is marked as completed. New messages will start a fresh session. See [Session Status](../concepts/session_status.md) for how statuses transition after ending a session.

- Name: `end-session`
- Arguments: (none)

## Internal tools

The following tools are managed automatically by Open Chat Studio. You do not enable or configure them directly — OCS enables them when your chatbot's configuration requires them.

### Attach media

Allows the bot to attach media when a media collection is configured.

- Name: `attach-media`
- Arguments:
    - `file_id`: The ID of the media file to attach.

### File search

Allows the bot to search indexed collections when a collection is configured.

- Name: `file-search`
- Arguments:
    - `query`: A natural language query to search for relevant information in the documents.

See [Collections](../concepts/collections/index.md) for more information on configuring media and indexed collections.

## LLM provider tools

Some LLM providers offer their own built-in tools that run inside the provider's infrastructure.

### OpenAI tools

#### OpenAI Web Search

- Search the web and pass the results to the LLM.
- See [OpenAI Web Search documentation](https://platform.openai.com/docs/guides/tools-web-search)
- :material-check-circle-outline:{ .green } Supported by OCS

#### OpenAI Code Interpreter

- Execute code to analyse data, generate graphs, and more.
- See [OpenAI Code Interpreter documentation](https://platform.openai.com/docs/guides/tools-code-interpreter)
- :material-check-circle-outline:{ .green } Supported by OCS

### Anthropic tools

#### Anthropic Web Search

- Search the web and pass the results to the LLM.
- See [Anthropic Web Search documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)
- :material-check-circle-outline:{ .green } Supported by OCS

#### Anthropic Code Execution

- Execute code to analyse data, generate graphs, and more.
- See [Anthropic Code Execution documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)
- :octicons-x-circle-24:{ .red } Not supported by OCS

### Gemini tools

#### Gemini Grounding with Search

- Search the web and pass the results to the LLM.
- See [Gemini Grounding with Search documentation](https://ai.google.dev/gemini-api/docs/google-search)
- :octicons-x-circle-24:{ .red } Not supported by OCS

#### Gemini Code Execution

- Execute code to analyse data, generate graphs, and more.
- See [Gemini Code Execution documentation](https://ai.google.dev/gemini-api/docs/code-execution)
- :octicons-x-circle-24:{ .red } Not supported by OCS
