# Tools

Tools let your chatbot take real actions during a conversation — not just respond with text. When a tool is enabled, the LLM can decide to use it at the right moment, and Open Chat Studio executes it on the LLM model's behalf.

For example, a chatbot with the Calculator tool can perform accurate arithmetic. A chatbot with reminder tools can schedule a message to be sent to the participant at a future time. Without tools, a chatbot can only generate text.

!!! tip

    You choose which tools to enable for each chatbot. Only enable tools that match what your chatbot needs to do — this keeps the chatbot focused and reduces the chance of unintended actions.

Tools in Open Chat Studio fall into three categories:

- **[User-configurable tools](#user-configurable-tools)** — tools you enable on each chatbot
- **[Internal tools](#internal-tools)** — tools OCS enables automatically based on your chatbot's configuration
- **[LLM provider tools](#llm-provider-tools)** — tools provided by LLM that OCS chatbots can use

## User-configurable tools

These tools appear in your chatbot's node settings. Enable only the ones your chatbot needs.

### Calculator

Performs reliable mathematical calculations. Use this when your chatbot needs to compute values accurately rather than relying on the language model's estimation.

### Recurring reminders

Schedules a repeating reminder for the participant — for example, a daily check-in message. You can set the start date, frequency, and an optional end date or maximum number of repetitions.

### One-off reminder

Schedules a single reminder message to be sent to the participant at a specific future date and time.

### Delete reminder

Cancels an existing reminder (either a one-off or a recurring one). Use this when your chatbot should let participants cancel scheduled messages.

### Move reminder date

Changes the date or time of an existing reminder. Use this to let participants reschedule a reminder without deleting and recreating it.

### Update participant data

Writes a value to a participant's stored data under a specific key. Use this when the chatbot should remember something about the participant across sessions, such as a preference or a recorded response.

See [Participant Data](../participant_data.md) for more information.

### Append to participant data

Adds a value to participant data at a specific key. If the key does not yet exist, it is created as a list. Use this to track multiple items over time — for example, a list of topics a participant has mentioned.

See [Participant Data](../participant_data.md) for more information.

### Increment counter

Increments a numeric counter stored in participant data. Use this to track how many times something has happened across sessions — for example, how many check-ins a participant has completed.

See [Participant Data](../participant_data.md) for more information.

### Set session state key

Stores a key-value pair in the session state, which persists for the duration of the current session. Useful in pipeline configurations where one part of the conversation needs to pass information to another.

### Get session state key

Retrieves a value previously stored in session state during the current session.

### Append to session state

Adds a value to a list in the session state at a specific key. Use this to track items within a single session — for example, a list of topics discussed so far.

See [Sessions](../sessions.md) for more information.

### Increment session state counter

Increments a numeric counter stored in session state. Use this to count events within a single session.

### End session

Marks the current session as complete. After this, any new message from the participant will begin a fresh session. Use this when the chatbot should formally close a conversation — for example, after a survey is complete.

See [Sessions](../sessions.md) for more information.

## Internal tools

The following tools are managed automatically by Open Chat Studio. You do not enable or configure them directly — OCS enables them when your chatbot's configuration requires them.

**Attach media** is enabled when your chatbot has a media collection configured. It allows the chatbot to attach files from that collection to a response.

**File search** is enabled when your chatbot has an indexed collection configured. It allows the chatbot to search indexed documents and include relevant information in its response.

See [Collections](../../concepts/collections/index.md) for more information on configuring media and indexed collections.

## LLM provider tools

Some LLM providers offer their own built-in tools — such as web search or code execution — that run inside the provider's infrastructure. Open Chat Studio can connect to some of these where the provider supports it.

Support varies by provider. The full list of provider tools and their current support status is in the [Tools Reference](../../tech-hub/tools.md#llm-provider-tools).

## Next steps

- To see full argument details for each user-configurable tool, see the [Tools Reference](../../tech-hub/tools.md).
- To add your own tools in the form of custom integrations, see [Custom Actions](../llm_custom_action.md).
