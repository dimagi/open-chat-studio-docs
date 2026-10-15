# Tag Rules for LLM Evaluators

Running an evaluation against hundreds of messages produces a results table too large to read row by row. **Tag Rules** solve this by automatically tagging the sessions or messages that meet a condition you define.

For example, you could flag every session with negative sentiment, or every response that scored below a threshold — so your team can jump straight to the conversations that need attention instead of reviewing everything.

Tag Rules are available only on [LLM evaluators](evaluators.md#llm-evaluator). They run automatically on every non-preview evaluation run; preview runs do not trigger tag application.

## How tags are applied

The target of the tag depends on the evaluator's mode:

- **Message mode**: the tag is applied to the specific chat message being evaluated.
- **Session mode**: the tag is applied to the session's chat.

Each tag application is shown in the **Applied Tags** column on the run results page. See [Run an Evaluation](../../how-to/evaluations/run-an-evaluation.md#read-the-results) for the results page, and [Clear Run History](../../how-to/evaluations/run-an-evaluation.md#clear-run-history-or-delete-the-evaluation) for how tags are removed.

## Tag reconciliation on rerun

When you rerun an evaluation, tags from its tag rules are updated to match the new results. If a message or session no longer meets a rule's condition, the rule's tag is removed, even if a person added that tag by hand. Tags that no rule manages are left alone.

See [Tag reconciliation on rerun](../../tech-hub/evaluations/evaluator-reference.md#tag-reconciliation-on-rerun) for which rows each kind of run updates.

## Defining a rule

Each rule has three parts:

| Field | Description |
|-------|-------------|
| Output field | The output schema field whose value is tested |
| Tag name | The tag to apply when the condition is met |
| Condition | The value or range that triggers the tag |

The condition options vary by the type of the output field:

| Output field type | Condition behavior |
|-------------------|---------------------|
| choices (enum) | Apply the tag when the field equals one of the defined choice values (e.g. `sentiment == "negative"`) |
| integer / float | Apply the tag when the field equals a specific value, or falls within a `min..max` range |
| string | Apply the tag when the field equals a specific value |
| binary | Apply the tag when the field equals 1 (the true label) or 0 (the false label). Ranges are not supported. |

## Example

Using the [example output schema](evaluators.md#output-schema) from the Evaluators page, you could define the following rules:

| Output field | Tag name | Condition |
|---|---|---|
| user_sentiment | negative-sentiment | equals `negative` |
| expected_helpfulness | low-helpfulness | range `1..2` |
| confidence_score | low-confidence | range `0.0..0.4` |
| answered_question | not-answered | equals `0` |

With these rules, any evaluation run will automatically tag messages or sessions that meet the conditions, without requiring manual review of every row.
