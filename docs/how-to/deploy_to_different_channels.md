# Deploy your bot to different platforms

To link a channel to your bot:

!!! info "Note"
    Not all channels require a provider.

1. Navigate to the **Chatbot** you wish to embed.
2. Click on the :material-plus: (plus) icon and select the [provider][2] from the dropdown.
3. Complete the form and click **Create**. Follow the guide below to get the required information for each channel.

You may need to [Configure a messaging provider][6] before you will be able to select it from the dropdown. 

## Web and API
The web channel uses the web interface and is enabled by default for all bots. Likewise, all bots can be accessed via the [APIs][api].

## Telegram
- Follow [this guide][1] to create a Telegram bot.
- Copy the bot token and paste it into the form on OCS. It will look something like this: `4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc`.


!!! info "Note"
    Depending on your usecase, you probably want to disable group joins for your bot on Telegram. Since your telegram bot is public, anyone can add it to a group, which could end up costing you a lot. To achieve this, use the [setjoingroups][5] setting in BotFather.

## WhatsApp

Open Chat Studio supports multiple WhatsApp providers. Choose the section below that matches the provider you have configured.

### Twilio and Turn.io

#### Setting Up Your WhatsApp Channel

1. **Add your WhatsApp number to the form** in the Open Chat Studio channels section.

2. **Configure the webhook URL in your provider:**

   The webhook URL is always: `https://openchatstudio.com/channels/whatsapp/incoming_message`

   This URL is the same for all WhatsApp chatbots and channels on Open Chat Studio.

#### Provider-Specific Configuration

##### For New WhatsApp Numbers
If you're setting up a brand new WhatsApp number, you'll need:
- Admin access to your Twilio/Turn.io account
- To register the number with Meta/WhatsApp
- To configure the webhook URL in your provider settings

##### For Existing WhatsApp Numbers
If you're reusing an existing WhatsApp number that was previously configured for Open Chat Studio:
- **No additional webhook configuration needed** - the number is already set up to forward messages to Open Chat Studio
- Simply add the number to your bot's channels in Open Chat Studio

##### Provider Instructions
- **For Twilio:** See [this page][3] to configure the webhook URL in your messaging service
- **For Turn.io:** Go to Settings → API & Webhooks → Add a webhook and paste the OCS webhook URL

### Meta Cloud API

Meta Cloud API connects your chatbot directly to the WhatsApp Business Platform without a third-party intermediary. The setup requires a Meta for Developers account and a WhatsApp Business Account.

See the [Meta Cloud API setup guide][meta] for full step-by-step instructions.


## Facebook Messenger
!!! info "Note"
    It is assumed that you already have a Facebook page and a Twilio account with the Facebook page linked. Follow [this guide][4] if this is not the case.

- Add the ID of your Facebook page.
- After you submit the form, you will be provided with a webhook URL. Copy this URL and navigate back to your provider's settings to configure it with this URL.
    - For Twilio, edit your Facebook page settings and paste the URL into the "Webhook URL for incoming messages" field.

## Slack

### Prerequisites

Before configuring a Slack channel for your bot, you need to set up a Slack messaging provider. This requires:

- Admin access to your Slack workspace
- Following the Slack OAuth and application installation flow
- Configuring the messaging provider in Open Chat Studio (see [Configure a messaging provider][6])

Once your Slack messaging provider is configured, you can link channels to your bot.

### Configuration Options

There are three different ways to configure how your bot responds to messages in Slack. The bot will check each configuration in order of priority:

### 1. Respond to messages from a single channel (Highest Priority)

- Specify the channel name (with or without the '#' prefix) in the channel configuration form.
- This is the highest specificity - messages on this channel will only be responded to by this bot.
- Only one bot can be configured per Slack channel.

### 2. Respond to messages from any channel using keyword matching

- Enter keywords separated by commas in the keyword field (e.g., `support, help, assistance`).
- Keywords are matched using exact word matching (case-insensitive) to the first word of the user's message.
- Multiple keywords can be used to trigger the bot.
- Keywords must be unique to this bot & Slack workspace combination.

### 3. Respond to messages from all channels (Lowest Priority)

- The bot will respond to any message on any channel if it hasn't matched one of the previous two configurations.
- This is the lowest priority matching option.
- Only one bot per Slack workspace can be configured with this option.

### Bot Interaction

