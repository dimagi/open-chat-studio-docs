# Set Up WhatsApp with Meta Cloud API

This guide walks you through connecting a WhatsApp number to Open Chat Studio (OCS) using the **Meta Cloud API**. This is an alternative to using Twilio or Turn.io as your WhatsApp provider.

## Overview

Setting up a WhatsApp channel via Meta Cloud API involves four main stages:

1. [Create a Meta Business Portfolio and add your phone number](#1-create-a-meta-business-portfolio-and-add-your-phone-number)
2. [Create a Meta App with the WhatsApp use case](#2-create-a-meta-app-with-the-whatsapp-use-case)
3. [Add your provider to OCS](#3-add-your-provider-to-ocs)
4. [Configure the webhook in your Meta App](#4-configure-the-webhook-in-your-meta-app)

## Supported media types

The Meta Cloud API integration supports sending and receiving media messages in addition to text. When a participant sends an image or document to your WhatsApp number, OCS downloads it, links it to the conversation, and passes it to the LLM automatically — no extra configuration is required.

The following media types are accepted:

| Media type | Accepted formats | Maximum file size |
|---|---|---|
| Image | JPG, PNG, WEBP | 5 MB |
| Video | MP4, 3GP | 16 MB |
| Audio | AAC, MP4, MPEG, AMR, OGG | 16 MB |
| Document | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 MB |

!!! warning "Size limits are enforced before sending"
    Files that exceed the per-type size limit are rejected before the send attempt is made. Ensure any media attached to bot responses falls within the limits above to avoid delivery failures.

---

## Prerequisites

- A Meta Business Portfolio (formerly Meta Business Manager)
- A phone number to register with WhatsApp (must not already be active on WhatsApp)
- Access to a tool for making API calls (e.g., cURL or Postman)
- Admin access to your OCS team

---

## 1. Create a Meta Business Portfolio and Add Your Phone Number

### Enable Two-Factor Authentication

Before proceeding, log in to [Meta Business Manager](https://business.facebook.com) and enable two-factor authentication (2FA) in the **Security Center**.

!!! warning "Required step"
    Two-factor authentication must be enabled before you can register a phone number or generate system user access tokens.

### Create a System User and Generate an Access Token

Follow the [Meta documentation on admin system users](https://developers.facebook.com/documentation/business-messaging/whatsapp/access-tokens#admin-system-users) to create a system user and generate an access token.

When generating the token, grant at minimum these permissions:

- `whatsapp_business_messaging`
- `whatsapp_business_management`

Copy and securely store the generated token — this is your **System User Access Token**.

!!! warning "Token expiry"
    Tokens can be set to never expire or to a fixed duration. For production use, a non-expiring token is recommended to avoid service interruptions.

### Add and Register Your Phone Number

1. Open **WhatsApp Manager** in your Business Portfolio.
2. Click **Add Phone Number** and follow the prompts to add your number.
3. Note the **Phone Number ID** displayed for your number — you will need this later.
4. Verify ownership of the number using the one-time code sent by Meta.
5. Wait for your **display name** to be verified by Meta before proceeding.

    !!! info "Display name verification"
        Display name verification typically takes 2–3 hours. You cannot complete the registration step until this is approved.

6. While waiting for display name verification, go to your [system user page](https://business.facebook.com/settings/system-users), click **Add Assets**, select **WhatsApp Accounts**, choose the newly created WhatsApp Business Account, and enable the **Phone numbers view and manage** permission. This is required so the system user's access token can register the phone number in the next step.

    !!! tip "Permission can be removed after registration"
        Once registration is complete, you can remove this permission from the system user.

7. Once your display name is verified, register your number by making a `POST` request to the `/register` endpoint. Replace `<PHONE_NUMBER_ID>` and `<SYSTEM_USER_ACCESS_TOKEN>` with your values:

```bash
curl -X POST \
  "https://graph.facebook.com/v18.0/<PHONE_NUMBER_ID>/register" \
  -H "Authorization: Bearer <SYSTEM_USER_ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"messaging_product": "whatsapp", "pin": "<YOUR_2FA_PIN>"}'
```

!!! tip "Using Postman"
    If you prefer a GUI over cURL, you can make this call using [Postman](https://www.postman.com/). Import the request above and set your credentials as environment variables.

!!! info "Reference"
    See the [Meta documentation on registering a business phone number](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/registration) for full details.

---

## 2. Create a Meta App with the WhatsApp Use Case

1. Follow the [Meta WhatsApp get-started guide](https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started) to create a new Meta App.
2. When prompted to select a use case, choose **WhatsApp**.
3. Link the app to your Business Portfolio.
4. Once the app is created, navigate to **App Settings** > **Basic** and note the following values:
    - **App ID**
    - **App Secret** — click **Show** to reveal it and store it securely.

---

## 3. Add Your Provider to OCS

Before connecting OCS to Meta, you need to configure a messaging provider in OCS. Gather the following values:

| Value | Where to find it |
|---|---|
| `WhatsApp Business Account ID` | In Business Settings > Accounts > WhatsApp Accounts, select your account and copy the **Account ID** |
| `App Secret` | **Meta App** > **App Settings** > **Basic** > **App Secret** |
| `Webhook Verify Token` | A random string you generate yourself (see note below) |
| `System User Access Token` | Generated in [Step 1](#create-a-system-user-and-generate-an-access-token) |

!!! tip "Generating a webhook verify token"
    The `Webhook Verify Token` is a secret string you create. It can be any random string (e.g., a UUID). Keep a copy — you will need it when configuring the webhook in Step 4.

To add the provider in OCS:

1. Navigate to your **Team Settings** in OCS.
2. Go to **Messaging Providers** and click **Add Provider**.
3. From the **Type** dropdown, select **Meta Cloud API**.
4. Fill in the form with the values gathered above:
    - **Name** — a label to identify this provider (e.g., `My WhatsApp Business`)
    - **WhatsApp Business Account ID**
    - **System User Access Token**
    - **App Secret**
    - **Webhook Verify Token**
    - **Template Language Code** — the language code for the out-of-service-window template (defaults to `en`; see [Out-of-service-window template messages](#out-of-service-window-template-messages) below)
5. Click **Save**.

The provider is now available to use when creating channels.

### Create a WhatsApp channel on your chatbot

1. Navigate to the **Chatbot** you want to deploy to WhatsApp.
2. Click the **+** (plus) icon to add a channel and select **WhatsApp**.
3. In the **Messaging Provider** field, select the Meta Cloud API provider you just created.
4. Enter the **WhatsApp phone number**:
    - If OCS has never checked this provider before, the field is a free-text box. Enter the number associated with your WhatsApp Business Account, including the country code (for example `+12025550123`).
    - If OCS has already checked this provider — either because a previous channel was saved on it, or because someone clicked **Refresh** on the provider's detail page (see [Automatic template and number checks](#automatic-template-and-number-checks)) — the field is instead a picker listing the numbers known to the WhatsApp Business Account. Select the number you want to use.
5. Click **Create**.

When you save a channel using the free-text box, OCS checks the number you entered against your WhatsApp Business Account and stores its phone number ID automatically. This also populates the provider's cache of known numbers, so the next channel created on this provider gets the picker instead of the free-text box. If this check fails, confirm that:

- The phone number is registered under the WhatsApp Business Account ID you provided.
- The System User Access Token has the required permissions.

When you select a number from the picker, there is nothing to validate — you're choosing directly from the numbers Meta reports for the account.

---

## Out-of-service-window template messages

### What is the 24-hour service window?

WhatsApp restricts when businesses can send messages to participants. Once a participant sends a message to your business number, a **24-hour service window** opens. During that window, your chatbot can reply freely. After 24 hours of inactivity from the participant, the window closes and the WhatsApp API rejects any outbound messages.

Without a fallback, a bot reply sent outside the service window is silently dropped. The out-of-service-window template message feature prevents this by automatically substituting a pre-approved WhatsApp message template when the window has expired.

!!! info "Automatic fallback"
    The fallback is automatic — no manual toggle is required. When the service window has expired, OCS attempts to send the configured template in place of the original message. If the template has not been created in Meta, the attempt fails gracefully without interrupting service.

### Voice message fallback chain

When a voice message fails because the service window has expired, OCS first falls back to sending the content as a text message. If the text message also fails due to the expired window, the template fallback applies. This means the template covers both text and voice-originated replies.

### Create the required template in Meta Business Manager

You must create a WhatsApp message template in your Meta Business account before the fallback can work. Meta requires templates to be reviewed and approved before they can be sent.

1. Go to [business.facebook.com](https://business.facebook.com) and find where to manage your WhatsApp message templates.
2. Create a new template with the following required settings:

    | Setting | Required value |
    |---|---|
    | Category | **Utility** (recommended) or **Marketing** |
    | Template name | `new_bot_message` |
    | Language | Select the language that matches your **Template Language Code** in OCS |

3. In the **Body** section, add a single text variable named `bot_message`. This variable will be replaced with the bot's actual message when sent.

4. Submit the template and wait for Meta to approve it.

!!! warning "Template name and variable must match exactly"
    The template name must be `new_bot_message` exactly, and it must have a single template variable (text type) named `bot_message`. OCS looks up this template by name and passes the message via this variable. If either does not match, the fallback will not work.

!!! warning "Template approval required"
    The template cannot be used until Meta approves it. Approval typically takes a few minutes to a few hours but may take longer. Until approval is granted, the fallback will fail silently.

### Automatic template and number checks

When you create a Meta Cloud API provider, OCS automatically checks Meta's Graph API to confirm the `new_bot_message` template is usable, and to find out which WhatsApp numbers the Business Account owns. OCS runs both checks again whenever you click **Refresh** on the provider's detail page.

The provider's detail page reports the results:

- Whether the template is usable, or an explanation of what is wrong with it.
- The WhatsApp numbers known to the Business Account.

For the template to be reported as usable, all of the following must be true:

- A template named `new_bot_message` exists in the WhatsApp Business Account.
- Its status is **Approved**.
- Its language matches the provider's **Template Language Code**.
- Its body has a text variable named `bot_message`.

The provider's detail page also includes a form for sending a real test message through the template, so you can confirm end-to-end delivery without waiting for a participant's service window to expire.

!!! info "Never checked yet"
    If the provider has never been checked — for example, immediately after it is created and before OCS's automatic check completes — the page reports that plainly rather than claiming the template is broken.

### Message formatting

Meta rejects template sends when the `bot_message` variable contains line breaks, tabs, or long runs of spaces. To avoid this, OCS collapses any run of whitespace in the bot's message — including line breaks and tabs — into a single space before inserting it into the template. This means a multi-paragraph bot reply arrives as a single paragraph when it is sent as a fallback template message.

Only the substituted `bot_message` text is flattened this way. The approved template's own static text keeps whatever line breaks it was approved with in Meta Business Manager.

!!! info "Broadcast messages use the same template"
    The broadcast dialog for sending a one-off message to all participants of a chatbot relies on this same `new_bot_message` template for any channel outside its service window. Before sending, it warns you if a ticked channel's provider has no usable template, or if the message contains line breaks, since Meta flattens them the same way described above.

### Character limits

| Element | Limit |
|---|---|
| Template static text | 100 characters |
| Dynamic message content (`bot_message`) | 974 characters |

Whitespace flattening happens before OCS checks the character limit, so the limit is measured against the message Meta actually receives. Flattening only ever shortens the text, so it never causes a message to exceed the limit.

If the bot's outgoing message exceeds 974 characters, OCS automatically splits it at word boundaries and sends it across multiple template messages.

### Set the template language code in OCS

The **Template Language Code** field in the Meta Cloud API provider form tells OCS which language variant of the `new_bot_message` template to use when sending the fallback message.

- The default value is `en` (English).
- Change this value to match the language you selected when creating the template in Meta Business Manager.
- Common codes include `en_US`, `es`, `fr`, `pt_BR`. For the full list, see the [Meta locale codes reference](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates#supported-languages).

To update the language code:

1. Navigate to **Team Settings** > **Messaging Providers** in OCS.
2. Click **Edit** on your Meta Cloud API provider.
3. Update the **Template Language Code** field.
4. Click **Save**.

---

## 4. Configure the Webhook in Your Meta App

!!! warning "Order matters"
    Only configure the webhook in Meta after the messaging provider has been saved in OCS. Meta verifies the webhook immediately, and OCS needs the provider to exist in order to respond successfully.

Open Chat Studio uses a **single global webhook endpoint** for all Meta Cloud API channels:

```uri
https://openchatstudio.com/api/channels/meta/incoming_message
```

!!! info "Global endpoint"
    Unlike Twilio or Turn.io, where each channel has its own webhook URL, all Meta Cloud API channels share this single endpoint. Open Chat Studio routes incoming messages to the correct chatbot based on the receiving phone number.

To configure the webhook:

1. Open your Meta App in the [Meta Developer Portal](https://developers.facebook.com/).
2. In the left sidebar, navigate to **WhatsApp** > **Configuration**.
3. Under **Webhook**, click **Edit**.
4. Enter the following values:

    | Field | Value |
    |---|---|
    | Callback URL | `https://openchatstudio.com/api/channels/meta/incoming_message` |
    | Verify Token | The `Webhook Verify Token` you created in Step 3 |

5. Click **Verify and Save**. Meta will send a verification request to OCS to confirm the token matches.
6. Once verified, subscribe to the **`messages`** webhook field to ensure incoming messages are forwarded to OCS.

!!! info "Reference"
    See the [Meta documentation on configuring webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint#configure-webhooks) for detailed instructions.

!!! warning "Webhook verification"
    If the verification step fails, double-check that the `Webhook Verify Token` in the Meta portal exactly matches the value saved in your OCS provider configuration.

!!! warning "Self-hosted instances"
    If you are running a self-hosted instance of Open Chat Studio, replace `https://openchatstudio.com` with your own domain. The path `/api/channels/meta/incoming_message` remains the same.

---

## Next Steps

Once your webhook is verified and the subscription is active, your Meta Cloud API provider is ready to use.

1. Send a WhatsApp message from a personal WhatsApp account to the business phone number you configured.
2. The chatbot should respond within a few seconds.
3. If there is no response, see the [Troubleshooting](#troubleshooting) section below.

---

## Troubleshooting

### The webhook verification failed

- Confirm that the **Webhook Verify Token** in Open Chat Studio and in the Meta App dashboard are identical (exact case match).
- Confirm that the webhook URL is reachable from the internet. On a self-hosted instance, ensure your server is publicly accessible and TLS is configured.

### Messages are not reaching the chatbot

- In your Meta App dashboard, go to **WhatsApp** > **Configuration** and confirm the `messages` webhook field is subscribed.
- Check that the phone number entered during channel creation matches exactly the number registered in your WhatsApp Business Account, including the country code.
- Confirm the System User Access Token has not expired.

### The `/register` API call returned an authorization error

This is almost always caused by the system user's access token not having permission to manage the WhatsApp Business Account's phone numbers.

- In [Meta Business Settings](https://business.facebook.com/settings), go to **Users** > **System Users** and select your system user.
- Confirm that your WhatsApp Business Account appears under the system user's assigned assets.
- Confirm that the **Phone numbers view and manage** permission is enabled for that asset.
- If the asset is missing, click **Add Assets**, select **WhatsApp Accounts**, choose the correct account, enable the permission, and save.
- Generate a new access token for the system user after updating permissions.

### Phone number validation failed during channel creation

This only applies when the phone number field is the free-text box, which is the case if the provider has never been checked before. Once a provider has synced numbers, the field becomes a picker, and there is nothing to mistype.

- Verify that the phone number is registered under the WhatsApp Business Account ID you provided.
- Verify that the System User Access Token has the `whatsapp_business_management` permission.
- Confirm there are no typos in the Account ID, access token, or phone number fields.

### Messages are delivered but the chatbot does not respond

- Confirm the chatbot is active and has a working LLM provider configured.
- Check that the channel is linked to the correct chatbot.
- Check the **Webhook Logs** in your Meta App dashboard to see whether delivery attempts are succeeding or returning errors.

### The out-of-service-window template message is not being sent

If the bot is not reaching participants after the 24-hour service window expires:

- Start with the Meta Cloud API provider's detail page in OCS. It reports whether the `new_bot_message` template is currently usable, and includes a **Refresh** button to re-check it against Meta. This is the fastest way to diagnose the problem.
- If the page reports the template as not usable, or reports that it has never been checked, use Meta Business Manager as a fallback: under **WhatsApp Manager** > **Account tools** > **Message templates**, confirm that a template named `new_bot_message` exists, its status is **Approved**, and its language matches the **Template Language Code** configured on the provider.
- Confirm that the template body has a text variable named `bot_message`, and that the static text surrounding it does not exceed 100 characters.
- If the template was recently approved, wait a few minutes, then click **Refresh** on the provider's page to pick up the change — there can be a short propagation delay on Meta's side.

---

## See also

- [Messaging providers](../concepts/team/messaging_providers.md)
- [Deploy your bot to different platforms](deploy_to_different_channels.md)
- [Meta WhatsApp Business Platform documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
