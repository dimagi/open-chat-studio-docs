# Participant Data

Participant data is the information collected from participants during their interactions with the system.

Participant data is scoped to the participant's channel platform and channel identifier, with separate data stored for each chatbot. That means the same person can have different data on different channels or in different chatbots.

This separation keeps each chatbot's data isolated. OCS does not automatically merge participant records across different channels.

## Managing participant records

You can view and edit participant data on the Participant Details page. Open it by selecting a participant from the Participants list.

You can also export and import participant data from the Participants list page. 

To add a participant manually, use the Create action and provide an identifier, platform, and optional name. If a participant with that platform and identifier already exists for the team, the form links you to the existing record.

## Using participant data

### Prompt variable

You can access participant data with the `{participant_data}` [prompt variable](prompt_variables.md). The value is a JSON object, so you can use it to personalize responses. For example, you can greet the participant by name.

### Pipeline nodes

[Pipeline nodes](../concepts/pipelines/index.md#node-types-for-complex-pipelines) can also read participant data.
For more information on each node type and how they use participant data, see the [pipeline node documentation](pipelines/nodes.md).

## System properties

The system automatically sets the `timezone` participant data property when a participant uses the web channel. It comes from the participant's browser and helps localize date and time values in prompts.

## Updating participant data

You can update participant data in the Web UI or dynamically during a conversation.

### Tools

Open Chat Studio provides [tools](../tech-hub/tools.md#update-participant-data) that let bots update participant data in real time from the Tools tab on the chatbot edit page.

### Pipeline nodes

The [Update Participant Data Node](../concepts/pipelines/nodes.md#update-participant-data-node) and the [Python Node](../concepts/pipelines/nodes.md#python-node) can both modify participant data. The Update Participant Data Node is commonly used with events, while the Python Node works in any pipeline.

### Events

You can also update the participant data using [events](events.md). This is useful if you want to update the data based on the
context of the conversation. This method also allows you to specify the schema for the data that is being updated.

An example of this is extracting tasks from the conversation history using a timeout event. The event could be
configured to run 15 minutes after the last message was sent. The event would execute a pipeline which would extract the
tasks from the conversation history and update the participant data using the appropriate pipeline node. In this example
the following schema could be used:

```json
{
  "tasks": [
    {
      "name": "name of the task",
      "due_date": "due date of the task in the format YYYY-MM-DD"
    }
  ]
}
```

### API

For API details, including request and response formats, see [Participant Data API](../tech-hub/participant_data.md).

For the full API schema, you can also refer to the generated [API docs](../api/index.md).
