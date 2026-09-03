# Channels

A **channel** is how your chatbot interacts with participants — such as Telegram, WhatsApp, or Slack. Linking a channel lets participants chat directly on a platform they already use, instead of requiring them to visit a separate web page.

!!! info "Channel vs. platform"
    OCS uses "channel" and "platform" interchangeably. You'll mostly see "channel" in these docs, but some parts of the OCS UI use the label "Platform" for the same thing.

Some channels work out of the box; others require you to first [configure a messaging provider][1] — the account that handles message delivery for that platform. Once a channel is linked to your chatbot, participants can start communicating with it through that platform.

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

## Public link

A **public link** gives your chatbot its own hosted chat page, so anyone with the link can chat with it — no embedding, website, or technical setup required. It's a good fit when you want to share a chatbot directly, for example in an email, a message, or a QR code, rather than adding it to a site with the [chat widget][chat-widget].

The page shows your chatbot's name and description above the chat, and starts participants off with the welcome message and starter questions you configure on the channel. Each chatbot can have one public link at a time.

!!! info "Ask your admin if you don't see this option"
    Public link is an opt-in feature. If it's missing from the add-channel menu, ask your Open Chat Studio admin to turn it on for your team.

!!! warning "Not the same as the public web chat link"
    A public link is a channel you add to the chatbot, with its own link that you can regenerate. It's separate from the older **public web chat link** in the chatbot's **Share** dialog, which sends participants through a consent page first.

### What visitors experience

Visitors always reach your chatbot's **published version** — the same version participants get on any other channel. If you haven't published a version yet, or you've disabled the channel, visitors see a banner instead of a live chat. Team members are exempt from this: while logged in, they can open the page to preview an unpublished chatbot.

A visitor's conversation is tied to their browser tab: it survives a page reload but disappears once the tab is closed. This also means a shared or public computer won't hand the next person the previous visitor's conversation.

See [Deploy your chatbot with a public link][public-link-howto] for how to set one up, share it, and regenerate or remove it.

## File support

Channels differ in whether participants can send files to the chatbot and whether the chatbot can send files back. When the chatbot produces a file that a channel cannot deliver — because the channel doesn't support file sending, or the file's type or size isn't allowed — OCS appends a download link to the chatbot's message instead, so the participant can still get the file.

| Channel | Participants can send files | Chatbot can send files | Types and limits |
|---|---|---|---|
| Web / Chat widget | Yes | As download links | Uploads of up to 50 MB per file (50 MB total per message). Text files are always accepted, along with common document, image, audio and video formats. See the [widget file attachments reference][widget-files] for the full list. |
| API | Yes | As attachment metadata | Same upload limits as the web channel. Files the chatbot produces are returned on the message as attachments with download links. |
| Telegram | No | Yes | Outgoing: images up to 10 MB; audio, video and documents up to 50 MB. Photos and documents sent by participants are not accepted. |
| WhatsApp | Yes | Yes | Incoming: images and documents (a caption becomes the message text). Outgoing: images up to 5 MB, audio and video up to 16 MB, documents up to 100 MB. Applies to all providers (Twilio, Turn.io, Meta Cloud API). |
| Facebook Messenger | No | As download links | No files in either direction; text and voice messages only. |
| Slack | No | Yes | Outgoing: images, audio, video and documents up to 50 MB. |
| Email | Yes | Yes | Attachments up to 20 MB in both directions. Executable file types are blocked. See [email file attachments][email-files] for details. |
| SureAdhere | No | As download links | No files in either direction; text messages only. |

!!! info "Voice notes"
    Voice notes are handled separately from file attachments. On channels with voice support (Telegram, WhatsApp and Facebook Messenger), a voice note from the participant is transcribed and processed as a regular message rather than being treated as a file.

!!! info "Public link"
    A public link hosts the same chat widget as the Web / Chat widget channel, so the same file support applies.

## Disabling a channel

Every linked channel has an **Enabled** toggle. Turning it off is a way to pause a channel — for maintenance, to retire it temporarily, or to stop unwanted traffic — without deleting the channel and losing its configuration.

While a channel is disabled:

- **Participants can't start a new conversation on it.** This covers the embedded chat widget, the public web chat link, Slack, and starting a chat from the chatbot's management pages in OCS itself. Two API endpoints are exceptions — see [Known limitations](../how-to/disable_a_channel.md#known-limitations).
- **The chatbot doesn't send anything to that channel on its own.** Scheduled messages, [event action](events.md) messages, and messages triggered through the API are all held back rather than delivered.
- **Messages sent to the channel are ignored.** They aren't processed or recorded, and the chatbot doesn't reply — unless you've configured a disabled message.

A **disabled message** is an optional static reply for the channel. When a participant messages a disabled channel, or tries to start a conversation on it, this message is sent back in place of a chatbot response. It's only ever sent as a reply to something a participant did — it's never pushed out on its own, so it won't appear alongside a scheduled or event message that got suppressed. Leaving it blank keeps the channel silent instead. Staff starting a chat from the OCS console see a generic error rather than this message.

!!! info "Public link is different"
    A disabled **public link** shows visitors a banner instead of the chat, rather than sending a disabled message. Disabling, deleting, or [regenerating the link][public-link-howto] also ends any conversations still open on it — see [Deploy your chatbot with a public link][public-link-howto].

See [Disable a channel](../how-to/disable_a_channel.md) for how to turn a channel off and what participants see on each entry point.

## See also
- [Disable a channel](../how-to/disable_a_channel.md)
- [Deploying your chatbot to different channels](../how-to/deploy_to_different_channels.md)
- [Deploy your chatbot with a public link][public-link-howto]

[1]: ./team/messaging_providers.md
[widget-files]: ../chat_widget/reference.md#file-attachments
[email-files]: ../how-to/deploy_email_channel.md#file-attachments
[chat-widget]: ../chat_widget/index.md
[public-link-howto]: ../how-to/deploy_public_link_channel.md
