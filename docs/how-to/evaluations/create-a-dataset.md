# Create a Dataset

A dataset is the set of conversations or test cases that an evaluation scores, so its rows decide what your evaluation checks. This guide explains the ways to add rows to a dataset.

Before you start, read [Evaluation Datasets](../../concepts/evaluations/dataset.md) to understand evaluation levels and which creation mode to use.

## Prerequisites

- A team with at least one chatbot.
- Permission to create datasets. Datasets are created from **Evaluations** > **Datasets** in the left navigation.

## Create a dataset

1. Click the **Add new** button to open the create dataset form.
2. Enter a name for the dataset.
3. Choose the **[Evaluation level](../../concepts/evaluations/dataset.md#evaluation-levels)**: **Message level** or **Session level**. You can't change this later, and it decides which creation modes you can use.
4. Choose a **Dataset creation mode** and follow the steps for that mode below.
5. Click **Create Dataset**.

## Dataset creation modes

The modes you can choose depend on the evaluation level you picked in step 3:

- [Clone from sessions](#clone-from-sessions)
- [Import from annotation queue](#import-from-annotation-queue)
- [Create manually](#create-manually) (message level only)
- [Upload CSV file](#upload-csv-file) (message level only)

### Clone from sessions

Cloning turns real past conversations into dataset rows. Use it to test your chatbot against real conversations.

Cloned rows keep a link to their original session. You can use it to open the conversation while reviewing results, or to import the session into an annotation queue.

!!! warning
    Editing a cloned row breaks its link to the original session.

Follow the steps for the evaluation level you chose. For how session data maps to dataset fields, see [Cloning field mappings](../../tech-hub/evaluations/dataset-structure.md#cloning-field-mappings).

=== "Message level"

    Each Human/AI message pair in the chosen sessions becomes one row.

    1. Use the filters to narrow the list of sessions by details like chatbot, date range and version.
    2. Choose which sessions to clone:
        - **Selected only**: clone only the sessions you check in the table.
        - **All matching filters**: clone every session that matches your current filters. There is no limit on how many sessions this can match.

    Every message in the chosen sessions is cloned. To clone only the messages that match your filters, create the dataset first, then [add messages](#add-to-an-existing-dataset) with **Filtered messages only**.

    While the clone runs, a progress bar shows how many sessions have been cloned.

=== "Session level"

    Each chosen session becomes one row.

    1. Use the filters to narrow the list of sessions by details like chatbot, date range and version.
    2. Choose which sessions to clone:
        - **Selected only**: clone only the sessions you check in the table.
        - **All matching filters**: clone every session that matches your current filters. There is no limit on how many sessions this can match.

!!! tip
    To pick sessions that no one has reviewed yet, set the **Annotation Queue** filter to **Not in any queue**.
    This filter is available only if your team has the human annotations feature flag.
    See [Annotation Queues on the Sessions List](../../concepts/sessions.md#annotation-queues-on-the-sessions-list).

### Import from annotation queue

Use this method to score sessions your team has already reviewed in an [annotation queue](../../concepts/annotations/queues.md).

Select an **Annotation queue** that contains sessions. Archived queues are not listed.

All sessions in the queue are added to the dataset, using the same field mapping as cloning:

- For a session-level dataset, each session becomes one row. See [session-level cloning](../../tech-hub/evaluations/dataset-structure.md#session-level-datasets).
- For a message-level dataset, each session's messages become Human/AI message pairs. See [message-level cloning](../../tech-hub/evaluations/dataset-structure.md#message-level-datasets), including how unpaired messages are handled.

Sessions already in the dataset are skipped.

### Create manually

Use this method to write individual test cases by hand for a **message-level** dataset. This is useful for testing specific behaviors or edge cases that have not appeared in real conversations yet.

1. Enter the human message and the AI response. Both are required.
2. Optionally, enter the history: previous turns that provide context for this message pair. Each line must start with `user:` or `assistant:`. See [History Syntax](../../tech-hub/evaluations/dataset-structure.md#history-syntax).
3. Optionally, enter context, [participant data](../../concepts/participant_data.md) or [session state](../../tech-hub/python_node.md#session-state) as JSON.
4. Click **Add Message Pair**.

Repeat for each test case. Pairs you have added are listed below the form, where you can edit or delete them before you create the dataset.

### Upload CSV file

Use this method to bulk-load message pairs from a file for a **message-level** dataset. This is the fastest way to migrate an existing test suite or import data prepared outside OCS.

1. Click **Choose CSV File** and select your file. A preview shows the rows found.
2. Map the **Human Message Column** and the **AI Response Column**. Both are required.
3. Optionally, map columns to **Context Fields**, **Participant Data Fields** and **Session State Fields**.
4. Set up the history in one of two ways:
    - Check **Automatically populate history** if your CSV is a single conversation in chronological order. Each row gets the previous rows as its history.
    - Select a history column, if your CSV has one.

To start again with another file, click **Upload Different File**.

For column naming conventions, dot notation for nested fields, and JSON structure examples, see the [CSV Format](../../tech-hub/evaluations/dataset-structure.md#csv-format) reference.

## Add to an existing dataset

Follow the steps for your dataset's evaluation level.

=== "Message level"

    1. Open the dataset.
    2. Click **Add Messages** and choose **Clone from sessions**, **Upload CSV** or **Add manually**.

    When cloning, you have two options the create form does not offer:

    - **Sample**: add a sample of the matching sessions.
    - **Clone**: when filters are active, choose **All messages** or **Filtered messages only**. **Filtered messages only** clones just the messages that match the filters.

    Click **Add N to dataset** to add the rows. The button shows how many sessions will be added.

=== "Session level"

    1. Open the dataset.
    2. Click **Add Sessions** and choose **Clone sessions** or **Import from annotation queue**.

    When cloning, click **Add N to dataset** to add the rows. The button shows how many sessions will be added.

**Export CSV** downloads the dataset's current rows. The **Download Template** link in the upload section gives you the same file, which you can edit and upload as a starting point.

## Next steps

- Pair the dataset with evaluators and score it.
  See [Run an Evaluation](run-an-evaluation.md).
- To keep a session-level dataset up to date from a live chatbot, see [Set Up a Real-Time LLM-as-a-Judge](realtime_llm_judge.md).
