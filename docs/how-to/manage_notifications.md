---
title: Managing Notifications
---
# Managing Notifications

Open Chat Studio provides a notification system that alerts you when events occur in your chatbots. You can view notification history, manage notification preferences, and control when you receive alerts.

## Understanding Notifications

Notifications are generated when [events](../concepts/events.md) are triggered in your chatbots. Each notification corresponds to a specific event, such as:

- Conversation starting or ending
- New messages from users or bots
- Safety layer activations
- Timeout events
- Participant actions

The notification system maintains a complete history of all events and notifications, allowing you to review past activity at any time.

## Viewing Notifications

To access your notifications:

1. Click the **notifications icon** (bell icon) in the top navigation bar
2. A dropdown panel will appear showing your notifications

The notifications panel displays:

- **Recent notifications**: New and unread notifications appear at the top
- **Notification history**: All past notifications remain accessible for review
- **Event details**: Each notification shows the event type, chatbot name, and timestamp
- **Unread indicators**: Visual markers help identify which notifications you haven't reviewed yet

!!! tip "Notification History"
    Unlike many notification systems that only show current alerts, Open Chat Studio maintains a complete history. This allows you to review past events and track patterns in your chatbot interactions over time.

## Muting Individual Notifications

You can mute notifications for specific events while continuing to receive alerts for others.

To mute a notification:

1. Open the **notifications panel** by clicking the bell icon
2. Locate the notification you want to mute
3. Click the **mute button** (usually displayed as a mute/bell-off icon) on that notification
4. The notification will be muted, and you'll no longer receive alerts for that specific event type

To unmute a previously muted notification:

1. Open the **notifications panel**
2. Find the muted notification (it will have a visual indicator showing it's muted)
3. Click the **unmute button** to restore notifications for that event

!!! note "Event-Based Muting"
    When you mute a notification, you're muting that specific event type. For example, if you mute "Conversation Start" notifications for a particular chatbot, you'll stop receiving alerts when new conversations begin for that chatbot, but you'll still receive other notification types.

## Using Do Not Disturb Mode

Do Not Disturb mode allows you to temporarily silence all notifications across all your chatbots.

### Enabling Do Not Disturb

To turn on Do Not Disturb mode:

1. Click the **notifications icon** in the top navigation bar
2. In the notifications panel, locate the **Do Not Disturb** toggle
3. Click the toggle to enable Do Not Disturb mode
4. All notifications will be muted until you disable this mode

When Do Not Disturb is enabled:

- You won't receive any notification alerts
- Events will still be recorded in your notification history
- You can review missed notifications when you disable Do Not Disturb
- A visual indicator shows that Do Not Disturb is active

### Disabling Do Not Disturb

To turn off Do Not Disturb mode:

1. Click the **notifications icon** in the top navigation bar
2. Click the **Do Not Disturb** toggle to disable it
3. Notifications will resume immediately

!!! tip "When to Use Do Not Disturb"
    Do Not Disturb is useful when:

    - You're in a meeting or need to focus without interruptions
    - You're working on development and don't want to be distracted by test notifications
    - You're reviewing notifications manually and don't need real-time alerts
    - You're away from your workspace but want to catch up on events later

## Best Practices

### Managing Notification Volume

If you're receiving too many notifications:

1. **Review your event configurations**: Check which events are configured in your chatbots under the [Events](../concepts/events.md) section
2. **Mute low-priority events**: Identify notification types that aren't urgent and mute them individually
3. **Use Do Not Disturb strategically**: Enable it during focused work periods, then review notifications in batches

### Staying Informed

To ensure you don't miss important events:

1. **Don't mute critical events**: Keep notifications enabled for important events like safety layer activations
2. **Review notification history regularly**: Even if you use Do Not Disturb, check your notification history periodically
3. **Set up event actions thoughtfully**: Configure your [events](../concepts/events.md) to trigger notifications only for meaningful activities

### Troubleshooting

**I'm not receiving notifications**

- Check if Do Not Disturb mode is enabled and disable it if needed
- Verify that the specific notification type isn't muted
- Ensure that events are properly configured in your chatbot settings
- Check your browser notification permissions if you've enabled browser alerts

**My notification panel is too cluttered**

- Use the mute feature to hide notifications for events you don't need to monitor
- Review your event configurations to reduce unnecessary events
- Consider adjusting which events trigger notifications vs. simply logging to history

**I missed important notifications while Do Not Disturb was on**

- Review your notification history to catch up on missed events
- Consider muting specific low-priority events instead of using Do Not Disturb for all notifications
- Set up alternative alerting methods (like email or messaging integrations) for critical events

## Related Documentation

- [Events Concept](../concepts/events.md) - Learn about the event system that generates notifications
- [Custom Actions](../concepts/custom_actions.md) - Set up external integrations that can be triggered by events
