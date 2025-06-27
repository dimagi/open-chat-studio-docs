---
hide:
  - navigation
---

# Changelog
## Jun 27, 2025
* **BUG** Fix attachment download link in chat transcript view.
* **NEW** Display image attachments in chat transcript view
* **BUG** Fix banner dismissal so they stay dismissed between page navigations.

## Jun 26, 2025
* **BUG** Fixed versioning not working properly with safety layers.

## Jun 24, 2025
* **NEW** Message and session tags can now be added from Python Nodes using the [`add_message_tag`](concepts/pipelines/nodes.md#python_node.add_message_tag) and [`add_session_tag`](concepts/pipelines/nodes.md#python_node.add_session_tag) functions.

## Jun 23, 2025
* **BUG** Fixed an issue with file citations where cited files are not always showing up as being cited.

## Jun 20, 2025
* **NEW** Add a new [tool](concepts/tools/index.md) that will end the current chat session when called.
* **NEW** Prompts can now reference pipeline temporary state and session state by using [prompt variables](concepts/prompt_variables.md).
* **NEW** Added support for OCS hosted indexes. See [indexed collections](./concepts/collections/indexed.md) for more details.

## Jun 19, 2025
* **BUG** Fixed an issue where chunked messages sent via Twilio arrive out-of-order at the user.

## Jun 11, 2025
* **CHANGE** Performance improvements to the versioning process.
* **CHANGE** Updated text diff widget for the "Create new version" page which preserves the original text formatting.

## Jun 4, 2025
* **NEW** Added the ability to create an indexed collection from an OpenAI assistant that uses File Search.

## Jun 3, 2025
* **NEW** Added support for filtering Chatbot sessions by relative date ranges. This adds the `range` operator as a filter option for date parameters with options such as `1 hour`, `1 day`. In addition, a top level filter is added which allows quick filtering of Chatbot sessions by 'Last Message' field.
* **CHANGE** For teams with Chatbots enabled, the default landing page will now be "Chatbots" replacing "Experiments"

## May 22, 2025
* **CHANGE** API update: The [list experiments](https://chatbots.dimagi.com/api/docs/#tag/Experiments/operation/experiment_list) endpoint now returns **only unreleased experiments** in the top-level response. A new `versions` key has been added to each experiment, containing all version of that experiment.
* **NEW** [Collections](./concepts/collections/index.md) are now generally available for all users who are using
pipelines

## May 16, 2025
* **NEW** Added support for [indexed collections](./concepts/collections/indexed.md) to support RAG use cases.
* **CHANGE** When using an OpenAI Assistant with a chatbot that has tracing enabled, a new event will be posted to the tracing provider with all the Assistant details. This makes it easier to see which assistant is being called.

## May 15, 2025
* **NEW** (UI) LLM provider names are now displayed in the dropdown menu on LLM nodes, making it easier to distinguish between providers of the same type.
* **NEW** The background color for pipeline nodes can be changed.
* **CHANGE** Trace spans for pipeline nodes are now named according to the node name and not the node ID. This makes it easier to understand traces.
* **NEW** Pipeline routing information is now exposed in pipeline state and can be easily accessed via 3 new helper functions in the PythonNode: get_selected_route, get_node_path, get_all_routes.

## May 9, 2025
* **NEW** Chatbot configurations can now be duplicated to create exact copies of the chatbot.

## May 8, 2025
* **BUG** Ensure that chatbot [events](./concepts/events.md) and scheduled messages utilize parameters from the published version of the chatbot.

## May 7, 2025
* **NEW** Link from chatbot version details to a read only view of a pipeline
* **NEW** Tag user messages which are not processed due to an unsupported message type
* **BUG** Correctly fire the 'participant joined' event for participants that already have sessions with other chatbots

## Apr 29, 2025
* **BUG** Fixed an issue where users are unable to view archived experiments / chatbots.
* **NEW** Dark mode support for the chat UI.
* **NEW** The session creation endpoint now supports passing state. Additionally, the state of an existing session can also be updated via the [update state](https://chatbots.dimagi.com/api/docs/#tag/Experiment-Sessions/operation/session_update_state) endpoint.

## Apr 25, 2025
* **NEW** Pipeline bots can now configure surveys and voice settings.

* **NEW** Default keyword can be configured by user on router nodes in pipelines.
* **BUG** Fixed switching between different experiments in participants data view.

## Apr 22, 2025
* **NEW** Router nodes in pipelines can be configured to tag output messages with the node name and the route that was selected. This is useful for understanding the flow of messages through the pipeline.

## Apr 21, 2025
* **NEW** We now only support the participant_data prompt variable for routers.
* **BUG** Fixed an issue where session messages would sometimes not load.

## Apr 15, 2025
* **NEW** Record and display the source of chats that originate from an [embedded chat widget](./how-to/embed.md).

## Apr 11, 2025
* **BUG** Fixed the `{participant_data}` prompt variable which was missing the participants scheduled messages.

## Apr 10, 2025
* **NEW** Bots can now send multimedia files to users using the [Collections feature](./concepts/media_collections.md).
* **BUG** Fixed reminder messages not appearing in web chats.

## Apr 7, 2025
* **BUG** Fixed an issue where if custom actions are removed from a node, it resulted in an error when creating a new version

## Apr 3, 2025
* **NEW** Added support for the static router to read from the session state

## Apr 1, 2025
* **BUG** Deselecting source material in a pipeline node no longer reports an error.

## Mar 31 2025
* **NEW** Page pagination added to chat transcript message list view for sessions with over 100 chats. 100 chats per page.

## Mar 27, 2025
* **NEW** History modes added for chat history compression
  * **Summarize**: Summarizes older messages when token count exceeds the limit.
  * **Truncate Tokens**: Removes older messages to stay within token limits.
  * **Max History Length**: Retains only the last N messages.
* **NEW** Allow chatbot builders to configure whether files referenced by assistants as citations can be downloaded.
* **NEW** Improve citation link rendering using footnotes.

## Mar 26, 2025
* **BUG** Resolved an issue preventing users from creating timeout events.

* **BUG** Can now download sessions with API key via 'Generate Export' button on Experiment Session page

Adds 'does not contain' to participant filter in sessions filter widget

* **BUG** API toggle updates automatically without modifying the filter widget

## Mar 25, 2025
* **NEW** Added a new state that is scoped to the participant's session and can be read and written to using a code node. See the section on [session state](./concepts/pipelines/nodes.md#session-state) for more information.

## Mar 20, 2025
* **BUG** Exclude 'thinking' messages from OpenAI assistant responses. Only the final message from the assistant will be shown.

## Mar 17, 2025
* **NEW** Access to participant's schedules from the python node added via the get_participant_schedules helper function.

* **BUG** Fix a bug where pipelines with tracing and assistant nodes is not working.

* **BUG** Allow using the `{participant_data}` and other prompt variables in Router Node prompts.

## Mar 11, 2025
* **NEW** Experiment Sessions table gains a new filter widget to replace the existing search bars which allows seaching on all and multiple columns.

## Mar 11, 2025
* **BUG** Upgrade the Langfuse library to fix an issue where bots with Langfuse tracing is not responsive.

## Mar 7, 2025

* **NEW** Scheduled messages for chat participants can now be cancelled via the participant's details page.

## Mar 6, 2025

* **NEW** The [Chat Completions API](https://chatbots.dimagi.com/api/docs/#tag/OpenAI) and [New Message API](https://chatbots.dimagi.com/api/docs/#tag/Channels/operation/new_api_message_versioned) endpoints now support a version parameter (`vN`) to specify the working version of the experiment.
* **NEW** Added a button in the versions table to copy the API URL for each version of the experiment.
* **BUG** Fix an error when reading `docx` files: "There is no item named '...' in the archive".
* **BUG** Fix a bug with pipelines which resulted in the bot generating a new scheduled message every time a scheduled message is triggered.

## Mar 5, 2025

* **NEW** Participant global data can be get & set in the Python Node.
* **CHANGE** UI update: Add "(upload file)" text behind title of Code Interpreter Files and File Search Files for clairty to upload files in both locations if desired.

## Feb 27, 2025
* **NEW** The `random` Python module is now available in the Python Node.

## Feb 26, 2025
* **BUG** Fixed an issue where the prompt used to generate ad-hoc bot messages were being saved in the chat history as a user message.
* **BUG** Fixed an issue with the code node causing the pipeline to not load.
* **BUG** Restores ability to create event for the bot to summarize the conversation.

## Feb 25, 2025
* **BUG** Fixed an issue where OpenAI's API message limit was reached before summarizing the conversation.
* **NEW** The Assistants UI now displays the number of uploaded files for code interpreter and file search
* **NEW** Bots will now inform users when something goes wrong while generating a message
* **BUG** Fixed an issue where empty responses caused the bot to malfunction. These responses are now saved as an AI message

## Feb 24, 2025
* **NEW** `.docx` attachments can now be read in the code node.
* **BUG** Prevent event messaging loops by restricting the event options when "a new bot message is received" is selected. This is a followup to the celery issues on Feb 7, 2025.

## Feb 21, 2025

* **NEW**: Add an AI helper for writing code in Python Nodes. [Demo](https://www.loom.com/share/2e2f04f9a8fe4e2da3a957d79f456c3e?sid=63ad91f7-453c-4977-87df-1bc1a6dc950b)

## Feb 19, 2025

* **NEW**: Add support [Deepseek](https://api-docs.deepseek.com/quick_start/pricing) models.
* **NEW**: Added theme toggle in the navbar which allows switching between dark and light theme.
* **CHANGE** The experiment description can now include markdown formatting which will be rendered when it is displayed on the public chatbot pages (the consent page and the pre-survey page).
* **CHANGE** All markdown links in the chatbot now open in a new tab.
* **NEW**: Team deletion modal allows user to select the subset of uses to asynchronously send a team deletion email: just the deleting user, all team admins, all team members.

## Feb 18, 2025:

* **CHANGE** Pipelines are now sorted by name in ascending order in both the pipelines table and dropdown list on the experiment edit page.
* **CHANGE** Allow unauthenticated users (public chat users) to access attachments in their chats.

## Feb 14, 2025:

* **BUG** Fixed an issue where the citations enabled toggle on an assistant node showed that it was disabled when the node was just added, where in reality it was actually enabled.
* **CHANGE** Update the embeddable chat widget to better support mobile devices & allow more customization of the styles.
* **CHANGE** Allow pipeline bots to toggle conversational consent.

## Feb 06, 2025:

* **NEW** Chatbots can now be embedded into external websites. See the [documentation](how-to/embed.md) for more information.
* **CHANGE** Enhanced the participants filter in the experiment sessions view to support multiple participants. This allows you to export chats for selected participants only.
* **CHANGE** Consent forms have become optional. If no consent form is configured then the user will not be prompted to accept a consent form before starting a chat. Pre- and post-surveys are still displayed if there are any configured.

## Jan 29, 2025:

* **CHANGE** Improved pipeline validation logic and display of errors.
* **CHANGE** Improve the changes UI when creating a new experiment version to show the details of referenced objects (e.g. pipelines, assistants, etc).
* **CHANGE** Tag UI improvements to make it easier to add and remove tags from chats and messages.

* **NEW** Chatbot versioning released. See the [documentation](concepts/versioning.md) for more information.
* **NEW** New nodes added to [Pipelines](concepts/pipelines/index.md).
    * [Python Node](concepts/pipelines/nodes.md#python-node): Allows you to run Python code in the pipeline.
    * [OpenAI Assistant Node](concepts/pipelines/nodes.md#assistant): Allows you to use an OpenAI Assistant in the pipeline.
    * [Static Router Node](concepts/pipelines/nodes.md#static-router): Allows you to route messages to different nodes based on a static mapping.
* **NEW** Pipelines can now be tested via the edit UI. This does not currently support history or participant data.
* **NEW** "Trigger Bot Message" API endpoint. This allows you to send a prompt to a bot which will trigger a message to the specified user. See the [API documentation](https://chatbots.dimagi.com/api/docs/#tag/Channels/operation/trigger_bot_message) for more information.
* **NEW** [Custom Actions](concepts/custom_actions.md) allow bots to connect to external APIs and services.
* **NEW** The web chat UI now supports :thumbsup: and :thumbsdown: reactions to bot messages. These reactions are saved as tags on the message.


<!-- commcare connect integration -->

## Dec 12, 2024:

* **NEW** When an experiment is in “debug mode”, errors will be shown to the user in the chat UI.

## Nov 6, 2024:

* **CHANGE** Auto populate channel names with the experiment’s name and improve the channel help text

* **NEW** Added the ability to toggle whether responses should include source citations in the case of assistant based
  experiments. To toggle this, you’ll need to have the “assistant” type selected in the experiment’s edit screen, then
  go
  to the “Advanced” tab. There you will see a “Citations enabled” setting. When this setting is “off”, no citations
  will
  be present in the response.

## Oct 29, 2024:

* **CHANGE**  _[Security update]_ Participants will now have to verify their email address before they can continue to
  the chat
  session.

* **NEW** Added a new “debug mode” for experiments. When an experiment is in debug mode, the user will be able to see.

## Aug 16, 2024:

* **CHANGE** API update: Ability to filter experiment session results using a newly supported “tags” parameter.

## Aug 16, 2024:

* **NEW** Integration with Langfuse for tracing.
* **NEW** Dynamic voice support in a multi bot setup. Users can now choose to let the child bot’s voice be used if it
  generated the output in a multi-bot setup. This behaviour is disabled by default, but can be enabled by going to the
  experiment’s voice configuration settings and checking the Use processor bot voice box.

## Aug 14, 2024:

* **BUG** Fixed tagging in the case where assistants were used as child bots in a router setup
* **CHANGE** Assistants cannot be used as router bots anymore, since this messes up the conversation history on OpenAI’s
  side.

## Aug 5, 2024:

* **NEW** Allow sorting of the “Started“ and “Last Message“ columns in the experiment sessions view
* **NEW** Terminal bot. You can now configure a bot (from an experiment’s homepage) to run at the end of every inference
  call. This terminal bot will change the input according to the configured prompt, even in a multi-bot configuration. A
  terminal bot is useful when you want to ensure that the bot always responds in a certain language.
* **CHANGE** The {source_material} and {participant_data} prompt variables can now only be used once in a prompt.
  Including this variable more than once in the same prompt will not be allowed.
* **BUG** Fixed an issue where assistant generated Word (.docx) files (and possibly others) were being corrupted.

## Aug 1, 2024:

* **CHANGE** Improved data extraction to handle long contexts

## July 26, 2024:

* **NEW** File download support for assistant bots. Cited files that were uploaded by the user or generated by the
  assistant
  can now be downloaded from within the chat. Please note that this only applies to webchats, and the user must be a
  logged in user to download these files.
* **NEW** Twilio numbers will now be verified at the selected provider account before allowing the user to link the
  whatsapp account to an experiement. Please note that this will not be done for Turn.io numbers, since they do not
  provide a mechanism for checking numbers.

## July 19, 2024:

* **NEW** In-conversation file uploads for assistant bots on web based chats. These files will be scoped only to the
  current
  chat/OpenAI thread, so other sessions with the same bot will not be able to query these files.

## July 15, 2024:

* **NEW** Participant data extraction through pipelines.
  You need the “Pipelines” feature flag enabled.
  Usage information can be found here.
* **BUG** Normalize numbers when adding or updating a whatsapp channel. This helps to avoid accidentally creating
  another whatsapp channel with the same number that is in a different format.
* **BUG** Verify Telegram token when adding a telegram channel

## July 8, 2024:

* **NEW** Add {current_datetime} prompt variable to inject the current date and time into the prompt
* **BUG** Fixed a bug with syncing files to OpenAI assistants vector stores
* **BUG** Ensure API keys have the current team attached to them
* **BUG** Enforce team slugs to be lowercase
* **BUG** Update chat history compression to take the full prompt into account including source material, participant
  data
  etc.
* **CHANGE** Redo UI to show team on all pages and use dropdown for team switching and team management links
* **CHANGE** Hide API sessions from ‘My Sessions’ list
* **NEW** User interface for creating and editing Experiment Routes (parent / child experiments)
  New tab on the main experiment page

**API changes**

  * **NEW** API documentation and schema now available at [https://chatbots.dimagi.com/api/docs/](https://chatbots.dimagi.com/api/docs/)
  * **NEW** Experiment session list, detail and create API
  * **CHANGE** Channel message API now takes an optional session field in the request body to specify the ID of a specific
    session
  * **CHANGE** Experiment API output renamed experiment_id to id
  * **CHANGE** Update participant data API POST body format changed. New format:

    ```[{"experiment": "<experiment_id>", "data": {"property1": "value1"}}]```

  * **NEW** OpenAI compatible ‘Chat Completions’ API for experiments. See API docs.

## Jun 24, 2024

* **NEW** Tagging messages based on which bot generated that response in a multi-bot setup

## Jun 17, 2024

* **NEW** Pipelines (alpha)
    * Look for "Pipelines" in the sidebar
    * Ability to run a pipeline based on event triggers
    * Ability to create a pipeline visually
* **NEW** Participant view
    * View participants with their data
    * We added a view where users can see all participants, when they joined initially and what experiments they participated in.
    * Experiment admins will also be able to add or update data to be associated with a participant. When the experiment prompt includes the `{participant_data}` variable, this data will be visible to the bot and participant specific details can be referenced or considered during the conversation.
    * Note that participant data is scoped to the specific experiment. This means that you have to manually add data pertaining to a particular participant to each experiment manually.
* **NEW** Slack integration
    * Ability to connect to a slack workspace as a messaging provider
    * Ability to link an experiment to a Slack Channel (via an experiment channel)
    * Ability to have one 'fallback' experiment which can respond to messages on channels where no other experiment is assigned
    * Experiment responds to 'mentions' and creates a new session as a Slack thread

## Jun 4, 2024

* **CHANGE** Individual tool selection
    * Users can now choose which tools to give to the bot to use.
    * Previously this was obscured by a single “tools enabled” checkbox which - when enabled - gave the bot all the tools that existed at that time.
    * Tools include: One-off Reminder, Recurring Reminder and Schedule Update
    * One-off Reminder: This allows the bot to create a one-time reminder message for some time in the future.
    * Recurring Reminder: This allows the bot to create recurring reminder messages.
    * Schedule Update: This allows the bot to update existing scheduled messages. Please note that this tool cannot update reminders created with the one-off and recurring reminder tools, since those are legacy tools using a different framework. Future work will fix this.
* **CHANGE** When and error occurs during the processing of a user message, the bot will tell the user that something went
    wrong instead of keeping quiet

## May 21, 2024

* **NEW** OpenAI Assistants v2 support
* **NEW** Multi-experiment bots
    * Allows users to combine multiple bots into a single bot, called the “parent” bot. The parent bot will decide which of the “child” bots the user query should be routed to, based on the prompt.
    * The prompt should give clear instruction to the parent bot on how it should decide to route the user query.

## May 15, 2024

* **CHANGE** Experiment search improvements
    * The search string will be used to search for experiments by name first, then by description
* **NEW** OpenChatStudio API: A few endpoints are exposed to allow chatting to a bot using the API

## May 10, 2024

* **NEW** Bots are given knowledge of the date and time
* **NEW** Added a new event type called “A new participant joined the experiment”
* **NEW** Added a new event handler to create scheduled messages

## May 9, 2024

* **NEW** Show participant data in the session review page
    * If participant data exists and was included in the prompt, then reviewers will be able to see the data in the session review page. Seeing the data that the bot had access to might help with understanding the conversation.
* **CHANGE** Anthropic now also supports tool usage!

## Apr 30, 2024

* **NEW** Participant data
    * Participant data allows the bot to tailor responses by considering details about the participant.
    * To include participant data in the prompt, go to the experiment edit page and add the `{participant_data}` variable to an appropriate place in the prompt.
    * Currently we have to create it manually through the admin dashboard, but a near future release will include a dedicated page to view/edit participant data.
    * Please note that participant data is experiment specific, meaning that data we have for a participant in one
experiment may not be the same for the next experiment.
