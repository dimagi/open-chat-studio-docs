# Evaluators

A dataset of example conversations is useful only once it has been scored, and an **evaluator** does the scoring.
An evaluator looks at each message and, optionally, your chatbot's generated response to it.
It outputs a judgment on whatever matters for your use case, such as whether the response was accurate, on-topic or polite.

You can run several evaluators over the same [dataset](dataset.md) at once.
A single evaluation run can then check multiple things, such as accuracy, tone and safety, without re-running your chatbot for each one.

Each evaluator has an **Evaluation mode**: **Message** (judging a single response) or **Session** (judging a whole conversation). It must match the [**Evaluation level** of the dataset](dataset.md#evaluation-levels) it is used with. Evaluators with the wrong mode for a dataset are hidden when you set up an evaluation.

## Evaluator types

### LLM evaluator
The LLM Evaluator uses language models to evaluate responses based on a custom prompt.
Use it as an [LLM-as-judge](../../how-to/evaluations/realtime_llm_judge.md) to evaluate the performance of a chatbot.
It can also assess the properties of both the participant's and the chatbot's messages.

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
    An evaluation run can make two kinds of LLM calls.
    One is the evaluator's own judging call.
    The other, if generation is enabled, generates the response being judged.
    Both count towards your team's total cost and usage.
    Neither is attributed to a specific chatbot, participant, or conversation.
    Filtering your team's cost and usage reporting by chatbot or participant therefore excludes evaluation spend, although it still adds to the team's total.
    For the same reason, a generated response's cost is not counted as chat usage.
    It does not appear on the session or conversation it was generated for.

    If your team runs evaluations with generation enabled, your team's total cost may be higher than you remember, since this spend is now captured.
    No chatbot, participant, or conversation became more expensive. The cost was not being recorded before.

### Template variables

A prompt can include variables that are filled in for each row.
Examples are the participant's message, the chatbot's response, or the conversation so far.
Which variables are available depends on the evaluator's evaluation mode.
A session-level evaluator works from the whole conversation, not a single message.

See [Template variables](../../tech-hub/evaluations/evaluator-reference.md#template-variables) for the full list.

### Output schema

The output schema defines the metrics that the LLM should attempt to output. Each item in the schema will become a column in the output table. You can specify the data type for each field to ensure structured, validated output.

**Available Types:**

- **string**: Text output (default behavior)
- **integer**: Whole numbers (e.g., counts, ratings)
- **float**: Decimal numbers (e.g., confidence scores, percentages)
- **choice (enum)**: Predefined options from a list
- **binary**: A yes/no result, stored as 1 or 0. You can set the label shown for each value, such as **Correct** and **Incorrect**. The defaults are **True** and **False**. Run results show the share of rows that scored 1.

OCS checks the LLM's output against these types and asks again if it doesn't match. See [Output validation](../../tech-hub/evaluations/evaluator-reference.md#output-validation) for the retry rules and what happens when the model gives no structured output.

**Example Output Schema:**

| Column Name | Type | Description |
|-------------|------|-------------|
| expected_helpfulness | integer | The helpfulness, on a scale of 1-5, of the expected assistant message |
| actual_helpfulness | integer | The helpfulness, on a scale of 1-5, of the actual assistant message |
| user_sentiment | choice | The sentiment of the user message (options: positive, neutral, negative) |
| confidence_score | float | Confidence in the evaluation, from 0.0 to 1.0 |
| answered_question | binary | Whether the assistant message answered the user's question (labels: Answered, Not answered) |

See [Tag Rules](./tag_rules.md) to automatically tag sessions or messages based on these output values.

### Python evaluator

Use the Python Evaluator when you need deterministic rules, custom string matching, or logic that an LLM prompt cannot reliably express. It runs custom code against each message instead of an LLM prompt.

See [Python Evaluator](../../tech-hub/evaluations/python_evaluator.md) for the function signature, arguments, and a worked example.

## Copying an evaluator

Copy an evaluator to reuse its configuration as a starting point for a new one.

1. Go to **Evaluations** > **Evaluators**.
2. Click the copy icon on the evaluator's row, between the edit and delete icons.
3. Edit the copy on the page that opens, then click **Update**.

The copy is named `<name> (copy)`.
It has the same type, prompt, output schema, evaluation mode, provider, model, and [tag rules](./tag_rules.md) as the original.

The copy starts active and is not part of any evaluation config.
Results and aggregates are not copied.

You can also copy an archived evaluator.
This restores a retired configuration without changing the archived evaluator's history.

!!! note
    Copying requires both the add evaluator and change evaluator permissions.
    The copy icon is hidden from users who lack either permission.
    The default groups are not affected by this requirement.

## Archiving Evaluators

Deleting an evaluator that has produced results or aggregates archives it instead of deleting it, so that data is not lost. An evaluator with no run history is still deleted outright.

The delete confirmation dialog tells you which will happen before you confirm.

Archived evaluators keep their results, aggregates, and applied tags. They still show up on the past runs and exports that used them, and you can still open and edit an archived evaluator. An **Archived** badge marks them in the evaluator list and in the evaluations table.

Archived evaluators are excluded from new work:

- They don't appear in the evaluator picker when you create a new evaluation config.
- They are skipped by every new run, including automatic delta runs triggered when a dataset is appended.

The one exception is editing an evaluation config that already uses an archived evaluator.
In that case, the picker still shows the config's own archived evaluators, with an *(archived)* suffix on the name.
You can untick one to remove it and still edit the rest of the config.
Archived evaluators that aren't already on the config are not offered.

Running a config whose evaluators are all archived is refused with an error, since it would produce no results.

An archived evaluator cannot be deleted while its results exist, so the **Delete** action is not shown for it. Use **Unarchive** to restore it instead. Once unarchived, it becomes available in the picker again and can be used in new runs. The **Unarchive** action is only shown to users who have delete permission for evaluators.

!!! note
    Neither archiving nor deleting an evaluator is allowed while a run that uses it is in progress.
