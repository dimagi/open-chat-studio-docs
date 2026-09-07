---
title: Migrate Assistants
---

# Migrate Assistants

OpenAI [retired](https://platform.openai.com/docs/deprecations#2025-08-20-assistants-api) the Assistants API on 26 August 2026. Open Chat Studio has removed the assistant pipeline node as a result — a pipeline that still contains an assistant node no longer builds, so its chatbot cannot run until you replace that node. See the [OpenAI Assistants (Removed)](../concepts/assistants.md) page for background.

!!! warning "Affected chatbots are already down"
    A chatbot whose pipeline still holds an assistant node cannot answer participants. Follow the steps below to replace that node with an LLM node and bring it back.

Open Chat Studio supports all the features of Assistants in alternative ways as shown in the table below:

| Assistant Feature | Replacement Feature                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------|
| Threads           | Open Chat Studio [sessions](../concepts/sessions.md)                                            |
| Code Interpreter  | [OpenAI Code Interpreter tool](../tech-hub/tools.md#openai-code-interpreter) in LLM nodes |
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

1. **Create an indexed collection** using the same files your assistant used under its "file search" tool.
2. **Set up or update your chatbot** to reference this collection.

### Step 1: Create the Collection

Click on the **"Collections"** tab in the sidebar and click the **"Create from Assistant"** button in the top right.

- Select the assistant you'd like to migrate.
- Give your new collection a name.
- Click **"Create Collection"**.

!!! note
    This button is the last place in Open Chat Studio that still lists your assistants. The Assistants pages themselves have been removed, so you can no longer open an assistant to check its configuration or files beforehand — select it by name here.

#### What Happens Behind the Scenes?

- A new **indexed collection** is created using the same LLM provider as your assistant.
- All files from the assistant’s "file search" tool are **copied** to this new collection.
- A **vector store** is created at OpenAI for the collection.
- The assistant’s original vector store and files remain unchanged.

### Step 2: Update your chatbot

Once your collection is created:

- Open your Chatbot's pipeline editor.
- If the pipeline still contains an assistant node, it renders as a **Removed Node** and the pipeline will not build. Delete it.
- Add an [LLM node][llm-node] to the pipeline in its place.
- Within the node, select your **newly created indexed collection**.

You're done!

[collections]: ../concepts/collections/index.md  
[llm-node]: ../concepts/pipelines/nodes.md#llm-node
