---
title: Migrate Assistants
---

OpenAI has [deprecated](https://platform.openai.com/docs/deprecations#2025-08-20-assistants-api) Assistants and will completely remove support on 2026-08-26.

Open Chat Studio supports all the features of Assistants in alternative ways as shown in the table below:

| Assistant Feature | Replacement Feature                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------|
| Threads           | Open Chat Studio [sessions](../concepts/sessions.md)                                            |
| Code Interpreter  | [OpenAI Code Interpreter tool](../concepts/tools/index.md#openai-code-interpreter) in LLM nodes |
| File Search       | [Indexed Collections](../concepts/collections/indexed.md)                                       |


## Migrating Code Interpreter

!!! info

    This guide assumes that you have enabled the [chatbots feature](../concepts/chatbots/index.md)

To use OpenAI's code interpreter tool without using Assistants:

* Create a [Chatbot](../concepts/chatbots/index.md) with an [LLM node][llm-node].
* Select an OpenAI LLM Provider
* Check the "Code Execution" checkbox under the "Builtin Tools" section of the configuration.

## Migrating File Search

!!! tip "Make sure you're familiar with the different types of [Collections][collections] before continuing."

### General Steps

1. **Create an indexed collection** using the same files your assistant uses under its "file search" tool.
2. **Set up or update your chatbot** to reference this collection.

### Step 1: Create the Collection

Click on the **"Collections"** tab in the sidebar and click the **"Create from Assistant"** button in the top right.

- Select the assistant you'd like to migrate.
- Give your new collection a name.
- Click **"Create Collection"**.

#### What Happens Behind the Scenes?

- A new **indexed collection** is created using the same LLM provider as your assistant.
- All files from the assistant’s "file search" tool are **copied** to this new collection.
- A **vector store** is created at OpenAI for the collection.
- The assistant’s original vector store and files remain unchanged.

### Step 2: Update your chatbot

Once your collection is created:

- Open your Chatbot's pipeline editor.
- Add an [LLM node][llm-node] to the pipeline. If you have been using an assistant node, this LLM node should **replace** your assistant node.
- Within the node, select your **newly created indexed collection**.

You're done!

[collections]: ../concepts/collections/index.md  
[llm-node]: ../concepts/pipelines/nodes.md#llm
