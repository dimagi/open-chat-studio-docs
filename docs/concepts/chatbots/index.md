# Chatbots

!!!info
    ### Announcement: Chatbots Feature Rolling Out
    We are excited to announce that we are releasing a new way to build chatbots in Open Chat Studio. You may already be using 'Pipelines'
    to build 'Experiments'. We are now transitioning to the term 'Chatbots' and away from 'Experiments'. This change is part of our ongoing effort to improve the user experience and make it easier for you to create and manage your chatbots.
    The term 'Experiment' will be phased out as we fully adopt 'Chatbots' instead. Bot building will shift from the current 'form-based' method to primarily using the pipeline approach. All existing experiments will continue to work without disruption during this rollout.

    Some key improvements include:

    - **Simplified Workflow**: Chatbots introduces a cleaner, more intuitive interface for building chatbots

    - **Streamlined Bot Building**: We're transitioning from the 'form-based' approach to make pipelines the primary (and eventually only) method for bot building

    - **Enhanced Features**: The new system allows building more bots with greater flexibility and complexity.

    - **Enhanced Features**: Chatbots includes features that are not availble to legacy 'Experiments' including:
        - LLM tools such as 'web search', 'code interpreter', and 'file search'

    For more information checkout out our [FAQ page](../chatbots/rollout_faq.md)


## What is a Chatbot?
A chatbot is a program that simulates conversation with people. It can use simple rules or advanced AI to understand and respond to messages. 

Within the context of Open Chat Studio, a chatbot is a specific configuration of a language model (LLM) that is designed to interact with users conversationally. It can be customized to perform various tasks, such as answering questions, providing information, or assisting with specific workflows.

The specific way that a chatbot is configured with Open Chat Studio is through the use of a [**Pipeline**](../pipelines/index.md). You can think of a pipeline as a flowchart that starts with user input on one end and ends with the chatbot’s response at the other. Each message sent to the bot follows a specific path through the pipeline to generate the final output. 

This approach can be useful if you want to build a complex bot that performs different tasks depending on the user’s request. Generally, trying to make a single bot prompt do multiple functions doesn’t work well, so it is better to create multiple prompts for each task and then combine them using a Pipeline. 


## What is a Pipeline?
As described above, a pipeline is a flowchart-like structure that defines how a chatbot processes user input and generates responses. It consists of a series of connected nodes, each representing a specific step in the workflow. Each node can perform a specific function, such as processing user input, generating responses, or integrating with external systems.

The simplest pipeline is a single node that takes user input and generates a response. More complex pipelines can include multiple nodes that work together to create a more sophisticated interaction.

You can read more about pipelines in the [Pipelines documentation](../pipelines/index.md).
