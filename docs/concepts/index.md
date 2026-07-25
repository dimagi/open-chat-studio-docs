---
title: Concepts
description: Conceptual Guide for Open Chat Studio and AI-powered chatbots
hide:
    - toc
---

# Conceptual Guide

This guide explains the key concepts behind Open Chat Studio and AI-powered chatbots. Use it to understand what each feature is and why it exists.

For step-by-step instructions on completing specific tasks, see the [How-to guides](../how-to/index.md). If you are new to OCS, start with the [Tutorials](../tutorials/index.md).

## Terms
[Annotations](annotations/index.md)
: A human review system that lets teams label and score chatbot sessions and messages against a defined schema — useful for quality assurance, content moderation, and building evaluation datasets.

[Assistant](assistants.md)
: A legacy chatbot type powered by the OpenAI Assistants API. OpenAI has deprecated this API — see the [migration guide](../how-to/assistants_migration.md) if you currently use Assistants.

[Authentication Provider](team/authentication_providers.md)
: Credentials — such as API keys, bearer tokens, or username/password pairs — used when your chatbot connects to external services via Custom Actions or Python nodes.

[Channel](channels.md)
: How a participant interacts with your chatbot — for example, WhatsApp, Telegram, the web, or Slack.

[Chatbot](chatbots/index.md)
: In OCS, this is the top-level configuration for your conversational experience. It defines the chatbot's behavior, connects it to one or more channels, and is published to participants.

[Collections](collections/index.md)
: A group of files you attach to a chatbot to give it access to content — either as a media collection for file delivery, or an indexed collection for AI-powered document search (RAG).

[Consent Forms](consent.md)
: An agreement screen shown to participants before a conversation begins, letting them read how their data is used and confirm they agree before interacting with your chatbot.

[Custom Actions](llm_custom_action.md)
: Reusable connections to external services that let your chatbot retrieve information or complete tasks in another system — such as looking up an order status or creating a support ticket.

[Evaluations](evaluations/index.md)
: A built-in testing system that runs your chatbot against sample conversations and scores the responses against criteria you define, such as accuracy, tone, or whether the chatbot stayed on topic.

[Events](events.md)
: Automated actions that fire when something specific happens in a chatbot session — for example, when a conversation starts, ends, or when a participant has been inactive for a set period.

[Large Language Models (LLMs)](llm.md)
: The AI model that powers your chatbot's ability to understand messages and generate responses. OCS lets you choose from a range of models and configure how they behave.

[LLM Service Provider](team/llm_providers.md)
: The account you configure with an LLM service — such as OpenAI, Anthropic, or Google — so your chatbots can use its models.

[Messaging Provider](team/messaging_providers.md)
: An provider account you configure for a messaging service — such as Twilio, Turn.io, or Slack — that some channels require in order to send and receive messages for your chatbot.

[Node](./pipelines/nodes.md)
: A single processing step in a pipeline. Each node performs one task, such as calling an LLM, running custom code, or routing the conversation based on its content.

[Participant Data](participant_data.md)
: Custom information stored against each participant that persists across chatbot sessions. Use it to remember preferences, track progress, or personalize chatbot responses.

[Pipelines](pipelines/index.md)
: The drag-and-drop canvas where you build your chatbot's conversation logic by connecting nodes together. Every chatbot in OCS is powered by a pipeline.

[Prompt](prompt_variables.md)
: The instructions you write to guide your chatbot's responses. OCS supports prompt variables — placeholders like `{participant_data}` or `{source_material}` — that inject dynamic values into your prompt at runtime.

[Session](sessions.md)
: A conversation thread between a participant and your chatbot on a specific channel. Each session has its own history and is independent of other sessions.

[Session Status](session_status.md)
: A label that shows where a conversation is in its lifecycle — from first contact through to completion — and determines how OCS handles transitions between states.

[Source Material](source_material.md)
: A knowledge base you attach to your chatbot — such as product documentation or FAQs — that it can reference when generating responses.

[Speech Service Provider](team/speech_providers.md)
: The account you configure with a voice service — such as ElevenLabs — so your chatbot can convert speech to text and text to speech.

[Tags](tags.md)
: Labels applied to sessions or messages to categorize and organize interactions — for example, flagging conversations that need follow-up or segmenting sessions based on content.

[Team](team/index.md)
: The organizational unit in OCS. Each team has its own chatbots, data, and settings.

[Tools](tools/index.md)
: Built-in capabilities you enable per chatbot so it can do more than generate text — for example, schedule reminders, perform calculations, or remember information about a participant across sessions.

[Tracing](tracing.md)
: A record of every conversation turn showing what the chatbot received, what it returned, and how long it took. Use it to understand and debug unexpected chatbot behavior.

[Versions](versioning.md)
: Snapshots of your chatbot's configuration that let you publish a stable version to participants while you continue developing and testing changes in the background.
