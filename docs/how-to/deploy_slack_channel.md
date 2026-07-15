# Deploy Your Chatbot to Slack

Users can interact with your chatbot directly from Slack, either in specific Slack channels or by mentioning the chatbot.

## Prerequisites

Before configuring a Slack channel for your chatbot, you need to set up a Slack [messaging provider](../concepts/team/messaging_providers.md). This requires:

- Admin access to your Slack workspace
- Following the Slack OAuth and application installation flow
- Configuring the messaging provider in Open Chat Studio (see [Configure a messaging provider][6])

Once your Slack messaging provider is configured, you can link channels to your chatbot.

## Configuration Options

There are three different ways to configure how your chatbot responds to messages in Slack. The chatbot checks each configuration in order of priority:

### 1. Respond to messages from a single channel (highest priority)
- Specify the channel name (with or without the '#' prefix) in the channel configuration form.
- This is the highest specificity - messages on this channel will only be responded to by this chatbot.
- Only one chatbot can be configured per Slack channel.

### 2. Respond to messages from any channel using keyword matching
- Enter keywords separated by commas in the keyword field (e.g., `support, help, assistance`).
- Keywords are matched using exact word matching (case-insensitive) to the first word of the user's message.
- Multiple keywords can be used to trigger the chatbot.
- Keywords must be unique to this chatbot & Slack workspace combination.

### 3. Respond to messages from all channels (lowest priority)
- The chatbot will respond to any message on any channel if it hasn't matched one of the previous two configurations.
- This is the lowest priority matching option.
- Only one chatbot per Slack workspace can be configured with this option.

## Chatbot Interaction

Once the channel is linked, users interact with the chatbot by mentioning it in Slack messages. The chatbot mention name is determined by your Slack app configuration. For example, on the Dimagi hosted instance of Open Chat Studio, the chatbot is mentioned using `@Dimagi Bots`.

!!! info "Priority and Precedence"
    If multiple chatbots could match a message, the chatbot with the most specific configuration wins:

    1. Single channel configuration (highest priority)
    2. Keyword matching
    3. Respond to all channels (lowest priority)

## See also

- [Deploy your chatbot to different platforms](deploy_to_different_channels.md)
- [Configure a messaging provider][6]

[6]: ../tutorials/configure_msg_providers.md
