# Annotation Queues

An **Annotation Queue** is the central object in the annotations system. It defines what to review (the items), how to review it (the schema), who reviews it (the assignees), and how many reviews each item needs.

## Annotation Schema

Before creating a queue, you need to decide what fields reviewers will fill in. These fields are defined as part of the queue's **schema**.

### Field Types

| Type | Description | Options |
|------|-------------|---------|
| **integer** | Whole number input | Optional min/max constraints |
| **float** | Decimal number input | Optional min/max constraints |
| **string** | Free-text input | Optional max length |
| **choices** | Dropdown with predefined options | List of allowed values (required) |

Each field has a **name** and an optional **description** to guide reviewers.

**Example schema:**

| Field Name | Type | Description |
|------------|------|-------------|
| `helpfulness` | integer (1–5) | How helpful was the assistant's response? |
| `tone` | choices (professional, neutral, inappropriate) | Describe the tone of the conversation |
| `notes` | string | Any additional observations |

### Field Order

Each field card in the schema builder has a drag handle and up/down buttons (▲▼) for reordering.

The order you set is used everywhere fields are displayed: the annotation form, the annotations list on an item, CSV and JSONL exports, the aggregate scores panel, and the summary column in the queue's items table.

Once an item in the queue has a submitted review, the queue's set of fields locks — you can no longer add or remove a field, or change its type, because that would invalidate earlier annotations.
Reordering is not affected by the lock.
Annotations are stored by field name, so changing the display order doesn't change what was recorded, and you can keep reordering fields at any time, including after the lock.

A queue that has never been saved since field ordering was introduced has no order of its own, and its fields keep appearing as they did before. Open the queue's form and save it to give it an explicit order.

!!! tip "Keyboard and screen reader support"
    Use the up/down buttons instead of dragging if you prefer not to use drag-and-drop.

## Queue Settings

A queue has a name, an optional description, schema fields, and a **Num reviews required**. To set one up, see [Create an Annotation Queue and Add Items](../../how-to/annotations/create-a-queue.md).

!!! tip "Multiple reviews"
    Set **Num reviews required** to more than 1 when you want several reviewers to annotate the same item independently, for example to measure inter-rater agreement or to get a consensus rating. An item is marked **Completed** only when it has received the required number of reviews.

### Queue Status

| Status | Meaning |
|--------|---------|
| **Active** | Open for annotation |
| **Paused** | Temporarily closed; reviewers cannot submit new annotations |
| **Completed** | All items have been reviewed |
| **Archived** | Queue is closed and no longer active |

## Changing Reviews Required After Annotation Starts

You can change the **Num reviews required** setting on a queue even after annotation is underway.
Because this affects how item statuses are calculated, the system recomputes the status of every item that is not Flagged when you save the change.

Before applying the change, a confirmation dialog summarises what will happen. Review it carefully before confirming.

### Effects of raising the requirement

Increasing **Num reviews required** can move items that were previously **Completed** back to **In Progress** or **Awaiting resolution** — if they no longer have enough reviews to meet the new threshold.

### Effects of lowering the requirement

Decreasing **Num reviews required** does not automatically complete items that still have unresolved reviews. Items where all required reviews are in but no authoritative annotation has been selected remain in **Awaiting resolution** until a reviewer picks one annotation as authoritative.

### Switching to multi-reviewer mode

When you increase **Num reviews required** from 1 to more than 1, any authoritative flags that were set automatically by the system are cleared. Authoritative flags that a reviewer set manually are kept. Aggregate scores are refreshed after the change.

!!! note
    Flagged items are not affected by a change to **Num reviews required** — their status remains **Flagged** until a manager unflags them.

## Adding Items

Items are sessions that reviewers will annotate. You can add them from a filterable session selector, by importing the sessions of an [evaluation dataset](../evaluations/dataset.md), or from a session's detail page. Sessions already in the queue are skipped. For the steps, see [Create an Annotation Queue and Add Items](../../how-to/annotations/create-a-queue.md#add-items-to-the-queue).

Sessions already in a queue are marked on the sessions list, and the **Annotation Queue** filter there can pick out sessions that are in no queue. See [Annotation Queues on the Sessions List](../sessions.md#annotation-queues-on-the-sessions-list).

## Monitoring Progress

The queue detail page shows a progress summary:

- **Total items** in the queue
- **Completed** items (reached required number of reviews; for multi-reviewer queues, an authoritative annotation has also been selected)
- **Flagged** items
- **Overall review progress** as a percentage (reviews done / reviews needed)

For multi-reviewer queues, the summary also surfaces two additional counts:

- **Resolved** — items that have an authoritative annotation, shown as `X / N items resolved`
- **Awaiting resolution** — items where all required reviews are in but no authoritative annotation has been selected yet (see [Resolving Multi-Reviewer Conflicts](annotating.md#resolving-multi-reviewer-conflicts))

## Aggregate Scores

After annotations are submitted, **aggregate scores** are automatically computed and displayed on the queue detail page.

| Field Type | Aggregates Shown |
|------------|-----------------|
| Numeric (integer, float) | Mean, median, min, max, standard deviation |
| Categorical (choices) | Mode, distribution percentages per option |

Aggregates are recomputed after each annotation submission, so you always see up-to-date stats.
They are listed in the queue's [field order](#field-order).

!!! note "Multi-reviewer aggregation"
    For multi-reviewer queues, aggregates prefer the **authoritative** annotation per item when one is set. Items without an authoritative pick fall back to averaging across all submitted annotations for that item.

## Exporting Results

You can export all submitted annotations from the queue detail page as CSV or JSONL. Each reviewer's answers appear side by side, and flagged items are always included. To export, see [Export Annotations](../../how-to/annotations/export-annotations.md). For the file contents, see [Annotation Export Format](../../tech-hub/annotations/export-format.md).

## Managing Assignees

Use **Manage Assignees** on the queue detail page to add or remove reviewers. Assignees receive access to the queue and can see it in their annotation queue list.

!!! note
    If a queue has no assignees, any team member with the annotation permission can annotate items in it. Once assignees are added, only they can submit annotations.
