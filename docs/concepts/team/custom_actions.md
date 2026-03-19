# Custom Actions

Custom Actions enable bots to communicate with 3rd party external services. For more information on features of Custom Actions see [here](../llm_custom_action.md)

## Team setup steps

### 1) Setup Authentication Provider

Before you create a Custom Action will need to create an Authentication Provider for your action to use (unless the API
you are using does not require authentication). You can do this by navigating to the [Authentication Providers][auth_providers] section in [Team Settings](../team/custom_actions.md) and creating a new Authentication Provider.

[auth_providers]: team/authentication_providers.md

### 2) Create a new Custom Action 
Add a Custom Action in [Team Settings](../team/custom_actions.md) 

## Custom Action Fields

### Base URL

This is the URL of the external service you want to communicate with. For example: `https://www.example.com`. Only HTTPS URLs are supported.

### API Schema

This is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

You should be able to get this from the service you want to connect to. For example, the default location for the schema for [FastAPI](https://fastapi.tiangolo.com/) services is `/openapi.json` (https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema).

