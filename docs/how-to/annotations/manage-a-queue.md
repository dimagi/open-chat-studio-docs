# Manage an Annotation Queue

This guide covers what to know before you edit a queue, unflag an item, remove a session or delete a queue.
To set up a new queue, see [Create an Annotation Queue and Add Sessions](create-a-queue.md).

## Edit the Queue Settings

In the left sidebar, open **Annotations** and click the edit icon in the queue's row.

Once a reviewer has submitted an annotation, the schema fields are locked.
See [Field Order](../../concepts/annotations/queues.md#field-order) for which changes are still allowed.

### Change Num Reviews Required

You can change **Num reviews required** after annotation has started.
OCS recomputes the status of every item that is not **Flagged** when you save.
If reviews have already been submitted, a confirmation dialog warns that some completed items may reopen.

- **Raising the number:** items that were **Completed** move back to **In Progress** or **Awaiting resolution** if they no longer have enough reviews.
- **Lowering the number:** items that now have enough reviews move to **Awaiting resolution**, or to **Completed** if they have a single review.
  Items with two or more reviews stay **Awaiting resolution** until a reviewer [picks an authoritative annotation](../../concepts/annotations/annotating.md#resolving-multi-reviewer-conflicts).
- **Going from 1 to more than 1:** authoritative annotations that OCS set automatically are cleared.
  Annotations that a reviewer marked authoritative are kept.
  Aggregate scores are refreshed.
- **Flagged items:** not affected. They stay **Flagged** until someone unflags them.

## Unflag an Item

In the **Items** table, hover over the **Flagged** badge to see who flagged the item and why, then click **unflag**.

The item's status is recalculated from the reviews it already has, so an item with reviews does not necessarily return to **Pending**.
See [Item Status Lifecycle](../../concepts/annotations/annotating.md#item-status-lifecycle).

!!! warning "Unflagging deletes the flag history"
    Unflagging deletes all the item's flag entries, including the reasons.
    The entries no longer appear in the items table or in [exports](export-annotations.md).
    To keep a record of them, export the queue before you unflag.

## Remove a Session

Click the trash icon in the session's row in the **Items** table.
A dialog lists the annotations and flags that will be deleted.

Removing a session permanently deletes all its annotations.
The session itself is not changed.
If you add the session to the queue again, it returns as a new **Pending** item with no annotations.

## Delete a Queue

Click the trash icon in the queue's row on the **Annotations** page.

!!! danger "Deleting a queue is immediate"
    Open Chat Studio does not ask you to confirm before it deletes a queue, and you can't undo it.
    To keep the results, [export the annotations](export-annotations.md) first.

Deleting a queue permanently deletes its items, every annotation in it and its aggregate scores.
The sessions themselves are not changed.
