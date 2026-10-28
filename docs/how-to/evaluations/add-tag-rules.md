# Add Tag Rules

This guide shows you how to add [tag rules](../../concepts/evaluations/tag_rules.md) to an LLM evaluator.
A tag rule tags a message or session automatically when an evaluator output meets a condition.
You can then find the rows that need attention without reading every result.

For example, a support chatbot's evaluator might rate each session's goal completion as `yes`, `partial` or `no`.
A rule that tags every `no` session as `goal-not-met` lets your team find those conversations and follow up on them first.

## Prerequisites

- An evaluation whose dataset rows come from [cloning sessions](../../concepts/evaluations/dataset.md#how-datasets-are-created), importing from an annotation queue, or auto-population.
  Rows created manually or from a CSV file are not tagged.
  See [Tag Rules](../../concepts/evaluations/tag_rules.md) for why.
- An [LLM evaluator](../../concepts/evaluations/evaluators.md#llm-evaluator) with at least one field in its [output schema](../../concepts/evaluations/evaluators.md#output-schema).
  Python evaluators do not support tag rules.
- Permission to change evaluators.

## Add a rule

1. Go to **Evaluations** > **Evaluators**.
2. Click the edit icon on the evaluator's row.
3. In the **Tag Rules** section, click **Add tag rule**.
4. Under **Tag**, select an existing tag or type a new name to create one.
5. Under **Field**, choose the output field to test.
   Only fields in the evaluator's output schema are listed.
6. Under **Condition**, choose **Equals** or **Range**, then enter the value, or the **Min** and **Max**.
   See [Conditions by field type](#conditions-by-field-type).
7. Repeat steps 3–6 for each rule you need.
8. To remove a rule, click the trash icon on it.
9. Click **Update**.

### Conditions by field type

The **Condition** list stays disabled until you choose a field.

| Output field type | Condition |
|---|---|
| choice | **Equals** one of the field's choices, for example `negative` |
| integer | **Equals** a whole number, or **Range** with whole-number **Min** and **Max** |
| float | **Equals** a number, or **Range** with **Min** and **Max** |
| string | **Equals** a specific value |
| binary | **Equals** one of the field's two labels. **Range** is not available. |

A range includes both ends, and **Min** can't be greater than **Max**.

### Example

These rules suit an output schema with a `goal_completion` choice field and a `quality_score` integer field:

| Tag | Field | Condition |
|---|---|---|
| `goal-not-met` | `goal_completion` | Equals `no` |
| `low-quality` | `quality_score` | Range, **Min** `1` and **Max** `2` |

## Check the result

Rules apply from the next run that uses the evaluator.
Existing results are not tagged until you run the evaluation again.

1. [Run the evaluation](run-an-evaluation.md#run-the-evaluation).
   A preview does not apply tags.
2. When the run completes, click **Download results**.
   The **Applied Tags** column lists the tags each row received.

See [How tag rules work](../../concepts/evaluations/tag_rules.md#how-tag-rules-work) for whether each tag is added to a message or a session.

To find the tagged conversations, go to the sessions list and use the **Tags** filter.
In message mode the **Tags** column of a matching session can be empty, because the tag is on a message.
See [Tags on the Sessions List](../../concepts/sessions.md#tags-on-the-sessions-list).

## Common issues

- **The Tag Rules section is missing.**
  The evaluator is a [Python evaluator](../../concepts/evaluations/evaluators.md#python-evaluator).
  Only LLM evaluators support tag rules.
- **Add tag rule is disabled.**
  The output schema has no usable field yet.
  Add a choice, integer, float, string or binary field first.
- **A field shows "(add choices to use)" and can't be selected.**
  It is a choice field with no choices.
  Add its choices to the output schema.
- **No tags appeared.** Check each of these:
    - The run was a preview.
    - No row met the condition.
    - The row failed.
      Failed rows are never tagged.
    - The row has no chat message or session to tag.
      This is the most common cause.
      It happens to rows that were added manually or from a CSV file.
      It also happens to cloned rows you edited, because editing breaks the link to the original session.
      In message mode, a cloned human message with no AI reply is not tagged either.
- **A tag someone added by hand disappeared.**
  After each run, OCS removes a rule's tag from any row in the run that no longer meets the condition.
  This includes tags a person added by hand.
  Previews do not apply or remove tags.
  See [Tag reconciliation on rerun](../../tech-hub/evaluations/evaluator-reference.md#tag-reconciliation-on-rerun).

## See also

- [Tag Rules](../../concepts/evaluations/tag_rules.md): why and when to use tag rules.
- [Run an Evaluation](run-an-evaluation.md): run the evaluation and read the results.
- [Set Up a Real-Time LLM-as-a-Judge](realtime_llm_judge.md): use tag rules to flag sessions from a live chatbot.
