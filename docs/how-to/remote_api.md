# Connecting to a remote API

Open Chat Studio allows you to connect to external services via HTTP API calls. This feature is useful for extending the functionality of your bot by integrating it with other services. This feature is analogous to OpenAI's [GPT Actions](https://platform.openai.com/docs/actions/introduction) feature.

To do this you will need to create a Custom Action by navigating to the [Authentication Providers](../team-configuration/authentication-providers.md) section in Team Settings. See the [Custom Actions](../conceptual_guide/custom_actions.md) guide for more information on how to create a Custom Action.

## Using the custom action in your bot

Once you have created a custom action you can add it to your bot by following these steps:

1. Open your Experiment's edit page.
2. Navigate to the *Tools* tab.
3. Select the action you want to add from the *Custom Actions* checkbox list.

## Testing the custom action

To test the custom action, you can open a chat with your Experiment and type a message that triggers the action. The bot will make an HTTP request to the external service and return the response to you.

To see more detail about the request and response, you can enable tracing in the *Advanced* tab of your Experiment.

<!---
TODO: add a link to the tracing docs
-->
