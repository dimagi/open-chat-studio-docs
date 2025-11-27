# Domain Migration

We will be migrating from the current [chatbots.dimagi.com](https://chatbots.dimagi.com) domain to [www.openchatstudio.com](https://www.openchatstudio.com).```

We will be configuring automatic redirects for most traffic, however, some features will require you to make changes to external systems. Please follow the migration guides below.

## Timeline

The timeline is not fully set yet, however, the new domain is live, and we recommend users start using the new domain.

## Migration Guides

### Messaging Providers

We are still investigating our options for migrating messaging providers. Where possible, we will perform automated migrations. If manual steps are required, we will provide clear instructions and sufficient advanced notice.

### APIs

Users of the APIs will be required to update their API clients to use the new domain name.

### Embedded Chat Widget

The recommended approach is to upgrade the chat widget to a version `>= v0.4.9`.

If you are using a version `< 0.4.0`, you should consider upgrading anyway. We will be phasing out the endpoints used by
that version of the widget in the future.
