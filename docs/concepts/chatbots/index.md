# Chatbots

A chatbot in Open Chat Studio is the chatbot configuration that participants interact with.
It defines the conversational experience, while the underlying [pipeline](../pipelines/index.md) controls how messages are processed and responses are generated.

Chatbots can connect to one or more [channels](../channels.md) and use [LLMs](../llm.md) to generate responses.
They can also include supporting logic such as [routing](../pipelines/router_nodes.md), [participant data](../participant_data.md), or [custom actions](../llm_custom_action.md).

## Creating a Chatbot
Every chatbot in Open Chat Studio is configured using a visual workflow called a [**Pipeline**](../pipelines/index.md).

Use the resources below to learn how to create a chatbot and how its pipeline works:

- :material-clock-fast:{ .lg .middle } [__Quickstart Guide__](../../tutorials/first_chatbot.md)
- :material-chat-question:{ .lg .middle } [__What is a Pipeline?__](../pipelines/index.md#what-is-a-pipeline)
- :material-whatsapp:{ .lg .middle } [__Deploying your chatbot__](../../how-to/channels/deploy_to_different_channels.md)

## Chatbot settings

Each chatbot has a **Settings** tab with options that apply to the whole chatbot.
These are separate from the settings on individual [pipeline nodes](../pipelines/nodes.md).
Settings changes reach participants on the published chatbot after you [publish a new version](../versioning.md).
For step-by-step instructions, see [Configure Chatbot Settings](../../how-to/configure_chatbot_settings.md).

### Speech

Speech settings let the chatbot reply with voice messages on channels that support voice.

- **Provider** is the team's [speech provider](../team/speech_providers.md) used to create audio.
- **Synthetic Voice** is the voice used for replies, chosen from the selected provider's voices.
- **Response Type** controls when the chatbot replies with voice: always, never, or only when the participant sends a voice note (**Reciprocal**).
- **Echo Transcript** sends the participant the text transcribed from their voice note.

See [Set up voice replies](../../how-to/configure_chatbot_settings.md#set-up-voice-replies).

### Tracing

**Trace Provider** sends the chatbot's traces to an external service such as Langfuse.
**Sample Rate** sets the fraction of conversation turns sent to that provider.
See [Tracing](../tracing.md) and [Configure Langfuse Trace Sampling](../../how-to/configure_langfuse_trace_sampling.md).

### Consent

**Conversational Consent** asks for consent inside the chat.
Turn it on for channels other than web chat, such as WhatsApp or Telegram.
**Consent Form** is the form shown to participants before they chat.
See [Consent Forms](../consent.md).

### Seed message

A seed message is sent to the chatbot when a new web chat session starts, so the chatbot speaks first.
See [Set a seed message](../../how-to/configure_chatbot_settings.md#set-a-seed-message).

### Unavailable message

The unavailable message is sent after the default error reply when the chatbot cannot reply, for example when its LLM provider is down.
See [Set an unavailable message](../../how-to/configure_chatbot_settings.md#set-an-unavailable-message).

### File uploads

When file uploads are enabled, participants can attach files to their messages for the chatbot to process.
See [Reading participant-uploaded files](../../how-to/workflow_cookbook.md#reading-participant-uploaded-files).

### Archive

Archiving retires a chatbot without deleting it and releases its channel identifiers for other chatbots.
You can un-archive it later.
See [Archive and un-archive a chatbot](../../how-to/configure_chatbot_settings.md#archive-and-un-archive-a-chatbot).

## See also

- [Configure Chatbot Settings](../../how-to/configure_chatbot_settings.md)
- [Chat Sessions](../sessions.md)
- [Versioning](../versioning.md)
- [Consent Forms](../consent.md)
