Prompt variables are a great way to make your prompt dynamic or tailored to the participant by injecting data into specified placeholders. These variables are predefined and look like this:

```
{variable}
```

The following variables are currently supported:

- `{source_material}` - The [source material](../how-to/add_a_knowledge_base.md) linked to your bot.
- `{participant_data}` - Information specific to this participant, bot and channel. See [here][participant_data] for more information. 
- `{current_datetime}` - This refers to the date and time at which the response is generated.

!!! info "Localizing injected datetime"
    The injected datetime will be localized to the participant's timezone if it exists in their participant data. When a participant uses the web UI, their browser's timezone will automatically be saved to their participant data.

!!! info "A note on prompt caching"
    Some LLM providers like OpenAI, use a technique called "prompt caching" to reduce latency and costs (See [here][prompt_caching]). This happens automatically. However, caching is only effective for static data i.e. data that does not change. To take full advantage of this caching mechanism, you should place prompt variables near the end of your prompt whenever possible

[participant_data]: ../concepts/participant_data.md
[prompt_caching]: https://platform.openai.com/docs/guides/prompt-caching
