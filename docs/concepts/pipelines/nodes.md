# Node Types

A node is a "step" in a [pipeline](index.md) workflow that processes a user’s input and produces a result. Each node in the pipeline performs a specific action (like calling an LLM, running Python code, or routing based on logic) and processes data that flows through the pipeline.

``` mermaid
graph LR
  A@{ shape: stadium, label: "User Input" } --> B(Node);
  B --> C@{ shape: stadium, label: "Result Output" };
```

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for examples of pipelines using different combinations of these node types.

## LLM Node
A conversational node using LLMs with prompts and tools. This node can be [configured](../llm.md#model-configuration-parameters) including:

- a [prompt](../llm.md#prompt) to give the LLM instructions on how to respond,
- selecting a [history mode](history.md) for the LLM,
- and to use [tools](../tools/index.md) which enable it to perform additional actions.

## Routing Nodes

See the [Router Node](./router_nodes.md) page for full documentation on Static Router and LLM Router.

## Python Node

Execute custom Python code for logic, data processing, or external API calls.

**Key capabilities:**

- **[Utility functions](../../tech-hub/python_node.md#utility-functions)** — read and write [participant data](../../concepts/participant_data.md), [temporary state](../../tech-hub/python_node.md#temporary-state) (per pipeline run), and [session state](../../tech-hub/python_node.md#session-state) (per user session).
- **[Attachments](../../tech-hub/python_node.md#attachments)** — access files uploaded by the user and read their contents (text, PDF, DOCX, XLSX, and [more](../../tech-hub/python_node.md#supported-file-types)).
- **[HTTP client](../../tech-hub/external-api-calls/http_client.md)** — make secure HTTP requests to external APIs using the built-in `http` global.
- **[Debugging](../../tech-hub/python_node.md#debugging-with-print)** — use `print()` to capture diagnostic output, visible in the trace detail view.

See the [Python Node](../../tech-hub/python_node.md) page for full documentation.

## Render a Template Node
Renders a [Jinja](https://jinja.palletsprojects.com/en/stable/templates/) template.

### Available Template Variables
The following variables are available in the template context:

| Key                     | Description                                                          | Type            |
|-------------------------|----------------------------------------------------------------------|-----------------|
| `input`                 | The input to the node                                                | String          |
| `node_inputs`           | The list of all inputs to the node in the case of parallel workflows | List of strings |
| `temp_state`            | Pipeline temporary state                                             | Dict            |
| `session_state`         | Session state                                                        | Dict            |
| `participant_details`   | Participant details (`identifier`, `platform`)                       | Dict            |
| `participant_data`      | Participant data                                                     | Dict            |
| `participant_schedules` | Participant schedule data                                            | List            |

### Sample Template
```
Input: {{ input }}
Node Inputs: {{ node_inputs }}
Temp State Key: {{ temp_state.my_key }}
Participant ID: {{ participant_details.identifier }}
Participant Platform: {{ participant_details.platform }}
Participant Data: {{ participant_data.custom_key }}
Schedules: {{ participant_schedules }}
```

## Send an Email Node
Send an email as part of a pipeline. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

The **subject**, **recipient**, and **body** fields all accept plain strings or [Jinja2](https://jinja.palletsprojects.com/en/stable/templates/) templates using the same [template variables](#available-template-variables) as the Template node.

The **recipient** field accepts a comma-separated list of email addresses and supports Jinja2 templates. For example:

- Single address: `{{ participant_data.email }}`
- List of addresses: `{{ participant_data.emails | join(',') }}`
- Delimited string: `{{ participant_data.emails | split(';') | join(',') }}`

The **body** field is optional. When left blank, the node input is used as the email body — this preserves backwards compatibility with existing pipelines.

!!! example "Dynamic subject and personalised body"

    **Subject:** `Update for {{ participant_details.identifier }}`

    **Body:**
    ```
    Hello {{ participant_data.name }},

    Here is your update: {{ input }}
    ```

## Extract Structured Data Node
Extract structured data from the input. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Update Participant Data Node
Extract structured data and save it as participant data.


