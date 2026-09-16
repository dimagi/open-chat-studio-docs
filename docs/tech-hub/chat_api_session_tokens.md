# Chat API Session Tokens

This page explains how Chat API session tokens expire and how to renew one.
It's aimed at integrations that authenticate with an OAuth bearer token — most commonly, the chat widget's [OAuth credential mode](../chat_widget/reference.md#oauth-credential-mode).
Renewing lets a long-running conversation survive past a single token's lifetime, instead of restarting.

`POST /api/chat/start/` returns a `session_token`, used to authenticate later calls on that session — sending messages, polling, and uploading files.
See [Chat sessions](../concepts/sessions.md) for what a session itself represents.

## Issuance and expiry

- Each session token carries an expiry claim, stamped when the token is issued.
- The lifetime comes from the channel's **Session token lifetime** setting, or a five-minute default if the channel doesn't set one.
- The lifetime counts from **issuance**, not from when the session was created. Renewing a token (see below) gives it a fresh lifetime, regardless of how old the underlying session is.
- Tokens issued before this behavior shipped don't carry the claim. OCS falls back to the previous rule for those: expiry measured from the session's creation time.

## Renewing a session token

Call `POST /api/chat/{session_id}/token/` to issue a fresh session token for an existing session, without starting a new one.

- **Authentication** works exactly like `POST /api/chat/start/`: an OAuth bearer token for the channel's chatbot. See [Tokens for starting chat sessions](../api/getting_started_with_oauth.md#tokens-for-starting-chat-sessions) for how to mint one with a short lifetime.
- **Live channel configuration.** The channel's configuration is re-read from the database on every renewal call. Deleting, disabling, or reconfiguring the channel takes effect on the very next renewal — see [Disable a channel](../how-to/disable_a_channel.md).
- **Throttling is per OAuth application, not per session.** One visitor renewing frequently can't exhaust another visitor's renewal quota, because the limit applies to the whole application, not the individual session.
- **Uniform refusal.** Any reason for refusing a renewal returns the same `401` response. This includes an expired or invalid OAuth token, a disabled channel, and a session ID that doesn't exist or isn't yours. The endpoint never reveals whether a given session ID exists.

Both `POST /api/chat/start/` and `POST /api/chat/{session_id}/token/` report an `expires_at` field, telling you when the returned session token expires.

## Recommended integration pattern

1. Mint an OAuth access token scoped to `chat:start` alone, so it expires after 60 seconds by default. See [Tokens for starting chat sessions](../api/getting_started_with_oauth.md#tokens-for-starting-chat-sessions).
2. Call `POST /api/chat/start/` with that token to start the session, and note the `expires_at` field in the response.
3. Before the session token expires, mint a fresh `chat:start`-scoped OAuth token and call `POST /api/chat/{session_id}/token/` to renew it.
4. Repeat step 3 for as long as the conversation continues.

!!! tip "Renew, don't restart"
    Renewing keeps the participant in the same session, with its existing history.
    Starting a new session instead loses that continuity.

## Why this is more secure

Previously, a stolen OAuth token could start new sessions for up to 10 hours, and a stolen session token lasted until the session expired.
Now, an OAuth token minted for starting a session lives 60 seconds by default.
The session token it produces lives 5 minutes by default, but is renewable.
A legitimate integration keeps the conversation going by renewing, while a stolen token has a much smaller window to be useful.

## See also

- [Getting started with OAuth2](../api/getting_started_with_oauth.md)
- [OAuth credential mode](../chat_widget/reference.md#oauth-credential-mode)
- [Chat sessions](../concepts/sessions.md)
- [Disable a channel](../how-to/disable_a_channel.md)
