---
hide:
  - navigation
---

# Changelog
## Jun 8, 2026
* **CHANGE** WhatsApp channels using a Twilio provider now have their webhook configured at Twilio automatically when the channel is created, edited, or deleted. If auto-configuration isn't possible (for example, on a Twilio sandbox number), the manual setup instructions are shown instead.

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

## Mar 31, 2026
* **NEW** Added three session selection modes when adding sessions to an annotation queue: **Selected only** (default, hand-pick via checkboxes), **All matching filters** (bulk-add every session matching the current filter), and **Sample** (add a random percentage of matching sessions using a configurable slider). A confirmation modal is shown for bulk operations.

## Mar 27, 2026
* **NEW** When uploading files to a media collection, it will now indicate which channels cannot send this file. Hovering over a channel will also show the reason why it cannot send the file.

## Mar 26, 2026
* **BUG** Fixed an issue where chat poll API responses could not generate correct URLs due to missing request context in the response serializer.
* **NEW** Added **ElevenLabs** as a speech service provider, supporting text-to-speech (TTS) and speech-to-text (STT). Providers can sync voices from the ElevenLabs catalog, and custom voices created in ElevenLabs are automatically synced to Open Chat Studio.
* **BUG** Fixed an authentication error that occurred when an invalid `chatbot_id` was provided in API requests.

## Mar 25, 2026
* **NEW** The Meta Cloud API WhatsApp provider now supports **media messages**. Users can send and receive images, videos, audio, and documents through WhatsApp channels.

## Mar 24, 2026
* **BUG** Fixed an error that could occur when displaying file sizes for files with no recorded content size.

## Mar 23, 2026
* **NEW** The Meta Cloud API WhatsApp provider now supports **template messages** as a fallback when the 24-hour service window has expired. When a bot cannot send a message due to an expired window, it automatically sends a pre-configured WhatsApp template instead of silently dropping the message.
* **BUG** Fixed an issue where timeout triggers stopped firing after publishing a new experiment version. Sessions created before the publish were silently excluded from timeout detection.
* **CHANGE** The default timeout for Custom Action HTTP calls has been increased from 10 seconds to 30 seconds to better accommodate complex or slow external services.

## Mar 19, 2026
* **NEW** Python Node code in pipelines can now use `print()` to capture debug and diagnostic output. Printed output is collected and visible as `console` data in the node's trace span, including in Langfuse.
* **NEW** The Meta Cloud API WhatsApp provider now supports **voice messages** in addition to text messages.
* **NEW** Excel and Word document attachments are now automatically converted to text before being sent to the LLM, enabling these file types to be processed in conversations alongside PDFs and images.

