# Chatbots

!!!info
    ### Announcement: Pipelines Feature Rolling Out
    We're excited to announce that Pipelines is now being rolled out across Open Chat Studio. This new feature will transform how you build and manage chatbots with several key improvements:

    - **Simplified Workflow**: Pipelines introduces a cleaner, more intuitive interface for building chatbots
    - **Streamlined Bot Creation**: We're transitioning from the 'form-based' approach to make Pipelines the primary (and eventually only) method for bot creation
    - **Seamless Transition**: All existing experiments will continue to work without disruption during this rollout
    - **Full Support Available**: The Dimagi team is ready to provide help and support as you explore this new feature

    We look forward to seeing what you create with Pipelines!


### Pipeline
[Pipelines](../pipelines/index.md) allow you to create more complex bots by defining a ‘graph’ (in the computer science sense) of nodes. You can think of this graph as a workflow that flows from input to output. Each message to the bot is processed by the graph to produce a final output. A single response from the chatbot will be one successful path through the graph from the input node to the output node.

This can be useful if you want to build a complex bot that performs different tasks depending on the user’s request. Generally, trying to make a single bot prompt do multiple functions doesn’t work well so it is better to create multiple prompts for each task and then combine them using a Pipeline. This is similar to the Multi-bot setup but allows more flexibility and complexity.
