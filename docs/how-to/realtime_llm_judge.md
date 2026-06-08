# Set Up a Real-Time LLM Judge

This guide shows you how to configure an LLM-as-a-judge that scores new chatbot sessions automatically as they arrive, with no manual intervention required. The pattern combines a session-level dataset that continuously ingests new sessions from a chatbot with an LLM evaluator set to run automatically on each new batch.

For background on evaluations, datasets, and evaluators, see [Evaluations](../concepts/evaluations/index.md).

## Prerequisites

- An existing chatbot with at least one active session.
- Permission to create datasets and evaluators in your team.

## Step 1: Create a session-level dataset

Session-level datasets are the only dataset type that supports continuous auto-population from a live chatbot. The evaluation level is set at creation and **cannot be changed later**, so choose session-level before saving.

See [Evaluation Datasets](../concepts/evaluations/dataset.md) for an overview of evaluation levels and how session data maps into dataset fields.

## Step 2: Add an auto-population rule

Once the dataset exists, add an auto-population rule to tell OCS which chatbot sessions should flow into it.

Each rule requires:

- **Source chatbot**: the chatbot whose sessions are considered for ingestion.
- **Filter criteria**: standard session filters (tags, participant, channel, date range, etc.) that narrow which sessions are picked up.

A dataset can have more than one rule — useful if you want to combine sessions from multiple chatbots or different filter criteria into the same dataset.

!!! note
    A rule only ingests sessions created **after the rule itself was created**. Enabling a rule does not backfill historical sessions.

**How ingestion works once the rule is active:**

- A background task polls each enabled rule every **5 minutes** and adds any new matching sessions not already in the dataset.
- A configurable lookback window (default: 30 days) limits how far back the poller scans, based on session creation date.
- If a rule fails three consecutive times, it is **automatically disabled** and a notification is raised. If ingestion appears to have stopped, check whether the rule is still enabled.

For full details, see [Auto-Population Rules](../concepts/evaluations/dataset.md#auto-population-rules).

## Step 3: Create a session-level LLM evaluator

Create an LLM evaluator and set its evaluation mode to **session-level** so it is compatible with the dataset from Step 1.

In session-level prompts, `{input.content}` and `{output.content}` are empty. Use these variables instead:

| Variable | What it contains |
|---|---|
| `{full_history}` | The full session transcript |
| `{context.[parameter]}` | Any context variable, e.g. `{context.current_datetime}` |

!!! note
    `{generated_response}` is not available for session-level evaluators. Generation is a message-level feature only.

**Example prompt:**

```
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
| `goal_completion` | choices | Options: `yes`, `partial`, `no` |
| `quality_score` | integer | Scale of 1–5 |

Define the output schema fields to match what you reference in the prompt. The evaluator validates the LLM's output against the schema and retries up to three times if the output does not match.

See [Evaluators](../concepts/evaluations/evaluators.md) for full details on output schema types and template variables.

## Step 4 (optional): Add tag rules to flag results automatically

Tag rules apply a tag to a session automatically when an evaluator output field meets a condition. They run on every non-preview evaluation run and make it easy to surface sessions of interest without reviewing every row.

In session mode, the tag is applied to the session's chat. Each application is recorded in the **Applied Tags** column on the run results page.

**Example rules using the output schema from Step 3:**

| Output field | Tag name | Condition |
|---|---|---|
| `goal_completion` | `goal-not-met` | equals `no` |
| `quality_score` | `low-quality` | range `1..2` |

With these rules in place, sessions where the goal was not met or where quality scored 1 or 2 are tagged automatically after each evaluation run.

!!! tip
    Tagged sessions can be filtered in the session list, so your team can prioritise follow-up without wading through all results.

See [Tag Rules](../concepts/evaluations/evaluators.md#tag-rules) for the full set of condition types.

## Step 5: Create an evaluation config with auto-run enabled

Create an **evaluation config** that references:

- The dataset from Step 1.
- The LLM evaluator from Step 3.

Then enable the **auto-run** flag on the config. This is what makes the judging happen automatically.

**What happens after auto-run is enabled:**

When the auto-population rule (Step 2) adds new sessions to the dataset, any evaluation config referencing that dataset with auto-run set is triggered automatically against the newly added rows. These are **delta runs** — they score only the rows added in that ingestion cycle, not the entire dataset.

Delta runs appear alongside full runs in the evaluation run table. Full runs score the entire dataset and are triggered manually; delta runs score only the newest rows and are triggered automatically.

!!! warning
    Auto-run is triggered **only** by the auto-population path. Manually importing sessions via CSV or filter-import does not trigger automatic evaluation runs.

## Verifying it works

After setup, confirm the pipeline is running end to end:

1. **New sessions appear in the dataset** — within approximately 5 minutes of a new session matching the rule's filter, the dataset row count should increase.
2. **Delta runs appear in the run table** — each ingestion cycle that adds new sessions should produce a corresponding delta run entry.
3. **Tags appear on matching sessions** — if you configured tag rules, check the Applied Tags column on the run results page and verify that sessions meeting the conditions are tagged.

If sessions are not appearing, verify that the auto-population rule is still enabled (see Step 2 for the three-failure auto-disable behaviour).
