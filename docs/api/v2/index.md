# v2

**Open Chat Studio** API version `v2`.

Build, deploy and monitor chatbots.

## LLM Docs

Simplified per-tag references for LLM consumption:

* [Channels](./channels.txt){:target="_blank"} — Trigger bot messages or deliver messages directly to users on a channel.
* [Chatbot Triggers](./chatbot_triggers.txt){:target="_blank"} — Add, change and archive the triggers that run an action on a conversation event, after inactivity, or at a set time.
* [Chatbots](./chatbots.txt){:target="_blank"} — List, retrieve and inspect chatbots (v2; formerly 'experiments').
* [Consent Forms](./consent_forms.txt){:target="_blank"}
* [Me](./me.txt){:target="_blank"} — Information about the authenticated user and the team the token is scoped to.
* [Pipelines](./pipelines.txt){:target="_blank"} — Discover the node types a pipeline may contain and the resource ids it may reference, and edit a chatbot's pipeline a node at a time.
* [Source Material](./source_material.txt){:target="_blank"}
* [Usage](./usage.txt){:target="_blank"} — Inspect team usage and activity data (message counts, and more).

## Endpoints

### Channels

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v2/trigger_bot/` | Trigger the bot to send a message to the user, or deliver a message directly |

### Chatbot Triggers

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v2/chatbots/{id}/scheduled-triggers/` | Add a Scheduled trigger |
| PATCH | `/api/v2/chatbots/{id}/scheduled-triggers/{trigger_id}/` | Update a Scheduled trigger |
| DELETE | `/api/v2/chatbots/{id}/scheduled-triggers/{trigger_id}/` | Archive a Scheduled trigger |
| POST | `/api/v2/chatbots/{id}/static-triggers/` | Add a Static trigger |
| PATCH | `/api/v2/chatbots/{id}/static-triggers/{trigger_id}/` | Update a Static trigger |
| DELETE | `/api/v2/chatbots/{id}/static-triggers/{trigger_id}/` | Archive a Static trigger |
| POST | `/api/v2/chatbots/{id}/timeout-triggers/` | Add a Timeout trigger |
| PATCH | `/api/v2/chatbots/{id}/timeout-triggers/{trigger_id}/` | Update a Timeout trigger |
| DELETE | `/api/v2/chatbots/{id}/timeout-triggers/{trigger_id}/` | Archive a Timeout trigger |

### Chatbots

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/chatbot/options/` | List Chatbot Setting Options |
| GET | `/api/v2/chatbots/` | List Chatbots |
| POST | `/api/v2/chatbots/` | Create Chatbot |
| GET | `/api/v2/chatbots/{id}/` | Retrieve Chatbot |
| PATCH | `/api/v2/chatbots/{id}/` | Update Chatbot |
| DELETE | `/api/v2/chatbots/{id}/` | Archive Chatbot |
| GET | `/api/v2/chatbots/{id}/inspect/` | Inspect Chatbot |
| POST | `/api/v2/chatbots/{id}/versions/` | Create a new version |
| PATCH | `/api/v2/chatbots/{id}/versions/{version_number}/` | Make chatbot version the published one |
| DELETE | `/api/v2/chatbots/{id}/versions/{version_number}/` | Archive a chatbot version |
| GET | `/api/v2/chatbots/{id}/versions/status/` | Version creation status |

### Consent Forms

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/consent-forms/` | List Consent Forms |
| POST | `/api/v2/consent-forms/` | Create Consent Form |
| GET | `/api/v2/consent-forms/{id}/` | Retrieve Consent Form |
| PATCH | `/api/v2/consent-forms/{id}/` | Update Consent Form |
| DELETE | `/api/v2/consent-forms/{id}/` | Archive Consent Form |

### Me

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/me/` | Current User |

### Pipelines

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v2/chatbots/{id}/pipeline/edges/` | Wire Pipeline Nodes |
| DELETE | `/api/v2/chatbots/{id}/pipeline/edges/{edge_id}/` | Unwire two Pipeline Nodes |
| POST | `/api/v2/chatbots/{id}/pipeline/nodes/` | Add a Pipeline Node |
| PATCH | `/api/v2/chatbots/{id}/pipeline/nodes/{node_id}/` | Edit a Pipeline Node |
| DELETE | `/api/v2/chatbots/{id}/pipeline/nodes/{node_id}/` | Remove a Pipeline Node |
| GET | `/api/v2/pipeline/nodes/` | List Pipeline Node Types |
| GET | `/api/v2/pipeline/nodes/{node_type}/` | Retrieve a Pipeline Node Type |
| GET | `/api/v2/pipeline/options/` | List Pipeline Node Options |
| GET | `/api/v2/pipeline/options/{node_type}/` | List One Node Type's Options |

### Source Material

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/source-material/` | List Source Material |
| POST | `/api/v2/source-material/` | Create Source Material |
| GET | `/api/v2/source-material/{id}/` | Retrieve Source Material |
| PATCH | `/api/v2/source-material/{id}/` | Update Source Material |
| DELETE | `/api/v2/source-material/{id}/` | Archive Source Material |

### Usage

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/usage/` | Usage |
