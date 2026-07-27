# Conversation History

!!! note "Definition"

    An LLM node's conversation memory is controlled by two independent, per-node settings: **History** decides *which* messages the model gets to see, and **History Mode** decides *how* those messages are compressed once there are too many. They apply only to nodes with an LLM response.

AI models have no memory of their own — each request OCS sends is self-contained. Open Chat Studio always stores the full conversation in the chatbot's [session](../sessions.md) regardless of how a node is configured; [History](#history) and [History Mode](#history-mode) only control what's *sent to the model*, not what's saved.

## History

The **History** setting controls *which* messages a node's LLM sees: its own, the whole conversation, or a shared slice of it.

### History Options

| History | What the LLM sees |
|---|---|
| [Global](#global) | The full conversation the participant sees. This is the default for an [LLM Node](./nodes.md#llm-node). |
| [Node](#node) | Only this node's own past inputs and outputs. This is the default for an [LLM Router](./router_nodes.md#llm-router-node) node. |
| [Named](#named) | A shared history that specific nodes contribute to together. |
| [No History](#no-history) | Nothing from earlier in the conversation. |

Each option is designed to solve a different problem, and in complex pipelines it is expected that a variety of History settings will be used across different nodes.

### Global
Nodes with `Global` history will supply the conversational history that the participant would see to the LLM. The [simple example](index.md) uses a global history as the participant is interacting directly with a single LLM.

### Node
`Node` history will maintain a specific history for this particular node. The input to the node will be saved, along with the output from the LLM.

!!! warning "LLM output is not necessarily the same as node output"

    In a [LLM Router](./router_nodes.md#llm-router-node) node, the `output` from the node will be the same as the `input` to that node. That is, once it has done its routing, it will be a passthrough for the `input`. The output of the LLM however, will be the classification label. This is an important distinction to keep in mind.

A common use case will be in a [LLM Router](./router_nodes.md#llm-router-node) node where we want to maintain a history of the node outputs (e.g., for continuity of what 'part' of the chatbot the participant is interacting with), and we want to ensure that the history is using LLM outputs so that we don't unintentionally supply the LLM with few-shot examples of the wrong type of output.

### Named
This option, allows you to specify a specific, named, history that can be shared between nodes. Each node using the same shared history will contribute their `input` and LLM output to the history.

!!! warning "Named history is updated immediately"

    If there are multiple nodes serially that use the same `Named` history, then each node will add to the history. In the case of serial nodes, this will result in multiple new history entries for every processed participant message.

The most common use case to this will be when we have multiple parallel nodes after an [LLM Router](./router_nodes.md#llm-router-node). In the [Advanced Pipelines Example](../../how-to/workflow_cookbook.md#split-a-chatbot-into-multiple-smaller-chatbots), the general, quiz, and roleplay LLM nodes would all likely use the same shared history, giving each node visibility into the larger conversation.

Note that for this particular example, each of the nodes could use a `Global` history to achieve the same thing. However, if there was a translation or formatting node before the final `output`, then the `Named` history option would enable the interim nodes to share a history in the original language / formatting.

### No History

Choosing `No History` means that when a completion is requested from the LLM, no conversational history will be supplied. One common use case might be a formatting or translation node where the previous history may not be applicable to generating the correct output.

## History Mode

This choice matters because everything sent to the LLM model — your prompt, the conversation history, and its reply — shares the same [token budget](../llm.md#max-token-limit). Sending more history gives the model more context, but costs more tokens and can slow responses down.

Once a node has more history than fits comfortably in the model's token budget, something has to give. **History Mode** controls what happens to older messages when that limit is reached. It only has an effect when History is set to `Node`, `Global`, or `Named` — with `No History` there's nothing to compress.

### History Mode Options

| History Mode | What happens to older messages |
|---|---|
| [Summarize](#summarize) | Condensed into a summary once the token limit is reached. This is the default. |
| [Truncate Tokens](#truncate-tokens) | Dropped once the token limit is reached, until back under it. |
| [Max History Length](#max-history-length) | Dropped once the message count exceeds N. |

### Summarize
Compresses older messages into a summary once the token limit is reached, keeping the most recent messages intact.

**Token Limit**: Maximum number of tokens allowed before summarization occurs.

### Truncate Tokens
Removes older messages once the token limit is reached, until the total is back under the threshold.

**Token Limit**: Maximum number of tokens allowed before truncation occurs.

### Max History Length
Keeps only the most recent N messages, dropping older ones once that limit is reached.

**Max History Length**: Number of recent messages to keep. Only this number of messages will be sent to the LLM.
