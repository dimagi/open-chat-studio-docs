
Prompt variables are an effective way to make your prompt dynamic or tailored towards the participant by inserting data into specified placeholders. These variables are predefined and formatted like this:

```
{variable}
```

The following varibles are currently supported:

{source_material} - The source material linked with your bot.
{participant_data} - Information specific to this participant. This data can only be accessed within the context of this bot and participant, ensuring only this bot can access it.
{current_datetime} - Refers to the date and time when the response is generated.

!!! info "Localizing injected datetime"

The injected datetime will be localized to the participants timezone if it exists in there participant data. When a participant uses the web UI, their browser's timezone is automatically saved in their participant data.

!!! info "A note on prompt caching"

Some LLM providers, such as OpenAI, use a method called "prompt caching" to decrease latency and costs (See here). This is done automatically. However, caching only works for static data i.e., data that does not change. To take full advantage of this caching mechanism, you should place prompt variables nearer the end of your prompt whenever possible.