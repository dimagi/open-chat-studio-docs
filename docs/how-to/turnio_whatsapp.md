# Set Up WhatsApp with Turn.io

This guide walks you through connecting a WhatsApp number to Open Chat Studio (OCS) using **Turn.io**, and
securing the webhook with an optional signing secret. This is an alternative to using Twilio or
Meta Cloud API as your WhatsApp provider.

## Overview

Setting up a WhatsApp channel via Turn.io involves these stages:

1. [Add your provider to OCS](#1-add-your-provider-to-ocs)
2. [Create a WhatsApp channel](#2-create-a-whatsapp-channel)
3. [Configure the webhook in Turn.io](#3-configure-the-webhook-in-turnio)
4. [Secure the webhook with a signing secret (optional)](#4-secure-the-webhook-with-a-signing-secret-optional)

## Prerequisites

- A Turn.io account with an approved WhatsApp number.
- Your Turn.io **Auth Token**.
- Admin access to your OCS team.

## 1. Add Your Provider to OCS

1. Navigate to your **Team Settings** in OCS.
2. Go to **Messaging Providers** and click **Add Provider**.
3. From the **Type** dropdown, select **Turn.io**.
4. Fill in the form:
    - **Name** — a label to identify this provider (e.g., `My Turn.io Account`).
    - **Auth Token** — from your Turn.io account.
5. Leave **Webhook HMAC Secret** blank for now. You can add it later, once you've created the
   matching secret in Turn.io — see [step 4](#4-secure-the-webhook-with-a-signing-secret-optional).
6. Click **Save**.

The provider is now available to use when creating channels.

## 2. Create a WhatsApp Channel

Follow the general [channel deployment steps](deploy_to_different_channels.md) to link a WhatsApp
channel to your chatbot, selecting the Turn.io provider you just created.

## 3. Configure the Webhook in Turn.io

Turn.io does not support automatic webhook configuration, so this step must be done manually.

1. In your Turn.io account, go to **Settings → API & Webhooks**.
2. Select **Add a webhook**.
3. Enter the following URL:

   `https://openchatstudio.com/channels/whatsapp/incoming_message`

!!! warning "Self-hosted instances"
    If you are running a self-hosted instance of Open Chat Studio, replace
    `https://openchatstudio.com` with your own domain.

At this point, your WhatsApp channel is functional. The remaining steps are optional and add
signature verification for extra security.

## 4. Secure the Webhook with a Signing Secret (Optional)

By default, OCS accepts any request sent to a Turn.io webhook URL without checking where it came
from. Adding a signing secret lets OCS verify that inbound requests genuinely came from Turn.io
before processing them.

1. In Turn.io, when you set up the webhook, configure a signing secret for that webhook. Copy the
   secret value.
2. In OCS, go to **Team Settings → Messaging Providers** and edit your Turn.io provider.
3. Paste the same value into the **Webhook HMAC Secret** field.
4. Click **Save**.

Once saved, OCS displays the secret as a masked value in the form, the same way it handles the
**Auth Token** field. To change the secret later, enter a new value and save again.

Once a secret is set, OCS checks the `X-Turn-Hook-Signature` header on every inbound webhook
request from that provider. Requests with a missing or mismatched signature are rejected with a
`401` response and are not passed to your chatbot.

To turn verification off again, clear the **Webhook HMAC Secret** field and save. OCS then accepts
requests without checking a signature, as it did before this field existed.

!!! warning "Turn.io stops retrying after a 401"
    Turn.io treats any `4xx` response as a reason to stop retrying delivery of that message. If
    the secret in OCS doesn't match the secret configured in Turn.io, affected messages are
    dropped rather than retried. Double-check both sides match before relying on this in
    production.

!!! warning "One secret per OCS provider"
    The **Webhook HMAC Secret** is set once per Turn.io messaging provider in OCS, not per
    webhook. If you use a single OCS provider to back multiple Turn.io webhooks that each have a
    *different* signing secret configured on the Turn.io side, only the webhook whose secret
    matches the one saved in OCS will verify successfully — the others will fail signature
    checks. If you need multiple webhooks with different secrets, use a separate Turn.io
    messaging provider in OCS for each one.

!!! info "Status callbacks are unaffected"
    Turn.io also sends status callbacks (delivery and read receipts) to the same webhook. OCS
    filters these out before signature verification runs, so they continue to return `200`
    regardless of whether a secret is configured.

## Troubleshooting

### Turn.io shows failed deliveries or has stopped retrying

- Confirm the **Webhook HMAC Secret** in OCS matches the signing secret configured for that
  webhook in Turn.io, exactly.
- Remember the field is masked after saving — if you're unsure of the current value, set a new
  one on both sides rather than trying to compare them.
- If you don't need signature verification, clear the **Webhook HMAC Secret** field in OCS and
  save to fall back to unverified delivery.

### Messages are not reaching the chatbot

- Confirm the webhook URL in Turn.io matches the URL generated for your channel in OCS.
- Confirm the Turn.io **Auth Token** in your OCS provider settings is still valid.
- Check whether a **Webhook HMAC Secret** is set in OCS but not configured (or configured with a
  different value) in Turn.io — this causes signature checks to fail and requests to be rejected.

### The webhook endpoint returns 405 or 400 responses

These are safeguards unrelated to the signing secret:

- A `405 Method Not Allowed` means something sent a non-`POST` request to the webhook URL, for
  example a browser visit or a manual test using the wrong HTTP method.
- A `400 Bad Request` means the request body wasn't valid JSON, or wasn't a JSON object. Confirm
  you haven't modified the webhook configuration in Turn.io in a way that changes the payload
  format.

## See also

- [Messaging providers](../concepts/team/messaging_providers.md)
- [Deploy your bot to different platforms](deploy_to_different_channels.md)
- [Set up WhatsApp with Meta Cloud API](whatsapp_meta_cloud_api.md)
