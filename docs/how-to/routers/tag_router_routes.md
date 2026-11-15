# Tag a Router's Route

This guide shows you how to tag a router's output message with the route it chose.
Route tags help you review how participants move through your chatbot.
This applies to both the **LLM Router** and **Static Router** nodes.

For background on message tags, see [Tags](../../concepts/tags.md#message-tags-and-session-tags).

For example, a router named `health_triage` sends questions about symptoms down a `CLINIC` route.
With tagging on, each of those messages carries the tag `health_triage:CLINIC`.

## Prerequisites

- A chatbot with a [router node](../../concepts/pipelines/router_nodes.md).

## How do I turn on route tagging?

1. Open your chatbot and view the **Pipeline** workflow.
2. Click the node edit button (or the **Advanced** link) to open the router node's settings.
3. In the **Advanced Settings**, turn on **Tag Output Message**.
   It is in the same place for the **LLM Router** and the **Static Router**.
4. Close the settings dialog to save your changes.
5. [Create and publish a version](../../tutorials/versioning_steps.md) of your chatbot.

## What is the name of a route tag?

OCS builds the tag name as `<node_name>:<route_name>`.
For the router above, a message routed to `CLINIC` gets `health_triage:CLINIC`.
Use a descriptive node name, such as `symptom_router`, because the node name is part of every tag.

If the router uses its [Default Output](index.md#the-default-output), OCS adds `:default` to the end, for example `health_triage:GENERAL:default`.
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
- **Filtering by `:default` misses some fallback messages.**
  A long node or route name can push the tag past 100 characters, and the cut removes `:default`.
  Shorten the node or route names so the full tag fits.

## See also

- [Router Nodes](index.md)
- [Tags](../../concepts/tags.md)
