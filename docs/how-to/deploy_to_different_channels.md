# Deploy your chatbot to different platforms

To link a channel to your chatbot:

!!! info "Note"
    Not all channels require a provider.

1. Navigate to the **Chatbot** you wish to embed.
2. Click on the :material-plus: (plus) icon and select the [provider][2] from the dropdown.
3. Complete the form and click **Create**. Follow the guide below to get the required information for each channel.

You may need to [Configure a messaging provider][6] before you will be able to select it from the dropdown.

## Web and API
The web channel uses the web interface and is enabled by default for all chatbots. Likewise, all chatbots can be accessed via the [APIs][api].

## Telegram
- Follow [this guide][1] to create a Telegram chatbot.
- Copy the chatbot token and paste it into the form on OCS. It will look something like this: `4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc`.

!!! info "Note"
    Depending on your usecase, you probably want to disable group joins for your chatbot on Telegram. Since your telegram chatbot is public, anyone can add it to a group, which could end up costing you a lot. To achieve this, use the [setjoingroups][5] setting in BotFather.

## WhatsApp

Open Chat Studio supports multiple WhatsApp providers. Choose the section below that matches the provider you have configured.

### Twilio and Turn.io

#### Twilio

When you create or edit a WhatsApp channel using a Twilio provider, Open Chat Studio automatically configures the webhook in your Twilio messaging service. When you delete the channel, the webhook is cleared automatically. You do not need to copy or paste any webhook URL.

!!! info "Sandbox numbers and other exceptions"
    Automatic webhook configuration is not supported for Twilio sandbox numbers or in cases where OCS cannot reach the Twilio API. If auto-configuration fails, OCS will display manual setup instructions instead. Follow the steps in the [Twilio webhook configuration guide][3] and enter the following webhook URL in your messaging service settings:

    `https://openchatstudio.com/channels/whatsapp/incoming_message`

#### Turn.io

Turn.io does not support automatic webhook configuration. After adding your WhatsApp number in Open Chat Studio, configure the webhook manually:

1. In your Turn.io account, go to **Settings → API & Webhooks**.
2. Select **Add a webhook**.
3. Enter the following URL:

   `https://openchatstudio.com/channels/whatsapp/incoming_message`

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

Before configuring a Slack channel for your chatbot, you need to set up a Slack messaging provider. This requires:

- Admin access to your Slack workspace
- Following the Slack OAuth and application installation flow
- Configuring the messaging provider in Open Chat Studio (see [Configure a messaging provider][6])

Once your Slack messaging provider is configured, you can link channels to your chatbot.

### Configuration Options

There are three different ways to configure how your chatbot responds to messages in Slack. The chatbot will check each configuration in order of priority:

### 1. Respond to messages from a single channel (Highest Priority)

- Specify the channel name (with or without the '#' prefix) in the channel configuration form.
- This is the highest specificity - messages on this channel will only be responded to by this chatbot.
- Only one chatbot can be configured per Slack channel.

### 2. Respond to messages from any channel using keyword matching

- Enter keywords separated by commas in the keyword field (e.g., `support, help, assistance`).
- Keywords are matched using exact word matching (case-insensitive) to the first word of the user's message.
- Multiple keywords can be used to trigger the chatbot.
- Keywords must be unique to this chatbot & Slack workspace combination.

### 3. Respond to messages from all channels (Lowest Priority)

- The chatbot will respond to any message on any channel if it hasn't matched one of the previous two configurations.
- This is the lowest priority matching option.
- Only one chatbot per Slack workspace can be configured with this option.

### chatbot Interaction

Once the channel is linked, users interact with the chatbot by mentioning it in Slack messages. The chatbot mention name is determined by your Slack app configuration. For example, on the Dimagi hosted instance of Open Chat Studio, the chatbot is mentioned using `@Dimagi Bots`.

!!! info "Priority and Precedence"
    If multiple chatbots could match a message, the chatbot with the most specific configuration wins:

    1. Single channel configuration (highest priority)
    2. Keyword matching
    3. Respond to all channels (lowest priority)

## SureAdhere
- Enter the Tenant ID that would have been provided to you when setting up your SureAdhere account.
- After you submit the form, you will be provided with a webhook URL. Copy this URL and navigate back to your provider's settings to configure it with this URL.

## Email

The email channel lets users interact with your chatbot by sending and receiving emails, including routing, thread continuity, and file attachments.

See the [Email channel guide](deploy_email_channel.md) for full setup and configuration details.

[1]: https://core.telegram.org/bots#how-do-i-create-a-bot
[2]: ../concepts/team/messaging_providers.md
[3]: https://www.twilio.com/docs/WhatsApp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/Facebook-messenger#setting-up-the-Facebook-messenger-channel
[5]: https://core.Telegram.org/bots/features#:~:text=/setjoingroups%20%E2%80%93%20toggle%20whether%20your%20bot%20can%20be%20added%20to%20groups%20or%20not.%20All%20bots%20must%20be%20able%20to%20process%20direct%20messages%2C%20but%20if%20your%20bot%20was%20not%20designed%20to%20work%20in%20groups%2C%20you%20can%20disable%20this.
[6]: ../tutorials/configure_providers.md
[api]: ../tech-hub/api_access.md
[meta]: ./whatsapp_meta_cloud_api.md
