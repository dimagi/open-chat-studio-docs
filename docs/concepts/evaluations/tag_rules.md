# Tag Rules for LLM Evaluators

Running an evaluation against hundreds of messages produces a results table too large to read row by row. **Tag Rules** solve this by automatically tagging the sessions or messages that meet a condition you define.

For example, you could flag every session with negative sentiment, or every response that scored below a threshold — so your team can go directly to the conversations that need attention instead of reviewing everything.

## How tag rules work

A tag rule checks one output field of an [LLM evaluator](evaluators.md#llm-evaluator). When the field's value meets the rule's condition, such as equalling `negative` or falling between 1 and 2, the rule applies its tag. Rules run on every evaluation run except previews, and they skip rows that failed.

The evaluator's mode decides what gets tagged:

- **Message mode**: the chat message being evaluated.
- **Session mode**: the session's chat.

A row can only be tagged if it has a chat message or session to tag. Message-level rows added manually or from a CSV file have none, so rules do not tag them.

Tags follow the latest results. After each run, a rule removes its tag from any message or session in the run that no longer meets its condition, even if a person added the tag by hand. See [Tag reconciliation on rerun](../../tech-hub/evaluations/evaluator-reference.md#tag-reconciliation-on-rerun).

## Next steps

- [Add Tag Rules](../../how-to/evaluations/add-tag-rules.md): add rules to an evaluator and check the results.
- [Set Up a Real-Time LLM-as-a-Judge](../../how-to/evaluations/realtime_llm_judge.md#step-4-optional-add-tag-rules-to-flag-results-automatically): use tag rules to flag sessions from a live chatbot.
