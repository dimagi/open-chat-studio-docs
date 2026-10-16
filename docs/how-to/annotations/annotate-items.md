# Annotate Queue Items

This guide shows how to work through an annotation queue as a reviewer: submit annotations, edit them, skip items, flag items and resolve items that reviewers disagree on.
To learn what the statuses mean, read [Annotating](../../concepts/annotations/annotating.md).
For the bigger picture, see the [Annotations overview](../../concepts/annotations/index.md).

## Prerequisites

- An annotation queue that contains items. See [Create an Annotation Queue and Add Items](create-a-queue.md).
- Permission to add annotations, and either assignment to the queue or an empty assignee list.
  See [User Groups](../../concepts/team/groups.md).

## Open Your Queue

1. In the left sidebar, open **Annotations**.
2. Click the queue you want to work on.

## Annotate Items

1. On the queue detail page, click **Start Annotating**.
   Items open one at a time, oldest first.
2. Read the session in the left panel.
   It shows the conversation history with roles and timestamps, a **Participant Data** tab and a **Session State** tab.
3. Fill in the annotation form in the right panel.
   The fields appear in the order the queue's author set.
   See [Annotation Schema](../../concepts/annotations/queues.md#annotation-schema) for the field types.
4. Click **Submit**.

The next item opens automatically.
The page shows how many items you have reviewed out of the total in the queue.
When no **Pending** or **In Progress** items are left for you, you return to the queue detail page.

## Edit Your Annotation

1. Open the item you annotated.
2. In the annotations list, click **Edit** next to your annotation.
   The form opens with your previous answers.
3. Change your answers and click **Save**.
   Click **Cancel** to discard your changes.

Saving updates your annotation and recalculates the queue's [aggregate scores](../../concepts/annotations/queues.md#aggregate-scores).

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

The item's status changes to **Flagged** and it no longer appears in the annotation sequence.
The flag is recorded with your name, the time and the reason.
Later flags are added to the list instead of replacing it.

The **Flag** button is on the annotation form, so you can only flag an item you haven't annotated yet.
To return a flagged item to the review workflow, see [Unflag an Item](manage-a-queue.md#unflag-an-item).

## Resolve an Item Awaiting Resolution

On queues that need more than one review, an item with all its reviews is **Awaiting resolution** until someone picks one annotation as the authoritative answer.
See [Resolving Multi-Reviewer Conflicts](../../concepts/annotations/annotating.md#resolving-multi-reviewer-conflicts).

1. On the queue detail page, find an item with the status **Awaiting resolution** in the **Items** table and click **Annotate**.
2. Compare the annotations in the list.
3. Click **Mark authoritative** next to the annotation you agree with.

The item becomes **Completed**, and the chosen annotation shows an **Authoritative** badge.
To choose a different annotation, click **Mark authoritative** on it.
To undo the choice, click **Clear authoritative**.

## Expected Outcome

- Items that have all required reviews become **Completed**, or **Awaiting resolution** on queues that need more than one review.
  See [Item Status Lifecycle](../../concepts/annotations/annotating.md#item-status-lifecycle).
- The queue's progress and [aggregate scores](../../concepts/annotations/queues.md#aggregate-scores) on its detail page update after each submission, edit and authoritative choice.

## See also

To analyse the results outside Open Chat Studio, see [Export Annotations](export-annotations.md).
