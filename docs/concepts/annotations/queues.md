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

## Creating a Queue

Navigate to **Annotation Queues** in the left sidebar and click **New Queue**.

| Field | Description |
|-------|-------------|
| **Name** | Unique name for this queue within your team |
| **Description** | Optional context for reviewers |
| **Schema** | Add one or more annotation fields (see above) |
| **Assignees** | Team members who will review items in this queue |
| **Reviews required** | Number of independent reviews needed per item (1–10, default: 1) |

!!! tip "Multiple reviews"
    Setting **Reviews required** to more than 1 is useful when you want multiple reviewers to independently annotate the same item — for example, to measure inter-rater agreement or to get a consensus rating. An item is marked **Completed** only when it has received the required number of reviews.

### Queue Status

| Status | Meaning |
|--------|---------|
| **Active** | Open for annotation |
| **Paused** | Temporarily closed; reviewers cannot submit new annotations |
| **Completed** | All items have been reviewed |
| **Archived** | Queue is closed and no longer active |

## Changing Reviews Required After Annotation Starts

You can change the **Reviews required** setting on a queue even after annotation is underway. Because this affects how item statuses are calculated, the system recomputes the status of every non-flagged item when you save the change.

Before applying the change, a confirmation dialog summarises what will happen. Review it carefully before confirming.

### Effects of raising the requirement

Increasing **Reviews required** can move items that were previously **Completed** back to **In Progress** or **Awaiting resolution** — if they no longer have enough reviews to meet the new threshold.

### Effects of lowering the requirement

Decreasing **Reviews required** does not automatically complete items that still have unresolved reviews. Items where all required reviews are in but no authoritative annotation has been selected remain in **Awaiting resolution** until a queue admin picks one annotation as authoritative.

### Switching to multi-reviewer mode

When you increase **Reviews required** from 1 to more than 1, any authoritative flags that were set automatically by the system are cleared. Authoritative flags that a queue admin set manually are kept. Aggregate scores are refreshed after the change.

!!! note
    Flagged items are not affected by a change to **Reviews required** — their status remains **Flagged** until a manager unflags them.

## Adding Items

Items can be added to a queue in three ways.

### 1. Session Selector

From the queue detail page, click **Add Sessions**. This opens a filterable table of experiment sessions. You can then choose how many sessions to add:

| Mode | Description |
|------|-------------|
| **Selected only** (default) | Add only the sessions you've checked |
| **All matching filters** | Add every session matching the current filter criteria |
| **Sample** | Add a random percentage of sessions matching the current filters |

!!! note
    A confirmation prompt is shown for bulk operations (all matching, or large samples).

Sessions that are already in the queue are excluded from the selector.

### 2. Import from Evaluations Dataset

Click **Import from Dataset** on the queue detail page to add sessions from an existing [evaluations dataset](../evaluations/dataset.md). This is useful when you want to annotate the same set of sessions you used for automated evaluations.

### 3. From a Session Detail Page

On any session detail page, use the **Add to Queue** button to add that session directly to one or more annotation queues.

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

!!! note "Multi-reviewer aggregation"
    For multi-reviewer queues, aggregates prefer the **authoritative** annotation per item when one is set. Items without an authoritative pick fall back to averaging across all submitted annotations for that item.

## Exporting Results

From the queue detail page (requires queue management permissions), you can export all submitted annotations:

| Format | Description |
|--------|-------------|
| **CSV** | Spreadsheet-friendly, one row per annotation |
| **JSONL** | One JSON object per line, suitable for programmatic processing |

The export includes the item details, reviewer, and all annotation field values. It also includes flagged items that have no reviewer annotations, so every flagged item appears in the export regardless of review status.

Each exported record contains the following fields:

| Field | Description |
|-------|-------------|
| Item details | Source data for the reviewed item (e.g. message content, session metadata) |
| Reviewer | The team member who submitted the annotation |
| Annotation field values | One value per schema field defined on the queue |
| `session_id` | External UUID of the session linked to the annotation item |
| `flagged` | Boolean indicating whether the item is flagged |
| `flagged_reason` | Full list of flag entries recorded on the item |
| `is_authoritative` | Boolean indicating whether this annotation is the authoritative answer for the item (always `true` on single-reviewer queues; set per-item by a queue admin on multi-reviewer queues) |

!!! note
    In CSV exports, `flagged_reason` is JSON-serialized as a string. Use JSONL format if you need to process flag entries programmatically without parsing JSON within a field.

## Managing Assignees

Use **Manage Assignees** on the queue detail page to add or remove reviewers. Assignees receive access to the queue and can see it in their annotation queue list.

!!! note
    If a queue has no assignees, any team member with the annotation permission can annotate items in it. Once assignees are added, only they can submit annotations.
