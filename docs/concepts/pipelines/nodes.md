# Node Types

A node is a discrete processing step in a [pipeline](index.md) that accepts a user’s input and produces an output to downstream nodes. Each node in the pipeline performs a specific task (like calling an LLM, running Python code, or routing based on logic) and processes data that flows through the pipeline.

``` mermaid
graph LR
  A@{ shape: stadium, label: "Input (ie data or prompt)" } --> B(Node);
  B --> C@{ shape: stadium, label: "Output (ie LLM response)" };
```

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for examples of pipelines using different combinations of these node types.

## LLM Node
A conversational node using AI models. This node can be [configured](../llm.md#model-configuration-parameters) including:

- a [prompt](../llm.md#prompt) to give the LLM instructions on how to respond,
- selecting a [history mode](history.md) for the LLM,
- and to use [tools](../tools/index.md) which enable it to perform additional actions.

## Routing Nodes

Routers are used to reduce cost, improve accuracy, and keep pipeline workflows flexible. A router will: receive input, analyze it, choose the next workflow step, and pass the request to the downstream node.
See the [Router Node](./router_nodes.md) page for full details.

## Python Node

Execute custom Python code for logic, data processing, or external API calls.

**Key capabilities:**

- **[Utility functions](../../tech-hub/python_node.md#utility-functions)** — read and write [participant data](../../concepts/participant_data.md), [temporary state](../../tech-hub/python_node.md#temporary-state) (per pipeline run), and [session state](../../tech-hub/python_node.md#session-state) (per user session).
- **[Attachments](../../tech-hub/python_node.md#attachments)** — access files uploaded by the user and read their contents (text, PDF, DOCX, XLSX, and [more](../../tech-hub/python_node.md#supported-file-types)).
- **[HTTP client](../../tech-hub/external-api-calls/http_client.md)** — make secure HTTP requests to external APIs using the built-in `http` global.
- **[Debugging](../../tech-hub/python_node.md#debugging-with-print)** — use `print()` to capture diagnostic output, visible in the trace detail view.

See the [Python Node](../../tech-hub/python_node.md) page for full documentation.

## Render a Template Node

The Render a Template node lets you shape the text flowing through a pipeline before it reaches the next step. You write a template that mixes fixed text with placeholders — the node fills in those placeholders at runtime using information about the current message, the participant, and the pipeline state.

Use this node to reformat a previous node's output, build a prompt for a downstream LLM node, or compose a message that includes personalized participant details.

See the [Render a Template and Send an Email Node](../../tech-hub/template_and_email_nodes.md#render-a-template-node) reference for the full variable list and template syntax.

## Send an Email Node

The Send an Email node sends an email as part of a pipeline run. The node acts as a passthrough: its output is identical to its input, so inserting it into a pipeline does not change what the next node receives.

You configure three fields — **recipient**, **subject**, and **body** — using the same Jinja2 template syntax as the Render a Template node. This means you can pull in participant details, session state, or the current message text directly into the email content.

The **body** field is optional. When left blank, the node uses the pipeline input as the email body.

See the [Render a Template and Send an Email Node](../../tech-hub/template_and_email_nodes.md#send-an-email-node) reference for recipient field syntax, variable reference, and examples.

## Extract Structured Data Node
Extract structured data from the input. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Update Participant Data Node
Extract structured data and save it as participant data.


