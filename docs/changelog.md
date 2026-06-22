---
hide:
  - navigation
---

# Changelog

!!! info

    Looking for the embeddable chat widget? See the [Chat Widget changelog](chat_widget/changelog.md).

## Jun 22, 2026
* **CHANGE** Reverting a chatbot to a previous version now opens a confirmation modal showing exactly what will change — a field- and node-level diff of the current working state against the target version. A warning appears when the working version has unreleased changes that the revert would overwrite.

## Jun 18, 2026
* **CHANGE** The `/api/v2/me/` endpoint now includes an `email_verified` field indicating whether the authenticated user has confirmed their email address.

## Jun 15, 2026
* **CHANGE** The session retrieval endpoint (`GET /api/sessions/{id}/`) now includes the session's state in its response payload, so consumers can read a session's stored state alongside its other details without a separate call.

## Jun 11, 2026
* **CHANGE** Surveys are deprecated and will be removed on **2026-07-10**. They are now decoupled from chatbots — the pre- and post-survey settings have been removed, so surveys are no longer presented to participants before or after a web chat. Existing surveys are read-only (you can no longer create new ones, only view or delete them) for a 30-day window so teams can export their data. A deprecation warning and an in-product notification announce the removal.

## Jun 10, 2026
* **CHANGE** The cursor-paginated list endpoints — `/api/sessions/`, `/api/participants/`, `/api/experiments/`, and `/api/v2/chatbots/` — now include a `count` field (the total number of matching records) on the first page of results, so consumers can show real progress while paging through a full sync. The field is omitted on subsequent (cursor-following) pages and is optional, so existing consumers are unaffected.
* **NEW** Added support for the **Claude Fable 5** model from Anthropic. Fable 5 offers a 1M-token context window with adaptive thinking and configurable effort levels (low, medium, high, max), and can now be selected for chatbots and pipelines.

## Jun 9, 2026
* **CHANGE** Chat sessions started through the API now require a per-session token to read their transcripts. `POST /api/chat/start/` returns a `session_token`, which must be sent as the `X-Session-Token` header on subsequent session calls (or an authenticated user with access to the session). This prevents session transcripts from being read by anyone who obtains a session ID. **Breaking change** for direct API consumers: send the returned `session_token` on subsequent calls, or opt out with `use_session_token: false`. Token access to sessions inactive for more than 7 days is rejected.
* **NEW** Added a read-only v2 chatbots API: `GET /api/v2/chatbots/` (list) and `/{id}/` (retrieve), plus `/{id}/inspect/?version=`, which returns a single denormalized view of a chatbot's full configuration — settings, channels, pipeline nodes with their resources inlined, and event triggers. The response is self-documenting via the OpenAPI schema, making it well suited to LLM-agent consumers.
* **BUG** Fixed an error when opening a chatbot's home page via a URL pointing to a version snapshot of the chatbot. Users are now redirected to the canonical URL of the active version instead of hitting an error.

## Jun 8, 2026
* **CHANGE** WhatsApp channels using a Twilio provider now have their webhook configured at Twilio automatically when the channel is created, edited, or deleted. If auto-configuration isn't possible (for example, on a Twilio sandbox number), the manual setup instructions are shown instead.
* **CHANGE** The `POST /api/participants/` endpoint now returns the full participant detail in its response, including the CommCare Connect `connect_channel_id` for each chatbot. Connect channels are created synchronously during the request, so callers no longer need to poll for the channel ID after updating a participant.

## Jun 5, 2026
* **CHANGE** Any annotation reviewer (any team member) can now mark or unmark a submitted annotation as **authoritative**. This was previously restricted to queue admins.
* **NEW** Added a **Clear all** button to the evaluation runs page. Users with delete permission can wipe a config's entire run history in one action; this also un-applies the tags those runs added to their targets (chats and chat messages), returning them to their pre-evaluation state. Tags applied by hand are left untouched.
* **CHANGE** The **number of reviews required** on an annotation queue can now be edited even after annotation has started. Saving the new value recomputes the status of every queue item: raising the requirement can move completed items back to **Awaiting resolution**, while lowering it leaves unresolved multi-review items awaiting resolution rather than silently marking them complete. A confirmation dialog warns before the change is applied.

