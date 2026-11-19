# Python Node
The Python node allows the chatbot builder to execute custom Python code to perform logic, data processing, or other tasks.
It provides the following:

 - [utility functions](#utility-functions) to interact with participant data and pipeline state ([temporary](python_node_state_and_attachments.md#temporary-state) and [session state](python_node_state_and_attachments.md#session-state))
 - [attachments](python_node_state_and_attachments.md#attachments): file uploads of the [supported file types](python_node_state_and_attachments.md#supported-file-types)
 - ability to call [external APIs](./external-api-calls/http_client.md)

## The Code

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

* `node_inputs: list[str]` - All the inputs that have reached the node at the time of execution, oldest first, with `input` as the last entry. This will be the same as `[input]` except when the node is part of a workflow with [parallel branches](../concepts/pipelines/parallel.md#which-input-a-node-receives).

!!! warning

    All code must be encapsulated in a `main` function. You can write other functions but they must be within the scope of the `main` function. For example:

    ```python
    def main(input, **kwargs):
        def important(arg):
            return arg + "!"

        return important(input)
    ```

## Utility Functions

The Python node provides a set of utility functions that can be used to interact with the participant's data and the pipeline state.

### ::: python_node.get_participant_data
### ::: python_node.set_participant_data
### ::: python_node.set_participant_data_key
### ::: python_node.append_to_participant_data_key
### ::: python_node.increment_participant_data_key
### ::: python_node.get_participant_schedules
### ::: python_node.get_temp_state_key
### ::: python_node.set_temp_state_key
### ::: python_node.get_session_state_key
### ::: python_node.set_session_state_key
### ::: python_node.get_selected_route
### ::: python_node.get_node_path
### ::: python_node.get_all_routes
### ::: python_node.add_message_tag
### ::: python_node.add_session_tag
### ::: python_node.get_node_output
### ::: python_node.require_node_outputs
### ::: python_node.wait_for_next_input
### ::: python_node.abort_with_message
### ::: python_node.end_session
### ::: python_node.add_file_attachment

!!! tip "Merging parallel branches"

    For worked examples using `require_node_outputs` and `wait_for_next_input` to merge branches that run an uneven number of times, or that only sometimes run, see [Merging Parallel Branches](merging_parallel_branches.md).

## Debugging with print()

You can use `print()` inside your Python Node code to capture debug or diagnostic output. Any printed text is collected and stored as `console` data in the node's trace span, making it visible in the [trace detail view](../concepts/tracing.md) and in Langfuse spans if Langfuse tracing is configured.

```python
def main(input, **kwargs) -> str:
    print("Processing input:", input)
    result = input.upper()
    print("Result:", result)
    return result
```

The captured output is joined into a single string and attached to the node's trace entry. This is useful for inspecting intermediate values without affecting the node's return value.

## State and Attachments

Python node code can read and change the pipeline's [temporary state](python_node_state_and_attachments.md#temporary-state) and the participant's [session state](python_node_state_and_attachments.md#session-state), and read files the participant uploaded as [attachments](python_node_state_and_attachments.md#attachments).
See [Python Node State and Attachments](python_node_state_and_attachments.md).
