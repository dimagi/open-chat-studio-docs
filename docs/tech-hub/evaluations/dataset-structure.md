# Dataset Structure Reference

This page is a field-level reference for evaluation dataset rows: what each field contains, how session data maps to dataset fields when [cloning](#cloning-field-mappings), and how to [format CSV uploads](#csv-format).

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

When cloning into a message-level dataset, or importing from an annotation queue into one, session chat messages are paired into (human, AI) pairs and mapped to dataset fields as follows:

| Session Data | Dataset Field | Description |
|---|---|---|
| Human `message.content` | `input.content` | The human message text |
| AI `message.content` | `output.content` | The AI response text |
| `message.created_at` | `context.current_datetime` | Timestamp of the human message |
| `message.comments` | `context.comments` | Any comments attached to either message |
| `message.tags` | `context.tags` | Non-system tags from either message |
| Prior messages in the session | `history` | All preceding messages, each with `message_type`, `content`, and `summary` (an AI-generated condensation of the message, if available) |
| `trace.participant_data` | `participant_data` | Participant data from the human message's trace, or empty if it has none |
| `trace.session_state` | `session_state` | Session state from the human message's trace, or empty if it has none |

Messages without a partner still become rows. A human message with no reply, for example, because generation failed, becomes a row with an empty AI response. An AI message with no preceding human message, such as a scheduled message or a seed message, becomes a row with an empty human message.
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

### Formula characters in exports and uploads

Spreadsheet applications such as Excel and Google Sheets treat a cell that starts with `=`, `+`, `-`, `@`, a tab, or a carriage return as a formula.
To prevent this, CSV downloads of datasets and evaluation results prefix any such cell with an apostrophe (`'`).
Results downloads also apply this to header cells, because evaluator field names and context keys are user-defined.

On upload, one leading apostrophe is removed from any cell whose remainder starts with one of those characters.
For dataset uploads (create from CSV, and update), this covers input, output, history, context, participant data, and session state values.
For results uploads, it covers the mapped evaluator columns and their column names.
A download followed by an upload therefore leaves the data unchanged.
A stored value that already starts with an apostrophe, such as `'=x`, is exported as `''=x` and restored to `'=x`.

The restore runs on every upload, not only on re-uploads of exported files.
In a CSV you create yourself, `'-5` is stored as `-5`, and `''=x` is stored as `'=x`.

This applies to CSV only.
JSON and HTML exports are unchanged.

## See also

- [Evaluation Datasets](../../concepts/evaluations/dataset.md): evaluation levels and how datasets are created.
- [Create a Dataset](../../how-to/evaluations/create-a-dataset.md): step-by-step instructions for each creation method.
- [Evaluator Reference](evaluator-reference.md): template variables that read these dataset fields.
