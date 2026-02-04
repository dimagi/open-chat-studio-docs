---
hide:
  - navigation
---

# Changelog
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