## Jun 4, 2026
* **CHANGE** The legacy embedded web chat endpoints (the old `/embed/start/` iframe flow) are now deprecated and will be removed on **2026-08-03**. Responses from these endpoints now include `Deprecation`, `Sunset`, and successor `Link` headers per RFC 8594. Sites still embedding chat via the old iframe flow should migrate to the current [chat widget](https://docs.openchatstudio.com/chat_widget/).

## Jun 3, 2026
* **CHANGE** Published chatbots now automatically reflect updates to their linked collections — scheduled document-source syncs to RAG indexes and manual edits to media (attachment) collections — instead of staying pinned to the snapshot captured at publish time. Existing published bots pick up this live behaviour the next time they're republished.
* **NEW** The trace table now has a **Session ID** filter, and quick links let you jump from a trace detail page or a chatbot session transcript straight to a trace table pre-filtered to that session, chatbot, or participant.
* **BUG** Fixed a crash that could occur with Azure text-to-speech when a voice was asked to speak text in a language it doesn't support. Azure could return a corrupted audio file in this case; the bot now detects the invalid output and gracefully falls back to a text response instead of erroring out.

## Jun 2, 2026
* **CHANGE** The **Annotation Reviewer** role now includes chat-view permission by default, so reviewers can open the sessions attached to the queue items they're working on without needing the chat viewer role granted separately. Trace icons are also now only rendered for users who have permission to view traces.
* **BUG** Bot messages pushed directly through the [Trigger Bot Message](https://www.openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) API with `message_text` (verbatim delivery, no LLM) are now captured in tracing alongside LLM-generated messages, so they appear in the session trace and observability views.

## Jun 1, 2026
* **NEW** WhatsApp channels now accept **inbound images and documents** across all three providers — Meta Cloud API, Twilio, and Turn.io. Incoming media is downloaded, persisted, attached to the session, and forwarded to the LLM alongside the user's message.
* **BUG** Fixed a 404 that could occur when downloading attachments received over the email channel. The `ChatAttachment` record required by the authorized download endpoint was not being created during inbound email hydration, so links generated for the bot's attachments resolved to "not found".

## May 29, 2026
* **CHANGE** The chatbot UI now surfaces a warning wherever a chatbot is viewed if no consent form is configured, making it easier to spot bots that may be collecting participant data without a consent mechanism in place.

## May 28, 2026
* **CHANGE** Rerunning an evaluation now reconciles tags applied by its evaluators' tag rules. After a rerun, any tag managed by those rules that no longer matches the latest evaluator output is removed from the affected message or session — even if it had originally been applied by a human. **FULL** reruns reconcile every row in the dataset; **DELTA** reruns only reconcile the rows in their scope. **PREVIEW** runs do not apply or remove tags.
* **CHANGE** Reorganised the evaluation dataset edit page: **Add Sessions** now opens a dedicated sub-page with a simplified selection UI (mirroring the annotation-queue Add Sessions surface), and the **Manual entry** and **CSV upload** forms are hidden behind a new **Add** dropdown until selected.
* **BUG** Fixed a retrieval-quality bug affecting local indexed collections that use Voyage AI or Google embedding models. Documents were previously embedded in "query" mode rather than "document" mode, weakening retrieval accuracy. OpenAI collections are unaffected.
* **BUG** Fixed local indexing for OpenAI providers configured against an OpenAI-compatible proxy or gateway (e.g. LiteLLM). The provider's custom base URL is now passed through to the embedding client during indexing, which previously always hit `api.openai.com` and failed with a 401.

## May 25, 2026
* **NEW** Added a **Concordance** view under Evaluations that compares an LLM judge's output against human annotations on a shared categorical field. The view shows side-by-side judge vs. human values per session, an overall agreement count and percentage, and matched / eval-only / human-only buckets with deep links per row. This feature is alpha and gated behind the `flag_assessments_concordance` feature flag.
* **NEW** Added a **Show usages** button to each service-provider edit page that lists the chatbots, assistants, pipelines, collections, and channels referencing that provider, with version badges and direct links to each working version. A staff-only **Find provider by API key** admin tool also lets administrators look up providers across teams by full key, suffix, or substring — useful for credential rotation and leaked-key triage.
* **BUG** Fixed an error that could appear when opening an evaluation dataset whose ingestion task was still queued. The dataset edit page now shows a "Queued. Waiting for task to start..." message instead of erroring out.
* **BUG** Fixed a `ValidationError` raised when the `Append to Participant Data` tool was called with a dictionary value (for example, multi-part responses from an `LLM Response With Prompt` node). Dict values are now accepted and appended to the participant data list as a single entry.
* **BUG** Fixed a `ValueError` that could prevent file downloads (notably `voice_note.ogg`) when an underlying `File` record had no stored content. Empty files are no longer created, and the download view now returns a 404 instead of erroring out for any pre-existing empty entries.

## May 22, 2026
* **BUG** Message exports now include AI messages that don't have an associated human input message (e.g. pre-tracing data), which were previously omitted. The "Trace ID" column is now sourced from each message's own trace info, so AI response rows will be empty where they previously inherited the trace ID from the input message.

## May 20, 2026
* **NEW** Evaluations can now be **edited** and **deleted** from the UI. A new Edit button on the evaluation detail page opens the configuration form, and Delete actions are available both on each row of the evaluations list and on the detail page. Deleting an evaluation cascades to its runs and results.
* **NEW** Multi-reviewer annotation queues now support **authoritative answers** for resolving conflicting annotations. Queue admins can mark one annotation as the authoritative response from a "Mark authoritative" button next to each annotation. Items with all required reviews submitted but no authoritative pick enter a new **Awaiting resolution** status, surfaced with an amber banner on the annotate page and `resolved / awaiting` counts on the queue detail. Aggregations prefer the authoritative annotation per item (falling back to all submitted when none is set), and CSV/JSONL exports now include an `is_authoritative` column.
* **BUG** Fixed CSV transcript exports so that special characters (curly apostrophes, accented letters, etc.) render correctly when opened directly in Excel.

## May 19, 2026
* **CHANGE** Outbound emails sent by the bot now use the `email_subject` value from session state as the subject line when set, falling back to "New message" when absent. Inbound reply threads continue to reuse the original subject.
* **CHANGE** The [Trigger Bot Message](https://www.openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) API now returns the session details (`session_id`, `url`, `team`, and `channel`) in its 200 response, so callers can reference the session immediately without a follow-up lookup.
* **CHANGE** The session list and detail API responses now include a `status` field, exposing the current state of a session (`setup`, `pending`, `active`, `complete`, etc.) to API consumers.
* **CHANGE** The session list and detail API responses now include a `platform` field, identifying the channel through which the session was created (e.g. `web`, `api`, `slack`).

## May 15, 2026
* **NEW** Session-level evaluation datasets can now be **auto-populated** from a source chatbot. Configure one or more filter-driven rules on a dataset, and matching new sessions are continuously ingested on a 5-minute polling cycle. When a rule is linked to an evaluation config, evaluators run automatically over only the newly added rows.
* **NEW** The [Trigger Bot Message](https://www.openchatstudio.com/api/docs/#tag/Channels/operation/trigger_bot_message) API now accepts an optional `message_text` parameter that delivers the exact text to the participant's channel without LLM processing. Requests must include either `prompt_text` (for an LLM-generated reply, existing behaviour) or `message_text` (for verbatim delivery), but not both.
* **NEW** Session-level evaluation datasets can now be populated by importing sessions from an annotation queue. From a session-level dataset's edit page, choose **Import from Annotation Queue** and pick any team queue that contains session items. Imports are de-duplicated against the existing sessions in the dataset.
* **NEW** Reviewers can now edit their own submitted annotations on a queue item. An **Edit** button appears next to each of your annotations, opening the form pre-filled with your existing responses; saving updates the annotation and recomputes the queue's aggregate stats.

## May 13, 2026
* **NEW** Added a `GET /api/participants` endpoint to list participants for your team along with their per-chatbot data. The endpoint supports filtering by `identifier`, `platform`, and `experiment` (chatbot public id), and is cursor-paginated. A new `participants:read` OAuth scope is required for read access.
* **CHANGE** The `ParticipantData` API field `experiment` has been renamed to `chatbot` (chatbot name) and `chatbot_id` (chatbot public id) to align with user-facing terminology.

## May 6, 2026
* **NEW** Added a **Create** action to the Participants page, letting you add a single participant by hand without using the bulk CSV importer. The form takes an identifier, platform, and optional name, and shows an inline link to the existing participant if one already exists for that platform and identifier.
* **CHANGE** v0.7.0 of the Chat Widget is released. See [widget chagelog](chat_widget/changelog.md) for details.

## May 5, 2026
* **CHANGE** Increased the HTTP request size limit from 512 KB to 1 MB and the response size limit from 1 MB to 5 MB for the restricted HTTP client used in pipelines.

## Apr 30, 2026
* **NEW** Added **Email** as a messaging channel. Users can now communicate with chatbots via email — inbound messages are received through a webhook, routed to the correct chatbot, and replied to in a threaded email conversation. This feature is gated behind the `flag_email_channel` feature flag.
* **NEW** The email channel now supports **bidirectional file attachments**. Inbound attachments (PDFs, CSVs, images, etc.) are saved and made available to the LLM or pipeline; oversized or blocked file types are surfaced as inline notes so the bot can explain the rejection. Outbound files produced by the pipeline (e.g. via `add_file_attachment()` in a Python node) are sent as MIME attachments in the same threaded reply.
* **NEW** Trace detail pages now include a **Performance Metrics** section showing LLM turn count, tool call count, total tokens, input tokens, and output tokens for each pipeline execution. Metrics are collected across all LLM nodes (Router and LLM nodes); pipelines without LLM nodes display "—" for all metrics.

## Apr 29, 2026
* **NEW** Added **Voyage AI** as a local embedding provider. Teams can now configure a Voyage AI service provider to embed and semantically search documents in collections using models such as `voyage-4-large`, `voyage-4`, and `voyage-3.5`.

## Apr 28, 2026
* **NEW** LLM evaluators can now automatically tag sessions or messages based on evaluation results. A new **Tag Rules** section on the evaluator form lets you define conditions (equals a value, or falls within a numeric range) that apply a tag when matched. Applied tags are recorded in an audit log and shown in the **Applied Tags** column on the run results page.

## Apr 25, 2026
* **NEW** Added **intron.io** as a Text-to-Speech (TTS) provider. Teams can configure an intron provider with an API key to access 90 voices across 45 African and international accents (male and female), including Afrikaans, Hausa, Igbo, Kinyarwanda, Swahili, Yoruba, Zulu, and more.

## Apr 23, 2026
* **NEW** Pipeline structure and event trigger data are now provided as context to the chat widget when viewing a pipeline, enabling you to ask the assistant questions about the pipeline you are currently viewing.
* **BUG** Fixed a `SyntaxError` in the evaluator form that prevented the variable autocomplete feature from loading correctly.

## Apr 22, 2026
* **NEW** Evaluation datasets now support **session-level evaluation**, allowing evaluators to judge an entire conversation holistically rather than individual message pairs. When creating a dataset, choose "Message level" (existing behavior) or "Session level" (new). Session-level datasets can be populated by cloning sessions, and incompatible evaluators are automatically filtered out when configuring evaluations.
* **BUG** Fixed a `TypeError` on mobile Safari that prevented the trends chart from rendering when the chatbot table was dynamically loaded.

## Apr 21, 2026
* **NEW** Annotation exports (CSV and JSONL) now include three additional fields: `session_id` (the UUID of the linked session), `flagged` (whether the item is flagged), and `flagged_reason` (the list of flag entries). Flagged items with no annotations are also included in the export.
* **BUG** Fixed an error that occurred when rapidly removing filters in the UI.
* **BUG** Fixed an API error that occurred when serializing sessions whose `external_id` contained a dot character (e.g., Slack-format identifiers). The sessions API endpoint now correctly handles all `external_id` formats.

## Apr 12, 2026
* **BUG** Fixed an issue where document indexing failed for certain markdown files containing multi-byte UTF-8 characters.

## Apr 10, 2026
* **NEW** Added date range and participant filters to the annotation queue view, making it easier to find specific sessions.

## Apr 8, 2026
* **NEW** Python Node code in pipelines can now call `end_session()` to programmatically end the current session, enabling more complex and deterministic session-ending logic.

## Apr 2, 2026
* **NEW** Added the ability to import sessions from an existing evaluation dataset into an annotation queue.

## Mar 2026
* Major WhatsApp expansion via the new **Meta Cloud API** provider, which gained support for media, voice, and template messages (the latter as a fallback after the 24-hour service window expires). New built-in session-state tools (**Set/Get Session State Key**, **Append to Session State**, **Increment Session State Counter**) let LLM nodes read and write [session state](concepts/sessions.md); **natural language filtering** became available to all users; and an **Annotation Reviewer** team role and flexible session-selection modes (Selected, All matching filters, Sample) were added to annotation queues. Other additions included **ElevenLabs** as a speech (TTS/STT) provider, Python node `print()` debug capture, automatic Excel/Word-to-text conversion, per-trace participant-data tracking, Session State in CSV exports, Jinja2 templates in the Send Email node, and deprecation/removal notifications for LLM models. **CHANGE:** the default Custom Action HTTP timeout was raised from 10 to 30 seconds.

## Feb 2026
* **Tracing** became generally available to all users (no feature flag), with a new Langfuse span-tree panel on the trace detail page. Added support for **Claude Opus 4.6** and **Claude Sonnet 4.6** — Sonnet 4.6 replaced Sonnet 4.5 as the **default Anthropic model**. The Python sandbox gained an `http_client` global (with SSRF protection and other guardrails) and an `add_file_attachment(filename, content, content_type=None)` helper for attaching HTTP-fetched files. A new notifications system added event history, per-event muting, and Do Not Disturb; voice notes now appear as attachments; and timeout events can measure inactivity from the first human message. **CHANGE:** LLM API calls now retry with exponential backoff on rate limits, and Python-node auth provider names are matched case-insensitively.

## Jan 2026
* Added a REST API endpoint for managing **session tags** (POST/DELETE), API support for passing arbitrary `remote_context` data merged into session state, **custom action health monitoring** (5-minute endpoint checks), and more granular conversation-end event types (by who ended the conversation). Users can now start a new session immediately after ending one, and dataset/evaluation table rows can be highlighted and shared via URL. **MIGRATION:** the defunct 'summarize' event action was removed — all events using it were deleted and affected team admins notified. **CHANGE:** router keywords are now normalized to uppercase, and OpenAI-hosted vectorstores are limited to 2 remote collections per LLM node (OpenAI's limit; local and non-OpenAI providers unaffected).

## Dec 2025
* Added support for **GPT-5.2 and GPT-5.2-pro** models, **bulk file downloads** for collections (zip archives expiring after 24 hours), the ability to manually end sessions, triggering a bot message from the participant details page, and type validation (integer, float, string, enum) for LLM evaluator output schemas. **CHANGE:** sessions generated during evaluation runs are now retained for 30 days (up from 7) before deletion.

## Nov 2025
* **OAuth2 authentication** (with PKCE) is now supported for API access — see the [OAuth2 integration guide](./api/getting_started_with_oauth.md). Model parameters (temperature, max tokens, etc.) can be configured directly in LLM nodes, and a "Select all" option was added to the sessions table. The Chat Widget reached **v0.5**, adding drag-to-reposition for the launch button, internationalization with translations for 9 languages, and a new `language` property — see the [widget changelog](chat_widget/changelog.md). **CHANGE:** seed message processing was removed from the chat API session-creation endpoint, so the `seed_message_task_id` field is no longer returned; client key security for the chat widget was also improved.

---

You can find older entries in the GitHub release notes: https://github.com/dimagi/open-chat-studio-docs/releases
