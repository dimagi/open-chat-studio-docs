---
hide:
  - toc
---
# Teams

Open Chat Studio is a [multitenant](https://en.wikipedia.org/wiki/Multitenancy) platform that can support multiple organizations using the same instance at the same time. Each 'tenant' is called a 'team'. Teams are created by an organization and can have multiple members. Each team has its own settings and experiments.

A user can be a member of multiple teams and have a different set of permissions in each team.

A team serves as the root container for all data in Open Chat Studio.

## Team configuration

There is a set of global configuration that can be set at the team level. This includes:

- LLM Service Providers
- Speech Service Providers
- Messaging Providers
- [Authentication Providers](../authentication-providers.md)
- [Custom Actions](../custom_actions.md)
- Tracing providers

<!--- TODO: user management -->
