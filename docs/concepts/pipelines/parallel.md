# Parallel Pipelines

Nodes in a pipeline can run in parallel, allowing multiple operations to proceed simultaneously. This follows directly from [how a pipeline runs](index.md#how-a-pipeline-runs): every node whose dependencies are satisfied executes in the same pass.

```mermaid
flowchart LR
    start([Input]) --> LLM1 & LLM2
    LLM1 --> out([Output])
    LLM2 --> out
```

!!! warning "Limitations"

    **Cycles**

    Configurations that result in cycles (recursive loops) are not supported.

    **Multiple execution**

    When the branches of a workflow have different lengths and then merge, the node after the merge runs more than once unless you handle this deliberately. See [Uneven branches](#uneven-branches) below.

## Dangling nodes

Nodes without connected outputs (dangling nodes) are supported and will execute in turn. The outputs of these nodes will still be recorded in the pipeline state.

```mermaid
flowchart LR
    start([Input]) --> LLM1 & PythonNode
    LLM1 --> out([Output])
    PythonNode
```

See this pattern used in the Workflow Cookbook: [Safety check in parallel](../../how-to/workflow_cookbook.md#safety-check-in-parallel), where an unconnected **safe** output lets compliant messages pass through unchanged.

## Multiple outputs

Connecting multiple outputs from one node (e.g. a router node) to the input of another node is allowed. If the node produces more than one output over the course of the run, the most recent one is passed on as input — see [Which input a node receives](#which-input-a-node-receives).

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

See this pattern used in the Workflow Cookbook: [Router for classification](../../how-to/workflow_cookbook.md#router-for-classification), where multiple category outputs feed into the same [Python node](nodes.md#python-node).

## Which input a node receives

A node runs once for every time an upstream branch reaches it. Each run has:

* **`input`** — the output that arrived most recently, i.e. from the branch that triggered this run.
* **`node_inputs`** — every output that has arrived so far, oldest first. On a node where branches merge this list grows with each run, which is how a node sees more than one branch at once.

Inputs are ordered by when they arrived, never by the order the connections were drawn, so redrawing the same graph does not change what a node receives.

!!! note "Reading the other branches"

    `node_inputs` is available to the [Python node](../../tech-hub/python_node.md#additional-keyword-arguments) as a keyword argument, and to the template and email nodes as `{{ node_inputs }}`. A Python node can also read any completed node by name with `get_node_output("Node Name")`, which is the clearest option when you know which branches you are merging.

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

Notice how `NodeD` gets executed twice. The first time it runs, only `NodeB` has reached it, so `NodeB`'s output is its `input` and its single `node_inputs` entry. By the second run `NodeC` has finished, so `NodeC`'s output becomes the `input` and `node_inputs` holds both.

To understand why this happens, see [how a pipeline runs](index.md#how-a-pipeline-runs).

If `NodeD` needs to see both `NodeB` and `NodeC` before it does its real work — merging both branches exactly once, rather than running twice — write that logic in a Python node using the `require_node_outputs` or `wait_for_next_input` utility functions. The same functions handle the related case where a branch is optional and may not run at all. See [Merging Parallel Branches](../../tech-hub/merging_parallel_branches.md) for worked examples of both.

## See also

- [Workflow Cookbook](../../how-to/workflow_cookbook.md)
- [Merging Parallel Branches](../../tech-hub/merging_parallel_branches.md)
