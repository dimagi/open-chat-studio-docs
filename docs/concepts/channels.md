# Channels

A **channel** is how your chatbot interacts with participants — such as Telegram, WhatsApp, or Slack. Linking a channel lets participants chat directly on a platform they already use, instead of requiring them to visit a separate web page.

!!! info "Channel vs. platform"
    Open Chat Studio (OCS) uses "channel" and "platform" interchangeably. You'll mostly see "channel" in these docs, but some parts of the OCS UI use the label "Platform" for the same thing.

Some channels work out of the box.
Others require you to first [configure a messaging provider][1], the account that handles message delivery for that platform.
Once a channel is linked to your chatbot, participants can start communicating with it through that platform.

The currently supported channels are:

- Web / Chat widget
- Public link
- Telegram
- WhatsApp
- Facebook Messenger
- Slack
- API
- SureAdhere In-App Messaging
- Email
- CommCare Connect

## Public link

A **public link** gives your chatbot its own hosted chat page.
Anyone with the link can chat with it, with no embedding, website, or technical setup required.
Use it to share a chatbot directly, such as in an email or QR code.
The alternative is adding the chatbot to a site with the [chat widget][chat-widget].

The page shows your chatbot's name and description above the chat.
It starts participants with the welcome message and starter questions you configure on the channel.
Each chatbot can have one public link at a time.

!!! warning "Not the same as the public web chat link"
    A public link is a channel you add to the chatbot, with its own link that you can regenerate. It's separate from the older **public web chat link** in the chatbot's **Share** dialog, which sends participants through a consent page first.

### What visitors experience

Visitors always reach your chatbot's [published version](versioning.md) — the same version participants get on any other channel. If you haven't published a version yet, or you've disabled the channel, visitors see a banner instead of a live chat. Team members are exempt from this: while logged in, they can open the page to preview an unpublished chatbot.

A visitor's conversation is tied to their browser tab: it survives a page reload but disappears once the tab is closed. On a shared or public computer, the next person cannot see the previous visitor's conversation.

See [Deploy your chatbot with a public link][public-link-howto] for how to set one up, share it, and regenerate or remove it.

## File support

Channels differ in whether participants can send files to the chatbot and whether the chatbot can send files back.
A channel may be unable to deliver a file the chatbot produces.
This happens when the channel doesn't support file sending, or when the file's type or size isn't allowed.
In that case, OCS appends a download link to the chatbot's message so the participant can still get the file.

