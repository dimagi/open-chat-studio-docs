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

[Consent Forms](consent.md)
: Forms that provide context to chatbot users on how their data will be used and who to contact regarding any concerns.

[Custom Actions](custom_actions.md)
: Custom actions are a way to extend the functionality of the bot by integrating with external systems via HTTP APIs.

[Evaluations](evaluations/index.md)
: Evaluations is a testing system for measuring chatbot performance against different metrics.

[Events](events.md)
: Events are a way to trigger actions in the bot based on specific conditions.

[Experiment](experiment/index.md)
: The current name used in Open Chat Studio to refer to a chatbot. An experiment links all the configuration and data for a chatbot, including user sessions, data, actions, etc.

[Large Language Models (LLMs)](llm.md)
: Large language models are a type of AI model that can generate human-like text, images and audio.

[Messaging Provider](team/messaging_providers.md)
: Messaging providers hold the configuration required to send messages to users on a specific channel.

[Participant Data](participant_data.md)
: Data that persists across sessions and is tied to the same `User, Channel, Chatbot` scope. It helps retain long-term user preferences and contextual information beyond a single session.

[Pipelines](pipelines/index.md)
: A pipeline is a way to build a bot by combining one or more steps together.

[Prompt](prompt_variables.md)
: A prompt is the instructions that are given to the LLM to generate a response. Prompts can include text, source material, and other variables.

[Session](sessions.md)
: The scope of conversations between a user and a chatbot within a specific channel. Sessions are isolated, ensuring data privacy and contextual continuity for the duration of an interaction.

[Source Material](source_material.md)
: Additional information that can be included in the bot prompt using the `{source_material}` prompt variable.

[Tracing Provider](team/tracing_providers.md)
: Tracing providers hold the configuration required to send traces to the tracing provider.

[Versions](versioning.md)
: The ability to create and manage different versions of a chatbot.
