---
title: Migrate Assistants
---

# Migrate Assistants

OpenAI [deprecated](https://platform.openai.com/docs/deprecations#2025-08-20-assistants-api) Assistants and removed support for the Assistants API on 2026-08-26.
Open Chat Studio's Assistants pages were removed on 2026-09-02 — assistants can no longer be created, viewed, edited, or archived in OCS.

If a chatbot or pipeline still uses an assistant node, it keeps running, but you can no longer manage that assistant from OCS.
Use this guide to move it onto native OCS features, as shown in the table below:

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

1. **Create an indexed collection** using the same files your assistant uses under its "file search" tool.
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
- Add an [LLM node][llm-node] to the pipeline. If you have been using an assistant node, this LLM node should **replace** your assistant node.
- Within the node, select your **newly created indexed collection**.

You're done!

[collections]: ../concepts/collections/index.md  
[llm-node]: ../concepts/pipelines/nodes.md#llm-node
