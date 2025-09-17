# Evaluation Datasets

**Datasets** are collections of messages that serve as the foundation for running evaluations.

Each dataset contains messages with the following structure:

- **Input**: The human message or prompt (required)
- **Output**: The expected AI response (required)
- **Context**: Additional metadata and context variables that can later be accessed in the evaluators (optional)
- **History**: Previous conversation messages for context (optional)

## Managing Datasets

Datasets can be created by cloning an existing session, manually created in the UI, or uploaded with a CSV.

### Cloning a session

When cloning a session, dataset messages are created automatically from messages from past conversations, including chat history and metadata. Selecting multiple sessions from the list will clone all the message from those sessions.

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

### CSV Upload

A CSV can also be uploaded to populate the dataset. There should be columns for human messages, ai responses, and any context data.

An example structure for this csv might be:

| Human Message | AI Response | Datetime | History |
|---------------|-------------|----------|---------|
| What's the weather like? | I don't have access to weather data | 2024-03-15T10:30:00Z | user: Hello<br/>assistant: Hi there!<br/>user: How are you?<br/>assistant: I'm doing well! |
| Tell me a joke | Why don't scientists trust atoms? Because they make up everything! | 2024-03-15T10:32:00Z | user: What's the weather like?<br/>assistant: I don't have access to weather data |
| What is 2+2? | 2+2 equals 4 | 2024-03-15T10:35:00Z | |

#### CSV History

When uploading a CSV, you can populate the history automatically from previous messages, or add it as a separate column.

Adding the history automatically assumes the CSV is the transcript of a single conversation, in chronological order.
