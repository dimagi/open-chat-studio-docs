# Tag Rules for LLM Evaluators

Running an evaluation against hundreds of messages produces a results table too large to read row by row.
**Tag Rules** solve this by automatically tagging the sessions or messages that meet a condition you define.

For example, you could flag every session with negative sentiment, or every response that scored below a threshold.
Your team can then go directly to the conversations that need attention instead of reviewing everything.

The tags are saved on the session or message in OCS, not only in the evaluation results.
You can filter the [sessions list](../sessions.md#tags-on-the-sessions-list) by tag at any time.
In session mode the tags also appear in its **Tags** column.
In message mode they appear on the message in the session view.

!!! warning "Tag rules do not work on every dataset"
    Tag rules can only tag a chat message or session that exists in OCS.
    Rows you create manually or upload from a CSV file have neither, so rules never tag them, even if the output meets the condition.
    Use tag rules with datasets built by [cloning sessions](dataset.md#how-datasets-are-created), importing from an annotation queue, or auto-population.
    Editing a cloned row breaks its link to the session, so keep cloned rows unedited. See [Common issues](../../how-to/evaluations/add-tag-rules.md#common-issues).

## How tag rules work

A tag rule checks one output field of an [LLM evaluator](evaluators.md#llm-evaluator).
When the field's value meets the rule's condition, such as equalling `negative` or falling between 1 and 2, the rule applies its tag.

The evaluator's mode decides what gets tagged:

- **Message mode**: the AI message of the evaluated human/AI message pair.
- **Session mode**: the session's chat.

A row can be tagged only if it has a chat message or session in OCS.
This is checked for each row, so a dataset can mix taggable and untaggable rows.
See [Common issues](../../how-to/evaluations/add-tag-rules.md#common-issues) for why a row might not be tagged.

Tags follow the latest results.
After each run, a rule removes its tag from any message or session in the run that no longer meets its condition.
This includes tags a person added by hand.
Previews do not apply or remove tags.
See [Tag reconciliation on rerun](../../tech-hub/evaluations/evaluator-reference.md#tag-reconciliation-on-rerun).

## See also

- [Add Tag Rules](../../how-to/evaluations/add-tag-rules.md): add rules to an evaluator and check the results.
- [Set Up a Real-Time LLM-as-a-Judge](../../how-to/evaluations/realtime_llm_judge.md#step-4-optional-add-tag-rules-to-flag-results-automatically): use tag rules to flag sessions from a live chatbot.
