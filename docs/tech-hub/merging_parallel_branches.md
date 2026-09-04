# Merging Parallel Branches

When parallel branches in a pipeline merge back into one node, that node can run more than once, or receive only some of the branches it expects. This page shows the Python node patterns for handling both cases predictably. `require_node_outputs` aborts a run until specific named nodes have all produced output. The lower-level `wait_for_next_input` handles merges that don't map to a fixed list of node names.

For the execution model that causes a merge node to run more than once, and the meaning of `input` and `node_inputs`, see [Which input a node receives](../concepts/pipelines/parallel.md#which-input-a-node-receives) and [Uneven branches](../concepts/pipelines/parallel.md#uneven-branches) in Parallel Pipelines.

## Merging branches that always run

Take a pipeline where two branches of different lengths — one running through `NodeA` then `NodeC`, the other through `NodeB` — merge into `NodeD`. Because the branches take a different number of steps to arrive, `NodeD` executes twice. It runs once when only `NodeB` has produced output, then again once `NodeC` catches up. If `NodeD` should only do its real work once both branches are in, use `require_node_outputs` to abort the first run:

```python
def main(input, **kwargs):
    # this will abort the first run since only `NodeB` has outputs
    require_node_outputs("NodeB", "NodeC")
    b = get_node_output("NodeB")
    c = get_node_output("NodeC")
    return f"{b}\n{c}"
```

Using the lower-level `wait_for_next_input` function you can do the same thing without naming the nodes explicitly:

```python
def main(input, **kwargs):
    b = get_node_output("NodeB")
    c = get_node_output("NodeC")
    if b is None and c is None:
        # abort until both are available
        wait_for_next_input()
    return f"{b}\n{c}"
```

## Merging branches that are optional

`require_node_outputs` assumes every named node will eventually produce output. That doesn't hold when a router sends a message down only one of several branches — the branches it didn't choose never run. Consider a pipeline where `NodeA` always runs in parallel with a `Router`, and the router sends its input to exactly one of `NodeB` or `NodeC`. All three feed into a `Merge` node.

```mermaid
flowchart LR
    start([Input]) --> Router
    start --> NodeA
    Router -.-> NodeB
    Router -.-> NodeC
    NodeA --> Merge
    NodeB --> Merge
    NodeC --> Merge
    Merge --> out([Output])
```

The `Merge` node will get output from `NodeA` and from either `NodeB` or `NodeC` — never both. `require_node_outputs` can't express "one of these two," so use `wait_for_next_input` instead:

=== "Option 1: check specific nodes"

    ```python
    def main(input, **kwargs):
        b = get_node_output("NodeB")
        c = get_node_output("NodeC")
        b_or_c = b or c
        if not b_or_c:
            # wait until we have either b or c
            wait_for_next_input()
        a = get_node_output("NodeA")
        return f"{a}\n{b_or_c}"
    ```

    `NodeA`'s output doesn't need a similar check — the pipeline's execution order guarantees it's already available by the time `NodeB` or `NodeC` finishes.

=== "Option 2: count inputs"

    This option uses the [`node_inputs`](../concepts/pipelines/parallel.md#which-input-a-node-receives) keyword argument, which lists every input available to the current run. Since `Merge` should wait for `NodeA` and (`NodeB` or `NodeC`), it can simply wait until it has at least two inputs:

    ```python
    def main(input, **kwargs):
        all_inputs = kwargs.get("node_inputs", [])
        if len(all_inputs) < 2:
            # wait until we have at least two inputs
            wait_for_next_input()
        return "\n".join(all_inputs)
    ```

## Related pages

- [Parallel Pipelines](../concepts/pipelines/parallel.md) — the execution model behind uneven and optional branches
- [Python Node](python_node.md) — full reference for `require_node_outputs`, `wait_for_next_input`, `get_node_output`, and the other Python node utility functions
- [Workflow Cookbook](../how-to/workflow_cookbook.md) — worked examples combining routers, Python nodes, and other node types
