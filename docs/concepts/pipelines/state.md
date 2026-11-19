# Pipeline State

A pipeline is a series of separate [nodes](nodes.md), and each node receives only the output of the node before it.
That is not enough for many chatbots.
A router may need to know what an earlier node decided, a later message may need to know what the participant said earlier, and a prompt may need a value that no node passed along.

**State** solves this.
It is data that nodes read and write so they can share values: a flag set early in the pipeline, a count that grows over the conversation, or a choice the participant made last week.
State is your own data. It is not the [session status](../session_status.md), which OCS sets to show how far a session has progressed.

Read this page to decide where to keep a value.
OCS has three places, and they differ in how long the value lasts:

| Store | Lasts for | Use it for |
|---|---|---|
| Temporary state | One pipeline run, which is one participant message | Passing a value from one node to a later node while the current message is processed |
| Session state | One [session](../sessions.md) | Remembering a value across the messages of a single conversation |
| [Participant data](../participant_data.md) | All of a participant's sessions with the chatbot | Facts about the participant that should survive a new session, such as language or name |

## Temporary State

Temporary state exists for a single pipeline run.
A new participant message starts a new run, with a fresh temporary state, so nothing carries over to the next message.

OCS fills it with the participant's message, the outputs of earlier nodes, and any attachments the participant sent.
Nodes can add their own values.

Use temporary state for values that only matter while one message is processed, such as a classification result that a later router uses to choose a route.

## Session State

Session state belongs to one [session](../sessions.md).
It keeps its values from message to message until the session ends.
A participant who starts a new session starts with empty session state.

Use session state for conversation-level progress, such as which step of a form the participant has reached.
For information about the participant that should last beyond the session, use [participant data](../participant_data.md).

Session state can also be set from outside the pipeline.
You can supply it with the `session_data` parameter when you trigger a bot message through the API, and when you [create evaluation test cases](../../how-to/evaluations/create-a-dataset.md).

## Where You Can Use State

| Where | Temporary state | Session state |
|---|---|---|
| [Python node](nodes.md#python-node) | Read and write | Read and write |
| [Static Router](router_nodes.md#static-router-node) | Read, to choose a route | Read, to choose a route |
| [Prompts](../prompt_variables.md) | Insert with `{temp_state}` | Insert with `{session_state}` |
| [Render Template and Send Email nodes](../../tech-hub/template_and_email_nodes.md) | Insert with `{{ temp_state }}` | Insert with `{{ session_state }}` |

Only the Python node can write state during a run.
The other nodes read it.

## Learn More

- [Python Node State and Attachments](../../tech-hub/python_node_state_and_attachments.md) — default keys, reserved keys, and the functions that read and write state in code.
- [Configure a Static Router](../../how-to/routers/static_router.md) — route on a state value.
- [Prompt Variables](../prompt_variables.md) — insert state into a prompt.
