# Custom Actions

Custom Actions enable bots to communicate with external services via HTTP API calls. 
This feature allows you to extend the functionality of your bot by integrating it with other services.

This feature is analogous to the OpenAI's [GPT Actions](https://platform.openai.com/docs/actions/introduction) feature.

## Custom Action Fields

### Authentication Provider

Before you create a Custom Action will need to create an Authentication Provider for your action to use (unless the API
you are using does not require authentication). You can do this by navigating to the [Authentication Providers][auth_providers] section
in Team Settings and creating a new Authentication Provider.

[auth_providers]: ../concepts/authentication-providers.md

### Base URL

This is the URL of the external service you want to communicate with. For example: `https://www.example.com`. Only HTTPS URLs
are supported.

### API Schema

This is a JSON or YAML [OpenAPI Schema](https://swagger.io/specification/) document.

You should be able to get this from the service you want to connect to. For example, the default location for the schema for [FastAPI](https://fastapi.tiangolo.com/) services is `/openapi.json` (https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema).

## How Custom Actions work

When you create a custom action, each API endpoint in the OpenAPI schema will be available as a separate action in the
Experiment configuration. This gives you full control over which actions are available to your bot.

When you add a Custom Action to your Experiment, the bot will be able to make HTTP requests to the external service
using the API endpoints you have configured. The bot will send the request and receive the response from the external
service, which it can then use to generate a response to the user.
