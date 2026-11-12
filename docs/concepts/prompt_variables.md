# Prompt Variables

Prompt variables make your [prompt](llm.md#prompt) dynamic or tailored to the [participant](./participant_data.md) by injecting data into placeholders.
These variables are predefined and look like this:

```text
{variable}
```

The following variables are currently supported:

- `{participant_data}` - Information specific to this participant, chatbot and channel.
  See [participant data][participant_data] for details.
- `{current_datetime}` - This refers to the date and time at which the response is generated.
- `{collection_index_summaries}` - This refers to the [indexed collections](./collections/indexed_collections/index.md).
- `{source_material}` - The [source material](../how-to/add_a_knowledge_base.md) linked to your chatbot.
- `{media}` - This refers to the linked [media collection](./collections/media_collections.md).
- `{temp_state}` - Access to the pipeline temporary state.
  See [Temporary State](../tech-hub/python_node.md#temporary-state).
- `{session_state}` - Access to the session state.
  See [Session State](../tech-hub/python_node.md#session-state).

!!! info "Localizing injected datetime"

    The injected datetime is localized to the participant's timezone if it exists in their participant data.
    When a participant uses the web UI, their browser's timezone is automatically saved to their participant data.

!!! info "A note on prompt caching"

    Some [LLM providers](team/llm_providers.md), like OpenAI, use a technique called [prompt caching][prompt_caching] to reduce latency and costs.
    This happens automatically.
    However, caching is only effective for static data, which is data that does not change.
    To benefit from caching, place prompt variables near the end of your prompt whenever possible.

[participant_data]: ../concepts/participant_data.md
[prompt_caching]: https://platform.openai.com/docs/guides/prompt-caching

## Using one value from your data

You don't have to insert everything stored in `{participant_data}`, `{session_state}` or `{temp_state}` into a prompt.
You can insert just the part you need, such as the participant's name.
This keeps the prompt short and gives the model only relevant information.
See [Nested data access](../tech-hub/prompt_variables.md#nested-data-access) for the syntax.

## Using variables in other nodes

Prompt variables, such as `{participant_data}`, only work in some nodes.
Other nodes that insert data into text use a different syntax and different variables.
If a variable does not work, check that you are using the syntax for that node.

- **LLM node prompts:** All the variables on this page.
- **Router node prompts:** Only some of them. See [Variables you can use in the prompt](../how-to/routers/llm_router.md#variables-you-can-use-in-the-prompt).
- **Render a Template and Send an Email nodes:** Not supported. These nodes use a different syntax and variables. See [Prompt variables vs. template variables](../tech-hub/prompt_variables.md#prompt-variables-vs-template-variables).

## Accessing remote context

Your website or app can send extra information with each participant message for your prompts to use.
This is an advanced feature for developers.
See [Remote context](../tech-hub/prompt_variables.md#remote-context) for how to send and read it.

## See also

- [Prompt Variables Reference](../tech-hub/prompt_variables.md)
- [Participant Data](participant_data.md)
- [Node Types](pipelines/nodes.md#llm-node)
