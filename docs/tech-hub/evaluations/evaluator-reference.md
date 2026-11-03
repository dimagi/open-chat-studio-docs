# Evaluator Reference

This page is a reference for LLM evaluator prompts, output validation and tag rule reconciliation.
Use it when writing an evaluator prompt or working out why a row failed or lost a tag.

For what evaluators are and when to use each type, see [Evaluators](../../concepts/evaluations/evaluators.md).
For tag rules, see [Tag Rules](../../concepts/evaluations/tag_rules.md).

## Template variables

The variables available in an LLM evaluator prompt depend on the evaluator's [evaluation mode](../../concepts/evaluations/evaluators.md).
For where each value comes from, see [Dataset Structure](dataset-structure.md#dataset-fields).

=== "Message level"

    | Variable | Description |
    |---|---|
    | `{input.content}` | The human message content |
    | `{output.content}` | The dataset message's AI response content. This may be an expected/reference answer (for manually created datasets) or the actual AI response (for session-cloned datasets). |
    | `{generated_response}` | The generated response from your chatbot (if generation is enabled) |
    | `{context.[parameter]}` | Any context variable, e.g. `{context.topic}` |
    | `{participant_data.[key]}` | Any field from the participant's data, e.g. `{participant_data.name}` |
    | `{session_state.[key]}` | Any field from the session's state, e.g. `{session_state.step}` |
    | `{full_history}` | Complete conversation history as formatted text |
    | `{span.input}`, `{span.output}`, `{span.error}` | The input, output and error of the selected [span](#spans). Only available when the evaluator selects a span. |

=== "Session level"

    In session-level mode, `{input.content}` and `{output.content}` are empty.
    Use the following variables instead:

    | Variable | Description |
    |---|---|
    | `{full_history}` | The full session transcript captured at the time of the last AI message |
    | `{context.[parameter]}` | Any context variable, e.g. `{context.current_datetime}` |
    | `{participant_data.[key]}` | Any field from the participant's data, e.g. `{participant_data.name}` |
    | `{session_state.[key]}` | Any field from the session's state, e.g. `{session_state.step}` |

    Generation is not available for session-level datasets, so `{generated_response}` does not apply in session-level prompts.

Python evaluators receive the same values as function arguments.
See [Python Evaluator](python_evaluator.md).

## Spans

A span is one part of the chatbot's generation: a node, a tool call or an LLM call.
An evaluator can target a span instead of the whole reply.
For an overview, see [Evaluating part of a generation](../../concepts/evaluations/evaluators.md#evaluating-part-of-a-generation).

### Settings

| Setting | Description |
|---|---|
| **Span** | What to target: the whole reply (default), a node, a tool call or an LLM call. |
| **Span name** | The node, tool or LLM node to pick. Required when **Span** is not the whole reply. |
| **Use span output as generated response** | When on, the evaluator judges the span's output as `generated_response`. Requires a **Span** selection. |

### Matching rules

| Span | Matches |
|---|---|
| Tool call | Tool calls by tool name, across every node of the pipeline. |
| LLM call | LLM calls by the name of the node the call ran in. |
| Node | Pipeline nodes by name. If a node ran more than once, each run is a span. |

The span's input and output depend on the type:

- **Tool**: the output is the tool's return value.
- **Node**: the output is the node's output.
  The input is the output of the node run that fed it.
  For a merge node, this is the output of the last branch to arrive.
  The first node has no input.
  Use `{input.content}` for the dataset input.
- **LLM**: the input is the message list the model saw.

### Prompt variables

LLM evaluator prompts can use these variables:

| Variable | Description |
|---|---|
| `{span.input}` | The span's input. |
| `{span.output}` | The span's output. |
| `{span.error}` | The span's error text, if any. |

Only these three exact names are accepted.
Sub-keys, indexes and format specs, such as `{span.output[0]}`, are rejected.
If the name matches more than once, such as a node that ran twice or a tool called twice, the variables render as lists.
The 10,000-character cap applies to these prompt variables.

### Use span output as generated response

With this setting on, `{generated_response}` contains the span's output instead of the bot's reply.
When several spans match, the last match is used.
The output is passed in full, with no character cap.

The stored result keeps the bot's reply in `generated_response`.
The results table and exports therefore still show what the bot said.
The judged text is stored under `judged_response`.
The per-result detail panel shows it as a **Judged response** block under the generated response, labelled with the evaluator's name.

### Validation

- A node, tool or LLM selector requires a **Span name**.
- **Use span output as generated response** requires a selector.
- An LLM evaluator prompt that references `{span.*}` without a selector is rejected.
- Session-level evaluators cannot use a selector, because no generation runs.
- An evaluation config with generation turned off refuses evaluators that use a selector.

### Errors

- If the name matches nothing, that message gets an error result that lists the available spans.
  A typo therefore shows up on the first run.
- If the matched span errored, the span is not judged and the result shows the span's error text.

### Known limits

- The available span names in the error come from the one generation that ran.
  A tool the bot did not call that time is reported as unavailable.
- An LLM selector on an agent node also lists the tool-request turns, which have an empty output, beside the final turn.

## Output validation

OCS validates the LLM's output against the evaluator's output schema, using a schema generated from the field types.
The evaluator tries again in two cases:

- The output does not match the schema.
- The provider returns a rate-limit or temporary error, such as a server error or timeout.

It makes up to 3 attempts in total (the first call plus up to 2 retries) before the row fails.

Binary fields are stored as 1 or 0.
The labels you set are added to the field description that is sent to the model.
They take the form `1 = <true label>, 0 = <false label>`.

### No structured output

Sometimes the model returns no structured output at all.
It may refuse in prose, the provider may block the reply, or it may never call the required tool.
This is not retried, because asking again is likely to give the same result.
Instead, the `error (<evaluator name>)` column for that row shows `The model did not return structured output:` followed by the model's reply.
If the model gave no reply, the provider's stop reason is shown instead.

This usually happens only after a provider refusal or safety block, so most runs never see it.

## Tag reconciliation on rerun

A message or session either meets a [tag rule's](../../concepts/evaluations/tag_rules.md) condition, or it does not.
To keep tags consistent with the latest results, rerunning an evaluation reconciles the tags managed by its evaluators' tag rules:

- OCS checks each message or session in the rerun's scope.
  It removes any tag that a tag rule names but the latest run did **not** apply.
- Reconciliation removes a tag regardless of who applied it.
  A person may have added a tag that a tag rule also manages.
  If the new evaluator output does not meet that rule, the tag is removed.
- **Full** runs, which score the entire dataset, reconcile every row.
  **Delta** runs, which score only rows added by [auto-population](auto_population.md#automatic-delta-evaluation-runs), reconcile only the rows in their scope.
- **Preview** runs neither apply nor remove tags.

Tags whose names are not referenced by any tag rule on the run's evaluators are never touched by reconciliation.

## See also

- [Evaluators](../../concepts/evaluations/evaluators.md): evaluator types and output schemas.
- [Tag Rules](../../concepts/evaluations/tag_rules.md): what tag rules tag and when.
- [Add Tag Rules](../../how-to/evaluations/add-tag-rules.md): the steps and condition types for adding a rule.
- [Python Evaluator](python_evaluator.md): the same values as function arguments.
- [Dataset Structure](dataset-structure.md): where the dataset fields come from.
