# Experiments

An 'Experiment' is the current name used in Open Chat Studio to refer to a 'chatbot'. This will soon be a legacy term as we transition fully to the term 'Chatbots.'

An Experiment links all the configuration and data for a chatbot including user sessions, data, actions etc.

!!! warning "Deprecation Warnig"

    The term will be phased out as we fully adopt 'Chatbots' instead. Bot building will shift from the current 'form-based' method to primarily using the pipeline approach. All existing experiments will be smoothly migrated with adequate notice, and users can contact the Dimagi team for assistance during this transition.

## Experiment Types

There are three different types of chatbots that you can build in Open Chat Studio:

- Base language model
- Assistant
- Pipeline

### Base language model

This kind of bot is the most commonly used and simple to configure. It is backed the standard language model APIs such as the OpenAI [chat completions API][1], Anthropic [messages API][2] or Google [Gemini API][3].

Bots configured in this way have all the basic features (memory, source material etc.) and can also use some of the advanced features like Scheduling and Reminders.


### Assistant
Assistant bots make use of OpenAI [Assistants][4]. The main advantage of using Assistants is that your bot gets access to the OpenAI tools:

#### Code Interpreter
This allows the bot to write and execute code to accomplish tasks.

For more information see the [OpenAI docs][5].

#### File Search
!!! warning

    The functionality described here is planned to be replaced by [Indexed Collections][indexed-collections] in the future. It’s recommended to start using Indexed Collections instead to ensure forward compatibility.


This allows the bot to search and reference information provided in uploaded files. Unless your bot needs either of these capabilities, you should use a Base Language Model type bot.

For more information see the [OpenAI docs][6].

### Pipeline
[Pipelines](../pipelines/index.md) allow you to create more complex bots by defining a ‘graph’ (in the computer science sense) of nodes. You can think of this graph as a workflow that flows from input to output. Each message to the bot is processed by the graph to produce a final output. A single response from the chatbot will be one successful path through the graph from the input node to the output node.

This can be useful if you want to build a complex bot that performs different tasks depending on the user’s request. Generally, trying to make a single bot prompt do multiple functions doesn’t work well so it is better to create multiple prompts for each task and then combine them using a Pipeline. This is similar to the Multi-bot setup but allows more flexibility and complexity.


[1]: https://platform.openai.com/docs/guides/text-generation
[2]: https://docs.anthropic.com/en/api/messages
[3]: https://ai.google.dev/
[4]: https://platform.openai.com/docs/assistants/overview
[5]: https://platform.openai.com/docs/assistants/tools/code-interpreter
[6]: https://platform.openai.com/docs/assistants/tools/file-search
[indexed-collections]: ../collections/indexed.md
