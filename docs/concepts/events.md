# Events

Open Chat Studio provides an event system that allows you to define actions triggered by specific events within a chat session. This functionality enables you to automate responses, manage session states, and enhance user interactions effectively.

## Overview

Events in Open Chat Studio are categorized into two types:

1. **Static Events**: Triggered by specific actions or occurrences within the chat session.
2. **Timeout Events**: Triggered after a specified duration of inactivity following the last interaction.

Each event has one action associated with it that is executed when the event occurs.

## Static Events

Static events are predefined triggers that occur based on specific actions or conditions within the chat session. The available static events are:

- **Conversation End**: Triggered when the conversation ends.
- **Last Timeout**: Triggered when the last timeout of any configured timeout events occur.
- **Human Safety Layer Triggered**: Triggered when the safety layer is activated by a message from the user.
- **Bot Safety Layer Triggered**: Triggered when the safety layer is activated by a response from the bot.
- **Conversation Start**: Triggered when a new conversation is started.
- **New Human Message**: Triggered when a new human message is received.
- **New Bot Message**: Triggered when a new bot message is received.
- **Participant Joined Experiment**: Triggered when a participant first starts interacting with the bot.

## Event Actions

Each event is associated with one action. The available actions are:

- **End the conversation**: Ends the conversation with the user. See [Resetting Sessions](sessions.md#resetting-sessions).
- **Prompt the bot to message the user**: Prompts the bot to message the user.
- **Trigger a schedule**: This will create a once off or recurring schedule. Each time the schedule is triggered, the bot will be prompted to message the user.
- **Start a pipeline**: This will run the given pipeline when the event triggers. The input to the pipeline can be configured.
