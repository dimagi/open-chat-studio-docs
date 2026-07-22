# Deploy Your Chatbot to Email

The email channel lets participants interact with your chatbot by sending and receiving emails.

## Configuration

When creating an email channel, the form has the following fields:

- **Email address**: The inbound address that participants send messages to. Incoming emails addressed to this value are routed to this chatbot.
- **From address**: The address that appears in the "From" field of outgoing replies.
- **Default channel**: When enabled, this channel acts as the fallback for inbound emails that do not match any other configured email address in your team.

!!! info "Note"
    Only one email channel per team can be set as the default.

## How routing works

Inbound emails are matched to the correct chatbot in this order:

1. **In-Reply-To header** - If the email is a reply to a previous message sent by the chatbot, it is routed to the same channel and continues the existing conversation thread.
2. **To address** - If no prior thread is found, the recipient address is matched against configured email channels.
3. **Default channel** - If no address match is found, the email is delivered to the team's default email channel (if one is configured).

## Thread continuity

Replying to a chatbot email continues the same conversation session. Sending a fresh email to the channel address starts a new session.

## Customizing the outbound subject

When the chatbot starts a new email thread (for example, via the [Trigger bot Message](https://www.openchatstudio.com/api/v1/docs/#tag/Channels/operation/trigger_bot_message) API), the subject line defaults to "New message". To override this, set an `email_subject` value in [session state](../tech-hub/python_node.md#session-state) before the email is sent — for example from a pipeline's Python node, or via the `session_data` parameter when triggering the chatbot. Inbound reply threads always reuse the subject of the original email and are unaffected by this value.

## File attachments

The email channel supports bidirectional file attachments. For a comparison of file support across all channels, see [channel file support](../concepts/channels.md#file-support).

### Inbound attachments (participant to chatbot)

When a participant emails files to the chatbot, each attachment is saved and made available to the LLM or pipeline as a file record. Attachments behave like files uploaded through any other channel: they appear in the `attachments` list in the pipeline's [temporary state](../tech-hub/python_node.md#attachments) and are passed to the LLM for processing.

The following attachments are rejected automatically:

| Rejection reason | How it appears to the chatbot |
|---|---|
| File exceeds 20 MB | Bracketed note in the message text, e.g. `[Attachment "report.zip" was rejected: file too large (max 20 MB)]` |
| Executable file type (e.g. `.exe`, `.sh`) | Bracketed note in the message text |
| Content-type mismatch (declared MIME type does not match actual file bytes) | Bracketed note in the message text |

Rejection notes are inserted inline into the participants's message so the chatbot can read them and explain the problem to the participant in its reply.

### Outbound attachments (chatbot to participant)

Files produced by the pipeline are sent as MIME attachments in the same threaded reply as the chatbot's text response. From a Python node, call `add_file_attachment()` to attach a file — see the [Python Node documentation](../tech-hub/python_node.md#python_node.add_file_attachment) for the full API reference and example.

If a pipeline-produced file cannot be sent as an attachment (for example, it exceeds the size limit or is a denylisted type), the email body will contain an inline download link for that file instead.

## See also

- [Deploy your chatbot to different channels](deploy_to_different_channels.md)
- [Python Node documentation](../tech-hub/python_node.md)
