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

### Template Variables

The available variables depend on the evaluator's evaluation mode.

#### Message-level variables

| Variable | Description |
|---|---|
| `{input.content}` | The human message content |
| `{output.content}` | The dataset message's AI response content. This may be an expected/reference answer (for manually created datasets) or the actual AI response (for session-cloned datasets). |
| `{generated_response}` | The generated response from your chatbot (if generation is enabled) |
| `{context.[parameter]}` | Any context variable, e.g. `{context.topic}` |
| `{full_history}` | Complete conversation history as formatted text |

#### Session-level variables

In session-level mode, `{input.content}` and `{output.content}` are empty. Use the following variables instead:

| Variable | Description |
|---|---|
| `{full_history}` | The full session transcript captured at the time of the last AI message |
| `{context.[parameter]}` | Any context variable, e.g. `{context.current_datetime}` |

!!! note
    Generation is not available for session-level datasets, so `{generated_response}` is not applicable in session-level prompts.

See [Evaluation Datasets](dataset.md) for how data is mapped into these fields.

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

## Clearing Run History

The evaluation runs page includes a **Clear all** button that deletes the entire run history for an evaluation config in a single action. This button is only shown to users who have delete permission for evaluation runs.

Clearing run history also removes the tags that those runs applied to their targets. Only tags that were applied by the evaluator's tag rules are removed — tags that a person added by hand are left untouched.

!!! warning "Clearing run history is permanent"
    Deleted runs and their results cannot be recovered. Export any results you need to keep before using **Clear all**.

A confirmation prompt appears before the action runs.
