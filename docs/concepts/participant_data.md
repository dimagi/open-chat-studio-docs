# Participant Data

Participant data is the information collected from participants during their interactions with the system.

Participant data is unique to each combination of channel platform, channel identifier and chatbot. This means that
the data for each bot may be different. For example, if the same person interacts with two different bots over the same
channel e.g. WhatsApp, the data for each bot will be different. Furthermore, if the same person interacts with the same
bot over two different channels e.g. WhatsApp and Telegram, the data for each channel will be different.

The reason for this is to ensure that the data is only accessible to the bot that it is intended for. There
is no way for the system to know whether the same person is interacting with the bot on different channels.

Participant data can be viewed and edited on the "Participant Details" page. This page can be accessed by clicking on
the participant's name in the list of participants on the "Participants" list page.

You can also export and import participant data from the "Participants" list page.

## Using participant data

### Prompt Variable

You can access the participant data using the `{participant_data}` prompt variable. This variable is a JSON object that
contains the data for the participant. You can use this data to personalize the responses from the bot. For example, you
can use the participant's name to personalize the greeting. For more information on prompt variables
see [here][prompt_variables].

[prompt_variables]: ../concepts/prompt_variables.md

### Pipeline Nodes

Other than using the prompt variable described above, there are also various pipeline nodes which allow you to access
the participant data:

* Python node: This node allows you to access the participant data using Python code.

For more information, see the [node documentation](pipelines/nodes.md).

## System properties

There is only one system property that is set automatically by the system and only if the user interacts with a bot via
the web channel. This is the `timezone` property. It is set to the timezone of the participant's browser. This is useful
for localizing datetime variables in prompts.

## Updating participant data

You can manually update the participant data using the Web UI. Participant data can also be updated dynamically using the methods described below.

### Tools

Open Chat Studio provides a [tool](tools/index.md) that allows bots to update the participant data. This tool is available in the "Tools"
tab of the experiment edit page.

Making this tool available to a bot allows it to update the data in real time as the user is interacting with the bot.

### Pipelines Nodes

Both the "Update Participant Data Node" and the "Python Node" can be used to make updates to participant data. The "Update participant data" node is primarily used in conjunction with events (see below). The "Python Node" can be used to
update the data using Python code as part of any pipeline.

For more information, see the [node documentation](pipelines/nodes.md).

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

You can also update the participant data using the API. This is useful if you want full control over the data or when
you want to update the data based from an external system. You can use the following endpoint to update the participant
data:

`POST /api/participants/`

```json
{
  "platform": "Name of the channel platform e.g. WhatsApp, Telegram etc.",
  "identifier": "ID of the participant on the specified platform",
  "name": "Optional name for the participant",
  "data": [
    {
      "experiment": "ID of the experiment the data is for",
      "data": {
        "key": "value"
      }
    }
  ]
}
```

See [the API docs][api_docs]{target="_blank"}
for more information on the API.

[api_docs]: https://chatbots.dimagi.com/api/docs/#tag/Participants/operation/update_participant_data
