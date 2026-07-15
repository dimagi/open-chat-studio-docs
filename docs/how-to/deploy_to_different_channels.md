# Deploy your chatbot to different channels

To link a channel to your chatbot:

1. Navigate to the **Chatbot** you wish to link to a channel.
2. Click on the :material-plus: (plus) icon and select the [channel][2] from the dropdown.
3. Complete the form and click **Create**.
4. Follow the guide below to get the required information for your selected channel.

!!! info "The channel you want is not shown in the dropdown"

    You may need to [configure a messaging provider][6] for the platform before you can select it from the dropdown.
    Not all channels require a messaging provider.

## Supported Channels

- [Web Embedded Widget](#web) — built-in chat interface, no setup required
- [Telegram](#telegram)
- [WhatsApp](#whatsapp) — Twilio, Turn.io, or [Meta Cloud API](#meta-cloud-api)
- [Facebook Messenger](#facebook-messenger)
- [Slack](#slack)
- [Email](#email)
- [SureAdhere](#sureadhere-for-in-app-messaging)
- [API](#api) — programmatic access, no setup required

## Web

The web channel is OCS's built-in chat interface. It's enabled by default for every chatbot — there's no provider to configure and nothing to link. Embed it on your own website with the [chat widget][chat-widget].

## Telegram

1. Follow [this guide][1] to create a Telegram chatbot.
2. Copy the chatbot token and paste it into the form on OCS. It will look something like this: `4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc`.

!!! info "Note"

    Depending on your use case, you probably want to disable group joins for your chatbot on Telegram. Since your Telegram chatbot is public, anyone can add it to a group, which could result in significant costs. To achieve this, use the [setjoingroups][5] setting in BotFather.

## WhatsApp

Open Chat Studio supports multiple WhatsApp providers. Choose the section below that matches the provider you have configured.

### Twilio

When you create or edit a WhatsApp channel using a Twilio provider, Open Chat Studio automatically configures the webhook in your Twilio messaging service. When you delete the channel, the webhook is cleared automatically. You do not need to copy or paste any webhook URL.

!!! info "Sandbox numbers and other exceptions"

    Automatic webhook configuration is not supported for Twilio sandbox numbers or in cases where OCS cannot reach the Twilio API. If auto-configuration fails, OCS will display manual setup instructions instead. Follow the steps in the [Twilio webhook configuration guide][3] and enter the following webhook URL in your messaging service settings:

    `https://openchatstudio.com/channels/whatsapp/incoming_message`

### Turn.io

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

The Slack channel lets users interact with your chatbot from Slack, either in specific channels, via keyword matching, or by mentioning the chatbot workspace-wide.

See the [Slack channel guide](deploy_slack_channel.md) for prerequisites, configuration options, and how chatbot mentions work.

## Email

The email channel lets users interact with your chatbot by sending and receiving emails, including routing, thread continuity, and file attachments.

See the [Email channel guide](deploy_email_channel.md) for full setup and configuration details.

## SureAdhere for In-App Messaging

1. Enter the Tenant ID that was provided when you set up your SureAdhere account.
2. After you submit the form, you will be provided with a webhook URL.
3. Copy this URL and navigate back to your provider's settings to configure it with this URL.

## API

Every chatbot can also be reached programmatically through the OCS [APIs][api], which is useful for integrating with third-party systems or building custom front ends.

[1]: https://core.telegram.org/bots#how-do-i-create-a-bot
[2]: ../concepts/team/messaging_providers.md
[3]: https://www.twilio.com/docs/WhatsApp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/Facebook-messenger#setting-up-the-Facebook-messenger-channel
[5]: https://core.Telegram.org/bots/features#:~:text=/setjoingroups%20%E2%80%93%20toggle%20whether%20your%20bot%20can%20be%20added%20to%20groups%20or%20not.%20All%20bots%20must%20be%20able%20to%20process%20direct%20messages%2C%20but%20if%20your%20bot%20was%20not%20designed%20to%20work%20in%20groups%2C%20you%20can%20disable%20this.
[6]: ../tutorials/configure_msg_providers.md
[api]: ../tech-hub/api_access.md
[meta]: ./whatsapp_meta_cloud_api.md
[chat-widget]: ../chat_widget/index.md
