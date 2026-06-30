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
| GET | `/api/export/analysis_queries/` | Analysis Queries |
| GET | `/api/export/annotation_items/` | Annotation Items |
| GET | `/api/export/annotation_queue_aggregates/` | Annotation Queue Aggregates |
| GET | `/api/export/annotation_queues/` | Annotation Queues |
| GET | `/api/export/annotations/` | Annotations |
| GET | `/api/export/applied_tags/` | Applied Tags |
| GET | `/api/export/auth_providers/` | Auth Providers |
| GET | `/api/export/chat_attachments/` | Chat Attachments |
| GET | `/api/export/chat_messages/` | Chat Messages |
| GET | `/api/export/chatbot_channels/` | Chatbot Channels |
| GET | `/api/export/chatbots/` | Chatbots |
| GET | `/api/export/chats/` | Chats |
| GET | `/api/export/collection_files/` | Collection Files |
| GET | `/api/export/collections/` | Collections |
| GET | `/api/export/consent_forms/` | Consent Forms |
| GET | `/api/export/custom_action_operations/` | Custom Action Operations |
| GET | `/api/export/custom_actions/` | Custom Actions |
| GET | `/api/export/custom_tagged_items/` | Custom Tagged Items |
| GET | `/api/export/dataset_auto_population_rules/` | Dataset Auto Population Rules |
| GET | `/api/export/document_sources/` | Document Sources |
| GET | `/api/export/embedding_provider_models/` | Embedding Provider Models |
| GET | `/api/export/evaluation_configs/` | Evaluation Configs |
| GET | `/api/export/evaluation_datasets/` | Evaluation Datasets |
| GET | `/api/export/evaluation_messages/` | Evaluation Messages |
| GET | `/api/export/evaluation_results/` | Evaluation Results |
| GET | `/api/export/evaluation_run_aggregates/` | Evaluation Run Aggregates |
| GET | `/api/export/evaluation_runs/` | Evaluation Runs |
| GET | `/api/export/evaluator_tag_rules/` | Evaluator Tag Rules |
| GET | `/api/export/evaluators/` | Evaluators |
| GET | `/api/export/event_actions/` | Event Actions |
| GET | `/api/export/event_users/` | Event Users |
| GET | `/api/export/file_chunk_embeddings/` | File Chunk Embeddings |
| GET | `/api/export/files/` | Files |
| GET | `/api/export/llm_provider_models/` | Llm Provider Models |
| GET | `/api/export/llm_providers/` | Llm Providers |
| GET | `/api/export/messaging_providers/` | Messaging Providers |
| GET | `/api/export/notification_event_types/` | Notification Event Types |
| GET | `/api/export/notification_events/` | Notification Events |
| GET | `/api/export/participant_data/` | Participant Data |
| GET | `/api/export/participants/` | Participants |
| GET | `/api/export/pipeline_chat_histories/` | Pipeline Chat Histories |
| GET | `/api/export/pipeline_chat_messages/` | Pipeline Chat Messages |
| GET | `/api/export/pipeline_nodes/` | Pipeline Nodes |
| GET | `/api/export/pipelines/` | Pipelines |
| GET | `/api/export/pricing_rules/` | Pricing Rules |
| GET | `/api/export/scheduled_messages/` | Scheduled Messages |
| GET | `/api/export/scores/` | Scores |
| GET | `/api/export/sessions/` | Sessions |
| GET | `/api/export/source_materials/` | Source Materials |
| GET | `/api/export/static_triggers/` | Static Triggers |
| GET | `/api/export/synthetic_voices/` | Synthetic Voices |
| GET | `/api/export/tags/` | Tags |
| GET | `/api/export/team/` | Team |
| GET | `/api/export/timeout_triggers/` | Timeout Triggers |
| GET | `/api/export/trace_providers/` | Trace Providers |
| GET | `/api/export/traces/` | Traces |
| GET | `/api/export/transcript_analyses/` | Transcript Analyses |
| GET | `/api/export/usage_records/` | Usage Records |
| GET | `/api/export/user_comments/` | User Comments |
| GET | `/api/export/user_notification_preferences/` | User Notification Preferences |
| GET | `/api/export/users/` | Users |
| GET | `/api/export/voice_providers/` | Voice Providers |
