# Deploy Your Chatbot with a Public Link

A public link gives your chatbot a hosted chat page that anyone can open — no embedding or website required. See [Public link](../concepts/channels.md#public-link) for what it is and what visitors see.

!!! info "This feature may not be turned on yet"
    Public link is an opt-in feature. If it doesn't appear in the add-channel dropdown, ask your Open Chat Studio admin to turn it on for your team.

## Prerequisites

- A **published version** of your chatbot. Visitors always reach the published version — if you haven't published one yet, they'll see a banner instead of the chat. See [Create & publish versions](../tutorials/versioning_steps.md).

## Add a public link

1. Navigate to the **Chatbot** you want to share.
2. Click the :material-plus: (plus) icon and select **Public link** from the dropdown.
3. Set a **Welcome message** and, optionally, **Starter questions** for the channel. These greet visitors when they open the page.
4. Click **Create**.

The channel dialog then shows your link — something like `https://www.openchatstudio.com/c/<token>/` — with a **copy** button. You can also copy it from the **Copy link** chip next to the channel button on the chatbot's home page.

Only one public link can be added per chatbot. If you already have one, add its welcome message and starter questions by opening the existing channel instead.

## Share the link

Share the link however you'd like — email, chat, a QR code, and so on. Anyone who opens it can start chatting immediately; they don't need an Open Chat Studio account.

The page shows your chatbot's name and description above the chat, always in light mode regardless of your app theme, and isn't indexed by search engines.

## Regenerate the link

If a link has been shared somewhere you no longer want it to work, open the channel and click **Regenerate link**.

!!! warning "Regenerating revokes the old link immediately"
    The previous link stops working right away, and any conversation still open on it is ended. Anyone who wants to keep chatting needs the new link.

## Turning it off

- **Disable the channel** (the **Enabled** toggle) to pause it without losing its configuration. Visitors see a banner instead of the chat, and any conversation still open on the link is ended. Re-enable it later to bring the same link back.
- **Delete the channel** to remove it and its link for good. This also ends any conversation still open on it.

Turning off the *Public link* feature for your team (an admin-level setting) only hides the option from the add-channel dropdown for new channels — it doesn't revoke links you've already shared. Regenerate or delete the channel if you need to close off an existing link.

See [Disabling a channel](../concepts/channels.md#disabling-a-channel) for how disabling works across channels generally.

## Troubleshooting

**Visitors see a banner instead of the chat**
: Check that the channel's **Enabled** toggle is on and that your chatbot has a published version. Team members can still preview an unpublished chatbot by opening the page while logged in.

**Visitors report the chat won't load**
: The page loads the chat widget from `unpkg.com` and its fonts and styles from `cdnjs.cloudflare.com`. If a visitor is on a restricted network (for example, a locked-down corporate network), ask them to check that those domains aren't blocked.

**Visitors are told to try again later**
: Public link chat starts are rate limited per visitor IP address to prevent abuse. Ask them to wait a moment and try again.

**A returning visitor doesn't see their previous conversation**
: This is expected — the conversation lives in that browser tab's session storage, so it ends when the tab closes. It also means a shared or public computer never hands a new visitor the previous person's conversation.

## See also

- [Public link](../concepts/channels.md#public-link)
- [Deploying your chatbot to different channels](deploy_to_different_channels.md)
- [Disable a channel](disable_a_channel.md)
