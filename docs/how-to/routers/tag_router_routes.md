# Tag a Router's Route

This guide shows you how to tag a router's output message with the route it chose.
Route tags help you review how participants move through your chatbot.
It applies to both the **LLM Router** and **Static Router** nodes.

For background on message tags, see [Tags](../../concepts/tags.md#message-tags-and-session-tags).

For example, a router named `health_triage` sends questions about symptoms down a `CLINIC` route.
With tagging on, each of those messages carries the tag `health_triage:CLINIC`.

## Prerequisites

- A chatbot with a [router node](../../concepts/pipelines/router_nodes.md).

## Turn on route tagging

1. Open your chatbot and view the **Pipeline** workflow.
2. Open the router node's settings.
3. Turn on **Tag Output Message**.
4. Close the settings dialog to save your changes.

## Check the tag name

OCS builds the tag name as `<node_name>:<route_name>`.
For the router above, a message routed to `CLINIC` gets `health_triage:CLINIC`.
Use a descriptive node name, such as `symptom_router`, because the node name is part of every tag.

If the router uses its [default output](index.md#the-default-output), OCS adds `:default` to the end, for example `health_triage:GENERAL:default`.
The router uses its default output when nothing matched or an error occurred.
This makes fallback routes easy to filter for when you review tags.

Tags longer than 100 characters are cut to 100 characters when saved.
Route tags are [system tags](../../concepts/tags.md#system-tags), so you cannot edit or delete them in **Manage Tags**.

## Expected outcome

Open a session after the router handles a message.
The router's output message carries the route tag.
To list sessions with the tag, see [Tags on the Sessions List](../../concepts/sessions.md#tags-on-the-sessions-list).

## Common issues

- **A router tag is missing.**
  Check that **Tag Output Message** is turned on for that router.

## See also

- [Router Nodes](index.md)
- [Tags](../../concepts/tags.md)