| Channel | Participants can send files | Chatbot can send files | Types and limits |
|---|---|---|---|
| Web / Chat widget | Yes | As download links | Uploads of up to 50 MB per file (50 MB total per message). Executable and installer files are rejected with an error naming the file. Text files are always accepted, along with common document, image, audio and video formats. See the [widget file attachments reference][widget-files] for the full list. |
| API | Yes | As attachment metadata | Same upload limits and executable file restrictions as the web channel. Files the chatbot produces are returned on the message as attachments with download links. |
| Telegram | No | Yes | Outgoing: images up to 10 MB; audio, video and documents up to 50 MB. Photos and documents sent by participants are not accepted. |
| WhatsApp | Yes | Yes | Incoming: images and documents (a caption becomes the message text). Executable and installer files are dropped and a note is added to the message text. Outgoing: images up to 5 MB, audio and video up to 16 MB, documents up to 100 MB. Applies to all providers (Twilio, Turn.io, Meta Cloud API). |
| Facebook Messenger | No | As download links | No files in either direction; text and voice messages only. |
| Slack | No | Yes | Outgoing: images, audio, video and documents up to 50 MB. |
| Email | Yes | Yes | Attachments up to 20 MB in both directions. Executable and installer files are dropped and a note is added to the message text. See [email file attachments][email-files] for details. |
| SureAdhere | No | As download links | No files in either direction; text messages only. |
| CommCare Connect | No | Yes | Images and files arrive in the Connect app with the message, encrypted end to end like the text. Each file can be up to 2.5 MB, and each reply can include up to 10 files and 15 MB in total. Attachments expire after 90 days. See [CommCare Connect attachments](#commcare-connect-attachments). |

!!! info "Executable and installer files"
    Participants cannot send executable or installer files (such as `.exe`, `.msi` and `.dmg`) on any channel.
    The check also uses the detected file content, so a Windows executable renamed to `report.pdf` is rejected.
    This restriction is always on and does not count as an abuse strike.

!!! info "Voice notes"
    Voice notes are handled separately from file attachments.
    On channels with voice support (Telegram, WhatsApp and Facebook Messenger), OCS transcribes a participant's voice note and processes it as a regular message.

!!! info "Public link"
    A public link hosts the same chat widget as the Web / Chat widget channel, so the same file support applies.

### CommCare Connect attachments

On the CommCare Connect channel, files and images that the chatbot sends are delivered in the Connect app together with the message.
Files can come from a [media collection](collections/media_collections.md) (through the attach media tool) or from a [Python node](pipelines/nodes.md#python-node).

- A file over 2.5 MB is sent as a download link in the message text instead.
- If a reply has more than 10 files or more than 15 MB of files in total, the files that exceed the limit are sent as download links in the message text.
- Attachments expire after 90 days.
- Participants on an app version that cannot show attachments see "Your version of the app is too old to see this message. Please update your Android app." in place of any message that has attachments.

## Disabling a channel

Every linked channel has an **Enabled** toggle.
Turning it off pauses a channel, for example for maintenance, to retire it temporarily, or to stop unwanted traffic.
The channel and its configuration are kept.

While a channel is disabled:

- **Participants can't start a new conversation on it.** This covers the embedded chat widget, the public web chat link, Slack, and starting a chat from the chatbot's management pages in OCS itself. Two API endpoints are exceptions — see [Known limitations](../how-to/disable_a_channel.md#known-limitations).
- **The chatbot doesn't send anything to that channel on its own.** Scheduled messages, [event action](events.md) messages, and messages triggered through the API are all held back rather than delivered.
- **Messages sent to the channel are ignored.** They aren't processed or recorded, and the chatbot doesn't reply — unless you've configured a disabled message.

A **disabled message** is an optional static reply for the channel. When a participant messages a disabled channel or tries to start a conversation on it, this message replaces the chatbot's response.
It is only sent as a reply to something a participant did.
It is never sent on its own, so it does not appear alongside a suppressed scheduled or event message.
Leaving it blank keeps the channel silent instead.
Staff starting a chat from the OCS console see a generic error rather than this message.

!!! info "Public link is different"
    A disabled **public link** shows visitors a banner instead of the chat, rather than sending a disabled message. Disabling, deleting, or [regenerating the link][public-link-howto] also ends any conversations still open on it — see [Deploy your chatbot with a public link][public-link-howto].

See [Disable a channel](../how-to/disable_a_channel.md) for how to turn a channel off and what participants see on each entry point.

## Archiving a chatbot

Archiving a chatbot releases the identifiers that connect it to its channels, such as a Telegram bot token.
While the chatbot is archived, another chatbot can use those identifiers.

When you un-archive the chatbot, you can choose to reconnect its channels.
OCS skips any channel whose identifier another chatbot now uses, and it always skips Slack channels.
To reconnect a skipped channel, free its identifier on the other chatbot if needed, then add the channel again.
See [Deploying your chatbot to different channels](../how-to/deploy_to_different_channels.md).

## See also

- [Disable a channel](../how-to/disable_a_channel.md)
- [Deploying your chatbot to different channels](../how-to/deploy_to_different_channels.md)
- [Deploy your chatbot with a public link][public-link-howto]
- [Chat Sessions](sessions.md)
- [Versioning](versioning.md)

[1]: ./team/messaging_providers.md
[widget-files]: ../chat_widget/reference.md#file-attachments
[email-files]: ../how-to/deploy_email_channel.md#file-attachments
[chat-widget]: ../chat_widget/index.md
[public-link-howto]: ../how-to/deploy_public_link_channel.md
