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
Runs Python code.

## Template
Renders a [Jinja](https://jinja.palletsprojects.com/en/stable/templates/) template.

## Email
Send the input to the list of addresses provided.

## Extract Structured Data
Extract structured data from the input.


## Update Participant Data
Extract structured data and save it as participant data.
