---
title: Concepts
description: Conceptual Guide for Open Chat Studio
hide:
    - toc
---

# Conceptual Guide

This guide provides explanations of the key concepts behind the Open Chat Studio platform and AI applications more
broadly.

The conceptual guide does not cover step-by-step instructions or specific examples — those are found in
the [How-to guides](../how-to/index.md).

## Terms
[Assistant](assistants.md)
: A chatbot that uses OpenAI\`s Assistant API. Assistants can write and execute code and search and reference
  information in uploaded files.

[Authentication Provider](team/authentication_providers.md)
: Authentication providers allow you to authenticate with external systems to access data or services.

[Channel](channels.md)
: The platform through which a chat occurs (e.g., WhatsApp, Telegram, Web, Slack).

[Chatbot](chatbots/index.md)
: A chatbot in Open Chat Studio is a bot configuration that interacts with users across one or more channels.

[Consent Forms](consent.md)
: Forms that provide context to chatbot users on how their data will be used and who to contact regarding any concerns.

[Custom Actions](llm_custom_action.md)
: Custom actions extend a bot's functionality by integrating with external systems and APIs.

[Evaluations](evaluations/index.md)
: Evaluations is a testing system for measuring chatbot performance against different metrics.

[Events](events.md)
: Events are a way to trigger actions in the bot based on specific conditions.

[Large Language Models (LLMs)](llm.md)
: Large language models are a type of AI model that can generate human-like text, images and audio.

[Max Token Limit](max_tokens.md)
: The fixed maximum number of tokens a model can process in one turn, covering both the input prompt and the output response. This is a property of the model itself and cannot be changed.

[Messaging Provider](team/messaging_providers.md)
: Messaging providers hold the configuration required to send messages to users on a specific channel.

[Node](./pipelines/nodes.md)
: A node is a single step in a chatbot's pipeline.

[Participant Data](participant_data.md)
: Data that persists across sessions and is tied to the same `User, Channel, Chatbot` scope. It helps retain long-term user preferences and contextual information beyond a single session.

[Pipelines](pipelines/index.md)
: A pipeline is the visual workflow that controls how a chatbot processes input and produces output.

[Prompt](prompt_variables.md)
: A prompt is the instructions that are given to the LLM to generate a response. Prompts can include text, source material, and other variables.

[Session](sessions.md)
: The scope of conversations between a user and a chatbot within a specific channel. Sessions are isolated, ensuring data privacy and contextual continuity for the duration of an interaction.

[Session Status](session_status.md)
: The lifecycle state of a chat session (for example, setup, active, pending review, complete) and the transitions between those states.

[Source Material](source_material.md)
: Additional information that can be included in the bot prompt using the `{source_material}` prompt variable.

[Tools](tools/index.md)
: Tools let your chatbot take real actions during a conversation — such as performing calculations, scheduling reminders, or storing information about a participant — rather than only responding with text.

[Tracing](tracing.md)
: Tracing captures a chatbot's inputs, outputs, and decision-making process so bot developers can understand and debug their chatbot's behavior.

[Versions](versioning.md)
: The ability to create and manage different versions of a chatbot.