## Mar 18, 2026
* **NEW** Added support for **Meta Cloud API** as a new WhatsApp messaging provider, enabling direct integration with the WhatsApp Business Platform without requiring a third-party intermediary. Configure it using your WhatsApp Business Account ID, System User Access Token, App Secret, and Webhook Verify Token.
* **NEW** Added a [**Set Session State Key**](./tech-hub/tools.md#set-session-state-key) and [**Get Session State**](./tech-hub/tools.md#get-session-state-key) built-in tools that allow LLM nodes to read and write data from the [session state](concepts/sessions.md) during a conversation.
* **NEW** Added [**Append to Session State**](./tech-hub/tools.md#append-to-session-state) and [**Increment Session State Counter**](./tech-hub/tools.md#increment-session-state-counter) built-in tools, mirroring the existing participant data tools for managing lists and counters in session state.

## Mar 17, 2026
* **BUG** Fixed an issue where pipelines triggered by events (e.g. conversation end, timeout) silently discarded updates to participant data, session state, and session tags. These state changes are now correctly persisted.

## Mar 16, 2026
* **NEW** Session CSV exports now include a **Session State** column containing the data stored in the `session_state` field, making it easier to inspect pipeline state alongside conversation history.
* **NEW** Session detail views now display participant data as of the latest trace, with a timestamp note. AI messages that triggered participant data changes show a diff icon — click it to see a color-coded popover of what was added, removed, or modified.

## Mar 11, 2026
* **NEW** Added an **Annotation Reviewer** team role that grants scoped access to annotation queues. Users with this role can view and annotate queues they are assigned to, but cannot manage queues, add sessions, export results, or access other parts of the app.

## Mar 10, 2026
* **NEW** Participant data changes are now tracked per trace. The trace detail page shows a color-coded summary of what data was added, removed, or modified during each conversation turn, and CSV exports include a Participant Data column with the data snapshot at each message.
* **CHANGE** The Send Email pipeline node's subject and recipient fields now support [Jinja2](https://jinja.palletsprojects.com/en/stable/templates/) templates, and a new optional body field also accepts Jinja2 templates — the same variables available in the Render Template node. Existing pipelines are unaffected.

## Mar 9, 2026
* **NEW** Natural language filtering is now available to all users. Type plain-English queries (e.g., "sessions from last week excluding WhatsApp") on session, message, traces, participants, and notifications tables and click **✨ Generate** to automatically build filter rows.

## Mar 4, 2026
* **NEW** Teams now receive in-app notifications when LLM models are deprecated or removed.

## Feb 27, 2026
* **NEW** Tracing is now available to all users — no feature flag required. View and debug conversation traces directly from the session detail page. [Learn more](concepts/tracing.md)

## Feb 26, 2026
* **NEW** The trace detail page now includes a Langfuse span tree panel when Langfuse tracing is configured, showing the full observation tree with status indicators and latency badges alongside a detail view for each span's input/output.

## Feb 25, 2026
* **NEW** Timeout events can now be configured to measure inactivity from the first human message instead of the last message, giving more control over session timeout behavior.
* **NEW** Added natural language filter input to session and message tables. Users can type plain-English queries (e.g., "sessions from last week excluding WhatsApp") and click **✨ Generate** to automatically create filter rows. This feature is in beta and can be enabled by team admins from the team feature flags page.

## Feb 20, 2026
* **NEW** Added support for Claude Sonnet 4.6 model with adaptive thinking. Claude Sonnet 4.6 is now the default Anthropic model, replacing Claude Sonnet 4.5 as the default.

## Feb 19, 2026
* **NEW** Document source sync logs are now accessible directly from the Collections page via a "View Sync Logs" button, allowing users to inspect sync history, file counts (added/updated/removed), duration, and error details without leaving the page.

## Feb 18, 2026
* **NEW** Notifications system now maintains event history, allowing users to view past notifications and events. Users can also mute notifications per-event or enable "Do Not Disturb" mode to mute all notifications.

## Feb 11, 2026
* **NEW** Python nodes can now attach files fetched via HTTP to AI response messages using the `add_file_attachment()` helper and `response_bytes` field on HTTP responses. Note: originally documented as `attach_file_from_response(response_bytes, filename)`; the correct name and signature is `add_file_attachment(filename, content, content_type=None)`.
* **NEW** Added notification events that alert you when something important or noteworthy happens in your system, including failures across custom actions (health checks, API failures), chat operations (pipeline execution, LLM errors, tool failures), media handling (audio synthesis/transcription), and message delivery (platform-specific failures). This feature is currently in beta and can be requested for your team.

## Feb 10, 2026
* **CHANGE** Authentication provider names in Python node HTTP requests are now case-insensitive, allowing `auth="My-Provider"` and `auth="my-provider"` to match the same provider.

## Feb 9, 2026
* **NEW** Added `http_client` global to Python sandbox for making HTTP requests with security guardrails including SSRF prevention, request/response size limits, timeout clamping, automatic retries, and authentication provider integration.

## Feb 6, 2026
* **NEW** Added support for Claude Opus 4.6 model with adaptive thinking control. Features configurable effort levels (low, medium, high, max), 200K context window, and 128K max output tokens.
* **CHANGE** LLM API calls now automatically retry with exponential backoff when rate limited by providers (OpenAI, Anthropic, Google), improving reliability during peak usage.

## Feb 3, 2026
* **BUG** Fixed character encoding issues when reading plaintext files by automatically detecting and converting different encoding schemes to unicode.

## Feb 2, 2026
* **NEW** Voice notes from users and bots are now displayed as attachments in the chat transcript, making it easier to review and access voice messages.

## Jan 31, 2026
* **BUG** Fixed an issue where local collection index validation in LLM nodes incorrectly required all collections to use the same LLM provider as the node. This restriction now only applies to remote collections.

## Jan 30, 2026
* **CHANGE** Indexed collections using OpenAI-hosted vectorstores are now limited to 2 remote collections per LLM node, enforcing OpenAI's vectorstore limit. Local indexes and non-OpenAI providers remain unaffected.

## Jan 27, 2026
* **CHANGE** Router keywords are now automatically converted to uppercase. All router configurations will only accept and match uppercase keywords.
* **NEW** Dataset messages table rows can now be highlighted and shared via URL. Each row has a link and copy button to easily share specific dataset messages with others, with automatic scrolling to the highlighted message.

## Jan 26, 2026
* **NEW** Custom actions now include health status monitoring. The system automatically checks custom action endpoints every 5 minutes to verify server availability, displaying the status in the custom actions table. Users can also manually trigger health checks.

## Jan 22, 2026
* **NEW** Added API support for passing arbitrary context data with messages that gets merged into session state under the `remote_context` key, enabling API clients to provide contextual information.
* **BUG** Fixed an issue where cited and generated files from OpenAI assistants were not being properly annotated for download.
* **BUG** Fixed an issue where built-in tools and tool configurations were not cleared when switching LLM providers.

## Jan 21, 2026
* **CHANGE** Router keywords are now automatically converted to lowercase. All router configurations will only accept and match lowercase keywords.
* **MIGRATION** Removed the defunct 'summarize' event action. All events using this action have been deleted, and team admins have been notified of affected chatbots.

## Jan 20, 2026
* **NEW** Evaluation results table rows can now be highlighted and shared via URL. Each row has a link and copy button to easily share specific evaluation results with others.
* **BUG** Fixed an issue where provider compatibility checks between LLM nodes and indexed collections were skipped when only one collection was used.
* **NEW** Added more granular conversation end event types. Users can now create events based on who ended the conversation (participant, bot, event, admin or API). The generic conversation end trigger remains as a catch-all that fires whenever any conversation ends.

## Jan 14, 2026
* **NEW** Added the ability to start a new session after ending the current one. Users can choose whether to trigger end conversation events and must provide a prompt for the bot's initial message (pre-filled with the seed message when available).

## Jan 9, 2026
* **NEW** Added REST API endpoint for managing session tags. Sessions can now be tagged via POST requests (adds tags) and DELETE requests (removes tags), enabling external integrations to organize and filter sessions programmatically.

## Dec 19, 2025
* **NEW** Collections now support bulk file downloads. When a collection contains multiple files, users can download all files as a zip archive with progress tracking. Downloaded archives expire after 24 hours.

## Dec 18, 2025
* **NEW** Users can now trigger the bot to send a message to a participant from the participant details page.

## Dec 16, 2025
* **NEW** Added the ability for users to manually end sessions.

## Dec 15, 2025
* **NEW** LLM Evaluators now support type validation for output schemas with integer, float, string, and enum (choices) types.
* **NEW** Added support for GPT-5.2 and GPT-5.2-pro models.
* **CHANGE** Sessions generated during evaluation runs are now retained for 30 days (increased from 7 days) before being permanently deleted.
* **BUG** Fixed an issue where temperature and top_p parameters were shown in GPT-5.2 model configurations when effort level was set, causing configuration conflicts.

## Dec 10, 2025
* **BUG** Fixed an issue where additional citation links were included in channel responses when using custom citation text.

## Nov 26, 2025
* **NEW** OAuth2 authentication is now supported for API access. This enables secure third-party integrations using industry-standard OAuth2 with PKCE. See the [OAuth2 integration guide](./api/getting_started_with_oauth.md) for implementation details.

## Nov 11, 2025
* **NEW** Users can now configure model parameters (temperature, max tokens, etc.) directly in LLM nodes alongside other node parameters, instead of requiring separate configuration.

## Nov 7, 2025
* **NEW** Added "Select all" option to sessions table for bulk selection of sessions.
* **CHANGE** Improved client key security for chat widget. See the [Chat Widget docs](chat_widget/reference.md#embed-authentication).

## Nov 3, 2025
* **NEW** Chat Widget releases v0.5. Key features include:
    * Users can drag and reposition the chat widget launch button when fixed, to avoid obscuring page content
    * Internationalization support with built-in translations for 9 languages (English, Spanish, French, Arabic, Hindi, Italian, Portuguese, Swahili, Ukrainian)
    * New `language` property to set widget UI language and `translations-url` property for custom translations
    * Updated default button logo to use the Open Chat Studio avatar
    * See the [widget changelog](chat_widget/changelog.md) for full details
* **CHANGE** Removed seed message processing from the chat API session creation endpoint. The `seed_message_task_id` field is no longer returned in API responses.
* **CHANGE** Improved version creation UI performance by truncating large change sets to 10 items and displaying the count of hidden changes.

---

You can find older entries in the GitHub release notes: https://github.com/dimagi/open-chat-studio-docs/releases
