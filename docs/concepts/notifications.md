# Notifications

Notifications let you know when something needs attention in your chatbots, without having to check on them yourself.
Open Chat Studio watches for problems like failed integrations, delivery errors, and deprecated models,
and shows them in a bell-icon notification center and, optionally, by email.

## Why notifications exist

Chatbots run continuously across channels like WhatsApp, Slack, and the web, often with no one watching in real time.
A message can fail to reach a participant, or an LLM model your chatbot depends on can be deprecated, and go unnoticed until someone complains.
Notifications close that gap by telling you as soon as something needs attention.

## What triggers a notification

- An error while a chatbot's [pipeline](pipelines/index.md) processes a message
- A voice message failing to transcribe or synthesize
- A file or message failing to deliver to a participant
- A [tool](tools/index.md) failing during execution
- An LLM model your team uses being deprecated or removed
- A [Custom Action](llm_custom_action.md) failing its periodic [health check](../tech-hub/custom_action/health_custom_action.md)

Repeated occurrences of the same issue are grouped into a single notification thread, rather than creating a new entry every time.

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

## Reducing noise

You can choose how you're notified, mute a repeating issue, or pause notifications for a whole team with [Do Not Disturb](../how-to/manage_notifications.md#turn-on-do-not-disturb).
These settings are personal and don't affect what your teammates see.

To try notifications yourself, see the [Manage Notifications](../how-to/manage_notifications.md) how-to guide.
