# Experiments (Deprecated feature)

An Experiment was the original name for a chatbot in Open Chat Studio. The UI now uses the term [Chatbots](../chatbots/index.md) throughout. You may still see "Experiment" in older parts of the interface, API responses, or documentation.

## Historical Notes

An Experiment links all the configuration and data for a chatbot including participant sessions, data, actions etc.

### Experiment Types

There were three different types of chatbots that you could build in Open Chat Studio:

- Base language model
- Assistant (since [removed](../assistants.md))
- Pipeline

#### Base language model

This kind of bot is the most commonly used and simple to configure. It is backed the standard language model APIs such as the OpenAI [chat completions API][1], Anthropic [messages API][2] or Google [Gemini API][3].

Bots configured in this way have all the basic features (memory, source material etc.) and can also use some of the advanced features like Scheduling and Reminders.

#### Assistant

!!! warning "Removed"
    Assistant-type bots have been [removed](../assistants.md) — OpenAI retired the Assistants API on 26 August 2026. See the [migration guide](../../how-to/assistants_migration.md) if you still need to move a chatbot off this type.

Assistant bots made use of OpenAI [Assistants][4]. The main advantage of using Assistants was that your bot got access to the OpenAI tools:

##### Code Interpreter
This allowed the bot to write and execute code to accomplish tasks. An [LLM node](../pipelines/nodes.md#llm-node) offers the same capability as a builtin tool.

For more information see the [OpenAI docs][5].

##### File Search
This allowed the bot to search and reference information provided in uploaded files. [Indexed Collections][indexed-collections] replace it.

For more information see the [OpenAI docs][6].

#### Pipeline
[Pipelines](../pipelines/index.md) allow you to create more complex bots by defining a ‘graph’ (in the computer science sense) of nodes. You can think of this graph as a workflow that flows from input to output. Each message to the bot is processed by the graph to produce a final output. A single response from the chatbot will be one successful path through the graph from the input node to the output node.

This can be useful if you want to build a complex bot that performs different tasks depending on the participant’s request. Generally, trying to make a single bot prompt do multiple functions doesn’t work well so it is better to create multiple prompts for each task and then combine them using a Pipeline. This is similar to the Multi-bot setup but allows more flexibility and complexity.

[1]: https://platform.openai.com/docs/guides/text-generation
[2]: https://docs.anthropic.com/en/api/messages
[3]: https://ai.google.dev/
[4]: https://platform.openai.com/docs/assistants/overview
[5]: https://platform.openai.com/docs/assistants/tools/code-interpreter
[6]: https://platform.openai.com/docs/assistants/tools/file-search
[indexed-collections]: ../collections/indexed.md
