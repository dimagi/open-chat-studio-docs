# Notifications

Notifications let you stay aware of problems with your chatbots without having to actively check on them. Open Chat Studio watches for things like failed integrations, delivery errors, and deprecated models, and surfaces them in a bell-icon notification center and, optionally, by email.

## Why notifications exist

Chatbots run continuously across channels like WhatsApp, Slack, and the web, often without anyone watching in real time. If a [custom action](llm_custom_action.md) starts failing, or a message fails to deliver to a participant, you may not notice until a participant complains. Notifications close that gap — Open Chat Studio tells you when something needs attention, so you can fix it before it affects more participants.

## What triggers a notification

Notifications cover a range of issues, including:

- A [custom action](llm_custom_action.md) failing its health check or an API call
- An error while a chatbot's [pipeline](pipelines/index.md) processes a message
- A voice message failing to transcribe or synthesize
- A file or message failing to deliver to a participant
- A [tool](tools/index.md) failing during execution
- An LLM model your team uses being deprecated or removed
- A new [chat widget](../chat_widget/index.md) version being released, or an older one being deprecated

Repeated occurrences of the same underlying issue — for example, the same custom action failing several times in a row — are grouped into a single notification thread instead of creating a new entry every time. Opening the thread shows every occurrence.

## Severity levels

Every notification has one of three severity levels:

| Level | Meaning |
|-------|---------|
| **Info** | General information or confirmation — nothing needs action. |
| **Warning** | A concerning but non-breaking condition, such as an approaching deprecation. |
| **Error** | A critical issue that likely needs your attention, such as a failed delivery. |

You can set a minimum severity level separately for in-app and email notifications — see [Delivery: in-app and email](#delivery-in-app-and-email) below.

## How notifications are scoped

Notifications belong to a [team](team/index.md), like most data in Open Chat Studio, but the notification list you see is personal to you:

- **Team-scoped data** — a notification is generated for the team that owns the affected chatbot, custom action, or other resource.
- **Cross-team list** — the notification bell and list show notifications from every team you belong to, so you don't need to switch teams to stay informed.
- **Per-user read state** — whether a notification is read, unread, or muted is tracked separately for each user. Marking a notification as read doesn't affect your teammates' view of the same event.
- **Permission-gated recipients** — some notifications only go to team members who could actually act on them. For example, only users who can manage custom actions receive custom-action failure notifications. Others, like message delivery failures, go to the whole team.

## Delivery: in-app and email

Notifications can reach you two ways, each with its own on/off switch and minimum severity, set from your profile page:

- **In-app** — shown in the notification bell and list. This also controls the unread count badge.
- **Email** — sent to your account email address when a notification meets your chosen minimum severity.

For example, you might keep in-app notifications set to Info so you see everything in the list, while limiting email to Error so you're only emailed about the most urgent issues.

## Muting and Do Not Disturb

Two controls let you reduce notification noise:

- **Mute a notification** — silence a single notification thread for a period you choose (for example, 8 hours or a week), so a recurring but already-known issue stops re-notifying you.
- **Do Not Disturb** — silence all notifications for one, several, or all of your teams, for a period you choose. This is useful during planned maintenance or when you know a team's chatbots will be noisy for a while. A widget on the notifications page shows which of your teams are currently silenced, with an option to cancel early.

Muting and Do Not Disturb only affect your own notifications — they don't change what your teammates see.

## Next steps

To try notifications yourself, see the [Get started with notifications](../tutorials/notifications.md) tutorial.
