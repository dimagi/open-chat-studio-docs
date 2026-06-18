# Evaluation Datasets

Every evaluation needs example conversations to test against — that's what a **dataset** provides. A dataset is the set of messages or sessions you want to score.

Dataset quality matters more than dataset size: a small, well-chosen set of realistic examples tells you more about how your chatbot behaves than scoring everything that happens to exist.

You can build a dataset from real conversations your chatbot has already had, or write your own test cases to check specific behaviors — including edge cases your chatbot hasn't encountered yet.

## Evaluation Levels

When creating a dataset, you choose an **Evaluation level** that determines how the dataset is structured and which evaluators are compatible with it.

| Level | Description | When to use |
|---|---|---|
| **Message level** | Each row represents a single Human/AI message pair | Judging individual responses for accuracy, tone, or correctness |
| **Session level** | Each row represents an entire conversation | Judging overall conversation quality, goal completion, or coherence across turns |

The evaluation level is set at dataset creation and cannot be changed later. Evaluators must share the same evaluation level as the dataset — incompatible evaluators are automatically disabled when configuring an evaluation run.

## How Datasets Are Created

There are four ways to populate a dataset. The right choice depends on the data you have available and the evaluation level you selected.

**Clone from a session** — turn real past conversations into test cases. Cloned rows keep a link back to their original session, which enables additional workflows such as importing into an annotation queue for human review.

**Import from an annotation queue** — pull sessions directly from an existing annotation queue into a session-level dataset. This is useful when you have already curated a set of conversations for human review and want to evaluate them automatically.

**Create rows manually** — add individual message pairs by hand in the UI. This is useful for writing targeted test cases that cover specific behaviors or edge cases your chatbot has not yet encountered in real conversations.

**Upload a CSV** — bulk-load message pairs from a file. This is the fastest way to migrate an existing test suite or import data from another tool.

!!! note
    Manual creation and CSV upload are only available for **message-level** datasets.

    **Session-level** datasets must be populated by cloning sessions, by configuring an [auto-population rule](../../tech-hub/evaluations/auto_population.md), or by importing sessions from an annotation queue.

For step-by-step instructions for each method, see [Create a Dataset](../../how-to/evaluations/create-a-dataset.md). For the full field reference and CSV format details, see [Dataset Structure](../../tech-hub/evaluations/dataset-structure.md).

## Auto-Population Rules

Session-level datasets can be continuously and automatically populated with new sessions from a live chatbot, instead of being created manually or from a one-off import. See [Auto-Population Rules](../../tech-hub/evaluations/auto_population.md) for how to configure rules and how ingestion works.

## Sharing Dataset Messages

When viewing dataset messages in the table, each row includes a link button that allows you to share a direct link to that specific message. When someone follows this link, the page automatically scrolls to the message and highlights it for easy identification.

This feature is useful for collaborating with team members, referencing specific test cases in discussions, or documenting particular dataset examples. Click the link icon next to any message and the URL will be copied to your clipboard with the message ID parameter included.
