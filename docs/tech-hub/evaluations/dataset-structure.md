# Dataset Structure Reference

This page is a field-level reference for evaluation dataset rows: what each field contains, how session data maps to dataset fields when cloning, and how to format CSV uploads.

For a conceptual overview of datasets and evaluation levels, see [Evaluation Datasets](../../concepts/evaluations/dataset.md). For step-by-step instructions on creating a dataset, see [Create a Dataset](../../how-to/evaluations/create-a-dataset.md).

## Dataset Fields

Each dataset row contains the following fields. Not all fields are populated for every evaluation level — see the [cloning field mappings](#cloning-field-mappings) below for details.

- **Input** (`input.content`): The human message or prompt (required for message-level rows)
- **Output** (`output.content`): The expected AI response (required for message-level rows)
- **Context** (`context`): Additional metadata and context variables that can be accessed individually in evaluators (e.g. `context.topic`, `context.current_datetime`) (optional)
- **History** (`history`): Previous conversation messages for context (optional)
- **Participant Data** (`participant_data`): Information about the participant that can be accessed during evaluation (optional)
- **Session State** (`session_state`): Session-specific state data that can be accessed during evaluation (optional)

## Cloning Field Mappings

### Message-level datasets

When cloning into a message-level dataset, session chat messages are paired into (human, AI) pairs and mapped to dataset fields as follows:

| Session Data | Dataset Field | Description |
|---|---|---|
| Human `message.content` | `input.content` | The human message text |
| AI `message.content` | `output.content` | The AI response text |
| `message.created_at` | `context.current_datetime` | Timestamp of the human message |
| `message.comments` | `context.comments` | Any comments attached to either message |
| `message.tags` | `context.tags` | Non-system tags from either message |
| Prior messages in the session | `history` | All preceding messages, each with `message_type`, `content`, and `summary` (an AI-generated condensation of the message, if available) |
| `trace.participant_data` | `participant_data` | Participant data captured at the time of the message |
| `trace.session_state` | `session_state` | Session state captured at the time of the message |

### Session-level datasets

When cloning into a session-level dataset, one row is created per session rather than one row per message pair. The full session transcript, captured at the time of the last AI message, carries the context the evaluator works from.

| Session Data | Dataset Field | Description |
|---|---|---|
| Session transcript | `full_history` | Full session transcript used by the evaluator |
| `message.created_at` | `context.current_datetime` | Timestamp of the last AI message |
| `trace.participant_data` | `participant_data` | Participant data at the time of the last message |
| `trace.session_state` | `session_state` | Session state at the time of the last message |

The `input` and `output` fields are empty for session-level rows. Evaluators working on session-level datasets use the `{full_history}` variable and session context variables rather than `{input.content}` or `{output.content}`.

!!! note
    Generation is not available for session-level datasets. Generation applies only to message-level evaluation.

## History Syntax

When adding history manually in the UI or as a column in a CSV, history must be a newline-separated list of messages, each prepended with either `user:` or `assistant:`. For example:

```text
user: Hello, how are you?
assistant: I am doing well, thank you for asking. How can I help you?
user: Please tell me the time.
assistant: It is currently 12:05 PM in Ankara.
```

## CSV Format

### Column naming

A CSV upload must include columns for the human message and AI response. You can also include `history`, `participant_data`, `session_state`, and `context` fields.

An example structure:

| Human Message | AI Response | Datetime | History | participant_data.name | session_state.count |
|---|---|---|---|---|---|
| What's the weather like? | I don't have access to weather data | 2024-03-15T10:30:00Z | user: Hello<br/>assistant: Hi there!<br/>user: How are you?<br/>assistant: I'm doing well! | John | 1 |
| Tell me a joke | Why don't scientists trust atoms? Because they make up everything! | 2024-03-15T10:32:00Z | user: What's the weather like?<br/>assistant: I don't have access to weather data | John | 2 |
| What is 2+2? | 2+2 equals 4 | 2024-03-15T10:35:00Z | | Jane | 1 |

### Dot-notation for nested fields

When including [participant_data](../../concepts/participant_data.md) or [session_state](../python_node.md#session-state) in your CSV, use dot notation to specify nested keys. For example:

- `participant_data.name` — sets the participant's name
- `participant_data.age` — sets the participant's age
- `session_state.counter` — sets a session state counter
- `context.foo` — sets the `foo` field in the context

You can also include complex JSON structures directly in these fields. For example, a column named `participant_data.tasks` can contain JSON such as `["Buy socks", "Feed the dog", "Clean the car"]`.

To supply participant data or session state as a single raw JSON object, use the keys `participant_data` and `session_state` without dot notation.

### Auto-generating history from the CSV

When uploading a CSV, you can populate the history column automatically from the preceding rows rather than providing a separate history column. This option assumes the CSV represents the transcript of a single conversation in chronological order, and constructs the history for each row from all earlier rows in the file.
