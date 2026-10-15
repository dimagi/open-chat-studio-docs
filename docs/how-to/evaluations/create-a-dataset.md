# Create a Dataset

This guide shows you each way to add rows to an evaluation dataset. A dataset is the set of conversations or test cases that an evaluation scores, so its rows decide what your evaluation checks. Before you start, read [Evaluation Datasets](../../concepts/evaluations/dataset.md) to understand evaluation levels and when to use each creation method.

## Prerequisites

- A team with at least one chatbot.
- Permission to create datasets. Datasets are created from the **Evaluations/Datasets** section in the left navigation.

## Create dataset

1. Click the **Add new** button to open the create dataset form.
2. Enter a name for the dataset.
3. Choose the **Evaluation level**: **Message level** or **Session level**. This cannot be changed later and determines which creation modes are available.
4. Choose a **Dataset creation mode** and follow the steps for that mode below.
5. Click **Create Dataset**.

---

## The dataset creation modes

- [Clone from sessions](#clone-from-sessions)
- [Import from annotation queue](#import-from-annotation-queue)
- [Create manually](#create-manually)
- [Upload CSV file](#upload-csv-file)

The form shows only the modes available for the evaluation level you chose. See [How datasets are created](../../concepts/evaluations/dataset.md#how-datasets-are-created) for which modes work at each level.

### Clone from sessions

Cloning turns real past conversations into dataset rows. Use this method when you want to evaluate chatbot behavior against actual participant interactions.

Rows created by cloning keep a link back to their original session in OCS. This link lets you go from a dataset row to the original conversation when reviewing evaluation output. It also makes those sessions eligible for import into an annotation queue for human review. Rows added by manual entry or CSV upload do not have a session link and are not eligible for annotation queue import.

!!! warning

    Modifying or updating a cloned message row will break the link to its original session.

A message-level dataset gets one row per message pair. A session-level dataset gets one row per session. For details of the cloning field mappings, see [Tech Hub dataset structure](../../tech-hub/evaluations/dataset-structure.md#cloning-field-mappings).

1. Use the filters to narrow the list of sessions by details like chatbot, date range and version.
2. Choose which sessions to clone:
    - **Selected only**: clone only the sessions you check in the table.
    - **All matching filters**: clone every session that matches your current filters, without checking them one by one.

    !!! warning
        Message-level datasets support up to 1000 sessions when using **All matching filters**. If your filters match more sessions than that, narrow them before creating the dataset. The page warns you when the limit is exceeded.

Every message in the chosen sessions is cloned. To clone only the messages that match your filters, create the dataset first, then [add messages](#add-to-an-existing-dataset) with **Filtered messages only**.

---

### Import from annotation queue

Use this method to populate a dataset from sessions that have already been curated in an [annotation queue](../../concepts/annotations/queues.md). This is useful when your team has reviewed a set of conversations and you want to run automated scoring against the same set.

1. Select an **Annotation queue** that contains sessions. Archived queues are not listed.

All sessions in the queue are added to the dataset. For a session-level dataset, each session becomes one row, using the same field mapping as [session-level cloning](../../tech-hub/evaluations/dataset-structure.md#session-level-datasets). For a message-level dataset, the sessions' messages are cloned as message pairs.

Sessions already in the dataset are skipped.

---

### Create manually

Use this method to write individual test cases by hand for a **message-level** dataset. This is useful for testing specific behaviors or edge cases that have not appeared in real conversations yet.

1. Enter the human message and the AI response. Both are required.
2. Optionally, enter the history: previous turns that provide context for this message pair. Each line must start with `user:` or `assistant:`. See [History Syntax](../../tech-hub/evaluations/dataset-structure.md#history-syntax).
3. Optionally, enter context, [participant data](../../concepts/participant_data.md) or [session state](../../tech-hub/python_node.md#session-state) as JSON.
4. Click **Add Message Pair**.

Repeat for each test case. Pairs you have added are listed below the form, where you can edit or delete them before you create the dataset.

---

### Upload CSV file

Use this method to bulk-load message pairs from a file for a **message-level** dataset. This is the fastest way to migrate an existing test suite or import data prepared outside OCS.

1. Click **Choose CSV File** and select your file. A preview shows the rows found.
2. Map the **Human Message Column** and the **AI Response Column**. Both are required.
3. Optionally, map columns to **Context Fields**, **Participant Data Fields** and **Session State Fields**.
4. Set up the history in one of two ways:
    - Check **Automatically populate history** if your CSV is a single conversation in chronological order. Each row gets the previous rows as its history.
    - Or select a history column from your CSV.

To start again with another file, click **Upload Different File**.

For column naming conventions, dot-notation for nested fields, and JSON structure examples, see the [CSV Format](../../tech-hub/evaluations/dataset-structure.md#csv-format) reference.

## Add to an existing dataset

1. Open the dataset.
2. Click **Add Messages** (message-level) or **Add Sessions** (session-level) and choose a method:

| Option | Message level | Session level |
|--------|---------------|---------------|
| **Clone from sessions** / **Clone sessions** | Yes | Yes |
| **Import from annotation queue** | No | Yes |
| **Upload CSV** | Yes | No |
| **Add manually** | Yes | No |

When cloning into an existing dataset, you have two options the create form does not offer:

- **Sample**: add a sample of the matching sessions. Message-level only.
- **Clone**: when filters are active on a message-level dataset, choose **All messages** or **Filtered messages only**. **Filtered messages only** clones just the messages that match the filters.

Click **Add N to dataset** to add the rows. The button shows how many sessions will be added.

**Export CSV** downloads the dataset's current rows. The **Download Template** link in the upload section gives you the same file, which you can edit and upload as a starting point.

## Next steps

- Pair the dataset with evaluators and score it. See [Run an Evaluation](run-an-evaluation.md).
