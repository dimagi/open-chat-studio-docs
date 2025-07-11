---
title: How to Migrate Your Assistant to an Indexed Collection
---

!!! tip "Make sure you're familiar with the different types of [Collections][collections] before continuing."

If you've been using the "file search" tool in an assistant and want more flexibility or better performance, migrating to an **indexed collection** is a great step forward.

## General Steps

1. **Create an indexed collection** using the same files your assistant uses under its “file search” tool.
2. **Set up or update your pipeline** to reference this collection.

## Step 1: Create the Collection

Click on the **“Collections”** tab in the sidebar. Instead of selecting “Add New”, click **“Create from Assistant.”**

- Select the assistant you'd like to migrate.
- Give your new collection a name.
- Click **“Create Collection.”**

### What Happens Behind the Scenes?

- A new **indexed collection** is created using the same LLM provider as your assistant.
- All files from the assistant’s “file search” tool are **copied** to this new collection.
- A **vector store** is created at OpenAI for the collection.
- The assistant’s original vector store and files remain unchanged.

## Step 2: Update or Create a Pipeline

Once your collection is created:

- Navigate to the **Pipelines** tab.
- Either create a new pipeline or edit an existing one that uses the assistant.
- Add an [LLM node][llm-node] to the pipeline. If you have been using an assistant node, this LLM node should **replace** your assistant node.
- Within the node, select your **newly created indexed collection**.

You're done!

[collections]: ../concepts/collections/index.md  
[llm-node]: ../concepts/pipelines/nodes.md#llm
