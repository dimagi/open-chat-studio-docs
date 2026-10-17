# Manage an Annotation Queue

This guide shows how to change an annotation queue after you have created it: edit its settings, change its reviewers, unflag items, remove sessions and delete the queue.
To set up a new queue, see [Create an Annotation Queue and Add Sessions](create-a-queue.md).

## Prerequisites

- An annotation queue. See [Create an Annotation Queue and Add Sessions](create-a-queue.md).
- Permission to manage annotation queues. See [User Groups](../../concepts/team/groups.md).
  [Unflag an Item](#unflag-an-item) needs only permission to change queue items, which the **Annotation Reviewer** role has.

## Edit the Queue Settings

1. In the left sidebar, open **Annotations**.
2. In the queue's row, click the edit icon.
3. Change the **Name**, **Description**, **Num reviews required** or schema fields.
4. Click **Update**.

Once a reviewer has submitted an annotation, the schema fields are locked.
You can still reorder fields and change whether each field is **Required**, but you can't add or remove fields or change any other field setting.
See [Field Order](../../concepts/annotations/queues.md#field-order).

If you change **Num reviews required** after reviews have started, a confirmation dialog warns that some completed items may reopen.
See [Changing Reviews Required After Annotation Starts](../../concepts/annotations/queues.md#changing-reviews-required-after-annotation-starts).

## Change the Reviewers

1. On the queue detail page, click **Manage Assignees**.
2. Select or clear team members.
3. Click **Save**.

See [Managing Assignees](../../concepts/annotations/queues.md#managing-assignees) for what happens when a queue has no assignees.

## Unflag an Item

Unflag an item once the problem that stopped reviewers from annotating it is fixed, or when it was flagged by mistake.

1. On the queue detail page, find the item in the **Items** table.
   To see who flagged it and why, hover over its **Flagged** badge.
2. Click **unflag** next to the badge.

The item's status is recalculated from the reviews it already has.
An item with no reviews becomes **Pending** and returns to the annotation sequence.
See [Item Status Lifecycle](../../concepts/annotations/annotating.md#item-status-lifecycle).

!!! warning "Unflagging deletes the flag history"
    Unflagging removes every flag entry on the item, including the reasons.
    The entries no longer appear in the items table or in [exports](export-annotations.md).
    To keep a record of them, export the queue before you unflag.

## Remove a Session

Remove a session when it doesn't belong in the queue, for example one that was added by mistake.

1. On the queue detail page, find the session in the **Items** table.
2. Click the trash icon in its row.
   A dialog lists the annotations and flags that will be deleted.
3. Click **Remove**.

Removing a session from the queue permanently deletes all its annotations.
The session itself is not changed.
If you add the session to the queue again, it returns as a new **Pending** item with no annotations.

## Delete a Queue

!!! danger "Deleting a queue is immediate"
    Open Chat Studio does not ask you to confirm before it deletes a queue, and you can't undo it.
    To keep the results, [export the annotations](export-annotations.md) first.

1. In the left sidebar, open **Annotations**.
2. In the queue's row, click the trash icon.

Deleting a queue permanently deletes its items, every annotation in it and its aggregate scores.
The sessions themselves are not changed.

## Expected Outcome

- Changes to the queue's settings and reviewers appear on its detail page.
- Unflagged items show their recalculated status in the **Items** table.
- Removed sessions no longer appear in the queue, and deleted queues are gone.
- The annotations of removed sessions and deleted queues are deleted with them.
