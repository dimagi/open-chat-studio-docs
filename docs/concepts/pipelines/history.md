# History Modes

There are several supported history modes for LLM-based nodes in a pipeline. Each is designed to solve a unique problem. In complex pipelines it is expected that a variety of history modes will be used across different nodes.

!!! info "Only valid for LLM nodes"

    Note that `history` is only applicable to nodes that have an LLM response as they affect the conversational history sent to that LLM during inference, or completion. 

## No History
Nodes will default to `No History` as their history mode. This means that when a completion is requested from the LLM, no conversational history will be supplied. One common use case might be a formatting or translation node where the previous history may not be applicable to generating the correct output.

## Node 
`Node` history will maintain a specific history for this particular node. The input to the node will be saved, along with the output from the LLM. 

!!! warning "LLM output is not necessarily the same as node output"

    In a [LLM Router](nodes.md#llm-router) node, the `output` from the node will be the same as the `input` to that node. That is, once it has done its routing, it will be a passthrough for the `input`. The output of the LLM however, will be the classification label. This is an important distinction to keep in mind.

A common use case will be in a [LLM Router](nodes.md#llm-router) node where we want to maintain a history of the node outputs (e.g., for continuity of what 'part' of the chatbot the user is interacting with), and we want to ensure that the history is using LLM outputs so that we don't unintentionally supply the LLM with few-shot examples of the wrong type of output.

## Global
Nodes with `Global` history will supply the conversational history that the user would see to the LLM. The [simple example](index.md) uses a global history as the user is interacting directly with a single LLM. 

## Named
The final history mode is called `Named` and allows you to specify a specific, named, history that can be shared between nodes. Each node using the same shared history will contribute their `input` and LLM output to the history.

!!! warning "Named history is updated immediately"

    If there are multiple nodes serially that use the same `Named` history, then each node will add to the history. In the case of serial nodes, this will result in multiple new history entries for every processed user message.


The most common use case to this will be when we have multiple parallel nodes after an [LLM Router](nodes.md#llm-router). In the [Advanced Pipelines Example](index.md#advanced-example), the general, quiz, and roleplay LLM nodes would all likely use the same shared history, giving each node visibility into the larger conversation.

Note that for this particular example, each of the nodes could use a `Global` history to achieve the same thing. However, if there was a translation or formatting node at before the final `output`, then the `Named` history mode would enable the interim nodes to share a history in the original language / formatting. 
