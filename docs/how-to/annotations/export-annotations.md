# Export Annotations

Export annotations to analyse reviewers' answers outside Open Chat Studio. The queue detail page shows aggregate scores. An export gives you every individual answer. Use it, for example, to compare how closely reviewers agree, to run your own statistics in a spreadsheet, or to prepare labelled sessions for model training or fine-tuning.

This guide shows how to download the submitted annotations from a queue as a CSV or JSONL file. For the columns and fields in each file, see [Annotation Export Format](../../tech-hub/annotations/export-format.md).

## Prerequisites

- A queue where at least one reviewer has submitted an annotation. See [Annotate Queue Items](annotate-items.md). Items in any status are exported, including items that are still waiting for more reviews. Items with no annotations are not.
- Permission to view annotations. See [User Groups](../../concepts/team/groups.md).

## Export a Queue

1. In the left sidebar, open **Annotations** and click the annotation queue you want get data from.
2. On the queue detail page, click **Export CSV** or **Export JSONL**.
   - Use **CSV** to open the results in a spreadsheet.
   - Use **JSONL** to process the results programmatically.

## Expected Outcome

Your browser downloads a file named after the queue, ending in `_annotations.csv` or `_annotations.jsonl`. It contains every submitted annotation, with each reviewer's answers side by side. Flagged items are included even when they have no annotations.
