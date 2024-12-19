# Deploy your bot to various platforms

## Web
The web channel uses the web interface and is enabled by default for all bots.

## Telegram
- Follow [this guide][1] to create a Telegram bot.
- Save your Telegram bot token. It will look something like this: `4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc`.
- Navigate to your bot on OCS and click the plus icon in the "Channels" section to add a Telegram channel.
- Paste your Telegram bot token and click Create.

## Whatsapp
!!! info "Note"
    It is assumed that you already have an account with a WhatsApp number from one of the providers listed below and that you have sufficient privileges to update the webhook URL linked to your WhatsApp number through the provider.

- Configure a WhatsApp [messaging provider][2]
- Navigate to your bot on OCS and click the plus icon in the "Channels" section to add a WhatsApp channel.
- Complete the form
- After linking the channel, you will be provided with a webhook URL. Copy this URL and paste it in the "webhook url" input at your provider. You can also get this URL by clicking on your whatsapp channel again.
    - For Twilio, see [this page][3]
    - For Turn.io, go to your settings -> API & Webhooks -> Add a webhook and paste the OCS webhook URL


## Facebook Messenger
!!! info "Note"
    It is assumed that you already have a Facebook page and a Twilio account with the Facebook page linked to your Twilio account. Follow [this guide][4] to set this up.

- Configure a Facebook Messenger [messaging provider][2].
- Navigate to your bot on OCS and click the plus icon in the "Channels" section to add a Facebook Messenger channel.
- Complete the form.
- After linking the channel, you will be provided with a webhook URL. Copy this URL and navigate back to your provider's settings.
    - For Twilio, edit your Facebook page settings and paste the URL into the "Webhook URL for incoming messages" field.


## SureAdhere
TODO

## Slack
TODO


[1]: https://flowxo.com/how-to-create-a-bot-for-telegram-short-and-simple-guide-for-beginners/
[2]: ../concepts/messaging_providers.md
[3]: https://www.twilio.com/docs/whatsapp/api#configuring-inbound-message-webhooks
[4]: https://www.twilio.com/docs/conversations/facebook-messenger#setting-up-the-facebook-messenger-channel