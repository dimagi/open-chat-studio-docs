# Tag a Node's Output Messages

Many nodes have a **Message Tag** field.
This guide shows you how to use it to make a node automatically tag every message it produces with a [message tag](../concepts/tags.md#message-tags-and-session-tags).

Use it when you want to find the messages a node produces, without tagging each by hand.
The tag applies to every message the node produces, so it works best on a node with a single purpose.
For example, an LLM node only advises participants to visit the clinic and explains how to book.
Tag its replies `clinic-referral`.
Every message with that tag is a referral, so you can review them together to check that the advice is safe and clear.
To tag a single message yourself, see [Create and Manage Tags](manage_tags.md#how-do-i-tag-a-message-or-session-by-hand).

## Prerequisites

- A chatbot with an [LLM node](../concepts/pipelines/nodes.md#llm-node), a [Render a Template node](../concepts/pipelines/nodes.md#render-a-template-node) or a [Python node](../concepts/pipelines/nodes.md#python-node).
- A published version of the chatbot and a channel to chat through, such as a [public link](channels/deploy_public_link_channel.md#add-a-public-link).

## How do I add a tag to a node's output?

The **Message Tag** field tags only the output of the node that has it.
These steps use the LLM node.
The field works the same way on the Render a Template and Python nodes, so the steps apply to them too.

1. Open your chatbot and view the **Pipeline** workflow.
2. Click the node edit button (or the **Advanced** link) to open its settings.
3. Find the **Message Tag** field and enter `clinic-referral`.
   If the tag does not exist yet, OCS creates it for you.
4. Close the settings dialog to save your changes.
5. [Create and publish a version](../tutorials/versioning_steps.md) of your chatbot.

To tag only some of a Python node's messages, or to tag a session, use the node's code instead.
See [Python node utility functions](../tech-hub/python_node.md#utility-functions) for `add_message_tag` and `add_session_tag`.

## How do I see the tag on the chatbot's reply?

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
