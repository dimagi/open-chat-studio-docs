# Set Up WhatsApp with Meta Cloud API

This guide walks you through connecting a chatbot to WhatsApp using the **Meta Cloud API** messaging provider. This integration connects Open Chat Studio directly to the WhatsApp Business Platform, without routing traffic through a third-party intermediary such as Twilio or Turn.io.

!!! note "Current limitations"
    Phase 1 of this integration supports **text messages only**. Audio message support is planned for a future release.

## Prerequisites

Before you begin, ensure you have the following:

- An active [Meta for Developers](https://developers.facebook.com/) account
- A [WhatsApp Business Account (WABA)](https://business.facebook.com/) with at least one registered phone number
- A **System User Access Token** with the `whatsapp_business_messaging` and `whatsapp_business_management` permissions
- Your **App Secret** from your Meta App dashboard
- Admin access to your Open Chat Studio team

## Overview

Setting up the Meta Cloud API integration involves three stages:

1. **Create a Meta Cloud API messaging provider** in Open Chat Studio with your Meta credentials.
2. **Create a WhatsApp channel** on your chatbot using the new provider.
3. **Configure the webhook** in your Meta App dashboard to forward incoming messages to Open Chat Studio.

---

## Step 1: Gather your Meta credentials

You will need four values from your Meta App dashboard. Collect these before creating the provider in Open Chat Studio.

### WhatsApp Business Account ID

1. Go to [business.facebook.com](https://business.facebook.com/) and sign in.
2. Navigate to **Business Settings** > **Accounts** > **WhatsApp Accounts**.
3. Select your WhatsApp Business Account and copy the **Account ID** displayed on the page.

### System User Access Token

1. In **Business Settings**, go to **Users** > **System Users**.
2. Select the system user you want to use (or create a new one with the `Employee` role).
3. Click **Generate New Token**.
4. Select your Meta App and grant at minimum these permissions:
    - `whatsapp_business_messaging`
    - `whatsapp_business_management`
5. Copy the generated token. Store it securely — it will not be shown again.

!!! warning "Token expiry"
    Tokens can be set to never expire or to a fixed duration. For production use, a non-expiring token is recommended to avoid service interruptions.

### App Secret

1. Go to [developers.facebook.com](https://developers.facebook.com/) and open your app.
2. Navigate to **App Settings** > **Basic**.
3. Click **Show** next to the **App Secret** field and copy the value.

### Webhook Verify Token

This is a value **you choose**. It is a secret string that Meta sends to your webhook endpoint during verification to confirm that the endpoint belongs to you. Use any strong, unique string (for example, a random UUID). Keep a copy — you will need it in both Open Chat Studio and the Meta App dashboard.

---

## Step 2: Create the Meta Cloud API messaging provider

1. In Open Chat Studio, navigate to your **Team Settings**.
2. Select **Messaging Providers**.
3. Click **Add Provider**.
4. From the **Type** dropdown, select **Meta Cloud API**.
5. Fill in the form:

    | Field | Value |
    |---|---|
    | Name | A label to identify this provider (e.g., `My WhatsApp Business`) |
    | WhatsApp Business Account ID | The Account ID from Step 1 |
    | System User Access Token | The access token from Step 1 |
    | App Secret | The App Secret from Step 1 |
    | Webhook Verify Token | The verify token you chose in Step 1 |

6. Click **Save**.

The provider is now available to use when creating channels.

---

## Step 3: Create a WhatsApp channel on your chatbot

1. Navigate to the **Chatbot** you want to deploy to WhatsApp.
2. Click the **+** (plus) icon to add a channel and select **WhatsApp**.
3. In the **Messaging Provider** field, select the Meta Cloud API provider you created in Step 2.
4. Enter the **WhatsApp phone number** associated with your WhatsApp Business Account (include the country code, for example `+12025550123`).
5. Click **Create**.

Open Chat Studio validates the phone number against your WhatsApp Business Account and stores the phone number ID automatically. If validation fails, check that:

- The phone number is registered under the WhatsApp Business Account ID you provided.
- The System User Access Token has the required permissions.

---

## Step 4: Configure the webhook in your Meta App dashboard

Open Chat Studio uses a **single global webhook endpoint** for all Meta Cloud API channels:

```
https://openchatstudio.com/api/channels/meta/
```

!!! info "Global endpoint"
    Unlike Twilio or Turn.io, where each channel has its own webhook URL, all Meta Cloud API channels share this single endpoint. Open Chat Studio routes incoming messages to the correct chatbot based on the receiving phone number.

To configure the webhook:

1. Go to [developers.facebook.com](https://developers.facebook.com/) and open your app.
2. In the left sidebar, click **WhatsApp** > **Configuration**.
3. Under **Webhook**, click **Edit**.
4. Enter the following values:

    | Field | Value |
    |---|---|
    | Callback URL | `https://openchatstudio.com/api/channels/meta/` |
    | Verify Token | The verify token you chose in Step 1 |

5. Click **Verify and Save**. Meta will send a verification request to the endpoint. Open Chat Studio will respond automatically if the verify token matches.
6. After verification succeeds, subscribe to the **`messages`** webhook field under **Webhook Fields**.

!!! warning "Self-hosted instances"
    If you are running a self-hosted instance of Open Chat Studio, replace `https://openchatstudio.com` with your own domain. The path `/api/channels/meta/` remains the same.

---

## Step 5: Test the integration

1. Send a WhatsApp message from a personal WhatsApp account to the business phone number you configured.
2. The chatbot should respond within a few seconds.
3. If there is no response, see the [Troubleshooting](#troubleshooting) section below.

---

## Troubleshooting

### The webhook verification failed

- Confirm that the **Verify Token** in Open Chat Studio and in the Meta App dashboard are identical (exact case match).
- Confirm that the webhook URL is reachable from the internet. On a self-hosted instance, ensure your server is publicly accessible and TLS is configured.

### Messages are not reaching the chatbot

- In your Meta App dashboard, go to **WhatsApp** > **Configuration** and confirm the `messages` webhook field is subscribed.
- Check that the phone number entered during channel creation matches exactly the number registered in your WhatsApp Business Account, including the country code.
- Confirm the System User Access Token has not expired.

### Phone number validation failed during channel creation

- Verify that the phone number is registered under the WhatsApp Business Account ID you provided.
- Verify that the System User Access Token has the `whatsapp_business_management` permission.
- Confirm there are no typos in the Account ID or access token fields.

### Messages are delivered but the chatbot does not respond

- Confirm the chatbot is active and has a working LLM provider configured.
- Check that the channel is linked to the correct chatbot.

---

## See also

- [Messaging providers](../concepts/team/messaging_providers.md)
- [Deploy your bot to different platforms](deploy_to_different_channels.md)
- [Meta WhatsApp Business Platform documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
