# Evaluations

This section covers Open Chat Studio's advanced evaluation features: writing custom Python evaluators and configuring continuous dataset ingestion.

For a non-technical overview of datasets, evaluators, and how evaluation runs work, see [Evaluations](../../concepts/evaluations/index.md).

## Pages in this section

- **[Dataset Structure](./dataset-structure.md)** — field-level reference for dataset rows, cloning field mappings, history syntax, and CSV format details.
- **[Python Evaluator](./python_evaluator.md)** — write custom Python code to score messages, for deterministic rules or logic an LLM prompt can't reliably express. See [Evaluators](../../concepts/evaluations/evaluators.md#python-evaluator) for when to choose it over the LLM Evaluator.
- **[Auto-Population Rules](./auto_population.md)** — continuously ingest new sessions into a session-level dataset from a live chatbot, and trigger automatic delta evaluation runs against the new rows.

