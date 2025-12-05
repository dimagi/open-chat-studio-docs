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

### Setting Up Your WhatsApp Channel

1. **Add your WhatsApp number to the form** in the Open Chat Studio channels section.

2. **Configure the webhook URL in your provider:**

   The webhook URL is always: `https://openchatstudio.com/channels/whatsapp/incoming_message`

   This URL is the same for all WhatsApp chatbots and channels on Open Chat Studio.

### Provider-Specific Configuration

#### For New WhatsApp Numbers
If you're setting up a brand new WhatsApp number, you'll need:
- Admin access to your Twilio/Turn.io account
- To register the number with Meta/WhatsApp
- To configure the webhook URL in your provider settings

#### For Existing WhatsApp Numbers
If you're reusing an existing WhatsApp number that was previously configured for Open Chat Studio:
- **No additional webhook configuration needed** - the number is already set up to forward messages to Open Chat Studio
- Simply add the number to your bot's channels in Open Chat Studio

#### Provider Instructions
- **For Twilio:** See [this page][3] to configure the webhook URL in your messaging service
- **For Turn.io:** Go to Settings → API & Webhooks → Add a webhook and paste the OCS webhook URL


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
- Only one bot can be configured like this per Slack workspace.

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


[1]: https://core.telegram.org/bots#how-do-i-create-a-bot
[2]: ../concepts/team/messaging_providers.md
[3]: https://www.twilio.com/docs/WhatsApp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/Facebook-messenger#setting-up-the-Facebook-messenger-channel
[5]: https://core.Telegram.org/bots/features#:~:text=/setjoingroups%20%E2%80%93%20toggle%20whether%20your%20bot%20can%20be%20added%20to%20groups%20or%20not.%20All%20bots%20must%20be%20able%20to%20process%20direct%20messages%2C%20but%20if%20your%20bot%20was%20not%20designed%20to%20work%20in%20groups%2C%20you%20can%20disable%20this.
[6]: ./configure_providers.md
[7]: https://openchatstudio.com/users/profile/
[8]: https://openchatstudio.com/api/docs/
[api]: ./api_access.md
