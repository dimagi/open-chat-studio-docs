# Parallel Pipelines
Nodes in a pipeline can run in parallel, allowing multiple operations to proceed simultaneously.

```mermaid
flowchart LR
    start([Input]) --> LLM1 & LLM2
    LLM1 --> out([Output])
    LLM2 --> out
```

!!! warning "Limitations"
    **Cycles**
    
    Configurations that result in cycles (recursive loops) are not supported.

    **Multiple Exectuion**
    
    In cases where the branches of a workflow do not have the same number of nodes and then merge, nodes after the merge will be executed more than once without special handling. See the section below on [Uneven Banches](#uneven-branches)

## Dangling nodes
Nodes without connected outputs (dangling nodes) are supported and will execute in turn. The outputs of these nodes will still be recorded in the pipeline state.

```mermaid
flowchart LR
    start([Input]) --> LLM1 & PythonNode
    LLM1 --> out([Output])
    PythonNode
```

## Multiple outputs
Connecting multiple outputs from one node (e.g. a router node) to the output of another node is allowed. If more than one of the outputs from the node have a value, the first one will be passed to the next node as input.

```mermaid
flowchart LR
    start([Input]) --> Router
    Router -.outputA.-> PythonNode
    Router -.outputB.-> PythonNode
    PythonNode --> out([Output])
```

Outputs can also be connected to multiple other nodes:

```mermaid
flowchart LR
    start([Input]) --> Router
    Router -.outputA.-> PythonNode
    Router -.outputB.-> PythonNode
    Router -.outputB.-> LLM
    LLM --> out([Output])
```

## Uneven branches

Consider the following graph:

```mermaid
flowchart LR
    start([Input]) --> NodeA
    start --> NodeB
    NodeA --> NodeC
    NodeC --> NodeD
    NodeB --> NodeD
    NodeD --> out([Output])
```

The execution steps are as follows:

1. `NodeA` and `NodeB` in parallel
2. `NodeC` and `NodeD` in parallel
3. `NodeD`

Notice how `NodeD` gets executed twice. The first time `NodeD` runs it will have the output from `NodeC` as it's input. The 2nd time it runs it will have both the outputs from `NodeB` and `NodeC` as its inputs.

To understand why this happens you need to understand the [execution model](index.md#pipeline-execution).

You can manage this challenge by using a `PythonNode` with some utility functions:

* `require_node_outputs`: This function will abort any node run if all the requested data is not available.
* `wait_for_next_input`: This is a lower level function that can be used when `require_node_outputs` isn't suitable.

In the example above, we could use the following code in `NodeD` to merge the outputs:

```python
def main(input, **kwargs):
    # this will abort the first run since only `NodeB` has outputs
    require_node_outputs("NodeB", "NodeC")
    b = get_node_output("NodeB")
    c = get_node_output("NodeC")
    return f"{b}\n{c}"
```

Using the lower level `wait_for_next_input` function we can do the same thing:

```python
def main(input, **kwargs):
    b = get_node_output("NodeB")
    c = get_node_output("NodeC")
    if b is None and c is None:
        # abort until both are available
        wait_for_next_input()
    return f"{b}\n{c}"
```

<div class="grid cards" markdown>

-   :material-hexagon-multiple-outline:{ .lg .middle } __More Example Workflows__

    ---

    [:octicons-arrow-right-24: Workflow Cookbook](../../how-to/workflow_cookbook.md)

</div>
