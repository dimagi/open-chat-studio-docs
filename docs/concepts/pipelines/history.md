# Conversation History

!!! note "Definition"
    An LLM node's conversation memory is controlled by two independent settings: **History** decides *which* messages the model gets to see, and **History Mode** decides *how* those messages are compressed once there are too many of them. They have similar names but solve different problems.

An AI model has no memory of its own. Each time OCS asks a model for a reply, it sends a fresh, self-contained request — the model only "remembers" earlier parts of the conversation if they are included in that request.

Open Chat Studio always stores every message in a chatbot's [session](../sessions.md), regardless of how any node is configured. Setting a node's History to `No History` doesn't stop messages from being saved — it only changes what gets sent to the model. Storage and memory are two separate things.

**History** and **History Mode** are where you control that second part. Both are per-node settings, so different nodes in the same pipeline can be given a different slice of the same stored conversation, compressed in different ways.

This choice matters because everything sent to the model — your prompt, the conversation history, and its reply — shares the same [token budget](../llm.md#max-token-limit). Sending more history gives the model more context, but costs more tokens and can slow responses down.

!!! info "Only valid for LLM nodes"

    History and History Mode are only applicable to nodes that have an LLM response, since they control the conversational history sent to that LLM during inference, or completion.

## History

The **History** setting controls *which* messages a node's LLM sees: its own, the whole conversation, or a shared slice of it.

### At a Glance

| History | What the LLM sees |
|---|---|
| [Global](#global) | The full conversation the participant sees.  This is the default.|
| [Node](#node) | Only this node's own past inputs and outputs. |
| [Named](#named) | A shared history that specific nodes contribute to together. |
| [No History](#no-history) | Nothing from earlier in the conversation. |

Each option is designed to solve a different problem, and in complex pipelines it is expected that a variety of History settings will be used across different nodes.

### No History
Nodes will default to `No History`. This means that when a completion is requested from the LLM, no conversational history will be supplied. One common use case might be a formatting or translation node where the previous history may not be applicable to generating the correct output.

### Node
`Node` history will maintain a specific history for this particular node. The input to the node will be saved, along with the output from the LLM.

!!! warning "LLM output is not necessarily the same as node output"

    In a [LLM Router](./router_nodes.md#llm-router-node) node, the `output` from the node will be the same as the `input` to that node. That is, once it has done its routing, it will be a passthrough for the `input`. The output of the LLM however, will be the classification label. This is an important distinction to keep in mind.

A common use case will be in a [LLM Router](./router_nodes.md#llm-router-node) node where we want to maintain a history of the node outputs (e.g., for continuity of what 'part' of the chatbot the participant is interacting with), and we want to ensure that the history is using LLM outputs so that we don't unintentionally supply the LLM with few-shot examples of the wrong type of output.

### Global
Nodes with `Global` history will supply the conversational history that the participant would see to the LLM. The [simple example](index.md) uses a global history as the participant is interacting directly with a single LLM.

### Named
The final History option is called `Named` and allows you to specify a specific, named, history that can be shared between nodes. Each node using the same shared history will contribute their `input` and LLM output to the history.

!!! warning "Named history is updated immediately"

    If there are multiple nodes serially that use the same `Named` history, then each node will add to the history. In the case of serial nodes, this will result in multiple new history entries for every processed participant message.

The most common use case to this will be when we have multiple parallel nodes after an [LLM Router](./router_nodes.md#llm-router-node). In the [Advanced Pipelines Example](../../how-to/workflow_cookbook.md#split-a-chatbot-into-multiple-smaller-chatbots), the general, quiz, and roleplay LLM nodes would all likely use the same shared history, giving each node visibility into the larger conversation.

Note that for this particular example, each of the nodes could use a `Global` history to achieve the same thing. However, if there was a translation or formatting node before the final `output`, then the `Named` history option would enable the interim nodes to share a history in the original language / formatting.

## History Mode

Once a node has more history than fits comfortably in the model's token budget, something has to give. **History Mode** controls what happens to older messages when that limit is reached. It only has an effect when History is set to `Node`, `Global`, or `Named` — with `No History` there's nothing to compress.

The History Mode dropdown offers three options:

### Summarize
The Summarize option compresses history when it exceeds a token limit by summarizing older messages while preserving more recent ones. If the token count exceeds the limit, older messages will be summarized while keeping the last few messages intact. This is the default History Mode.

**Token Limit**: Sets the maximum number of tokens before summarization occurs. When this threshold is reached, the system will summarize older messages to reduce token count.

### Truncate Tokens
The Truncate Tokens option removes older messages when a token limit is reached, ensuring the total token count stays below a specified threshold. If the token count exceeds the limit, older messages will be removed until the token count is below the limit.

 **Token Limit**: Sets the maximum number of tokens before truncation occurs. When this threshold is reached, the system will remove older messages to reduce token count.

### Max History Length
The Max History Length option keeps only the last N messages, where N is the specified number, dropping older ones once that limit is reached.

**Max History Length**: Specifies how many of the most recent messages to keep in the history. Only this number of messages will be sent to the LLM.

These History Mode options help pipeline authors balance context preservation with performance and cost considerations, particularly for long-running conversations or complex applications.
