# Node Types

!!! note Examples

    See [cookbook](../../how-to/workflow_cookbook.md) for example usage. 

## LLM
Use an LLM to respond to the node input. This node can be configured with a prompt to give the LLM instructions on how to respond. It can also be configured to use [tools](../tools/index.md) which enable it to perform additional actions.

## Routers

Router nodes allow you to route the input to one of the linked nodes. This is useful if you want your bot to behave
differently depending on the input or some persistent context. For example, you might want to route the input to a different node if the user is asking for help with a specific topic.

Router nodes share some common configuration such as the list of route options. Router nodes can also be configured to
tag the output message with the selected route. This is useful for debugging and for tracking the flow of messages through the pipeline.
The format of the tag is `<node_name>:<route_name>` where `<route_name>` is the name of the route selected by the router node.

!!! info "Router Keywords Are Case-Insensitive"

    All router keywords are automatically converted to lowercase. When configuring router outputs, use lowercase keywords to match this behavior. Keyword matching is case-insensitive, so "HELP", "Help", and "help" will all match the same route.

### LLM Router
Routes the input to one of the linked nodes using an LLM. In this case, the LLM acts as a classifier using the prompt provided to classify an incoming message into a set of discrete categories that allow messages to be routed.

The `outputs` listed by the node are the available classification labels. These should match the classification categories specified in your prompt. They can be adjusted through the `Advanced` settings for the node. The top output, which is prepended by a blue `*` is the default label. In the event that the LLM generates a response outside of the specified `outputs`, the route with the default label will be taken.

!!! info "Best practices for configuring a LLM Router"

    It is advisable to use the [Node history mode](history.md#node) for an LLM Router to avoid unintentionally supplying few-shot examples to the node with an incorrect output format.

### Static Router
The Static Router node allows you to route the input to one of the linked nodes based on the value of a specific key in the data source. This is useful if you want your bot to behave differently depending on the value of a specific key in the data source.

The data source can be any of the following:

* [Participant Data](../participant_data.md)
* [Session State](#session-state)
* [Temporary State](#temporary-state)

The key should be a name of a field in the data source and supports selecting nested fields via the `<field>.<subfield>` syntax. For example, if the data source is a JSON object with the following structure:

```json
{
    "user": {
        "name": "John",
        "age": 30
    }
}
```

You can select the `name` field using the key `user.name` and the `age` field using the key `user.age`.

If the field is not present in the data source, the router will not route the input to the first linked node.

## Assistant
Use an OpenAI assistant to respond to the input.

## Python Node
The Python node allows the bot builder to execute custom Python code to perform logic, data processing, or other tasks.

The code **must** define a `main` function which takes the node input as a string and returns a string to pass to the next node.
The `main` function must also accept arbitrary keyword arguments to support future features. Here is an example of what the code might look like:

```python
def main(input, **kwargs) -> str:
    # Put your code here
    return input
```

The `input` parameter is a string that contains the input to the node. The return value of the function is a string that will be passed to the next node in the pipeline.

### Additional Keyword Arguments

The following additional arguments are provided:

* `node_inputs: list[str]` - A list of all the inputs to the node at the time of execution. This will be the same as `[input]` except when the node is part of a workflow with [parallel branches](./index.md#parallel-nodes).

!!! warning

    All the code must be encapsulated in a `main` function. You can write other functions but they must be within the scope of the `main` function. For example:

    ``` py
    def main(input, **kwargs):
        def important(arg):
            return arg + "!"

        return important(input)
    ```

### Utility Functions

The Python node provides a set of utility functions that can be used to interact with the user's data and the pipeline state.

#### ::: python_node.get_participant_data
#### ::: python_node.set_participant_data
#### ::: python_node.set_participant_data_key
#### ::: python_node.append_to_participant_data_key
#### ::: python_node.increment_participant_data_key
#### ::: python_node.get_participant_schedules
#### ::: python_node.get_temp_state_key
#### ::: python_node.set_temp_state_key
#### ::: python_node.get_session_state_key
#### ::: python_node.set_session_state_key
#### ::: python_node.get_selected_route
#### ::: python_node.get_node_path
#### ::: python_node.get_all_routes
#### ::: python_node.add_message_tag
#### ::: python_node.add_session_tag
#### ::: python_node.get_node_output
#### ::: python_node.require_node_outputs
#### ::: python_node.wait_for_next_input
#### ::: python_node.abort_with_message

### Temporary State
The Python node can also access and modify the temporary state of the pipeline. The temporary state is a dictionary that is unique to each run of the pipeline (each new message from the user) and is not stored between sessions.

The temporary state can be accessed and modified using the [get_temp_state_key](#python_node.get_temp_state_key) and [set_temp_state_key](#python_node.set_temp_state_key) utility functions.

Temporary state contains the following keys by default. These keys can not be modified or deleted:

| Key           | Description                                                                  |
|---------------|------------------------------------------------------------------------------|
| `user_input`  | The message sent by the user                                                 |
| `outputs`     | The outputs generated by the previous node                                   |
| `attachments` | A list of attachments passed in by the user. See [Attachments](#attachments) |

In addition to these keys, the temporary state can also contain custom key-value pairs that can be set and accessed by the Python node and by the [Static Router](#static-router) node.

Here is an example of a temporary state dictionary:

```python
{
    "user_input": "Please help me with my problem",
    "outputs": {
        "Assistant": "I'm here to help! What can I do for you?"
    },
    "attachments": [
        Attachment(...),
    ],
    "my_custom_key": "my_custom_value",
}
```

### Session State
The Python node can also access and modify the state of the participant's session. This state is a dictionary that is scoped to each session that the user might have with the bot.

The session state can be accessed and modified using the [get_session_state_key](#python_node.get_session_state_key) and [set_session_state_key](#python_node.set_session_state_key) utility functions.

### Attachments

Part of the temporary state is a list of attachments. Attachments are files that the user has uploaded to the bot. Each attachment has the following fields:

| Field                 | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `name`                | The name of the file                                                  |
| `size`                | The size of the file in bytes                                         |
| `content_type`        | The MIME type of the file                                             |
| `upload_to_assistant` | Whether the file should be uploaded to the assistant as an attachment |
| `read_bytes()`        | Reads the attachment content as bytes.                                |
| `read_text()`         | Reads the attachment content as text.                                 |

Here is an example of an attachment object:

```python
attachment = Attachment(
    name="proposal.pdf",
    size=1234,
    content_type="application/pdf",
    upload_to_assistant=False,
)
content = attachment.read_text()
```

#### Supported File Types
The Python node currently only supports reading the contents of the following file types:

- Text-based formats (TXT, CSV, HTML, JSON, XML, etc.)
- PDF
- DOCX
- XLSX
- XLS
- Outlook
- PPTX

Other file types can still be uploaded to assistants but the Python Node is not able to read the file contents using the `read_text()` method on the attachment.

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

## Email
Send the input to the specified list of email addresses. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Extract Structured Data
Extract structured data from the input. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Update Participant Data
Extract structured data and save it as participant data.
