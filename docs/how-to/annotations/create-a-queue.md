# Create an Annotation Queue and Add Sessions

This guide shows how to set up an annotation queue and fill it with the sessions you want reviewed.

To understand what queues, schema fields and reviews are before you start, read the [Annotations overview](../../concepts/annotations/index.md) and [Annotation Queues](../../concepts/annotations/queues.md).

## Prerequisites

- Chatbot sessions to review, or a finished [dataset](../evaluations/create-a-dataset.md) with rows linked to sessions.

## Create the Queue

1. In the left sidebar, open **Annotations** and click **Add new**.
2. Enter a **Name** and a **Description**, then set **Num reviews required** (1 to 10), the number of reviews each session needs.
   See [Queue Settings](../../concepts/annotations/queues.md#queue-settings) for when to require more than one.
3. In the **Schema Fields** section, add the fields reviewers will fill in.
   For each field, enter a name, choose a type and set any options.
   Add a description to guide reviewers.
   See [Field Types](../../concepts/annotations/queues.md#field-types) for the available types and options.
4. Arrange the fields in the order you want reviewers to see them.
5. Save the queue.
6. On the queue detail page, click **Manage Assignees**, select the team members who will review the sessions, and click **Save**.
   See [Managing Assignees](../../concepts/annotations/queues.md#managing-assignees) for what happens when a queue has no assignees.

!!! note
    Once a reviewer has submitted an annotation, you can no longer add or remove fields or change their settings.
    You can still change their order and whether they are **Required**.
    See [Field Order](../../concepts/annotations/queues.md#field-order).

## Add Sessions to the Queue

You can add sessions in three ways.
Sessions that are already in the queue are skipped each time.

### Add Sessions from Chatbots

Use this method to pick sessions by filter.

1. On the queue detail page, click **Add Sessions**, then **Import from Chatbots**.
2. Use the filters to narrow the table to the sessions you want.
3. Choose how many sessions to add:
    - **Selected only** (default): add only the sessions whose checkboxes you ticked.
    - **All matching filters**: add every session that matches the current filters.
    - **Sample**: add a random percentage of the sessions that match the current filters.
      Set the percentage with the slider.
4. Click **Add to Queue**.

### Import Sessions from a Dataset

Use this method to review the same sessions you used in an [evaluation dataset](../../concepts/evaluations/dataset.md).

1. On the queue detail page, click **Add Sessions**, then **Import from Dataset**.
2. Select a **Dataset** and click **Import**.

Each session linked to a row in the dataset becomes a queue item.
Dataset rows without a session link, such as rows entered by hand or uploaded from CSV, are ignored.

### Add a Session from Its Detail Page

Use this method to add a single session while you are reading it.

1. Open the session's detail page to view the **Session Transcript** and its details.
2. Click **Add to Queue**.
3. Select one or more queues to add the session to.
   Only queues with the status **Active** are listed.

## Expected Outcome

- The queue appears in the **Annotation Queues** list for you and for each assignee you selected.
- The queue detail page shows the items you added, all with the status **Pending**.
- Assignees can click **Start Annotating**. See [Annotate Queue Items](annotate-items.md).
- To change the queue later, remove sessions or delete it, see [Manage an Annotation Queue](manage-a-queue.md).
