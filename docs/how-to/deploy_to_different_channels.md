# Deploy your bot to different platforms

To link a channel to your bot:

!!! info "Note"
    Not all channels require a provider.

- Choose a [provider][2] for your channel.
- [Configure a messaging provider][6]. You will need to get the required credentials from your chosen provider.
- Once the provider is set up, navigate to your bot on OCS and click the plus icon in the "Channels" section.
- Choose your channel and complete the form. Follow the guide below to get the required information for each channel.

## Web
The web channel uses the web interface and is enabled by default for all bots.

## Telegram
- Follow [this guide][1] to create a Telegram bot.
- Copy the bot token and paste it into the form on OCS. It will look something like this: `4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc`.


!!! info "Note"
    Depending on your usecase, you probably want to disable group joins for your bot on Telegram. To achieve this, use the [setjoingroups][5] setting in BotFather.

## WhatsApp
- Add your WhatsApp number to the form.
- After you submit the form, you will be provided with a webhook URL. Copy this URL and paste it in the 'webhook url' input at your provider. You can also get this URL by clicking on your WhatsApp channel again.
    - For Twilio, see [this page][3]
    - For Turn.io, go to your settings -> API & Webhooks -> Add a webhook and paste the OCS webhook URL


## Facebook Messenger
!!! info "Note"
    It is assumed that you already have a Facebook page and a Twilio account with the Facebook page linked. Follow [this guide][4] if this is not the case.

- Add the ID of your Facebook page.
- After you submit the form, you will be provided with a webhook URL. Copy this URL and navigate back to your provider's settings.
    - For Twilio, edit your Facebook page settings and paste the URL into the "Webhook URL for incoming messages" field.

## Slack
- Choose the channel mode.
- If you chose to link a specific channel, enter the name of the Slack channel you want your bot to be available on.
- Once the channel is linked, you will be able to chat with it using the `@Dimagi Bots` reference.


[1]: https://flowxo.com/how-to-create-a-bot-for-Telegram-short-and-simple-guide-for-beginners/
[2]: ../concepts/messaging_providers.md
[3]: https://www.twilio.com/docs/WhatsApp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/Facebook-messenger#setting-up-the-Facebook-messenger-channel
[5]: https://core.Telegram.org/bots/features#:~:text=/setjoingroups%20%E2%80%93%20toggle%20whether%20your%20bot%20can%20be%20added%20to%20groups%20or%20not.%20All%20bots%20must%20be%20able%20to%20process%20direct%20messages%2C%20but%20if%20your%20bot%20was%20not%20designed%20to%20work%20in%20groups%2C%20you%20can%20disable%20this.
[6]: ./configure_providers.md
