Prompt variables are a great way to make your prompt dynamic or tailored to the participant by injecting data into specified placeholders. These variables are predefined and look like this:

```
{variable}
```

The following variables are currently supported:

- `{source_material}` - The [source material](../how-to/add_a_knowledge_base.md) linked to your bot.
- `{participant_data}` - Information specific to this participant, bot and channel. See [here][participant_data] for more information. 
- `{current_datetime}` - This refers to the date and time at which the response is generated.
- `{media}` - (pipelines only) This refers to the linked [media collection](./media_collections.md).
- `{temp_state}` - (pipelines only) Access to the pipeline temporary state. See [Temporary State](pipelines/nodes.md#temporary-state).
- `{session_state}` - (pipelines only) Access to the session state. See [Session State](pipelines/nodes.md#session-state)

!!! info "Localizing injected datetime"
    The injected datetime will be localized to the participant's timezone if it exists in their participant data. When a participant uses the web UI, their browser's timezone will automatically be saved to their participant data.

!!! info "A note on prompt caching"
    Some LLM providers, like OpenAI, use a technique called "prompt caching" to reduce latency and costs (See [here][prompt_caching]). This happens automatically. However, caching is only effective for static data, i.e. data that does not change. To take full advantage of this caching mechanism, you should place prompt variables near the end of your prompt whenever possible

[participant_data]: ../concepts/participant_data.md
[prompt_caching]: https://platform.openai.com/docs/guides/prompt-caching

## Nested data access

The following prompt variables allow referencing specific parts of the data:

* `{participant_data}`
* `{temp_state}`
* `{session_state}`

Subsets of the data can be accessed using dot notation. For example, if you have a participant data object that looks like this:

```json
{
  "name": "John Doe",
  "address": {
    "street": "123 Main St"
  },
  "tasks": [
    {
      "name": "Fix the roof"
    }
  ]
}
```

You can access specific parts of the data using the following prompt variables:

```
{participant_data.name}
{participant_data.address.street}
{participant_data.tasks[0].name}  # lists are zero-indexed
```
