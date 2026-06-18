# Evaluation Datasets

Every evaluation needs example conversations to test against — that's what a **dataset** provides. A dataset is the set of messages or sessions you want to score.

Dataset quality matters more than dataset size: a small, well-chosen set of realistic examples tells you more about how your chatbot behaves than scoring everything that happens to exist.

You can build a dataset from real conversations your chatbot has already had, or write your own test cases to check specific behaviors — including edge cases your chatbot hasn't encountered yet.

## Evaluation Levels

When creating a dataset, you choose an **Evaluation level** that determines how the dataset is structured and which evaluators are compatible with it.

| Level | Description | When to use |
|---|---|---|
| **Message level** | Each row represents a single Human/AI message pair | Judging individual responses for accuracy, tone, or correctness |
| **Session level** | Each row represents an entire conversation | Judging overall conversation quality, goal completion, or coherence across turns |

The evaluation level is set at dataset creation and cannot be changed later. Evaluators must share the same evaluation level as the dataset — incompatible evaluators are automatically disabled when configuring an evaluation run.

## Dataset Structure

Each dataset row contains the following fields. Not all fields are populated for every evaluation level — see the sections below for details.

- **Input** (`input.content`): The human message or prompt (required)
- **Output** (`output.content`): The expected AI response (required)
- **Context** (`context`): Additional metadata and context variables that can be accessed individually in evaluators (e.g. `context.topic`, `context.current_datetime`) (optional)
- **History** (`history`): Previous conversation messages for context (optional)
- **Participant Data** (`participant_data`): Information about the participant that can be accessed during evaluation (optional)
- **Session State** (`session_state`): Session-specific state data that can be accessed during evaluation (optional)

## Managing Datasets

Datasets can be created by cloning an existing session, manually created in the UI, uploaded with a CSV, or — for session-level datasets — auto-populated continuously from a source chatbot via [auto-population rules](../../tech-hub/evaluations/auto_population.md).

!!! note
    Manual creation and CSV upload are only available for **message-level** datasets. Session-level datasets must be populated by cloning sessions, by configuring an auto-population rule, or by importing sessions from an annotation queue.

### Cloning a session

#### Message-level datasets

When cloning a message-level session, dataset rows are created automatically from past conversations. Session chat messages are paired into (human, AI) pairs and mapped to dataset message fields as follows:

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

When selecting messages to clone, you have three options:

- **Multiple sessions** — clones all messages from each selected session(s).
- **Filtered messages** — clones only the messages that match the active filter parameters.
- **All messages** — clones every message in the session.

Messages that are cloned from a session will be "connected" to their actual message in OCS, and you will be able to follow links back to their original conversation when viewing the output of an evaluator. However, modifying or updating a cloned message will break this link.

Because cloned messages retain this session connection, the sessions they belong to can be imported into an annotation queue for human review. Only dataset entries with a linked session are eligible for this import — messages added manually or via CSV upload do not have a session link and cannot be imported into an annotation queue.

#### Session-level datasets

When cloning into a **session-level** dataset, one row is created per session rather than one row per message pair. The full session transcript, captured at the time of the last AI message, carries the context the evaluator works from.

| Session Data | Dataset Field | Description |
|---|---|---|
| Session transcript | `full_history` | Full session transcript used by the evaluator |
| `message.created_at` | `context.current_datetime` | Timestamp of the last AI message |
| `trace.participant_data` | `participant_data` | Participant data at the time of the last message |
| `trace.session_state` | `session_state` | Session state at the time of the last message |

The `input` and `output` fields are empty for session-level rows. Evaluators working on session-level datasets use the `{full_history}` variable and session context variables rather than `{input.content}` or `{output.content}`.

!!! note
    Generation is not available for session-level datasets. Generation applies only to message-level evaluation.

### Importing from an annotation queue

Session-level datasets can also be populated from an existing [annotation queue](../annotations/queues.md). From the dataset edit page, click **Import from Annotation Queue** and select any team queue that contains session items (archived queues are excluded). Each session item in the queue becomes a row in the dataset using the same mapping as session cloning.

Imports are idempotent — sessions already present in the dataset are skipped, so re-running the import after adding new items to the queue will only append the new sessions.

!!! note
    This option is only available on session-level datasets.

### Manually creating a dataset

Messages can be manually added in the UI. You must enter a Human Message, an AI response, and optionally the history for this message and any context.

History must be entered as a new-line separated list of messages prepended with either `user:` or `assistant:`. For example:

```
user: Hello, how are you?
assistant: I am doing well, thank you for asking. How can I help you?
user: Please tell me the time.
assistant: It is currently 12:05 PM in Ankara.
```

### CSV Upload

A CSV can also be uploaded to populate the dataset. There should be columns for human messages, ai responses, and any context data. You can also include `participant_data` and `session_state` fields.

An example structure for this csv might be:

| Human Message | AI Response | Datetime | History | participant_data.name | session_state.count |
|---------------|-------------|----------|---------|------------------------|---------------------|
| What's the weather like? | I don't have access to weather data | 2024-03-15T10:30:00Z | user: Hello<br/>assistant: Hi there!<br/>user: How are you?<br/>assistant: I'm doing well! | John | 1 |
| Tell me a joke | Why don't scientists trust atoms? Because they make up everything! | 2024-03-15T10:32:00Z | user: What's the weather like?<br/>assistant: I don't have access to weather data | John | 2 |
| What is 2+2? | 2+2 equals 4 | 2024-03-15T10:35:00Z | | Jane | 1 |

#### Participant Data and Session State

When including [participant_data](../participant_data.md) or [session_state](../../tech-hub/python_node.md#session-state) in your CSV, you can use dot notation to specify nested keys. For example:

- `participant_data.name` - Sets the participant's name
- `participant_data.age` - Sets the participant's age
- `session_state.counter` - Sets a session state counter
- `context.foo` - Sets the `foo` field in the context

You can also include complex JSON structures directly in these fields. For example, if you have a column named `participant_data.tasks` you can include JSON data like `["Buy socks", "Feed the dog", "Clean the car"]`.

You can also specify participant data and session state as raw JSON objects by using the keys `participant_data` and `session_state` (without dot notation).

#### CSV History

When uploading a CSV, you can populate the history automatically from previous messages, or add it as a separate column.

Adding the history automatically assumes the CSV is the transcript of a single conversation, in chronological order.

## Auto-Population

Session-level datasets can be continuously and automatically populated with new sessions from a live chatbot, instead of being created manually or from a one-off import. See [Auto-Population Rules](../../tech-hub/evaluations/auto_population.md) for how to configure rules and how ingestion works.

## Sharing Dataset Messages

When viewing dataset messages in the table, each row includes a link button that allows you to share a direct link to that specific message. When someone follows this link, the page automatically scrolls to the message and highlights it for easy identification.

This feature is useful for collaborating with team members, referencing specific test cases in discussions, or documenting particular dataset examples. Simply click the link icon next to any message, and the URL will be copied to your clipboard with the message ID parameter included.
