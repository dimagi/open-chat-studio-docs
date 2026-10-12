# Annotation Export Format

Reference for the CSV and JSONL files exported from an annotation queue. To run an export, see [Export Annotations](../../how-to/annotations/export-annotations.md).

Both formats pivot the results so that **each reviewer's answers appear side by side**, making it easy to compare reviewers on the same item. Both list fields in the queue's [field order](../../concepts/annotations/queues.md#field-order).

| Format | Structure |
|--------|-----------|
| **CSV** | Spreadsheet-friendly. One row per (item, schema field), with a column for each reviewer. |
| **JSONL** | One JSON object per item, suitable for programmatic processing. Each field holds its reviewers' values, keyed by email. |

The export covers every item's submitted annotations. Flagged items are always included, even when they have no annotations, so every flagged item appears regardless of review status.

## Shared Fields

Each exported item carries these fields:

| Field | Description |
|-------|-------------|
| `item_id` | ID of the annotation item |
| `item_type` | `session` or `message` |
| `session_id` | External UUID of the linked session (for message items, the session of the message's chat) |
| `flagged` | Whether the item is flagged |
| `flags` | List of flag entries recorded on the item (empty when not flagged) |
| `authoritative_annotator` | Email of the reviewer whose annotation was picked as authoritative for the item; blank if none has been picked. Auto-set on single-reviewer queues; chosen during resolution on multi-reviewer queues. |
| `annotated_at` | Timestamp of the most recent annotation on the item |

## Reviewer Answers

Each reviewer's answers to the schema fields are added differently in each format:

- **CSV** adds a `field` column (the schema field name) and one column per reviewer email. Each row is one item/field combination; the reviewer columns hold that reviewer's value, blank where they did not answer.
- **JSONL** adds a `fields` object shaped `{field: {reviewer_email: value}}`. A field a reviewer did not answer is `null`, and values keep their JSON types (numbers stay numbers).

Example JSONL record:

```json
{
  "item_id": 67, "item_type": "session", "session_id": "d99c...",
  "flagged": false, "flags": [],
  "authoritative_annotator": "marcus@example.com", "annotated_at": "2026-07-15T13:17:02Z",
  "fields": {
    "tone":     {"fatima@example.com": "friendly", "marcus@example.com": "too casual"},
    "accuracy": {"fatima@example.com": "accurate", "marcus@example.com": "missed grammar"}
  }
}
```

!!! note
    In CSV exports, `flags` is serialized as JSON in a single cell. Use JSONL if you need to process flag entries or field values programmatically without parsing JSON from within a column.
