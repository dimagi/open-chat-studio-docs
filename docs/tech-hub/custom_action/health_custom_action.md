# Custom Action Health Monitoring

Open Chat Studio regularly checks whether each Custom Action is available so you can see whether the connection is working.

## How Custom Action health checks work

Automatic checks run once every hour.
They check only Custom Actions used by a non-archived node on a non-archived chatbot.
For a chatbot's working version, the check also requires that the node still allows at least one of the action's operations.
Actions used only by archived chatbots, or not used at all, are not checked automatically.

If a check finds that a previously working Custom Action has gone down,
a [notification](../../concepts/notifications.md) is sent to team members who can manage Custom Actions.

## Viewing health status

You can view the health status of your Custom Actions in two places in the [Developers](../../concepts/team/developer.md) section of Team Settings:

1. **Custom Actions table**: The list of Custom Actions gives you a quick view of which services are available, along with a status indicator.
2. **Custom Action page**: When you open a Custom Action for your team, you can check its status while updating the configuration.

## Manual health checks

In addition to automatic monitoring, you can manually trigger a health check at any time.
This is useful when:

- you have just configured a new Custom Action and want to verify connectivity immediately
- you have made changes to your external service and want to confirm that it is still reachable
- the automatic check shows that a service is down and you want to verify that it is back online

When you run a manual check, the result appears right away.
Manual checks run for any Custom Action, including unused ones, and record the resulting status.
The team is notified only when the status changes to Down for a Custom Action that a non-archived chatbot uses.
If a manual check records Down for an unused action, you are not notified again when a chatbot later starts using it.

## Health status values

A Custom Action can report one of the following states:

- **Up**: the external service is reachable and responds successfully to the health check
- **Down**: the external service could not be reached or returned an error
- **Unknown**: no health check has completed yet. This can occur when:
    - the health check endpoint has not been configured for the Custom Action
    - the Custom Action was recently created and the automatic health check task has not yet run
    - the Custom Action is not used by a non-archived chatbot, so the automatic check skips it and no manual check has been run

!!! tip "Troubleshooting"
    If a Custom Action shows as "Down" or is not behaving as expected, verify that:

    - the base URL is correct and accessible
    - your Authentication Provider credentials are valid
    - the OpenAPI schema matches the deployed API
    - the external service is running and accepting connections
    - any firewall or network rules allow connections from Open Chat Studio

## See also

- [Notifications](../../concepts/notifications.md) — how health check failures and other issues are surfaced to your team
- [Failure notifications](./index.md#failure-notifications) — alerts for Custom Action calls that fail during a conversation
