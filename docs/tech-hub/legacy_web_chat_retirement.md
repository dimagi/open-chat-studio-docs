# Legacy Web Chat Retirement

Operator reference for the retirement of the legacy web chat: the public `/start/` link, email invitations, the chat page those links open, and the full-page chat for logged-in users.
For what changes for chatbot builders and how to move a chatbot to the public link, see [Moving off the legacy web chat](../how-to/deploy_public_link_channel.md#moving-off-the-legacy-web-chat).

## Response headers

Every legacy chat route answers with the [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594) deprecation headers:

| Header | Value |
|---|---|
| `Deprecation` | `true` |
| `Sunset` | The removal date, as an HTTP date |
| `Link` | `<https://docs.openchatstudio.com/how-to/deploy_public_link_channel/>; rel="successor-version"` |

The removal date is the `LEGACY_WEB_CHAT_SUNSET_AT` constant in the application code, not an environment variable.

## Enforcement flag

The removal date alone never closes a route.
Once the date has passed, the `flag_sunset_legacy_web_chat_enforce` flag closes the legacy entry points for the teams it is active for: the old `/start/` and invitation links return `410 Gone` with the same headers.
The `410` body names the chatbot's public link when it has a live one, and the public link how-to otherwise.
Chats that are already open keep working, because only the entry points are gated.

Set the flag in `/admin/flags/`, per team or for everyone.
The flag is created on first check, so it appears there only after a request has reached a legacy route.
Turning it off reopens the entry points without a deploy.

## Notification task

The Celery beat task `ocs_notifications.tasks.notify_http_sunsets` runs daily at 02:30, so Celery beat must be running for the notices to go out.
It notifies the team members who can add channels when a chatbot still has legacy web chat traffic and no live public link.
A chatbot counts as affected when it had a legacy web chat session in the last 30 days and has no published version with an enabled public link.
Each team gets one notice when it is first detected, then 30, 14, 7, and 1 days before the removal date.
Teams the flag is already active for are not notified.

See the [operator changelog](https://github.com/dimagi/open-chat-studio/blob/main/CHANGELOG.md) for the upgrade notes that introduced the flag and the task.
