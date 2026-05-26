# Tools

Tools let your chatbot take real actions during a conversation — not just respond with text. When a tool is enabled, the LLM can decide to use it at the right moment, and Open Chat Studio executes the tool on the LLM model's behalf.

For example, a chatbot with the Calculator tool can perform accurate arithmetic. A chatbot with reminder tools can schedule a message to be sent to the participant at a future time. Without tools, a chatbot can only generate text.

!!! tip

    You choose which tools to enable for each chatbot. Only enable tools that match what your chatbot needs to do — this keeps the chatbot focused and reduces the chance of unintended actions.

## Calling a tool in a prompt

Once a tool is enabled, the AI will use it when it judges it to be appropriate. You can also guide it explicitly by referring to the tool by name in your system prompt. For example:

> When the participant asks to be reminded about something, use the `recurring-reminder` tool to schedule it.

Each tool name below links to its full argument details in the [Tools Reference](../../tech-hub/tools.md).

Tools in Open Chat Studio fall into two categories:

- **[User-configurable tools](#user-configurable-tools)** — tools you enable on each chatbot
- **[LLM provider tools](#llm-provider-tools)** — tools provided by AI models that are available for OCS chatbots to use

## User-configurable tools

These tools appear in your chatbot's node settings. Enable only the ones your chatbot needs.

### Reminders

Schedule messages to be delivered to participants at a future time — even after the conversation has ended. See [Schedule Reminders](../../how-to/reminders.md) for a step-by-step guide.

- **[Recurring reminders](../../tech-hub/tools.md#recurring-reminders)** — Schedules a repeating reminder for the participant — for example, a daily check-in message. You can set the start date, frequency, and an optional end date or maximum number of repetitions.
- **[One-off reminder](../../tech-hub/tools.md#one-off-reminder)** — Schedules a single reminder message to be sent to the participant at a specific future date and time.
- **[Delete reminder](../../tech-hub/tools.md#delete-reminder)** — Cancels an existing reminder (either a one-off or a recurring one). Use this when your chatbot should let participants cancel scheduled messages.
- **[Move reminder date](../../tech-hub/tools.md#move-reminder-date)** — Changes the date or time of an existing reminder. Use this to let participants reschedule a reminder without deleting and recreating it.

### Participant data

Store and update information about a participant that persists across sessions. See [Participant Data](../participant_data.md) for more information.

- **[Update participant data](../../tech-hub/tools.md#update-participant-data)** — Writes a value to a participant's stored data under a specific key. Use this when the chatbot should remember something about the participant across sessions, such as a preference or a recorded response.
- **[Append to participant data](../../tech-hub/tools.md#append-to-participant-data)** — Adds a value to participant data at a specific key. Use this to track multiple items over time — for example, a list of topics a participant has mentioned.
- **[Increment counter](../../tech-hub/tools.md#increment-counter)** — Increments a numeric counter stored in participant data. Use this to track how many times something has happened across sessions — for example, how many check-ins a participant has completed.

### Session

Read and write data within the current session, or manage the session lifecycle. Data stored here is available only for the duration of the session. See [Sessions](../sessions.md) for more information.

- **[Set session state key](../../tech-hub/tools.md#set-session-state-key)** — Stores a key-value pair in the session state, which persists for the duration of the current session. Useful in pipeline configurations where one part of the conversation needs to pass information to another.
- **[Get session state key](../../tech-hub/tools.md#get-session-state-key)** — Retrieves a value previously stored in session state during the current session.
- **[Append to session state](../../tech-hub/tools.md#append-to-session-state)** — Adds a value to a list in the session state. Use this to track items within a single session — for example, a list of topics discussed so far.
- **[Increment session state counter](../../tech-hub/tools.md#increment-session-state-counter)** — Increments a numeric counter stored in session state. Use this to count events within a single session.
- **[End session](../../tech-hub/tools.md#end-session)** — Marks the current session as complete. After this, any new message from the participant will begin a fresh session. Use this when the chatbot should formally close a conversation — for example, after a survey is complete. See [Session Status](../session_status.md) for status transitions.

### Utilities

- **[Calculator](../../tech-hub/tools.md#calculator)** — Performs reliable mathematical calculations. Use this when your chatbot needs to compute values accurately rather than relying on the language model's estimation.


## LLM provider tools

Some LLM providers offer their own built-in tools — such as web search or code execution — that run inside the provider's infrastructure. Open Chat Studio can connect to some of these where the provider supports it.

Support varies by provider. The full list of provider tools and their current support status is in the [Tools Reference](../../tech-hub/tools.md#llm-provider-tools).

## OCS Internal tools

Open Chat Studio also manages a small set of internal tools automatically - `Attach media` and `File Search`. See the [Tools Reference](../../tech-hub/tools.md#internal-tools) for details.

## Next steps

- To see full argument details for each user-configurable tool, see the [Tools Reference](../../tech-hub/tools.md).
- To add your own tools in the form of custom integrations, see [Custom Actions](../llm_custom_action.md).
