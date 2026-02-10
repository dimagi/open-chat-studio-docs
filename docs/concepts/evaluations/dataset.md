# Evaluation Datasets

**Datasets** are collections of messages that serve as the foundation for running evaluations.

Each dataset contains messages with the following structure:

- **Input**: The human message or prompt (required)
- **Output**: The expected AI response (required)
- **Context**: Additional metadata and context variables that can later be accessed in the evaluators (optional)
- **History**: Previous conversation messages for context (optional)
- **Participant Data**: Information about the participant that can be accessed during evaluation (optional)
- **Session State**: Session-specific state data that can be accessed during evaluation (optional)

## Managing Datasets

Datasets can be created by cloning an existing session, manually created in the UI, or uploaded with a CSV.

### Cloning a session

When cloning a session, dataset messages are created automatically from messages from past conversations, including chat history and metadata. Selecting multiple sessions from the list will clone all the message from those sessions. Selecting "filtered messages" will only clone the messages that match the filter parameters. Selecting "All messages" will clone all the messages in that session.

Messages that are cloned from a session will be "connected" to their actual message in OCS, and you will be able to follow links back to their original conversation when viewing the output of an evaluator. However, modifying or updating a cloned message will break this link.

### Manually creating a dataset

Messages can be manually added in the UI. You must enter a Human Message, an AI response, and optionally the history for this message and any context.

History must be entered as a new-line separated list of messages prepended with either `user:` or `assistant:`. For example:


```
user: Hello, how are you?
assistant: I am doing well, thank you for asking. How can I help you?
user: Please tell me the time.
assistant: It is currently 12:05 PM in Ankara.
```

## Sharing Dataset Messages

When viewing dataset messages in the table, each row includes a link button that allows you to share a direct link to that specific message. When someone follows this link, the page automatically scrolls to the message and highlights it for easy identification.

This feature is useful for collaborating with team members, referencing specific test cases in discussions, or documenting particular dataset examples. Simply click the link icon next to any message, and the URL will be copied to your clipboard with the message ID parameter included.

### CSV Upload

A CSV can also be uploaded to populate the dataset. There should be columns for human messages, ai responses, and any context data. You can also include `participant_data` and `session_state` fields.

An example structure for this csv might be:

| Human Message | AI Response | Datetime | History | participant_data.name | session_state.count |
|---------------|-------------|----------|---------|------------------------|---------------------|
| What's the weather like? | I don't have access to weather data | 2024-03-15T10:30:00Z | user: Hello<br/>assistant: Hi there!<br/>user: How are you?<br/>assistant: I'm doing well! | John | 1 |
| Tell me a joke | Why don't scientists trust atoms? Because they make up everything! | 2024-03-15T10:32:00Z | user: What's the weather like?<br/>assistant: I don't have access to weather data | John | 2 |
| What is 2+2? | 2+2 equals 4 | 2024-03-15T10:35:00Z | | Jane | 1 |

#### Participant Data and Session State

When including [participant_data](../participant_data.md) or [session_state](../pipelines/python_node.md#session-state) in your CSV, you can use dot notation to specify nested keys. For example:

- `participant_data.name` - Sets the participant's name
- `participant_data.age` - Sets the participant's age
- `session_state.counter` - Sets a session state counter
- `context.foo` - Sets the `foo` field in the context

You can also include complex JSON structures directly in these fields. For example, if you have a column named `participant_data.tasks` you can include JSON data like `["Buy socks", "Feed the dog", "Clean the car"]`.

You can also specify participant data and session state as raw JSON objects by using the keys `participant_data` and `session_state` (without dot notation).

#### CSV History

When uploading a CSV, you can populate the history automatically from previous messages, or add it as a separate column.

Adding the history automatically assumes the CSV is the transcript of a single conversation, in chronological order.
