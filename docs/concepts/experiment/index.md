# Experiments

An 'Experiment' is the current name used in Open Chat Studio to refer to a 'chatbot'. The name may change in the
future.

An Experiment links all the configuration and data for a chatbot including user sessions, data, actions etc.

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
This allows the bot to search and reference information provided in uploaded files. Unless your bot needs either of these capabilities, you should use a Base Language Model type bot.

For more information see the [OpenAI docs][6].

### Pipeline
This is a beta feature that has not yet been fully released. Pipelines allow you to create more complex bots by defining a ‘graph’ of nodes. Each message to the bot is processed by the graph to produce a final output.

This can be useful if you want to build a complex bot that performs different tasks depending on the user’s request. Generally, trying to make a single bot prompt do multiple functions doesn’t work well so it is better to create multiple prompts for each task and then combine them using a Pipeline. This is similar to the Multi-bot setup but allows more flexibility and complexity.


[1]: https://platform.openai.com/docs/guides/text-generation
[2]: https://docs.anthropic.com/en/api/messages
[3]: https://ai.google.dev/
[4]: https://platform.openai.com/docs/assistants/overview
[5]: https://platform.openai.com/docs/assistants/tools/code-interpreter
[6]: https://platform.openai.com/docs/assistants/tools/file-search
