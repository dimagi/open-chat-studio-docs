# Ending Sessions from a Chatbot

This page is a technical reference for the ways a chatbot can end a [chat session](../concepts/sessions.md) programmatically. For how this fits into the overall session lifecycle, see [Session Status](../concepts/session_status.md).

You have three ways to end a session programmatically from within your chatbot. All three behave identically once triggered — the session moves to `PENDING_REVIEW`, the end time is recorded, and any configured conversation-end [events](../concepts/events.md) fire.

## The End Session tool

Add the **End Session** tool to your LLM node's tool list. The LLM can then choose to end the chat when it judges the conversation is over.

The tool description presented to the LLM is: *"End the current chat session. This will mark the session as completed. New messages will result in a new session being created."*

In that description, "completed" means the conversation is finished — the session moves to `PENDING_REVIEW`. It does not move directly to the `COMPLETE` status, which only happens once the participant submits the post-conversation review.

The session ends after the chatbot's reply is delivered to the participant.

For full configuration details, see the [End Session tool reference](tools.md#end-session).

!!! warning "Not available for Assistant-style chatbots"
    The End Session tool cannot be used with Assistant-style chatbots.

Use this approach when the decision to end the conversation belongs to the LLM — for example, "end the session once the user confirms they are done".

## The `end_session()` helper in a Python node

Inside a [Python pipeline node](python_node.md), the runtime exposes an `end_session()` helper:

```python
def main(input, **kwargs):
    if should_finish(input):
        end_session()
    return "Goodbye!"
```

Calling `end_session()` ends the session after the pipeline finishes and the response is delivered. The returned message is still sent to the participant first.

Use this approach when the decision to end the conversation belongs to your custom logic — for example, a state-machine progression or a specific sentinel input from the participant.

## Events with an "End the conversation" action

Configure an [event](../concepts/events.md) whose action is **End the conversation**:

- **Static triggers** — fire on a lifecycle event such as a new chatbot message, a participant joining, or a conversation starting. Useful when you want the session to end as soon as the chatbot sends a specific goodbye message.
- **Timeout triggers** — fire after a period of inactivity. Useful for "end the session if the participant is silent for 30 minutes".

Use this approach when the decision to end the conversation should be driven by lifecycle conditions outside the pipeline itself.
