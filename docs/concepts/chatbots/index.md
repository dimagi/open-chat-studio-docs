# Chatbots

A chatbot in Open Chat Studio is the bot configuration that participants interact with.
It defines the conversational experience, while the underlying [pipeline](../pipelines/index.md) controls how messages are processed and responses are generated.

Chatbots can connect to one or more [channels](../channels.md) and use [LLMs](../llm.md) to generate responses.
They can also include supporting logic such as [routing](../pipelines/router_nodes.md), [participant data](../participant_data.md), or [custom actions](../llm_custom_action.md).

## Creating a Chatbot
Every chatbot in Open Chat Studio is configured using a visual workflow called a [**Pipeline**](../pipelines/index.md).

Use the resources below to learn how to create a chatbot and how its pipeline works:

- :material-clock-fast:{ .lg .middle } [__Quickstart Guide__](../../tutorials/first_chatbot.md)
- :material-chat-question:{ .lg .middle } [__What is a Pipeline?__](../pipelines/index.md#what-is-a-pipeline)
- :material-whatsapp:{ .lg .middle } [__Deploying your bot__](../../how-to/channels/deploy_to_different_channels.md)

## Unavailable message

Sometimes a chatbot cannot reply, for example when its LLM provider is down or rejects the configured API key.
Participants then get a default error reply: "Sorry, something went wrong while processing your message. Please try again later".

Set **Unavailable Message** on the chatbot's **Settings** tab to send your own text after that reply, such as when to try again or another way to get help.
It is sent on every channel.
Errors the participant can fix, such as an unsupported file type, keep their own message.

The setting is versioned, so it reaches participants on the published chatbot once you [publish a new version](../versioning.md).

## See also

- [Chat Sessions](../sessions.md)
- [Versioning](../versioning.md)
- [Consent Forms](../consent.md)
