# Domain Migration

We will be migrating from the current [chatbots.dimagi.com](https://chatbots.dimagi.com) domain to [www.openchatstudio.com](https://www.openchatstudio.com).

We will be configuring automatic redirects for most traffic, however, some features will require you to make changes to external systems. Please follow the migration guides below.

## Timeline

TODO

## Migration Guides

### Messaging Providers

TODO

### APIs

* Update all URLs to use the new domain.
* Alternately ensure the callers handle redirects (301 response code).

### Embedded Chat Widget

The recommended approach is to upgrade the chat widget to a version `>= v0.4.9`.

If you are using a version `< 0.4.0` you should consider upgrading anyway because we will be phasing out the
endpoints used by that version of the widget soon.
