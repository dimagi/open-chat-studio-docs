# Evaluators

A dataset full of example conversations only becomes useful once it's been scored — that's the job of an **evaluator**. An evaluator looks at each message (and, optionally, your chatbot's generated response to it) and outputs a judgment: was it accurate, on-topic, polite, or whatever else matters for your use case.

You can run several evaluators over the same dataset at once, so a single evaluation run can check multiple things — accuracy, tone, safety — without re-running your chatbot for each one.

Each evaluator works in one of two **evaluation modes** — **message-level** (judging a single response) or **session-level** (judging a whole conversation) — and must match the mode of the dataset it's used with. Evaluators using the wrong mode for a dataset are automatically disabled when configuring a run.

## Evaluator Types

### LLM Evaluator
The LLM Evaluator uses language models to evaluate responses based on a custom prompt. This can be used as an [LLM-as-judge](../../how-to/evaluations/realtime_llm_judge.md) to evaluate the performance of a chatbot, or to gain insight into the properties of both the user and assistant messages.

For the how-to guide, see [Set Up a Real-Time LLM Judge](../../how-to/evaluations/realtime_llm_judge.md).

**Example prompt:**

```text
Rate the helpfulness and accuracy of this response on a scale of 1-5:

User question: {input.content}
Reference answer: {output.content}
Generated answer: {generated_response}

Consider the conversation context: {context.topic}
```

!!! note "Evaluation cost and usage"
    An evaluation run can make two kinds of LLM calls: the evaluator's own judging call, and — if generation is enabled — the call that generates the response being judged. Both count towards your team's total cost and usage, but neither is attributed to a specific chatbot, participant, or conversation. This means filtering your team's cost and usage reporting by chatbot or participant will not include evaluation spend, even though it still adds to your team's overall total. For the same reason, the generated response's own cost is not counted as chat usage, so it will not appear on the session or conversation it was generated for.

    If your team runs evaluations with generation enabled, your team's total cost may be higher than you remember, since this spend is now captured. No chatbot, participant, or conversation becomes more expensive — the cost was simply not being recorded before.

### Template Variables

The available variables depend on the evaluator's evaluation mode.

#### Message-level variables

| Variable | Description |
|---|---|
| `{input.content}` | The human message content |
| `{output.content}` | The dataset message's AI response content. This may be an expected/reference answer (for manually created datasets) or the actual AI response (for session-cloned datasets). |
| `{generated_response}` | The generated response from your chatbot (if generation is enabled) |
| `{context.[parameter]}` | Any context variable, e.g. `{context.topic}` |
| `{participant_data.[key]}` | Any field from the participant's data, e.g. `{participant_data.name}` |
| `{session_state.[key]}` | Any field from the session's state, e.g. `{session_state.step}` |
| `{full_history}` | Complete conversation history as formatted text |

#### Session-level variables

In session-level mode, `{input.content}` and `{output.content}` are empty. Use the following variables instead:

| Variable | Description |
|---|---|
| `{full_history}` | The full session transcript captured at the time of the last AI message |
| `{context.[parameter]}` | Any context variable, e.g. `{context.current_datetime}` |
| `{participant_data.[key]}` | Any field from the participant's data, e.g. `{participant_data.name}` |
| `{session_state.[key]}` | Any field from the session's state, e.g. `{session_state.step}` |

!!! note
    Generation is not available for session-level datasets, so `{generated_response}` is not applicable in session-level prompts.

See [Evaluation Datasets](dataset.md) for how data is mapped into these fields, and [Dataset Structure](../../tech-hub/evaluations/dataset-structure.md#dataset-fields) for where `participant_data` and `session_state` come from.

### Output Schema

The output schema defines the metrics that the LLM should attempt to output. Each item in the schema will become a column in the output table. You can specify the data type for each field to ensure structured, validated output.

**Available Types:**

- **string**: Text output (default behavior)
- **integer**: Whole numbers (e.g., counts, ratings)
- **float**: Decimal numbers (e.g., confidence scores, percentages)
- **choice (enum)**: Predefined options from a list

The system automatically validates the LLM's output against the specified types using a dynamically generated schema. If the output doesn't match the expected format, the system will retry up to 3 times before failing, ensuring reliable structured data.

**Example Output Schema:**

| Column Name | Type | Description |
|-------------|------|-------------|
| expected_helpfulness | integer | The helpfulness, on a scale of 1-5, of the expected assistant message |
| actual_helpfulness | integer | The helpfulness, on a scale of 1-5, of the actual assistant message |
| user_sentiment | choice | The sentiment of the user message (options: positive, neutral, negative) |
| confidence_score | float | Confidence in the evaluation, from 0.0 to 1.0 |

See [Tag Rules](./tag_rules.md) to automatically tag sessions or messages based on these output values.

### Python Evaluator

Use the Python Evaluator when you need deterministic rules, custom string matching, or logic that an LLM prompt cannot reliably express. It runs custom code against each message instead of an LLM prompt.

See [Python Evaluator](../../tech-hub/evaluations/python_evaluator.md) for the function signature, arguments, and a worked example.

## Archiving Evaluators

Deleting an evaluator that has produced results or aggregates archives it instead of deleting it, so that data is not lost. An evaluator with no run history is still deleted outright.

The delete confirmation dialog tells you which will happen before you confirm.

Archived evaluators keep their results, aggregates, and applied tags. They still show up on the past runs and exports that used them, and you can still open and edit an archived evaluator. An **Archived** badge marks them in the evaluator list and in the evaluations table.

Archived evaluators are excluded from new work:

- They don't appear in the evaluator picker when you create a new evaluation config.
- They are skipped by every new run, including automatic delta runs triggered when a dataset is appended.

The one exception is editing an evaluation config that already uses an archived evaluator. In that case, the picker still shows the config's own archived evaluators, with an *(archived)* suffix on the name, so you can untick one to remove it without losing the ability to edit the rest of the config. Archived evaluators that aren't already on the config are not offered.

Running a config whose evaluators are all archived is refused with an error, since it would produce no results.

An archived evaluator cannot be deleted while its results exist, so the **Delete** action is not shown for it. Use **Unarchive** to restore it instead. Once unarchived, it becomes available in the picker again and can be used in new runs. The **Unarchive** action is only shown to users who have delete permission for evaluators.

!!! note
    Neither archiving nor deleting an evaluator is allowed while a run that uses it is in progress.

## Clearing Run History

The evaluation runs page includes a **Clear all** button that deletes the entire run history for an evaluation config in a single action. This button is only shown to OCS users who have delete permission for evaluation runs.

Clearing run history also removes the tags that those runs applied to their targets. Only tags that were applied by the evaluator's tag rules are removed — tags that a person added by hand are left untouched.

!!! warning "Clearing run history is permanent"
    Deleted runs and their results cannot be recovered. Export any results you need to keep before using **Clear all**.

A confirmation prompt appears before the action runs.
