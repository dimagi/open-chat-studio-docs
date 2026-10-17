# Annotation Queues

An **annotation queue** is the central object in the annotations system. It defines what to review (the sessions), how to review it (the schema fields), who reviews it (the assignees), and how many reviews each session needs.

## Schema Fields

Before creating a queue, you need to decide what fields reviewers will fill in. You add them in the **Schema Fields** section of the queue form.

### Field Types

| Type | Description | Options |
|------|-------------|---------|
| **Text** | Free-text input | Optional **Max length** |
| **Integer** | Whole number input | Optional **Minimum** and **Maximum** |
| **Float** | Decimal number input | Optional **Minimum** and **Maximum** |
| **Choice** | Dropdown with predefined options | List of allowed values (required) |
| **Binary** | Dropdown with two answers, such as yes and no | **True label** and **False label**, the words reviewers see (default `True` and `False`) |

Each field has a **name**, an optional **description** to guide reviewers, and a **Required** checkbox, which is selected by default.
Reviewers can't submit an annotation until they answer every required field.

A **Binary** field stores the answer as `1` (the true label) or `0` (the false label), whatever the labels say.
The labels appear only in the annotation form and the aggregate scores.

**Example schema fields:**

| Field Name | Type | Description |
|------------|------|-------------|
| `helpfulness` | Integer (1–5) | How helpful was the assistant's response? |
| `tone` | Choice (professional, neutral, inappropriate) | Describe the tone of the conversation |
| `resolved` | Binary (Yes / No) | Did the assistant resolve the user's question? |
| `notes` | Text | Any additional observations |

### Field Order

Each field card in the **Schema Fields** section has a drag handle and up/down buttons (▲▼) for reordering.

The order you set is used everywhere fields are displayed: the annotation form, the annotations list on an item, CSV and JSONL exports, the aggregate scores panel, and the summary column in the queue's items table.

Once an item in the queue has a submitted review, the schema fields lock because changing them would invalidate earlier annotations.
The queue form shows a banner saying the schema structure is locked.
You can no longer add or remove a field or change its name, type, description or options.
You can still change whether each field is **Required**, and reordering is not affected by the lock.
Annotations are stored by field name, so changing the display order doesn't change what was recorded, and you can keep reordering fields at any time, including after the lock.

A queue that has never been saved since field ordering was introduced has no order of its own, and its fields keep appearing as they did before. Open the queue's form and save it to give it an explicit order.

!!! tip "Keyboard and screen reader support"
    Use the up/down buttons instead of dragging if you prefer not to use drag-and-drop.

## Queue Settings

A queue has a name, an optional description, schema fields, and a **Num reviews required**. To set one up, see [Create an Annotation Queue and Add Sessions](../../how-to/annotations/create-a-queue.md).

!!! tip "Multiple reviews"
    Set **Num reviews required** to more than 1 when you want several reviewers to annotate the same session independently, for example to measure inter-rater agreement or to get a consensus rating. A session is marked **Completed** only when it has received the required number of reviews.

### Queue Status

<!-- TODO(human): describe queue status accurately. See the conversation for what the code does. -->

## Adding Sessions

Each session you add to a queue becomes an item in its **Items** table. You can add sessions from a filterable session selector, by importing the sessions of an [evaluation dataset](../evaluations/dataset.md), or from a session's detail page. Sessions already in the queue are skipped. For the steps, see [Create an Annotation Queue and Add Sessions](../../how-to/annotations/create-a-queue.md#add-sessions-to-the-queue).

## Monitoring Progress

The **Progress** card on the queue detail page shows:

- A progress bar and the review count, such as `12/20 reviews (60%)`: the reviews submitted out of the reviews needed (items × **Num reviews required**)
- The completed item count, such as `5/10 items resolved`
- The number of items **awaiting resolution**, when there are any (see [Resolving Multi-Reviewer Conflicts](annotating.md#resolving-multi-reviewer-conflicts))
- The number of **flagged** items, when there are any

The queue list shows the same review count for every queue.

## Aggregate Scores

Aggregate scores summarise reviewers' answers for each field across the whole queue.
They appear in the **Aggregate Scores** card on the queue detail page once the first annotation is submitted, with one panel per field in the queue's [field order](#field-order).
**Text** fields have no aggregate.

### What Each Panel Shows

| Field Type | Aggregates Shown |
|------------|-----------------|
| **Integer**, **Float** | Mean, median, minimum and maximum |
| **Choice** | The most common answer (mode) and the percentage of answers for each option |
| **Binary** | The mean, which is the share of answers that were the true label, and the count for each label, such as `Yes: 7/10` |

The top right of each panel shows how many annotations were counted.
An annotation that left the field blank isn't counted.
If a Binary field has stored values other than `1` and `0`, they are left out and shown as **excluded**.

### Which Annotations Are Counted

For each item, the aggregates use the item's authoritative annotation if it has one.
Items without an authoritative annotation contribute every submitted annotation, so an item with three reviews counts three times.
On single-reviewer queues, every reviewed item has an authoritative annotation, so each item counts once.

When the counted annotations include both kinds, the panel shows a second line, such as `6 authoritative · 4 from unresolved items`.
A large unresolved count means the scores still include disagreeing reviews.
To count one answer per item, [resolve the items awaiting resolution](../../how-to/annotations/annotate-items.md#resolve-an-item-awaiting-resolution).

All items count, including flagged ones and items still **In Progress**.

### When Aggregates Update

Aggregates are recalculated when a reviewer submits or edits an annotation, when someone marks or clears an authoritative annotation, and when a change to **Num reviews required** clears authoritative annotations.

## Exporting Results

You can export all submitted annotations from the queue detail page as CSV or JSONL. Each reviewer's answers appear side by side, and flagged items are always included. To export, see [Export Annotations](../../how-to/annotations/export-annotations.md). For the file contents, see [Annotation Export Format](../../tech-hub/annotations/export-format.md).

## Managing Assignees

Use **Manage Assignees** on the queue detail page to add or remove reviewers. Assignees receive access to the queue and can see it in their annotation queue list.

!!! note
    If a queue has no assignees, any team member with the annotation permission can annotate items in it. Once assignees are added, only they can submit annotations.

    Team members who can't manage queues, such as those with the **Annotation Reviewer** role, see only the queues they are assigned to.
    To give them access to a queue, assign them to it.
