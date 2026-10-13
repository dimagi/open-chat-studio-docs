# Evaluation Datasets

An evaluation needs example conversations to test against. A **dataset** is that set of messages or sessions, and it is what the [evaluators](./evaluators.md) score.

A small set of realistic examples tells you more about your chatbot than scoring everything that exists. You can build a dataset from real conversations your chatbot has already had, or write your own test cases to check specific behaviors, including edge cases your chatbot has not met yet.

## Evaluation levels

When you create a dataset, you choose an **Evaluation level**. It decides how the dataset is structured and which evaluators can use it.

| Level | Each row is | Use it to judge |
|---|---|---|
| **Message level** | A single Human/AI message pair | Individual responses, for accuracy, tone or correctness |
| **Session level** | An entire conversation | Overall quality, goal completion, or coherence across turns |

The level cannot be changed after the dataset is created. An evaluator's **Evaluation mode** (Message or Session) must match the dataset's level, and incompatible evaluators are hidden when you set up an evaluation.

## How datasets are created

Which methods are available depends on the evaluation level.

| Method | Message level | Session level | Use it when |
|---|---|---|---|
| [Clone from sessions](../../how-to/evaluations/create-a-dataset.md#clone-from-sessions) | Yes | Yes | You want to test against real past conversations. Cloned rows keep a link to their original session. |
| [Import from an annotation queue](../../how-to/evaluations/create-a-dataset.md#import-from-an-annotation-queue) | No | Yes | Your team has already curated conversations for [human review](../annotations/queues.md) and you want to score the same set automatically. |
| [Create rows manually](../../how-to/evaluations/create-a-dataset.md#create-manually) | Yes | No | You want to write targeted test cases or edge cases that have not happened yet. |
| [Upload a CSV](../../how-to/evaluations/create-a-dataset.md#upload-csv-file) | Yes | No | You have an existing test suite or data from another tool. |
| [Auto-population rules](../../tech-hub/evaluations/auto_population.md) | No | Yes | You want new sessions from a live chatbot added continuously. |

## Sharing dataset messages

Each row in the dataset table has a link button that copies a direct link to that message. Anyone who opens the link is taken to the message, which is highlighted. Use it to refer to a specific test case in a discussion.

## Next steps

- [Create a Dataset](../../how-to/evaluations/create-a-dataset.md) — step-by-step instructions for each method.
- [Run an Evaluation](../../how-to/evaluations/run-an-evaluation.md) — score the dataset once you have evaluators.
- [Dataset Structure](../../tech-hub/evaluations/dataset-structure.md) — field reference and CSV format.
