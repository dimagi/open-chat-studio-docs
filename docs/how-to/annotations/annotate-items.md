# Annotate Queue Items

This guide shows how to work through an annotation queue as a reviewer: submit annotations, edit them, skip items, flag items and resolve items that reviewers disagree on.
For the bigger picture, see the [Annotations overview](../../concepts/annotations/index.md).

## Prerequisites

- An annotation queue that contains sessions. See [Create an Annotation Queue and Add Sessions](create-a-queue.md).

## Open Your Queue

1. In the left sidebar, open **Annotations**.
2. Click the queue you want to work on.

The queue detail page has two ways to start annotating.

## Choose How to Annotate

| Option | Where | What it does |
|--------|-------|--------------|
| **[Start Annotating](#start-annotating-a-queue)** | Button at the top of the page | Takes you through the queue in order, one session at a time. It serves only **Pending** and **In Progress** items that you haven't annotated yet, and continues until none are left. |
| **[Annotate](#annotate-or-edit-a-single-item)** | Button in a row of the **Items** table | Opens that one item, whatever its status. Use it to annotate a specific session, to [edit your annotation](#annotate-or-edit-a-single-item) or to [resolve an item](#resolve-an-item-awaiting-resolution). |

## Start Annotating a Queue

1. On the queue detail page, click **Start Annotating**.
   The oldest **Pending** or **In Progress** item that you haven't annotated opens.
2. Read the session conversation in the left panel.
   It shows the participant's identifier, then all the messages in the session with timestamps and an icon for who sent each one.
3. Fill in your answers in the right panel for the fields where the description will help clarify how to answer.
   Below the form, the **Participant Data** and **Session State** tabs show more context to help you annotate.
4. Click **Submit**.
5. The next item opens automatically.
   Repeat steps 2 to 4, or [skip](#skip-an-item) or [flag](#flag-an-item) an item you can't annotate.

The badge at the top of the page shows how many items you have reviewed out of the total number of items in the queue.
The total includes items that are flagged or completed, so the count may not reach the total when you finish.

## Annotate or Edit a Single Item

Use this to annotate a specific session out of queue, or to change an annotation you already submitted.

1. On the queue detail page, click **Annotate** on the item's row in the **Items** table.
   The item opens whatever its status.
2. What you see depends on whether you have annotated the item:

    | Your situation | What opens |
    |----------------|------------|
    | You haven't annotated it | The annotation form to fill in the fields. |
    | You already annotated it | The annotations form with the previous answers to the fields |

3. Change them and click **Save**, or click **Cancel** to discard your changes.

Saving an edit updates your annotation and recalculates the queue's [aggregate scores](../../concepts/annotations/queues.md#aggregate-scores).
You can edit only your own annotations.

## Skip an Item

Click **Skip** to move to the next item without annotating this one.
The skipped item stays in the queue.
Because items are served oldest first, it opens again after you submit the next item.

## Flag an Item

Flag an item when something prevents you from annotating it, such as missing content, a corrupted session, or content that needs an admin to review.

1. Click **Flag** on the annotation form.
2. Optionally, enter a reason.
   A reason helps whoever reviews the flag decide what to do.
3. Click **Flag Item**.

The item's status changes to **Flagged**.
See [Flagging Items](../../concepts/annotations/annotating.md#flagging-items) for what a flag records and how flagged items are treated.

The **Flag** button is on the annotation form, so you can only flag an item you haven't annotated yet.
To return a flagged item to the review workflow, see [Unflag an Item](manage-a-queue.md#unflag-an-item).

## Resolve an Item Awaiting Resolution

Do this on queues that need more than one review, for items with the status **Awaiting resolution**.
See [Resolving Multi-Reviewer Conflicts](../../concepts/annotations/annotating.md#resolving-multi-reviewer-conflicts) for why and when.

1. On the queue detail page, find an item with the status **Awaiting resolution** in the **Items** table and click **Annotate**.
2. Compare the annotations in the list.
   The list replaces the form only if you have already annotated the item, or the queue has assignees and you are not one of them.
   See [Read-Only View](../../concepts/annotations/annotating.md#read-only-view).
3. Click **Mark authoritative** next to the annotation you agree with.

The item becomes **Completed**, and the chosen annotation shows an **Authoritative** badge.
To choose a different annotation, click **Mark authoritative** on it.
To undo the choice, click **Clear authoritative**.

## Expected Outcome

- Annotation items move through the statuses described in [Item Status Lifecycle](../../concepts/annotations/annotating.md#item-status-lifecycle).
- The queue's [progress](../../concepts/annotations/queues.md#monitoring-progress) and [aggregate scores](../../concepts/annotations/queues.md#aggregate-scores) on its detail page update after each submission, edit and authoritative choice.

## See also

- To analyse the results outside OCS, see [Export Annotations](export-annotations.md).
- To unflag items, change reviewers or edit the queue, see [Manage an Annotation Queue](manage-a-queue.md).
