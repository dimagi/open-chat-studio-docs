# Node Types

!!! note Examples

    See [chatbot workflow cookbook](../../how-to/workflow_cookbook.md) for example usage. 

## LLM Node
Use an LLM to respond to the node input. This node can be [configured](../llm.md#model-configuration-parameters) including:
- a [prompt](../llm.md#prompt) with promptto give the LLM instructions on how to respond,
- selecting a [history mode](history.md) for the LLM,
- and to use [tools](../tools/index.md) which enable it to perform additional actions.

## Routing Nodes

See the [Router Node](./router_nodes.md) page for full documentation including both Static Router and LLM Router

## Assistant as a Node
Use an [OpenAI assistant](../../concepts/assistants.md) for advanced conversational AI.

## Python Code Node
Execute custom Python code for logic, data processing, and external API calls. 
 - See the [Python Node](./python_node.md) page for full documentation including [utility functions](./python_node.md#utility-functions) to interact with users data
  - Utility functions can interact with pipeline state including [Temporary State](./python_node.md#temporary-state) and user [Session State](./python_node.md#session-state)
 - and [attachments](./python_node.md#attachments) uploaded by user
 - See the [HTTP client](../../tech-hub/http_client.md) documentation for calling external APIs

## Template
Renders a [Jinja](https://jinja.palletsprojects.com/en/stable/templates/) template.

## Available Template Variables
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

## Email Node
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