Once the channel is linked, users interact with the bot by mentioning it in Slack messages. The bot mention name is determined by your Slack app configuration. For example, on the Dimagi hosted instance of Open Chat Studio, the bot is mentioned using `@Dimagi Bots`.

!!! info "Priority and Precedence"
    If multiple bots could match a message, the bot with the most specific configuration wins:

    1. Single channel configuration (highest priority)
    2. Keyword matching
    3. Respond to all channels (lowest priority)

## SureAdhere
- Enter the Tenant ID that would have been provided to you when setting up your SureAdhere account.
- After you submit the form, you will be provided with a webhook URL. Copy this URL and navigate back to your provider's settings to configure it with this URL.

## Email

The email channel lets users interact with your bot by sending and receiving emails.

### Configuration

When creating an email channel, the form has the following fields:

- **Email address**: The inbound address that users send messages to. Incoming emails addressed to this value are routed to this bot.
- **From address**: The address that appears in the "From" field of outgoing replies.
- **Default channel**: When enabled, this channel acts as the fallback for inbound emails that do not match any other configured email address in your workspace.

!!! info "Note"
    Only one email channel per workspace can be set as the default.

### How routing works

Inbound emails are matched to the correct bot in this order:

1. **In-Reply-To header** - If the email is a reply to a previous message sent by the bot, it is routed to the same channel and continues the existing conversation thread.
2. **To address** - If no prior thread is found, the recipient address is matched against configured email channels.
3. **Default channel** - If no address match is found, the email is delivered to the workspace's default email channel (if one is configured).

### Thread continuity

Replying to a bot email continues the same conversation session. Sending a fresh email to the channel address starts a new session.

### File attachments

The email channel supports bidirectional file attachments.

#### Inbound attachments (user to bot)

When a user emails files to the bot, each attachment is saved and made available to the LLM or pipeline as a file record. Attachments behave like files uploaded through any other channel: they appear in the `attachments` list in the pipeline's [temporary state](../tech-hub/python_node.md#attachments) and are passed to the LLM for processing.

The following attachments are rejected automatically:

| Rejection reason | How it appears to the bot |
|---|---|
| File exceeds 20 MB | Bracketed note in the message text, e.g. `[Attachment "report.zip" was rejected: file too large (max 20 MB)]` |
| Executable file type (e.g. `.exe`, `.sh`) | Bracketed note in the message text |
| Content-type mismatch (declared MIME type does not match actual file bytes) | Bracketed note in the message text |

Rejection notes are inserted inline into the user's message so the bot can read them and explain the problem to the user in its reply.


#### Outbound attachments (bot to user)

Files produced by the pipeline are sent as MIME attachments in the same threaded reply as the bot's text response. To attach a file from a Python node, call `add_file_attachment()`:

```python
def main(input, **kwargs) -> str:
    response = http.get("https://api.example.com/report.pdf", auth="reports-api")

    if response["is_success"]:
        add_file_attachment(
            filename="report.pdf",
            content=response["response_bytes"]
        )
        return "I've attached the report."

    return "Failed to retrieve the report."
```

See the [Python Node documentation](../tech-hub/python_node.md#python_node.add_file_attachment) for the full `add_file_attachment()` API reference.

If a pipeline-produced file cannot be sent as an attachment (for example, it exceeds the size limit or is a denylisted type), the email body will contain an inline download link for that file instead.


[1]: https://core.telegram.org/bots#how-do-i-create-a-bot
[2]: ../concepts/team/messaging_providers.md
[3]: https://www.twilio.com/docs/WhatsApp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/Facebook-messenger#setting-up-the-Facebook-messenger-channel
[5]: https://core.Telegram.org/bots/features#:~:text=/setjoingroups%20%E2%80%93%20toggle%20whether%20your%20bot%20can%20be%20added%20to%20groups%20or%20not.%20All%20bots%20must%20be%20able%20to%20process%20direct%20messages%2C%20but%20if%20your%20bot%20was%20not%20designed%20to%20work%20in%20groups%2C%20you%20can%20disable%20this.
[6]: ../tutorials/configure_providers.md
[7]: https://openchatstudio.com/users/profile/
[8]: https://openchatstudio.com/api/docs/
[api]: ../tech-hub/api_access.md
[meta]: ./whatsapp_meta_cloud_api.md
