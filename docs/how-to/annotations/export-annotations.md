# Export Annotations

Export annotations to analyse reviewers' answers outside Open Chat Studio.
The queue detail page shows [aggregate scores](../../concepts/annotations/queues.md#aggregate-scores).
An export gives you every individual answer.
Use it to compare how closely reviewers agree, to run your own statistics in a spreadsheet, or to prepare labelled sessions for model training.

This guide shows how to download the submitted annotations from a queue as a CSV or JSONL file.
For the columns and fields in each file, see [Annotation Export Format](../../tech-hub/annotations/export-format.md).
For how exports fit into the review process, see [Exporting Results](../../concepts/annotations/queues.md#exporting-results).

## Prerequisites

- A queue with at least one submitted annotation. See [Annotate Queue Items](annotate-items.md).

## Export a Queue

1. In the left sidebar, open **Annotations** and click the annotation queue you want to get data from.
2. On the queue detail page, click **Export CSV** or **Export JSONL**.
   - Use **CSV** to open the results in a spreadsheet.
   - Use **JSONL** to process the results programmatically.

## Expected Outcome

Your browser downloads a file named after the queue, ending in `_annotations.csv` or `_annotations.jsonl`.
It contains every submitted annotation, with each reviewer's answers side by side.
Items in any status are included, even if they are still waiting for more reviews.
Items with no annotations are left out, unless they are [flagged](annotate-items.md#flag-an-item).
