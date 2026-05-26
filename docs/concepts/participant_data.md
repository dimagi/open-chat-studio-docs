# Participant Data

Participant data is custom information you store against a participant to personalize their experience. You can use it to remember preferences, track progress, or pass context into your chatbot's prompts.

Each participant record is tied to a specific [channel](./channels.md) (such as WhatsApp or the web) and a specific chatbot. The same person using two different channels, or two different chatbots, will have separate participant records for each. OCS does not automatically merge these records.

## Managing participant records

You can view and edit participant data on the **Participant Details** page. Open it by selecting a participant from the Participants list. You can also export and import participant data from the Participants list page.

The **Session details** screen shows both the **Participant's Data** and their **participant Schedules** - the [reminders](../how-to/reminders.md) and scheduled messages set for that participant — in one place.

To add a participant manually, use the Create action and provide an identifier, platform, and optional name. If a participant with that platform and identifier already exists for the team, the form links you to the existing record.

## Using participant data

### Prompt variable

You can access participant data with the `{participant_data}` [prompt variable](prompt_variables.md). Use it to personalize responses — for example, to greet the participant by name or tailor content to their preferences.

### Pipeline nodes

[Pipeline nodes](pipelines/index.md#node-types-for-complex-pipelines) can read participant data. For more information on each node type and how they use participant data, see [Node Types](pipelines/nodes.md).

## Updating participant data

You can [update participant data in the web UI](#managing-participant-records) or dynamically during a conversation, as explained below.

### Update with tools

OCS provides [tools](../tech-hub/tools.md#update-participant-data) that let chatbots update participant data in real time.

### Update with pipeline nodes

The [Update Participant Data Node](pipelines/nodes.md#update-participant-data-node) and the [Python Node](pipelines/nodes.md#python-node) can both modify participant data.

### Update with events

You can trigger participant data updates automatically using [events](events.md). This approach is useful when you want to extract and store information from a conversation without manual intervention.

A common pattern is to use a timeout event to process conversation history after a period of inactivity. For example, you could configure an event to fire 15 minutes after the last message, run a pipeline that extracts tasks from the conversation, and then write those tasks to participant data using the Update Participant Data Node.

When using the [Update Participant Data Node](pipelines/nodes.md#update-participant-data-node) in a pipeline, you can provide a JSON schema to validate the structure of the data before it is saved. For example, to store a list of tasks extracted from a conversation:

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

### Update with API

You can also update the participant data using the API. This is useful if you want full control over the data or when you want to update the data based from an external system.

For the full details on using the API, see the [API docs](https://openchatstudio.com/api/docs/).

## Participant Timezone for web channel

The system automatically sets the `timezone` participant data property when a participant uses the web channel. It comes from the participant's browser and helps localize date and time values in prompts.
