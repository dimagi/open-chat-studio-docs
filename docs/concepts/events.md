# Events

Open Chat Studio provides an event system that allows you to define actions triggered by specific events within a [chat session](sessions.md). This functionality enables you to automate responses, manage session states, and enhance participant interactions effectively.

## Overview

Events in Open Chat Studio are categorized into three types:

1. **Static Events**: Triggered by specific actions or occurrences within the chat session.
2. **Timeout Events**: Triggered after a specified duration of inactivity. By default, inactivity is measured from the last interaction, but you can configure a timeout to be measured from the first human message instead.
3. **Scheduled Events**: Triggered once at a specific date, time, and timezone that you configure, rather than in response to anything happening in a session.

Each event has one action associated with it that is executed when the event occurs.

## Static Events

Static events are predefined triggers that occur based on specific actions or conditions within the chat session. The available static events are:

- **Conversation End**: A catch-all trigger that fires whenever any conversation ends, regardless of how it ended. This trigger is always fired alongside any of the specific conversation end sub-triggers listed below. Use this trigger when you want to perform an action for all conversation endings, or use the sub-triggers when you need to respond to specific end conditions.
    - **The Conversation is Ended by the Participant**: Triggered when the participant explicitly ends the conversation.
    - **The Conversation is Ended by the Bot**: Triggered when the chatbot ends the conversation.
    - **The Conversation is Ended via the API**: Triggered when the conversation ends via an API call.
    - **The Conversation is Ended by an Event**: Triggered when the conversation ends due to an event.
    - **The Conversation is manually ended by an Admin**: Triggered when an admin manually ends the conversation.

    !!! note "How Sub-triggers Work"
        When a specific end condition occurs (e.g., participant ends conversation), both the specific sub-trigger AND the generic "Conversation End" trigger will fire. This allows you to create both targeted events (using sub-triggers) and catch-all events (using the generic trigger) that respond to any conversation ending.

- **Last Timeout**: Triggered when the last timeout of any configured timeout events occur.
- **Human Safety Layer Triggered**: Triggered when the safety layer is activated by a message from the participant.
- **Bot Safety Layer Triggered**: Triggered when the safety layer is activated by a response from the chatbot.
- **Conversation Start**: Triggered when a new conversation is started.
- **New Human Message**: Triggered when a new human message is received.
- **New Bot Message**: Triggered when a new bot message is received.
- **Participant Joined Chatbot**: Triggered when a participant starts interacting with the chatbot for the very first time.

## Timeout Events

Timeout events fire after a participant has been inactive for a duration you configure.
By default, inactivity is measured from the last message in the session.
You can configure a timeout event to measure from the first human message instead.

## Scheduled Events

Scheduled events fire once, at a specific real-world moment, rather than in response to anything happening in a session.
Use them for actions tied to a date rather than to conversation activity — for example, sending a message on a participant's appointment date.

To create one, open a chatbot's **Events** tab and select **Create Scheduled Event**.
Configure:

- **Trigger date and time**: the local date and time the event should fire.
- **Timezone**: chosen from the full IANA timezone list.

The form does not let you save a trigger date and time that has already passed.

!!! note "Daylight saving time"
    Open Chat Studio converts the date, time, and timezone you enter into UTC when you save the event.
    Daylight saving changes in the chosen timezone can shift how the saved UTC time lines up with local time when the event fires.
    A local time that is ambiguous during a "fall back" transition resolves to standard time.
    A local time that does not exist during a "spring forward" transition is moved forward to the next valid time.

A scheduled event fires only once, and cannot fire twice even if it is checked more than once around the trigger time.
Open Chat Studio checks for due scheduled events roughly every 60 seconds, so an event fires within about a minute of its configured time rather than to the exact second.
To repeat an action on a recurring schedule, use the **Trigger a schedule** action described below, rather than creating multiple scheduled events.

Like static and timeout events, a scheduled event only fires on a [published version](versioning.md) of a chatbot.
You can toggle it active or inactive, or archive it, from the **Events** tab.
When you publish a new chatbot version, its scheduled events are copied to that version, and each copy starts out as not yet fired.

A scheduled event acts on the chatbot's most recently created [session](sessions.md), not a session belonging to a specific participant.
If the chatbot has no session yet when the event fires, the failure is recorded in the event logs rather than raising an error.

## Event Actions

Each event is associated with one action. The available actions are:

- **End the conversation**: Ends the conversation with the participant. See [Ending session with events](../tech-hub/ending_sessions.md#events-with-an-end-the-conversation-action) for more details.
- **Prompt the bot to message the user**: Prompts the chatbot to message the participants.
- **Trigger a schedule**: This will create a once off or recurring schedule. Each time the schedule is triggered, the chatbot will be prompted to message the participant. This action is a way to schedule a *message*, and is separate from a **Scheduled Event** trigger, which schedules *when a trigger fires*.
- **Start a pipeline**: This will run the given pipeline when the event triggers. The input to the pipeline can be configured.

## Event Logs

Each time an event fires, whether its action succeeded or failed is recorded in that event's logs, viewable from the chatbot's **Events** tab.
Actions that support it can be re-triggered from the event logs, so a failed action can be retried without waiting for the event to fire again.
