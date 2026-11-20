# Configure Chatbot Settings

This guide covers the chatbot settings that take more than one step to configure.
For a short description of every field on the **Settings** tab, see [Chatbot settings](../concepts/chatbots/index.md#chatbot-settings).

The **Settings** tab is on the chatbot's page, next to **Sessions**, **Versions** and **Events**.
It is not the same as the **Advanced** settings on a [pipeline node](../concepts/pipelines/nodes.md).

## Prerequisites

- You have permission to change chatbots.
- For voice replies, your team has a [speech provider](../concepts/team/speech_providers.md) set up.

## Edit the settings

1. Open the chatbot.
2. Select the **Settings** tab.
3. Click **Edit**.
4. Change the fields you need, then save.

Settings changes apply to the unreleased version.
They reach participants on the published chatbot after you [publish a new version](../tutorials/versioning_steps.md).

## Set up voice replies

Voice replies work on channels with voice support: Telegram, WhatsApp and Facebook Messenger.

1. Open the **Settings** tab and click **Edit**.
2. Under **Speech**, select a **Provider**.
3. Select a **Synthetic Voice**.
   The list shows only the voices of the selected provider.
4. Set **Response Type**:
    - **Always**: every reply is sent as a voice message.
    - **Reciprocal**: the chatbot replies with voice only when the participant sends a voice note.
    - **Never**: every reply is sent as text.
5. Optionally, select **Echo Transcript**.
   The chatbot then sends the participant the text it transcribed from their voice note, before its reply.
6. Save, then publish a new version.

A participant who sends a voice note on WhatsApp gets a voice reply in the selected voice when **Response Type** is **Reciprocal**.
If they type a message, they get a text reply.

## Set a seed message

A seed message starts a new web chat session without waiting for the participant.

1. Open the **Settings** tab and click **Edit**.
2. In **Seed Message**, enter the text to send to the chatbot when a session starts.
   Write it as an instruction to the chatbot, for example "Greet the participant and ask for their name."
3. Save, then publish a new version.

When a participant opens a new web chat, OCS sends the seed message to the chatbot.
The participant sees the chatbot's reply as the first message of the chat.

## Set an unavailable message

Sometimes a chatbot cannot reply, for example when its LLM provider is down or rejects the configured API key.
Participants then get a default error reply: "Sorry, something went wrong while processing your message. Please try again later".

1. Open the **Settings** tab and click **Edit**.
2. In **Unavailable Message**, enter the text to send after the default error reply.
   For example, say when to try again or give another way to get help.
3. Save, then publish a new version.

The message is sent on every channel.
Errors the participant can fix, such as an unsupported file type, keep their own message.

## Archive and un-archive a chatbot

Archive a chatbot to retire it without losing it.

1. Open the chatbot and select the **Settings** tab.
2. Click **Archive** and confirm.

Archiving does the following:

- It releases the chatbot's channel identifiers, such as a Telegram bot token, so another chatbot can use them.
- It deletes the chatbot's scheduled messages.
- It archives the chatbot's pipeline, unless another live chatbot uses it or a static trigger starts it.
  The pipeline builder of an archived chatbot opens read-only.

To bring the chatbot back:

1. Open the archived chatbot.
   The **Archived** badge appears on its page.
2. Click **Un-archive**, beside the **Archived** badge.
3. Optionally, select the checkbox to reconnect the chatbot's channels.
   The checkbox is off by default.
4. Confirm.

The chatbot, all its versions and its pipeline are restored.
Scheduled messages deleted at archive time are not restored.

When you reconnect channels, OCS skips any channel whose identifier another chatbot now uses, and names each skipped channel in a warning.
It always skips Slack channels.
To reconnect a skipped channel, free its identifier on the other chatbot if needed, then [add the channel again](channels/deploy_to_different_channels.md).

## Common issues

- **No voices are listed.** Your team has no speech provider, or no **Provider** is selected yet.
- **A setting change doesn't reach participants.** Publish a new version of the chatbot.
- **The Archive or Un-archive button is missing.** You may not have permission to change chatbots.
- **A channel is still disconnected after un-archiving.** You did not select the checkbox, another chatbot uses the identifier, or it is a Slack channel.

## See also

- [Chatbots](../concepts/chatbots/index.md)
- [Speech Service Providers](../concepts/team/speech_providers.md)
- [Consent Forms](../concepts/consent.md)
- [Configure Langfuse Trace Sampling](configure_langfuse_trace_sampling.md)
- [Versioning](../concepts/versioning.md)
