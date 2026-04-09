## Health Status Monitoring of Custom Actions

Open Chat Studio regularly checks whether your Custom Action is available so you can see if the connection is working.

### How Health Checks Work

Automatic checks run every 5 minutes.

### Viewing Health Status

You can view the health status of your custom actions in two places on your [Teams page](../concepts/team/index.md):

1. **Custom Actions Table**: Your Teams list of "Custom Actions" gives you a quick view of which services are available with a status indicator.

2. **Custom Action Page**: When editing a Custom Action for you Team, you can check status while updating your configuration.

### Manual Health Checks

In addition to automatic monitoring, you can manually trigger a health check at any time. This is useful when:

- You've just configured a new custom action and want to verify connectivity immediately
- You've made changes to your external service and want to confirm it's still reachable
- The automatic check shows a service is down and you want to verify it's back online

When you run a manual check, you see the result right away.

## Health status values

A Custom Action can report one of the following states:

- **Up**: the external service is reachable and has responded successfully to the health check
- **Down**: the external service could not be reached or returned an error
- **Unknown**: no health check has completed yet. This can occur when:
    - the health check endpoint has not been configured for the custom action
    - the custom action was recently created and the automatic health check task has not yet run

!!! tip "Troubleshooting"
    If a custom action shows as "Down" or is not behaving as expected, verify that:

    - The base URL is correct and accessible
    - Your Authentication Provider credentials are valid
    - The OpenAPI schema matches the deployed API
    - The external service is running and accepting connections
    - Any firewall or network rules allow connections from Open Chat Studio


