# Set Up a Real-Time LLM Judge

This guide shows you how to set up an LLM-as-a-judge: an [LLM evaluator](../../concepts/evaluations/evaluators.md#llm-evaluator) that scores each new chatbot session automatically as it arrives. Use it to monitor the quality of a live chatbot without starting evaluation runs by hand.

The pattern combines a [session-level dataset](../../concepts/evaluations/dataset.md#evaluation-levels) that continuously ingests new sessions from a chatbot with an [LLM evaluator](../../concepts/evaluations/evaluators.md#llm-evaluator) set to run automatically on each new batch.

For background on evaluations, datasets, and evaluators, see [Evaluations](../../concepts/evaluations/index.md).

## Prerequisites

- An existing chatbot with at least one active session.
- Permission to create datasets and evaluators in your team.

## Step 1: Create a session-level dataset

The dataset holds the sessions that the evaluator scores. Each row is one complete session from your chatbot.

Session-level datasets are the only dataset type that supports continuous auto-population from a live chatbot. The evaluation level is set at creation and **cannot be changed later**, so choose **Session level** before saving.

See [Evaluation Datasets](../../concepts/evaluations/dataset.md) for an overview of evaluation levels and how session data maps into dataset fields.

## Step 2: Add an auto-population rule

Once the dataset exists, add an auto-population rule to tell OCS which chatbot sessions to add to it. For full details, see [Auto-Population Rules](../../tech-hub/evaluations/auto_population.md).

Each rule requires:

- **Source chatbot**: the chatbot whose sessions are considered for ingestion.
- **Filter criteria**: standard session filters (tags, participant, channel, date range, etc.) that narrow which sessions are picked up.

A dataset can have more than one rule — useful if you want to combine sessions from multiple chatbots or different filter criteria into the same dataset.

!!! note
    A rule only ingests sessions created **after the rule itself was created**. Enabling a rule does not backfill historical sessions.

For full details of **how ingestion works once the rule is active**, see [Auto-Population Rules on Tech Hub](../../tech-hub/evaluations/auto_population.md#how-ingestion-works).

## Step 3: Create a session-level LLM evaluator

Create an LLM evaluator and set its **Evaluation mode** to **Session** so it is compatible with the dataset from Step 1.

Session-level prompts use `{full_history}` for the conversation. See [Template variables](../../tech-hub/evaluations/evaluator-reference.md#template-variables) (**Session level** tab) for the full list.

**Example prompt:**

```text
You are evaluating a support chatbot conversation. Review the session below and assess:
1. Whether the participant's goal was completed.
2. The overall quality of the responses.

Session transcript:
{full_history}

Respond with the fields defined in the output schema.
```

**Example output schema:**

| Column name | Type | Notes |
|---|---|---|
| `goal_completion` | choice | Options: `yes`, `partial`, `no` |
| `quality_score` | integer | Scale of 1–5 |

Define the output schema fields to match what you reference in the prompt. See [Output schema](../../concepts/evaluations/evaluators.md#output-schema) for the field types.

## Step 4 (optional): Add tag rules to flag results automatically

[Tag rules](../../concepts/evaluations/tag_rules.md) apply a tag to a session automatically when an evaluator output field meets a condition. Use them to find the sessions you need to review without checking every row.

**Example rules using the output schema from Step 3:**

| Output field | Tag name | Condition |
|---|---|---|
| `goal_completion` | `goal-not-met` | equals `no` |
| `quality_score` | `low-quality` | range `1..2` |

With these rules in place, sessions where the goal was not met or where quality scored 1 or 2 are tagged automatically after each evaluation run.

!!! tip
    Tagged sessions can be filtered in the session list, so your team can follow up on them first without reviewing every result.

See [Tag Rules](../../concepts/evaluations/tag_rules.md) for the full set of condition types.

## Step 5: Create an evaluation with auto-run turned on

1. Under **Evaluations**, click **Add new**. See [Create an evaluation](run-an-evaluation.md#create-an-evaluation) for the full form.
2. Select the dataset from Step 1 as the **Dataset**.
3. Select the LLM evaluator from Step 3 under **Evaluators**.
4. Check **Auto-run when new rows are auto-populated**. This is what makes the judging happen automatically.
5. Click **Create**.

**What happens after auto-run is turned on:**

Each time the auto-population rule (Step 2) adds new sessions to the dataset, the evaluation runs automatically on just those rows. These are **delta runs**, and they appear alongside full runs in the runs list. Sessions you add to the dataset by hand do not start a run. See [Automatic delta evaluation runs](../../tech-hub/evaluations/auto_population.md#automatic-delta-evaluation-runs) for details.

!!! note "Ongoing cost"
    Because auto-run keeps judging new sessions as they arrive, it keeps making LLM calls in the background. This adds to your team's total cost and usage over time, though it is never attributed to the source chatbot or its participants. See [Evaluation cost and usage](../../concepts/evaluations/evaluators.md#llm-evaluator) for details.

## Verifying it works

After setup, confirm the pipeline is running end to end:

1. **New sessions appear in the dataset** — once a new session matches the rule's filter, the dataset row count should increase within the [polling interval](../../tech-hub/evaluations/auto_population.md#how-ingestion-works).
2. **Delta runs appear in the run table** — each ingestion cycle that adds new sessions should produce a corresponding delta run entry.
3. **Tags appear on matching sessions** — if you configured tag rules, check the Applied Tags column on the run results page and verify that sessions meeting the conditions are tagged.

If sessions are not appearing, verify that the [auto-population rule](../../tech-hub/evaluations/auto_population.md) is still enabled.

## See also

- [Auto-Population Rules](../../tech-hub/evaluations/auto_population.md): how ingestion, the lookback window and automatic delta runs work.
- [Tag Rules](../../concepts/evaluations/tag_rules.md): the condition types available for flagging results.
- [Run an Evaluation](run-an-evaluation.md): create, preview and run an evaluation by hand.
