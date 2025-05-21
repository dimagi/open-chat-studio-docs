# Chatbots

!!!info
    ### Announcement: Pipelines Feature Rolling Out
    We're excited to announce that Pipelines is now being rolled out across Open Chat Studio. This new feature will transform how you build and manage chatbots with several key improvements:

    - **Simplified Workflow**: Pipelines introduces a cleaner, more intuitive interface for building chatbots
    - **Streamlined Bot Building**: We're transitioning from the 'form-based' approach to make Pipelines the primary (and eventually only) method for bot building
    - **Seamless Transition**: All existing experiments will continue to work without disruption during this rollout
    - **Full Support Available**: The Dimagi team is ready to provide help and support as you explore this new feature

    We look forward to seeing what you create with Pipelines!


### Pipeline
[Pipelines](../pipelines/index.md) lets you build more advanced bots by defining a graph—a network of connected nodes representing different steps in a workflow. You can think of this graph as a flowchart that starts with user input and ends with the bot’s response. Each message sent to the bot follows a specific path through the graph to generate the final output.

This approach is especially useful when you want your bot to handle different types of tasks based on the user’s request. Instead of forcing a single prompt to do everything (which can lead to more testing and building time), it’s better to create separate prompts for each function and link them together using a Pipeline. This concept is similar to the Multi-bot setup but offers greater flexibility and complexity.
