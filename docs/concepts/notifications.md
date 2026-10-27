# Notifications

Notifications let you know when something needs attention in your chatbots, without having to check on them yourself.
Open Chat Studio (OCS) watches for problems like failed integrations, delivery errors, and deprecated models,
and shows them in a bell-icon notification center and, optionally, by email.

## Why notifications exist

Chatbots run continuously across channels like WhatsApp, Slack, and the web, often with no one watching in real time.
A message can fail to reach a participant, or an LLM model your chatbot depends on can be deprecated.
Either problem can go unnoticed until someone complains.
Notifications tell you as soon as something needs attention.

## What triggers a notification

- An error while a chatbot's [pipeline](pipelines/index.md) processes a message
- A voice message failing to transcribe or synthesize
- A file or message failing to deliver to a participant
- A [tool](tools/index.md) failing during execution
- An LLM provider [refusing a request](../concepts/team/llm_providers.md#provider-errors-during-a-conversation) for a reason only your team can fix, such as an exhausted balance, revoked key, or withdrawn model
- An LLM model your team uses being [deprecated or removed](../concepts/team/llm_providers.md#model-lifecycle-and-deprecation)
- A [Custom Action](llm_custom_action.md) failing its periodic [health check](../tech-hub/custom_action/health_custom_action.md)
- A [Custom Action](llm_custom_action.md) call [failing during a conversation](../tech-hub/custom_action/index.md#failure-notifications)

Repeated occurrences of the same issue are grouped into a single notification thread, rather than creating a new entry every time.
The notification list shows how many times an issue has recurred, such as `×3`, once it's happened more than once.

## Severity levels

Every notification is **Info**, **Warning**, or **Error** —
from general information up to a critical issue that needs your attention.

You can require a minimum severity before something reaches your notification list or your inbox.
See the [Manage Notifications](../how-to/manage_notifications.md#set-your-notification-preferences) how-to guide for setting your preferences.

## Scope: personal list, team-owned data

Notifications belong to a [team](team/index.md), like most data in OCS, but the notification list you see is personal to you:

- The bell and list show notifications from every team you belong to, so you don't need to switch teams to stay informed.
- Whether a notification is read, unread, or muted is tracked per user —
  marking one as read doesn't affect your teammates' view of the same event.
- Some notifications only go to team members who could act on them.
  For example, only users who can manage [Custom Actions](llm_custom_action.md) receive custom-action failure notifications;
  others, like message delivery failures, go to the whole team.

## Slack notification channels

A team can also post notifications to a Slack channel, in addition to the in-app and email notifications.
Slack notification channels belong to the team, not to a user, so one setup serves everyone on the team.
Team admins configure them under **Team settings > Notifications**.

Each notification channel connects one Slack workspace and one Slack channel (such as `#alerts`) to a minimum severity [level](#severity-levels):

- An **Info** channel receives every notification.
- A **Warning** channel receives Warning and Error notifications.
- An **Error** channel receives only Error notifications.

A team can have only one notification channel for each Slack workspace and level.
It can have several channels in the same workspace at different levels, for example Error notifications in `#alerts` and Info notifications in `#updates`.

Each Slack message shows the notification title, the team name, and the level.
It also includes any links attached to the notification and a **View in OCS** link to the notification page.

Slack posting is independent of each team member's in-app and email notification preferences.
Slack messages are sent in the background.
If a message fails to post, the in-app and email notifications are not affected.

To set up a channel, see [Post notifications to Slack](../how-to/manage_notifications.md#post-notifications-to-slack).

## Reducing noise

You can choose how you're notified, mute a repeating issue, or pause notifications for a whole team with [Do Not Disturb](../how-to/manage_notifications.md#turn-on-do-not-disturb).
These settings are personal and don't affect what your teammates see.

To try notifications yourself, see the [Manage Notifications](../how-to/manage_notifications.md) how-to guide.

## See also

- [Manage Notifications](../how-to/manage_notifications.md)
- [Custom Actions](llm_custom_action.md)
- [Tools](tools/index.md)
- [LLM Providers](team/llm_providers.md)
