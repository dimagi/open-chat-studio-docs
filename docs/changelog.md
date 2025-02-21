---
hide:
  - navigation
---

# Changelog

## Feb 21, 2025

* **NEW**: Add an AI helper for writing code in Python Nodes. [Demo](https://www.loom.com/share/2e2f04f9a8fe4e2da3a957d79f456c3e?sid=63ad91f7-453c-4977-87df-1bc1a6dc950b)
* **NEW** `.docx` attachments can now be read in the code node.

## Feb 19, 2025

* **NEW**: Add support [Deepseek](https://api-docs.deepseek.com/quick_start/pricing) models.
* **NEW**: Added theme toggle in the navbar which allows switching between dark and light theme. 
* **CHANGE** The experiment description can now include markdown formatting which will be rendered when it is displayed on the public chatbot pages (the consent page and the pre-survey page).
* **CHANGE** All markdown links in the chatbot now open in a new tab.

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
