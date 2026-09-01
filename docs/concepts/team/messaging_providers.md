# Messaging Providers

Messaging providers offer access to communication channels such as WhatsApp, Facebook Messenger, Slack, and more.
Configuring a messaging provider lets you use the channel for your chatbot, so participants can interact with it there.

## Supported providers

Below is a list of supported providers and their channels:

- **Twilio**
    - WhatsApp
    - Facebook Messenger
- **Turn.io**
    - WhatsApp
- **Meta Cloud API**
    - WhatsApp
- **Slack**
- **SureAdhere mobile app**
    - In-App secure messaging

## Choosing a WhatsApp provider

Open Chat Studio supports three WhatsApp providers. The table below summarises the key differences to help you choose:

| Feature | Twilio | Turn.io | Meta Cloud API |
|---|---|---|---|
| Direct Meta integration | No | No | Yes |
| Third-party intermediary required | Yes | Yes | No |
| Webhook URL | Per-chatbot | Per-chatbot | Single global endpoint |
| Text messages | Yes | Yes | Yes |
| Media messages (images, video, audio, documents) | Yes | Yes | Yes |
| Setup complexity | Moderate (account + WhatsApp sender setup) | Moderate (account + approval process) | Higher (direct Meta Business Platform configuration, webhook setup, token management) |
| Pricing model | Per-message fees + WhatsApp conversation fees | Subscription + WhatsApp conversation fees | WhatsApp conversation fees only (no intermediary markup) |

Use **Meta Cloud API** when you want a direct connection to the WhatsApp Business Platform without routing traffic through a third-party service. Use **Twilio** or **Turn.io** when you already have an account with one of those providers.

Meta Cloud API providers automatically verify that their out-of-service-window message template is usable and keep track of which WhatsApp numbers the account owns, refreshing this information on demand. See [Set up WhatsApp with Meta Cloud API](../../how-to/whatsapp_meta_cloud_api.md) for details.

## Verifying Turn.io webhook requests

Turn.io messaging providers support an optional **Webhook HMAC Secret**. When you set one, Open
Chat Studio checks a signature on every incoming webhook request to confirm it genuinely came
from Turn.io, rejecting anything else. This protects your chatbot from spoofed or malformed
requests reaching your webhook endpoint. Leaving it blank keeps the previous behavior — webhooks
are accepted without this check.

See [Set up WhatsApp with Turn.io](../../how-to/turnio_whatsapp.md) for setup steps.

## See also
- [Channels](../channels.md)
- [Configure a messaging provider](../../tutorials/configure_msg_providers.md)
- [Set up WhatsApp with Turn.io](../../how-to/turnio_whatsapp.md)
- [Deploy to WhatsApp via Meta Cloud API](../../how-to/whatsapp_meta_cloud_api.md)
