# Tag Rules

Tag Rules let you automatically apply tags to sessions or messages when an evaluator output field matches a condition. This makes it easy to surface and filter results — for example, flagging all sessions where the evaluator detected negative sentiment, or marking messages that scored below a threshold.

Tag Rules are available only on [LLM evaluators](evaluators.md#llm-evaluator). They run automatically on every non-preview evaluation run. Preview runs do not trigger tag application.

## How tags are applied

The target of the tag depends on the evaluator's mode:

- **Message mode**: the tag is applied to the specific chat message being evaluated.
- **Session mode**: the tag is applied to the session's chat.

Each tag application is recorded in an audit log and displayed in the **Applied Tags** column on the run results page.

## Tag reconciliation on rerun

The philosophy behind tag rules is simple: a message or session either meets the criteria for a tag, or it does not. To keep tag state consistent with the latest evaluation results, rerunning an evaluation reconciles the tags managed by its evaluators' tag rules:

- For each message or session in the rerun's scope, any tag named by an evaluator's tag rules that was **not** applied by the latest run is removed from that message or session.
- Reconciliation removes a tag regardless of who applied it. If a human had previously added a tag that is also managed by a tag rule, and the new evaluator output does not satisfy that rule, the human-applied tag is removed.
- **FULL** runs (which score the entire dataset) reconcile every row. **DELTA** runs (which score only newly added rows, triggered automatically by [auto-population](../../tech-hub/evaluations/auto_population.md)) reconcile only the rows in their scope.
- **PREVIEW** runs neither apply nor remove tags.

Tags whose names are not referenced by any tag rule on the run's evaluators are never touched by reconciliation.

## Defining a rule

Each rule has three parts:

| Field | Description |
|-------|-------------|
| Output field | The output schema field whose value is tested |
| Tag name | The tag to apply when the condition is met |
| Condition | The value or range that triggers the tag |

The condition options vary by the type of the output field:

| Output field type | Condition behaviour |
|-------------------|---------------------|
| choices (enum) | Apply the tag when the field equals one of the defined choice values (e.g. `sentiment == "negative"`) |
| integer / float | Apply the tag when the field equals a specific value, or falls within a `min..max` range |
| string | Apply the tag when the field equals a specific value |

## Example

Using the [example output schema](evaluators.md#output-schema) from the Evaluators page, you could define the following rules:

| Output field | Tag name | Condition |
|---|---|---|
| user_sentiment | negative-sentiment | equals `negative` |
| expected_helpfulness | low-helpfulness | range `1..2` |
| confidence_score | low-confidence | range `0.0..0.4` |

With these rules, any evaluation run will automatically tag messages or sessions that meet the conditions, without requiring manual review of every row.
