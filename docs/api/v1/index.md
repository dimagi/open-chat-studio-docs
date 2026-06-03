# v1

**Open Chat Studio** API version `1`.

Build, deploy and monitor chatbots.

## LLM Docs

Simplified per-tag references for LLM consumption:

* [Channels](./channels.txt){:target="_blank"} — Trigger bot messages or deliver messages directly to users on a channel.
* [Chat](./chat.txt){:target="_blank"} — The Chat API is designed to be used for integrating chatbots into external systems.
* [Experiment Sessions](./experiment_sessions.txt){:target="_blank"} — Manage chatbot sessions including session state, and session tags.
* [Experiments](./experiments.txt){:target="_blank"} — List and retrieve chatbots (formerly 'experiments').
* [Files](./files.txt){:target="_blank"} — Download the content of files associated with chat messages.
* [OpenAI](./openai.txt){:target="_blank"} — OpenAI-compatible endpoints for interacting with chatbots.
* [Participants](./participants.txt){:target="_blank"} — Manage participants, their data, and their schedules.

## Endpoints

### Channels

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/trigger_bot` | Trigger the bot to send a message to the user, or deliver a message directly |
| POST | `/channels/api/{experiment_id}/incoming_message` | New API Message |
| POST | `/channels/api/{experiment_id}/v{version}/incoming_message` | New API Message Versioned |

### Chat

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/chat/{session_id}/{task_id}/poll/` | Poll for task updates |
| POST | `/api/chat/{session_id}/message/` | Send a message to a chat session |
| GET | `/api/chat/{session_id}/poll/` | Poll for new messages in a chat session. Do not poll more than once every 30 seconds |
| POST | `/api/chat/{session_id}/upload/` | Upload files for a chat message |
| POST | `/api/chat/start/` | Start a new chat session for a widget |

### Experiment Sessions

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/sessions/` | List Chatbot Sessions |
| POST | `/api/sessions/` | Create Chatbot Session |
| GET | `/api/sessions/{id}/` | Retrieve Chatbot Session |
| POST | `/api/sessions/{id}/end_experiment_session/` | End Chatbot Session |
| POST | `/api/sessions/{id}/tags/` | Add Tags to Session |
| DELETE | `/api/sessions/{id}/tags/` | Remove Tags from Session |
| PATCH | `/api/sessions/{id}/update_state/` | Update Chatbot Session State |

### Experiments

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/experiments/` | List Chatbots |
| GET | `/api/experiments/{id}/` | Retrieve Chatbot |

### Files

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/files/{id}/content` | Download File Content |

### OpenAI

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/openai/{experiment_id}/chat/completions` | Chat Completions API for Experiments |
| POST | `/api/openai/{experiment_id}/v{version}/chat/completions` | Versioned Chat Completions API for Experiments |

### Participants

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/participants` | List Participants |
| POST | `/api/participants` | Update Participant Data |
| GET | `/api/participants/` | List Participants |
| POST | `/api/participants/` | Update Participant Data |
