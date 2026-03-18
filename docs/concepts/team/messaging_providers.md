# Messaging Providers

Messaging providers offer access to communication platforms such as WhatsApp, Facebook Messenger, Slack, and more. Connecting a chatbot to these services allows users to interact with the bot on the respective service.

## Supported providers

Below is a list of supported providers and their integrated platforms in OCS:

- Twilio
    - WhatsApp
    - Facebook Messenger
- Turn.io
    - WhatsApp
- Meta Cloud API
    - WhatsApp
- Slack
- SureAdhere

## Choosing a WhatsApp provider

Open Chat Studio supports three WhatsApp providers. The table below summarises the key differences to help you choose:

| Feature | Twilio | Turn.io | Meta Cloud API |
|---|---|---|---|
| Direct Meta integration | No | No | Yes |
| Third-party intermediary required | Yes | Yes | No |
| Webhook URL | Per-experiment | Per-experiment | Single global endpoint |
| Text messages | Yes | Yes | Yes |
| Audio messages | Yes | Yes | Planned |
| Setup complexity | Moderate (account + WhatsApp sender setup) | Moderate (account + approval process) | Higher (direct Meta Business Platform configuration, webhook setup, token management) |
| Pricing model | Per-message fees + WhatsApp conversation fees | Subscription + WhatsApp conversation fees | WhatsApp conversation fees only (no intermediary markup) |

Use **Meta Cloud API** when you want a direct connection to the WhatsApp Business Platform without routing traffic through a third-party service. Use **Twilio** or **Turn.io** when you already have an account with one of those providers or require features not yet available in the Meta Cloud API integration.

## See also
- [Configure a messaging provider](../../how-to/configure_providers.md)
- [Deploy to WhatsApp via Meta Cloud API](../../how-to/whatsapp_meta_cloud_api.md)
