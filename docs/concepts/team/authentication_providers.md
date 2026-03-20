# Authentication Providers

Authentication Providers are used to authenticate with external services via HTTP API calls. They are setup in your [Team](index.md) settings so you can manage your authentication credentials for integrations. 

These credentials are used by features like [Custom Actions](../llm_custom_action.md) and the [HTTP Client](../pipelines/http_client.md) in Python nodes.

## Authentication Provider Types

Select the type that matches the API service you will be using.

### Basic Auth

Basic Auth is a simple authentication scheme built into the HTTP protocol where you provide the username and password.

### API Key

API Key is a simple authentication scheme that involves sending a key with the request to authenticate the user. The key is sent in a header of the request. The name of the header can be customized when creating your Authentication Provider.

### Bearer Token

Bearer Token is a type of access token that is sent with the request to authenticate the user. The token is sent in the
Authorization header of the request.

### CommCare

[CommCare HQ](https://www.commcarehq.org/) uses a custom authentication scheme as described in the [CommCare Documentation][1]

[1]: https://dimagi.atlassian.net/wiki/spaces/commcarepublic/pages/2279637003/CommCare+API+Overview#API-Key-authentication
