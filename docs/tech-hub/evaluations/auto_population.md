# Auto-Population Rules

Auto-population keeps a [session-level dataset](../../concepts/evaluations/dataset.md#evaluation-levels) up to date by adding new sessions from a source chatbot automatically, so you don't have to add them by hand. Each dataset can have one or more **auto-population rules**, and each rule defines:

- **Source chatbot**: The chatbot whose sessions should be considered for ingestion.
- **Filter criteria**: Standard session filters (tags, participant, channel, date range, etc.) that determine which sessions match the rule.

!!! note
    Auto-population is available for **session-level** datasets only. Message-level datasets must be populated by one of the [other creation methods](../../concepts/evaluations/dataset.md#how-datasets-are-created).

    See [Evaluation Datasets](../../concepts/evaluations/dataset.md#evaluation-levels) for an overview of session-level vs. message-level datasets.

For a step-by-step setup that combines auto-population with an evaluator, see [Set Up a Real-Time LLM Judge](../../how-to/evaluations/realtime_llm_judge.md).

## How ingestion works

A background task polls each enabled rule every **5 minutes** and adds any new sessions that match its filters and are not already in the dataset. Ingestion is bounded:

- Only sessions created **after the rule itself was created** are eligible — enabling a rule does not backfill historical sessions.
- A configurable lookback window (default: 30 days) limits how far back the poller scans, based on session creation date. This means a rule will only ingest sessions created within the lookback window, even if they otherwise match the filter (e.g. a session matching a tag filter will only be picked up if it was created less than 30 days ago).

If a rule fails repeatedly (e.g. due to a misconfigured filter or a transient database error), it is automatically **disabled after three consecutive failures** and a [notification](../../concepts/notifications.md) is raised so the rule can be reviewed.

## Automatic delta evaluation runs

Auto-population works together with the **Auto-run when new rows are auto-populated** setting on an evaluation (stored as `auto_run_on_append`). When new sessions are added to a dataset by an auto-population rule, any evaluation that uses that dataset *and* has this setting turned on runs automatically against the newly added rows.

Each automatic run scores only the rows added in that ingestion cycle, producing a **delta** result set rather than re-evaluating every row in the dataset. The evaluation run table lists both **full** runs (which score the entire dataset) and **delta** runs (which score only newly added rows), so you can track results from manual full runs and automatic delta runs side by side.

Manual filter-import and CSV-import paths do not trigger automatic evaluation runs — only the auto-population path does.

An automatic run is skipped if the config has no evaluators, or if every evaluator on it is [archived](../../concepts/evaluations/evaluators.md#archiving-evaluators), since it would produce no results. The skip is only recorded in the server log; nothing is shown in the app.

## See also

- [Set Up a Real-Time LLM Judge](../../how-to/evaluations/realtime_llm_judge.md): a worked setup that uses auto-population.
- [Run an Evaluation](../../how-to/evaluations/run-an-evaluation.md): how full and delta runs appear in the runs list.
