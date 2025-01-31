# Node Types

## LLM
Uses an LLM to respond to the input.

## LLM Router
Routes the input to one of the linked nodes using an LLM. In this case, the LLM acts as a classifier using the prompt provided to classify an incoming message into a set of discrete categories that allow messages to be routed.

!!! info "Constrained outputs"

    Currently the LLM Router node does not enforce constrained outputs, however, in the very near future, they will. This will be accomplished using a strict `json_mode` (for supporting models) that ensure that the LLM only generates one of the valid classification labels.

The `outputs` listed by the node are the available classification labels. These should match the classification categories specified in your prompt. They can be adjusted through the `Advanced` settings for the node. The top output, which is prepended by a blue `*` is the default label. In the event that the LLM generates a response outside of the specified `outputs`, the route with the default label will be taken.

!!! info "Best practices for configuring a LLM Router"

    It is advisable to use the [Node history mode](history.md#node) for an LLM Router to avoid unintentionally supplying few-shot examples to the node with an incorrect output format.

## Static Router
Routes the input to a linked node using the participant data or temporary state of the pipeline.

## Assistant
Uses an OpenAI assistant to respond to the input.

## Python Node
The Python node allows the bot builder to execute custom Python code to perform logic, data processing, or other tasks.

All the code must be encapsulated in a `main` function, which takes the node input as a string and returns a string to pass to the next node.
The `main` function must also accept arbitrary keyword arguments to support future features. Here is an example of what the code might look like:

```python
def main(input, **kwargs) -> str:
    # Put your code here
    return input
```

The `input` parameter is a string that contains the input to the node. The return value of the function is a string that will be passed to the next node in the pipeline.

The `kwargs` parameter is currently unused, but it is included to support future features that may require additional arguments to be passed to the function (though it is required to be present in the function signature).

### Utility Functions

The Python node provides a set of utility functions that can be used to interact with the user's data and the pipeline state.

#### ::: python_node.get_participant_data
#### ::: python_node.set_participant_data
#### ::: python_node.get_temp_state_key
#### ::: python_node.set_temp_state_key

## Template
Renders a [Jinja](https://jinja.palletsprojects.com/en/stable/templates/) template.

## Email
Send the input to the list of addresses provided.

## Extract Structured Data
Extract structured data from the input.


## Update Participant Data
Extract structured data and save it as participant data.
