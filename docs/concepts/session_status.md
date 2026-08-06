# Session Status

Every [chat session](sessions.md) in Open Chat Studio has a **status** that reflects where the participant is in their journey — from first contact through to a completed, reviewed conversation.

Understanding session status helps you:

- Predict how participants will move through your chatbot's flow.
- Choose the right method to end a session from within the chatbot.
- Interpret session lists, exports, and reports correctly.

## The statuses

| Status | Label | What it means |
|--------|-------|---------------|
| `SETUP` | Setting Up | A session has been created but the participant has not yet been contacted or arrived. This is the default starting point for every session. |
| `PENDING` | Awaiting Participant | The participant has been invited (for example, by email) or prompted for consent, but has not yet agreed to start. |
| `ACTIVE` | Active | The conversation is in progress. |
| `PENDING_REVIEW` | Awaiting Final Review | The conversation has ended and is waiting for the participant to submit the post-conversation review or for an admin to review the session. |
| `COMPLETE` | Complete | The session is fully finished. No further activity is expected. |
| `UNKNOWN` | Unknown | A safety fallback for sessions in unexpected states. Sessions are never deliberately placed here. |

## How sessions move through statuses

Sessions flow through statuses automatically. The path depends on how the participant arrived and what features are configured for your chatbot.

### Web invitation flow

Used when participants arrive via an invitation link or public web chat link. The path differs depending on whether the participant was invited by email or arrived via a public link.

**Invitation email flow** — the session is created in `SETUP`, the email is sent, and the participant accepts consent on the invitation page:

```mermaid
stateDiagram-v2
    [*] --> SETUP
    SETUP --> PENDING: invitation email sent
    PENDING --> ACTIVE: consent accepted
    ACTIVE --> PENDING_REVIEW: session ended
    PENDING_REVIEW --> COMPLETE: review submitted
    COMPLETE --> [*]
```

**Public link flow** — the session is created and immediately moves out of `SETUP` as the participant accepts consent on arrival:

```mermaid
stateDiagram-v2
    [*] --> SETUP
    SETUP --> ACTIVE: consent accepted
    ACTIVE --> PENDING_REVIEW: session ended
    PENDING_REVIEW --> COMPLETE: review submitted
    COMPLETE --> [*]
```

### Messaging channel flow

Used for [channels](channels.md) such as Telegram, WhatsApp, the web widget, and the API.

- **If [conversational consent](consent.md) is disabled** (the common case): the session is created directly in `ACTIVE`. The early statuses are skipped entirely.
- **If conversational consent is enabled**: the chatbot walks the participant through a chat-driven consent flow, traversing `SETUP → PENDING → ACTIVE`.

!!! note
    Messaging channel sessions do not typically reach `PENDING_REVIEW` or `COMPLETE` on their own. Those terminal statuses are driven by the post-conversation review form or an explicit end-conversation action.

## Reaching the terminal statuses

### PENDING_REVIEW

A session moves to `PENDING_REVIEW` whenever the conversation ends. This can happen in several ways.

**Participant actions:**

- Clicks **End chat and give feedback** on the OCS hosted web chat page.
- Sends `/reset` on a messaging channel (also surfaced as "Restart chat" on Telegram).

**Chatbot-driven actions** — the chatbot itself ends the session, using one of three methods described in [Ending sessions from a chatbot](../tech-hub/ending_sessions.md):

- The LLM calls the [End Session tool](../tech-hub/ending_sessions.md#the-end-session-tool).
- A Python pipeline node calls [`end_session()`](../tech-hub/ending_sessions.md#the-end_session-helper-in-a-python-node).
- An [event](events.md) fires with an [End the conversation action](../tech-hub/ending_sessions.md#events-with-an-end-the-conversation-action).

**Team member actions:**

- Clicks **End Session** button on a Chatbot Review session detail page in the OCS admin.
- Clicks **New Session** button on a messaging channel session (ie non-web channels), which ends the old session as a side effect.

**API:**

- An integrator calls the public end session endpoint.

### COMPLETE

There is exactly one path to `COMPLETE`: the participant is redirected to the review page after the chat ends, and they submit the review form. If the participant closes the browser without submitting, the session remains in `PENDING_REVIEW` indefinitely.

### UNKNOWN

No deliberate action places a session in `UNKNOWN`. It exists as a defensive fallback. If you see sessions landing here, this indicates an unexpected state — worth investigating rather than ignoring.

## Observing how a session ended

Regardless of what ends a session — participant, chatbot, admin, API caller, or event — you can attach further actions to the conversation-end event using static triggers. This lets you respond differently depending on who or what ended the conversation.

| Trigger type | Fires when |
|--------------|------------|
| The Conversation is Ended by the Participant | The participant ends the chat (web "End chat and give feedback" or `/reset`). |
| The Conversation is Ended by the Bot | The chatbot ends the chat (End Session tool or `end_session()`). |
| The Conversation is Ended via the API | An API caller ends the session. |
| The Conversation is Ended by an Event | An "End the conversation" event action ended the session. |
| The Conversation is Manually Ended by an Admin | A team member ended the session via the OCS admin. |

The generic **Conversation End** trigger fires for all of the above. Use it when you want to take the same action regardless of how the session ended. See [Events](events.md) for more detail.

## Status and reporting

Three statuses are treated as "this chat is over" for the purposes of filtering, exports, and reports:

- `PENDING_REVIEW`
- `COMPLETE`
- `UNKNOWN`

`UNKNOWN` is included here because sessions in this state will not progress further — they have left the normal flow and should not be treated as in-progress conversations. Only `COMPLETE` is considered fully done — meaning the participant has submitted the post-conversation review.

## Things to keep in mind

- **Status is managed automatically.** OCS transitions sessions through the flow. You do not need to set it manually.
- **Channel sessions usually start in ACTIVE.** If you are wondering why a session is already active before any interaction, check whether [conversational consent](consent.md) is enabled on your chatbot.
- **UNKNOWN is a fallback, not a destination.** If sessions are landing in `UNKNOWN`, something unexpected has occurred. Investigate rather than treating it as a normal terminal state.
