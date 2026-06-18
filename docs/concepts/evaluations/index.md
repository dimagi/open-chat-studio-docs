# Evaluations

Building a chatbot is the easy part. Knowing if it's actually working well — especially as you tweak prompts, swap models, or add new features — is harder. **Evaluations** let you check this systematically: run your chatbot against a set of sample conversations, and automatically score the results against criteria you define, such as accuracy, tone, or whether it stayed on topic.

Running evaluations regularly gives you an early warning when a change makes responses worse, and proof when a change makes them better — instead of relying on spot-checking conversations by hand.

In Open Chat Studio, evaluations can be run against existing conversation messages already in the system, or against a custom set of test cases you upload.

## Overview

- **Evaluations** are made up of a [dataset](./dataset.md) and one or more [evaluators](./evaluators.md).
- **Datasets** are collections of test case messages that serve as the foundation for running evaluations. Datasets can either be created directly from existing [sessions](../sessions.md), manually created in the UI, or uploaded with a CSV. See [Create a Dataset](../../how-to/evaluations/create-a-dataset.md) for step-by-step instructions. They are inputs for an evaluation.
- **Evaluators** define the logic for analyzing messages and generating evaluation metrics, either as an [LLM-as-judge prompt](./evaluators.md#llm-evaluator) or [custom python code](./evaluators.md#python-evaluator). Each evaluator takes individual messages from a dataset and optionally a generated response, then outputs structured results in a table. You can apply many evaluators to a dataset in parallel, and the outputs of each will be added as new columns to the table.
- **[Tag Rules](./tag_rules.md)** automatically tag sessions or messages whose evaluator output meets a condition you define, such as a low confidence score or negative sentiment, so you can jump straight to the conversations that need attention.

## Next steps

- [Create a Dataset](../../how-to/evaluations/create-a-dataset.md) — build your first dataset by cloning sessions, importing from an annotation queue, or uploading a CSV.
- [Evaluations Reference](../../tech-hub/evaluations/index.md) — evaluation execution and other advanced details.
