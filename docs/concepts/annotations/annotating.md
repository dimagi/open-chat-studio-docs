# Annotating

Reviewers work through a queue one session at a time.
Once you add a session to a queue, OCS calls it an **item**: the queue's **Items** table lists it, and its status shows its review progress.
Reviewers submit an annotation, edit it, skip the item or flag it.
This page explains how an item moves between statuses and how conflicting reviews are resolved.
For the steps a reviewer follows, see [Annotate Queue Items](../../how-to/annotations/annotate-items.md).

## Item Status Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> InProgress : First annotation submitted
    InProgress --> Completed : Required reviews reached (single-reviewer queue)
    InProgress --> AwaitingResolution : Required reviews reached (multi-reviewer queue)
    AwaitingResolution --> Completed : Reviewer marks one annotation authoritative
    Completed --> AwaitingResolution : Reviewer clears the authoritative annotation
```

An item in any status can also be **Flagged**.
Unflagging returns it to the status its reviews give it, as shown in the diagram.
See [Flagging Items](#flagging-items).

| Status | Meaning |
|--------|---------|
| **Pending** | No annotations yet |
| **In Progress** | At least one annotation submitted, but not yet at the required count |
| **Awaiting resolution** | Multi-reviewer item has all required reviews, but no annotation has been marked **authoritative** yet |
| **Completed** | Required number of reviews have been submitted (and, for multi-reviewer queues, an authoritative annotation has been selected) |
| **Flagged** | Marked for follow-up; left out of the annotation sequence until unflagged |

!!! note "Single vs multi-reviewer queues"
    On single-reviewer queues (the default, **Num reviews required = 1**), the first submitted annotation is automatically marked as authoritative and the item moves straight to **Completed**. The authoritative workflow below only applies to queues configured with **Num reviews required > 1**.

## Resolving Multi-Reviewer Conflicts

When a multi-reviewer queue collects all required reviews for an item, the item enters **Awaiting resolution** until a reviewer picks one annotation as the authoritative answer.
**Start Annotating** only serves **Pending** and **In Progress** items, so open an item awaiting resolution from the queue's **Items** table.

The annotations list replaces the annotation form once you have annotated the item yourself, or if the queue has assignees and you are not one of them.
On that list, any team member who can open the item sees:

- An amber **Awaiting resolution** banner at the top of the list
- A **Mark authoritative** button next to each annotation

The banner says an admin must make the choice, but no admin permission is needed.
For the steps, see [Resolve an Item Awaiting Resolution](../../how-to/annotations/annotate-items.md#resolve-an-item-awaiting-resolution).

Clicking **Mark authoritative** on an annotation flips the item to **Completed** and shows an **Authoritative** badge on that row (with a tooltip recording who marked it and when). Selecting a different annotation moves the badge — only one annotation per item can be marked authoritative at a time. Use **Clear authoritative** to return the item to **Awaiting resolution**.

!!! tip "Why this matters"
    Aggregate scores prefer the authoritative annotation when one is set; only when no annotation is authoritative do they fall back to averaging across all submitted annotations. Marking an authoritative answer therefore both resolves the conflict and ensures the queue's aggregate scores reflect the agreed answer.

## Flagging Items

Flagging marks an item that cannot be annotated, such as one with missing content or a corrupted session.
Each flag records the reviewer's name, the time and an optional reason.
Flagging an item again adds another entry rather than replacing the earlier one.

A **Flagged** item stays out of the annotation sequence until someone unflags it.
Its annotations stay in place and still count towards the queue's aggregate scores.
Flagged items are always included in [exports](../../how-to/annotations/export-annotations.md), with their flag entries.

Anyone with permission to change queue items can flag or unflag them, including users with the **Annotation Reviewer** role.
Unflagging recalculates the item's status from its reviews and deletes all its flag entries.

For the steps, see [Flag an Item](../../how-to/annotations/annotate-items.md#flag-an-item) and [Unflag an Item](../../how-to/annotations/manage-a-queue.md#unflag-an-item).

## Read-Only View

Each reviewer can submit only one annotation per item.
When you open an item you've already annotated, you see the item content and the annotations list without the submission form.
To change your answers, see [Edit Your Annotation](../../how-to/annotations/annotate-items.md#edit-your-annotation).

If the queue has assignees and you are not one of them, you also see the annotations list instead of the form.
You can read the item and its annotations, but you can't submit one.
