# Configure Slack for Notifications on a Self-Hosted Instance

Posting [team notifications to Slack](../how-to/send_notifications_to_slack.md) needs the OCS instance to be configured with a Slack app.
This is operator-level work for whoever runs the server.
On the hosted `openchatstudio.com` instance, this is already done.

## Settings

Set these three settings on the instance:

| Setting                | Value                                |
|------------------------|--------------------------------------|
| `SLACK_CLIENT_ID`      | The client ID of your Slack app      |
| `SLACK_CLIENT_SECRET`  | The client secret of your Slack app  |
| `SLACK_SIGNING_SECRET` | The signing secret of your Slack app |

If any of these are not set, nothing is posted to Slack.

## After configuring

Team Admins can then connect a Slack workspace and add notification channels.
See [Send Notifications to Slack](../how-to/send_notifications_to_slack.md).

## See also

- [Send Notifications to Slack](../how-to/send_notifications_to_slack.md)
- [Team Settings: Notifications](../concepts/team/notifications.md)
