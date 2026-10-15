# Evaluation Datasets

An evaluation needs example conversations to test against. A **dataset** is that set of messages or sessions, and it is what the [evaluators](./evaluators.md) score.

A small set of realistic examples tells you more about your chatbot than scoring everything that exists. You can build a dataset from real conversations your chatbot has already had, or write your own test cases to check specific behaviors, including edge cases that have not come up in real conversations yet.

## Example

A participant has this conversation with a clinic's appointment chatbot:

> **User:** Can I book a check-up for Tuesday?
>
> **Bot:** Yes, there is a slot at 10:00 or 14:30. Which would you like?
>
> **User:** 14:30 please.
>
> **Bot:** Booked. You'll get a reminder the day before.

A dataset can store this conversation in two ways, depending on its [evaluation level](#evaluation-levels).

In a **message-level** dataset, the conversation becomes two rows. Each row holds one Human/AI message pair, the participant's message and the chatbot's reply, with the earlier turns as history:

| Row | Human Message | AI Message | History |
|---|---|---|---|
| 1 | Can I book a check-up for Tuesday? | Yes, there is a slot at 10:00 or 14:30. Which would you like? | (none) |
| 2 | 14:30 please. | Booked. You'll get a reminder the day before. | The two messages from row 1 |

An evaluator scores each reply separately, using the history for context. For example: "Did the chatbot offer times that were actually available?"

In a **session-level** dataset, the conversation becomes one row that holds all four messages. An evaluator scores the conversation as a whole. For example: "Did the participant end up with a booking?"

## Evaluation levels

When you create a dataset, you choose its **Evaluation level**.

| Level | Each row is | Use it to judge |
|---|---|---|
| **Message level** | A single Human/AI message pair | Individual responses, for accuracy, tone or correctness |
| **Session level** | An entire conversation | Overall quality, goal completion, or coherence across turns |

Choose **message level** if you want to:

- Test a new chatbot version by having it generate fresh replies to score.
- Write test cases by hand or upload them from a CSV file.

Choose **session level** if you want to:

- Judge whether whole conversations went well.
- Add new conversations from a live chatbot automatically.

You cannot change the level after the dataset is created.
Each evaluator is also set to message or session level, and you can only use evaluators set to the same level as the dataset.
See [Evaluators](./evaluators.md).

## How datasets are created

Which methods are available depends on the evaluation level.

| Method | Message level | Session level | Use it when |
|---|---|---|---|
| [Clone from sessions](../../how-to/evaluations/create-a-dataset.md#clone-from-sessions) | Yes | Yes | You want to test against real past conversations. Cloned rows keep a link to their original session. |
| [Import from an annotation queue](../../how-to/evaluations/create-a-dataset.md#import-from-annotation-queue) | When creating the dataset only | Yes | Your team has already curated conversations for [human review](../annotations/queues.md) and you want to score the same set automatically. |
| [Create rows manually](../../how-to/evaluations/create-a-dataset.md#create-manually) | Yes | No | You want to write targeted test cases or edge cases that have not happened yet. |
| [Upload a CSV](../../how-to/evaluations/create-a-dataset.md#upload-csv-file) | Yes | No | You have an existing test suite or data from another tool. |
| [Auto-population rules](../../tech-hub/evaluations/auto_population.md) | No | Yes | You want new sessions from a live chatbot added continuously. |

## Sharing dataset messages

Each row in the dataset table has a link button that copies a direct link to that message. Anyone who opens the link is taken to the message, which is highlighted. Use it to refer to a specific test case in a discussion.

## Next steps

- [Create a Dataset](../../how-to/evaluations/create-a-dataset.md) — step-by-step instructions for each method.
- [Run an Evaluation](../../how-to/evaluations/run-an-evaluation.md) — score the dataset once you have evaluators.
- [Dataset Structure](../../tech-hub/evaluations/dataset-structure.md) — field reference and CSV format.
