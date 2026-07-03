# Channels

To enable users to interact with your bot through external social media platforms and similar services, OCS integrates with various [messaging providers][1]. This integration allows you to deploy your bot to external platforms. Once a platform is linked to your bot, users can communicate with it through that platform. In OCS, the term "channel" is synonymous with "platform."

The currently supported channels are:

- Telegram
- WhatsApp
- Facebook Messenger
- Slack
- API
- SureAdhere
- Email

## File support

Channels differ in whether users can send files to the bot and whether the bot can send files back. When the bot produces a file that a channel cannot deliver — because the channel doesn't support file sending, or the file's type or size isn't allowed — OCS appends a download link to the bot's message instead, so the user can still get the file.

| Channel | Users can send files | Bot can send files | Types and limits |
|---|---|---|---|
| Web / Chat widget | Yes | As download links | Uploads of up to 50 MB per file (50 MB total per message). Text files are always accepted, along with common document, image, audio and video formats. See the [widget file attachments reference][widget-files] for the full list. |
| API | Yes | As attachment metadata | Same upload limits as the web channel. Files the bot produces are returned on the message as attachments with download links. |
| Telegram | No | Yes | Outgoing: images up to 10 MB; audio, video and documents up to 50 MB. Photos and documents sent by users are not accepted. |
| WhatsApp | Yes | Yes | Incoming: images and documents (a caption becomes the message text). Outgoing: images up to 5 MB, audio and video up to 16 MB, documents up to 100 MB. Applies to all providers (Twilio, Turn.io, Meta Cloud API). |
| Facebook Messenger | No | As download links | Text and voice messages only. |
| Slack | No | Yes | Outgoing: images, audio, video and documents up to 50 MB. |
| Email | Yes | Yes | Attachments up to 20 MB in both directions. Executable file types are blocked. See [email file attachments][email-files] for details. |
| SureAdhere | No | As download links | Text messages only. |

!!! info "Voice notes"
    Voice notes are handled separately from file attachments. On channels with voice support (Telegram and WhatsApp), a voice note from the user is transcribed and processed as a regular message rather than being treated as a file.

## See also
- [Deploying your bot to different channels](../how-to/deploy_to_different_channels.md)

[1]: ./team/messaging_providers.md
[widget-files]: ../chat_widget/reference.md#file-attachments
[email-files]: ../how-to/deploy_to_different_channels.md#file-attachments
