# Create an Annotation Queue and Add Items

This guide shows how to set up an annotation queue and fill it with the sessions you want reviewed. To understand what queues, schemas and reviews are before you start, read [Annotation Queues](../../concepts/annotations/queues.md).

## Prerequisites

- Permission to manage annotation queues and add items to them. See [User Groups](../../concepts/team/groups.md) for which roles have it.
- At least one chatbot with sessions, if you plan to add sessions from the session selector or from a session page.
- An evaluation dataset whose sessions you want reviewed, if you plan to import from a dataset. The dataset must have finished building and contain rows linked to sessions. See [Create a Dataset](../evaluations/create-a-dataset.md).

## Create the Queue

1. In the left sidebar, open **Annotations** and click **Add new**.
2. Enter a **Name**, a **Description** and **Num reviews required** for each item (1 to 10).
3. Add the fields reviewers will fill in, in the **Schema Fields** section. For each field, enter a name, choose a type and set any options. Add a description to guide reviewers. See [Field Types](../../concepts/annotations/queues.md#field-types) for the available types and options.
4. Arrange the fields in the order you want reviewers to see them.
5. Save the queue.
6. On the queue detail page, click **Manage Assignees**, select the team members who will review items, and click **Save**.

!!! Note
    Once a reviewer has submitted an annotation, you can no longer add or remove fields or change their types. You can still change their order. See [Field Order](../../concepts/annotations/queues.md#field-order).

## Add Items to the Queue

You can add sessions in three ways. Sessions that are already in the queue are skipped each time.

### Add Sessions with the Session Selector from a Chatbot

Use this method to pick sessions by filter.

1. On the queue detail page, click **Add Sessions**, then **Import from Chatbots**.
2. Use the filters to narrow the table to the sessions you want.
3. Choose how many sessions to add:
    - **Selected only** (default): add only the sessions whose checkboxes you ticked.
    - **All matching filters**: add every session that matches the current filters.
    - **Sample**: add a random percentage of the sessions that match the current filters. Set the percentage with the slider.
4. Click **Add to Queue**.

### Import Sessions from a Dataset

Use this method to review the same sessions you used for an automated [evaluation dataset](../../concepts/evaluations/dataset.md).

1. On the queue detail page, click **Add Sessions**, then **Import from Dataset**.
2. Select a **Dataset** and click **Import**.

Each session linked to a row in the dataset becomes a queue item. Dataset rows without a session link, such as rows entered by hand or uploaded from CSV, are ignored.

### Add a Session from Its Detail Page

Use this method to add a single session while you are reading it.

1. Open the session's detail page to view the **Session Transcript** and its details.
2. Click **Add to Queue**.
3. Select the queue, or queues, to add the session to. Only queues with the status **Active** are listed.

## Expected Outcome

- The queue appears in the **Annotation Queues** list for you and for each assignee you selected.
- The queue detail page shows the items you added, all with the status **Pending**.
- Assignees can click **Start Annotating**. See [Annotate Queue Items](annotate-items.md).
