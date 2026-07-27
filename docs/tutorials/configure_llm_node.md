---
title: Configure an LLM Node
description: Add and configure an LLM node in a pipeline — the core building block of most chatbots
---

# Configure an LLM Node

The [LLM node](../concepts/pipelines/nodes.md#llm-node) is the heart of most chatbots in Open Chat Studio. It sends the conversation to an AI model and returns the model's reply.

This tutorial walks you through adding an LLM node to a [pipeline](../concepts/pipelines/index.md) and setting up the handful of options you'll use most often. By the end you will have a working LLM node that responds to messages using a model, a [prompt](../concepts/llm.md#prompt), and [conversation memory](../concepts/pipelines/history.md).

!!! note "Before you start"
    You'll need:

    - A new chatbot by following the [Create your first chatbot](first_chatbot.md) steps.
    - An [LLM provider](configure_llm_providers.md) configured for your team so that models are available to choose from.

## Step 1: Open your chatbot

1. Open your chatbot and view the **Pipeline** workflow. This is the visual canvas where you build your chatbot's conversation flow.  
2. New chatbots start with a [single LLM node already on the pipeline](../concepts/pipelines/index.md#a-simple-example), connected between the input and the output. If you see one, skip to [Step 2](#step-2-choose-a-model).  

??? info "Adding an LLM node manually"  
    If your pipeline has no LLM node:  

    1. On the pipeline, click the purple :material-plus-box: (plus) icon button on the top left.  
    2. Choose **LLM** from the list of node types.  

## Step 2: Choose a model

The model determines which AI does the thinking.

1. Click the LLM node edit button (or the **Advanced** link) to open its settings.
2. Find the **LLM Model** dropdown and pick a model.
3. If you're unsure which to choose, start with a general-purpose model and the defaults.

!!! tip "Not sure which model to pick?"
    See [Choose an LLM Model](../how-to/choose_llm_model.md) for help deciding between general-purpose and reasoning models. Only models from a [provider your team has configured](configure_llm_providers.md) will appear here.

## Step 3: Write a prompt

The [prompt](../concepts/llm.md#prompt) tells the model who it is and how to respond. It's the single most important setting on the node.

1. In the LLM node settings, find the prompt field.
2. Describe the chatbot's role, tone, and any rules it should follow.

A good starting prompt is short and specific:

```text
You are a friendly support assistant for Acme Co.
Answer questions about our products clearly and concisely.
If you don't know an answer, say so and suggest contacting support@acme.co.
```

!!! tip
    Write instructions the way you'd brief a new teammate — state the goal, the tone, and what to do when unsure.

## Step 4: Personalize with prompt variables (optional)

[Prompt variables](../concepts/prompt_variables.md) let you drop dynamic information into the prompt, so each participant gets a tailored response.

Insert a variable using curly braces. For example, to greet the participant by name:

```text
You are a helpful assistant. The participant's details are: {participant_data.name}.
Use their name when appropriate and keep replies concise.
```

See [Prompt variables](../concepts/prompt_variables.md) for the full list of supported variables.

## Step 5: Set the conversation history

A LLM node can be configured to remembers earlier messages in the conversation so it can respond in context. This memory is controlled by the node's **history** setting.

- For a normal back-and-forth chatbot, switch to `Global` history so the model can see the full conversation.
- Leave it on the default of `No History` for stateless tasks like translations.

See [LLM Node History](../concepts/pipelines/history.md) for how each history mode behaves.

## Step 6: Adjust the response style (optional)

Depending on the LLM model you chose, the node exposes a **temperature** or an **effort** setting that shapes how the model responds. The defaults work well for most chatbots, so you can safely skip this at first.

- **Temperature** — lower for consistent, predictable answers; higher for more varied, creative ones.
- **Effort** — how much a reasoning model "thinks" before answering.

For step-by-step guidance, see [Adjust LLM Node Model Parameters](../how-to/adjust_llm_node_model_parameters.md).

## Step 7: Save and test

1. Click the **x** on the popup node settings to close the dialog and save your changes.
2. Open the chat preview and send a test message.
3. Confirm the reply reflects your prompt and model choice. Tweak the prompt and re-test until the responses look right.

!!! tip
    When you're happy with the behaviour, [create a version](versioning_steps.md) so users keep a stable experience while you continue editing.

## Next steps

You've built a working LLM node. When you're ready to do more, an LLM node can also:

- Use [Tools](../concepts/tools/index.md) to take actions like scheduling reminders.
- Ground answers in your own documents with [Collections](../concepts/collections/index.md) (RAG).
- Connect to external systems with [Custom Actions](../concepts/llm_custom_action.md).
- Combine with other [node types](../concepts/pipelines/nodes.md) to build richer workflows — see the [Workflow Cookbook](../how-to/workflow_cookbook.md) for examples.
