# Prompt Variables

Prompt variables insert data into your chatbot's [prompt](llm.md#prompt), so its responses can use information about the [participant](./participant_data.md) and your content.
You write a variable in curly braces, and OCS replaces it with its current value when the chatbot responds:

```text
{variable}
```

OCS supports these variables:

- `{participant_data}` - Information stored about this participant, chatbot and channel.
  See [participant data](./participant_data.md).
- `{current_datetime}` - The date and time when the response is generated.
- `{collection_index_summaries}` - The name and summary of each [indexed collection](./collections/indexed_collections/index.md) linked to your chatbot.
- `{source_material}` - The [source material](../how-to/add_a_knowledge_base.md) linked to your chatbot.
- `{media}` - The files in the linked [media collection](./collections/media_collections.md).
- `{temp_state}` - Data kept only for the current pipeline run.
  See [Temporary State](../tech-hub/python_node.md#temporary-state).
- `{session_state}` - Data kept for the whole session.
  See [Session State](../tech-hub/python_node.md#session-state).

!!! info "Localizing injected datetime"

    The injected datetime is localized to the participant's timezone if it exists in their participant data.
    When a participant uses the web UI, their browser's timezone is automatically saved to their participant data.

!!! tip "Lower cost with prompt caching"

    Place prompt variables near the end of your prompt.
    Some [LLM providers](team/llm_providers.md), like OpenAI, reuse the unchanged start of a prompt to reduce latency and cost.
    This is called [prompt caching](https://platform.openai.com/docs/guides/prompt-caching) and happens automatically.
    A variable whose value changes stops that reuse for everything after it, so put changing data last.

## Using one value from your data

You don't have to insert everything stored in `{participant_data}`, `{session_state}` or `{temp_state}` into a prompt.
You can insert just the part you need, such as the participant's name.
This keeps the prompt short and gives the model only relevant information.
See [Nested data access](../tech-hub/prompt_variables.md#nested-data-access) for the syntax.

## Using variables in other nodes

All the variables on this page work in LLM node prompts.
Router prompts accept only some of them, and other nodes use a different syntax.
If a variable does not work, see [Prompt variables vs. template variables](../tech-hub/prompt_variables.md#prompt-variables-vs-template-variables) for the syntax each node uses.

## Accessing remote context

Your website or app can send extra information with each participant message for your prompts to use.
This is an advanced feature for developers.
See [Remote context](../tech-hub/prompt_variables.md#remote-context) for how to send and read it.

## See also

- [Prompt Variables Reference](../tech-hub/prompt_variables.md)
- [Participant Data](participant_data.md)
- [Node Types](pipelines/nodes.md#llm-node)
