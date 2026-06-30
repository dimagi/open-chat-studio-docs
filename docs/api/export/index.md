# export

**Open Chat Studio** API version `export`.

Read-only, team-scoped endpoints for the Open Chat Studio data sync/export. **Unversioned and intended only for OCS export** — it carries no backwards-compatibility guarantee and may change without notice.

## LLM Docs

Simplified per-tag references for LLM consumption:

* [Manifest](./manifest.txt){:target="_blank"}
* [Team](./team.txt){:target="_blank"}

## Endpoints

### Manifest

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/export/manifest/` | Manifest |

### Team

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/export/auth_providers/` | Auth Providers |
| GET | `/api/export/chatbots/` | Chatbots |
| GET | `/api/export/chats/` | Chats |
| GET | `/api/export/consent_forms/` | Consent Forms |
| GET | `/api/export/embedding_provider_models/` | Embedding Provider Models |
| GET | `/api/export/llm_provider_models/` | Llm Provider Models |
| GET | `/api/export/llm_providers/` | Llm Providers |
| GET | `/api/export/messaging_providers/` | Messaging Providers |
| GET | `/api/export/participant_data/` | Participant Data |
| GET | `/api/export/participants/` | Participants |
| GET | `/api/export/pipeline_nodes/` | Pipeline Nodes |
| GET | `/api/export/pipelines/` | Pipelines |
| GET | `/api/export/sessions/` | Sessions |
| GET | `/api/export/source_materials/` | Source Materials |
| GET | `/api/export/synthetic_voices/` | Synthetic Voices |
| GET | `/api/export/team/` | Team |
| GET | `/api/export/trace_providers/` | Trace Providers |
| GET | `/api/export/users/` | Users |
| GET | `/api/export/voice_providers/` | Voice Providers |
