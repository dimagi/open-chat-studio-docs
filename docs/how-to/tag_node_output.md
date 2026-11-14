---
title: Tag a Node's Output Messages
description: Use a node's Message Tag field so the node tags every message it produces, then see the tag on the chatbot's reply
---

# Tag a Node's Output Messages

Many nodes have a **Message Tag** field.
This guide shows you how to use it to make a node automatically tag every message it produces with a [message tag](../concepts/tags.md#message-tags-and-session-tags).
The LLM, Render a Template, and Python nodes have the field.

Use it when you want to find the messages a node produces, without tagging each by hand.
For example, an LLM node answers participants' health questions and advises them to visit the clinic when a symptom needs a check-up.
Tag its replies `clinic-referral`.
You can then review every referral together to check that the advice is safe and clear.
To tag a single message yourself, see [Create and Manage Tags](manage_tags.md#tag-a-message-or-session-by-hand).

## Prerequisites

- A chatbot with an [LLM node](../concepts/pipelines/nodes.md#llm-node).
  See [Configure an LLM Node](../tutorials/configure_llm_node.md) if you do not have one.
- A published version of the chatbot and a channel to chat through, such as a [public link](channels/deploy_public_link_channel.md#add-a-public-link).

## Add the tag to the node

The **Message Tag** field tags only the output of the node that has it.

1. Open your chatbot and view the **Pipeline** workflow.
2. Click the LLM node edit button (or the **Advanced** link) to open its settings.
3. Find the **Message Tag** field and enter `clinic-referral`.
   If the tag does not exist yet, OCS creates it for you.
4. Click the **x** on the node settings dialog to close it and save your changes.
5. [Create and publish a version](../tutorials/versioning_steps.md) of your chatbot.

## See the tag

1. Open the chatbot through your channel and send a test message.
   For example: `I have had a cough for two weeks. Should I see someone?`
2. Select **All Sessions** in the left menu and find the participant who sent your test message.
3. Click the view icon on the session to open the **Session Transcript**.
4. Find the chatbot's reply.

## Expected outcome

The tag `clinic-referral` appears on the chatbot's reply.
Your own message does not have the tag, because only the node's reply is tagged.

## Common issues

- **The tag is missing from the reply.**
  Check that you saved the node settings and published a new version, and that you chatted with the published version.

## See also

- [Tags](../concepts/tags.md)
- [Create and Manage Tags](manage_tags.md)
- [Tag a Router's Route](routers/tag_router_routes.md)
