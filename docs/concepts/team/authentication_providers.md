# Authentication Providers

Authentication Providers are used to authenticate with external services via HTTP API calls. Authentication Providers
provide a centralized location to manage the credentials and tokens required to authenticate with external services.

These credentials are used by features like [Custom Actions](../custom_actions.md).

## Authentication Provider Types

Open Chat Studio supports various different authentication types. You should select the type that matches the API
service you will be using.

### Basic Auth

Basic Auth is a simple authentication scheme built into the HTTP protocol.

### API Key

API Key is a simple authentication scheme that involves sending a key with the request to authenticate the user. The key
is sent in a header of the request. The name of the header can be customized when creating the Authentication Provider.

### Bearer Token

Bearer Token is a type of access token that is sent with the request to authenticate the user. The token is sent in the
Authorization header of the request.

### CommCare

[CommCare HQ](https://www.commcarehq.org/) uses a custom authentication scheme as described in the [CommCare Documentation][1]

[1]: https://dimagi.atlassian.net/wiki/spaces/commcarepublic/pages/2279637003/CommCare+API+Overview#API-Key-authentication
