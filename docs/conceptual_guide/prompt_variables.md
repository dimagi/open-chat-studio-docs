Prompt variables are a great way to make your prompt dynamic or tailored to the participant by injecting data into specified placeholders. These variables are predefined and look like this:

```
{variable}
```

The following variables are currently supported:

- `{source_material}` - The [source material](../how-to/adding_source_material.md) linked to your bot.
- `{participant_data}` - Data available for this participant. This data is scoped to a specific participant and bot, meaning that only this bot will "see" this data.
- `{current_datetime}` - This refers to the date and time at which the response is generated.

!!! info "Localizing injected datetime"
    The injected datetime will be localized to the participant's timezone if it exists in their participant data. When a participant uses the web UI, their browser's timezone will automatically be saved to their participant data.


!!! info "A note on prompt caching"
    Some LLM providers like OpenAI, use a technique called "prompt caching" to reduce latency and costs (See [here][0]). This happens automatically. However, caching is only effective for static data i.e. data that does not change. To take full advantage of this caching mechanism, you should place prompt variables near the end of your prompt whenever possible

[0]: https://platform.openai.com/docs/guides/prompt-caching