# Custom Action Health Monitoring

Open Chat Studio regularly checks whether each Custom Action is available so you can see whether the connection is working.

## How Custom Action health checks work

Automatic checks run every 5 minutes.

## Viewing health status

You can view the health status of your Custom Actions in two places in [Team Settings](../../concepts/team/index.md):

1. **Custom Actions table**: The list of Custom Actions gives you a quick view of which services are available, along with a status indicator.
2. **Custom Action page**: When you open a Custom Action for your team, you can check its status while updating the configuration.

## Manual health checks

In addition to automatic monitoring, you can manually trigger a health check at any time. This is useful when:

- you have just configured a new Custom Action and want to verify connectivity immediately
- you have made changes to your external service and want to confirm that it is still reachable
- the automatic check shows that a service is down and you want to verify that it is back online

When you run a manual check, the result appears right away.

## Health status values

A Custom Action can report one of the following states:

- **Up**: the external service is reachable and responds successfully to the health check
- **Down**: the external service could not be reached or returned an error
- **Unknown**: no health check has completed yet. This can occur when:
    - the health check endpoint has not been configured for the Custom Action
    - the Custom Action was recently created and the automatic health check task has not yet run

!!! tip "Troubleshooting"
    If a Custom Action shows as "Down" or is not behaving as expected, verify that:

    - the base URL is correct and accessible
    - your Authentication Provider credentials are valid
    - the OpenAPI schema matches the deployed API
    - the external service is running and accepting connections
    - any firewall or network rules allow connections from Open Chat Studio
