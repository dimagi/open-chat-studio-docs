# Pipelines

A **pipeline** is a visual workflow that defines how your chatbot processes a user's message and generates a response. It is made up of connected **nodes** — each node performs one task, such as calling an AI model, running custom logic, or routing the conversation to a different path. A message enters the pipeline as **input**, passes through one or more nodes, and exits as the chatbot's **output**.

!!! info "Pipelines are now the standard way to build bots"

    Pipelines are the default way to build bots in Open Chat Studio. They replace older approaches and support everything from simple single-step responses to complex workflows with branching, parallel steps, and safety layers.

## A Simple Example

The pipeline below has a single node. The user sends a message, the LLM generates a reply, and that reply is sent back to the user. That's it.

<figure markdown="span">
  ![A Simple Pipeline](../../assets/images/pipeline-basic.png)
  <figcaption>A simple pipeline</figcaption>
</figure>

``` mermaid
graph LR
  A@{ shape: stadium, label: "Input" } --> B(LLM);
  B --> C@{ shape: stadium, label: "Output" };
```

Analyzing this pipeline from left to right:

* the user sends a message to the bot (this is the `input`)
* the message is then passed to the LLM which generates a response
* the response is then sent back to the user (this is the `output`)

Every time a user sends a message, the pipeline workflow runs from start to finish and the final output is sent back to the user.

Each step in a pipeline is called a **node**. Pipelines can have as many nodes as your workflow requires. See [Node Types](nodes.md) for a full list of what each node can do.

## How a Pipeline Runs

Open Chat Studio  runs your application in organized steps. Think of it like a well-coordinated team where different parts of your application (pipeline **nodes**) communicate through shared **channels** (pipeline edges / connections).

When a user sends a message, Open Chat Studio processes the pipeline in repeating cycles:

**Plan** → **Execute** → **Update** → Repeat

1. **Plan**: Identify which nodes are ready to run. On the first cycle, this is the node connected to the user's input. On later cycles, it is any node whose dependencies have been satisfied.

2. **Execute**: Run all ready nodes at the same time. Each node works independently — it cannot see the results of other nodes running in the same cycle. Collect the results from all nodes just executed and make them available to the next cycle

3. **Update**: Share the results from all nodes so they're available for the next step.

This repeats until all nodes have completed or a maximum step limit is reached.

!!! tip "Running nodes in parallel"

    Because multiple nodes can execute in the same cycle, pipelines naturally support parallel processing. See [Parallel Pipelines](./parallel.md) for details.

## Asking the Assistant About a Pipeline

!!! tip "Chat widget context"

    When you are viewing a pipeline in Open Chat Studio, the in-app chat widget automatically receives the pipeline's structure (nodes and connections) and event trigger data as context. This means you can ask the assistant questions about the pipeline you are currently editing — for example, what a particular node does or how the flow is connected. The context updates automatically as you make changes to the pipeline.
