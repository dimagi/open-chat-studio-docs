# Annotate Queue Items

This guide shows how to work through an annotation queue as a reviewer: submit annotations, edit them, skip items and flag items that cannot be annotated. To learn what the statuses mean, read [Annotating](../../concepts/annotations/annotating.md).

## Prerequisites

- An annotation queue that contains items. See [Create an Annotation Queue and Add Items](create-a-queue.md).
- Permission to add annotations, and either assignment to the queue or an empty assignee list. See [User Groups](../../concepts/team/groups.md).

## Open Your Queue

1. In the left sidebar, open **Annotation Queues**.
2. Click the queue you want to work on.

You see the queues you are assigned to. With queue management permissions, you see all team queues. With the **Annotation Reviewer** role, the navigation is limited to annotation pages.

## Annotate Items

1. On the queue detail page, click **Start Annotating**. Items open one at a time, oldest first.
2. Read the item in the left panel. For a session, it shows the conversation history with roles and timestamps, a **Participant Data** tab and a **Session State** tab.
3. Fill in the annotation form in the right panel. The fields appear in the order the queue's author set.
4. Click **Submit**.

The next item opens automatically. The page shows how many items you have reviewed out of the total in the queue.

Each reviewer can submit one annotation per item.

## Edit Your Annotation

1. Open the item you annotated.
2. In the annotations list, click **Edit** next to your annotation. The form opens with your previous answers.
3. Change your answers and click **Save**. Click **Cancel** to discard your changes.

Saving updates your annotation and recalculates the queue's aggregate scores. You cannot edit annotations from other reviewers. If you lack annotation permission, the item opens read-only.

## Skip an Item

Click **Skip** to leave an item for later. Skipped items stay in the queue and come up again after you have been through the other available items.

## Flag an Item

Flag an item when something prevents you from annotating it, such as missing content, a corrupted session, or content that needs an admin to review.

1. Click **Flag** on the annotation form.
2. Enter the reason. It is required.
3. Click **Flag Item**.

The item's status changes to **Flagged** and it no longer appears in your annotation sequence. The reason is recorded with your name and the time, and later flags are added to the list instead of replacing it. A queue manager can unflag the item, which returns it to the review workflow.

## Expected Outcome

- Each submitted item shows your annotation in its annotations list.
- Items that have all required reviews become **Completed**, or **Awaiting resolution** on queues that need more than one review. See [Item Status Lifecycle](../../concepts/annotations/annotating.md#item-status-lifecycle).
- The queue's progress and aggregate scores on its detail page update after each submission.
