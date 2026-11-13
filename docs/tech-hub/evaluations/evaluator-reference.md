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
    | `{generation.node_outputs}`, `{generation.path}`, and five more | What the chatbot did during the generation step. See [Generation variables](#generation-variables). |

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
    A session-level evaluator can reference `{generation.*}` variables, but they are always empty.

Python evaluators receive the same values as function arguments.
See [Python Evaluator](python_evaluator.md).

### Generation variables

A message-level evaluator can judge what the chatbot did, not only what it said.
When **Run generation step before evaluation** is enabled on the [evaluation](../../how-to/evaluations/run-an-evaluation.md), OCS keeps a generation record of what the chatbot did while producing the response.
The record covers every node's output, the path the pipeline took, the tags added, the change to participant data, and the LLM and tool calls.

| Variable | Contents |
|---|---|
| `{generation.node_outputs}` | The output of every node. |
| `{generation.path}` | The path the pipeline took. |
| `{generation.message_tags}` | The tags put on the reply. |
| `{generation.session_tags}` | The tags put on the session. |
| `{generation.participant_data_diff}` | The change made to participant data. |
| `{generation.llm_calls}` | The LLM calls, each with its full message list. |
| `{generation.tool_calls}` | The tool calls, in the order they started. |

Each variable renders as JSON and is capped at 10,000 characters.
The cap applies to each variable separately, so all seven together can reach about 70,000 characters.

Node names come from the pipeline graph.
If a node has no name, the raw node ID is used.

!!! tip
    `{generation.llm_calls}` carries the full message list of each call, so it usually reaches the cap.
    Judge prompts work better with `{generation.tool_calls}` and `{generation.node_outputs}`.

#### Validation

The values are pre-rendered JSON, so sub-keys and indexes are not supported.
The evaluator form accepts exactly the seven names above and rejects anything else under `generation`.
For example, it rejects `{generation.tags}`, `{generation.tool_calls[0]}`, and any conversion or format spec such as `{generation.llm_calls!s:>60000}`.
The error message lists the valid names.
The seven variables appear in the evaluator form's hints and autocomplete.

#### Behavior and limits

- If a generation fails part-way, the record still includes the calls captured before the error.
- Tools that return a LangGraph `Command`, such as the participant-data and session-state tools, record their tool message as the output.
- An LLM turn that only requests tools has an empty `output`.
  The tool call appears in `{generation.tool_calls}`.
- Calls made outside any node, such as replies for interrupts and errors, are not in the record.
- A node that LangGraph retries is recorded once per attempt.
- A history-summarization call inside a node looks like the node's own call.

#### Participant data during evaluation runs

Evaluators see the change a chatbot makes to participant data, but an evaluation run does not save it.
Evaluation runs no longer write participant data to the team's shared "evaluations" participant.
Session tags and session state still persist to the temporary evaluation session.
Participants renamed by evaluation runs before this change keep the name.

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
