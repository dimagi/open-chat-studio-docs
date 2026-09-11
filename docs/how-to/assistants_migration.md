---
title: Migrate Assistants
---

# Migrate Assistants

OpenAI [retired](https://platform.openai.com/docs/deprecations#2025-08-20-assistants-api) the Assistants API on 2026-08-26.
Open Chat Studio's Assistants pages were removed on 2026-09-02 — assistants can no longer be created, viewed, edited, or archived in OCS.
The assistant pipeline node has since been removed too, so a pipeline that still contains one no longer builds.
See the [OpenAI Assistants (Removed)](../concepts/assistants.md) page for background.

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

Create the collection manually — there's no automated import from an assistant, since assistants are no longer visible in OCS.

- Click on the **"Collections"** tab in the sidebar and click **"Add new"**.
- Choose **[Indexed Collection][collections]** and give it a name.
- Choose between a [Remote Index](../concepts/collections/indexed.md#remote-index) and a [Local Index](../concepts/collections/indexed.md#local-index). A remote index is closest to how an assistant's "file search" tool worked — the files are indexed by the LLM provider you select, so pick the same provider your assistant used.
- Upload the same files your assistant used for its "file search" tool. If you no longer have local copies, download them from your file storage at OpenAI.

### Step 2: Update your chatbot

Once your collection is created:

- Open your Chatbot's pipeline editor.
- If the pipeline still contains an assistant node, it renders as a **Removed Node** and the pipeline will not build. Delete it.
- Add an [LLM node][llm-node] to the pipeline in its place.
- Within the node, select your **newly created indexed collection**.

You're done!

[collections]: ../concepts/collections/index.md  
[llm-node]: ../concepts/pipelines/nodes.md#llm-node
