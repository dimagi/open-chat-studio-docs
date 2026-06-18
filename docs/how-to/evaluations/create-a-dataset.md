# Create a Dataset

This guide walks you through each method for populating an evaluation dataset. Before you start, read [Evaluation Datasets](../../concepts/evaluations/dataset.md) to understand evaluation levels and when to use each creation method.

## Prerequisites

- A team with at least one chatbot.
- An existing dataset, or permission to create one. Datasets are created from the **Evaluations** section in the left navigation.
- When you create a dataset, choose the **Evaluation level** (message-level or session-level) — this cannot be changed later and determines which creation methods are available to you.

!!! note

    If you choose a **message-level** dataset, then manual creation and CSV upload are available. If you choose **session-level**, then the datasets must be populated by cloning sessions, by importing from an annotation queue, or by configuring an [auto-population rule](../../tech-hub/evaluations/auto_population.md).

---

## Clone a Session

Cloning turns real past conversations into dataset rows automatically. Use this method when you want to evaluate chatbot behavior against actual user interactions.

Rows created by cloning keep a link back to their original session in OCS. This link lets you navigate directly from a dataset row to the original conversation when reviewing evaluation output. It also makes those sessions eligible for import into an annotation queue for human review. Rows added by manual entry or CSV upload do not have a session link and are not eligible for annotation queue import.

!!! warning

    Modifying or updating a cloned message row will break the link to its original session.

Based on the evaluation level you have chosen, the system will clone either the message pairs (one row per message pair) or the sessions (one row is created per session). For details of the cloning field mappings see [Tech Hub dataset structure](../../tech-hub/evaluations/dataset-structure.md).

### Clone a Session for a message-level dataset:

1. Open the dataset and click **Add from session**.
2. Select at least one session you want to clone from. 
3. You can search and filter by chatbot, date range, tags, or other session attributes.
4. Choose how much of each session to include:
    - **Multiple sessions** — clones all messages from each selected session.
    - **Filtered messages** — clones only the messages that match the active filter parameters.
    - **All messages** — clones every message in the selected sessions.
5. Click **Clone** to create the dataset rows.

### Clone a Session for a session-level dataset:

1. Open the dataset and click **Add from session**.
2. Select the sessions you want to clone from. You don't have to select a session if you want to auto-populate later.
3. You can search and filter by chatbot, date range, tags, or other session attributes.
4. Choose how much of each session to include:
    - **Multiple sessions** — clones all messages from each selected session.
5. Click **Clone** to create the dataset rows.

---

## Import from an Annotation Queue

Use this method to populate a **session-level** dataset from sessions that have already been curated in an [annotation queue](../../concepts/annotations/queues.md). This is useful when your team has reviewed a set of conversations and you want to run automated scoring against the same set.

1. Open the dataset edit page.
2. Click **Import from Annotation Queue**.
3. Select a team queue that contains session items. Archived queues are excluded from the list.
4. Click **Import**.

Each session item in the queue becomes one row in the dataset, using the same field mapping as [session-level cloning](../../tech-hub/evaluations/dataset-structure.md#session-level-datasets).

Imports are idempotent — sessions already present in the dataset are skipped. You can re-run the import after adding new items to the queue and only the new sessions will be added.

---

## Create Rows Manually

Use this method to write individual test cases by hand for a **message-level** dataset. This is particularly useful for testing specific behaviors or edge cases that have not appeared in real conversations yet.

1. Open the dataset and click **Add message**.
2. Enter a **Human Message** (required).
3. Enter an **AI Response** (required).
4. Optionally, enter **History** — previous turns that provide context for this message pair. See [History Syntax](../../tech-hub/evaluations/dataset-structure.md#history-syntax) for the required format.
5. Optionally, add any **Context** key-value pairs.
6. Click **Save**.

Repeat for each test case you want to add.

---

## Upload a CSV

Use this method to bulk-load message pairs from a file for a **message-level** dataset. This is the fastest way to migrate an existing test suite or import data prepared outside OCS.

1. Open the dataset and click **Upload CSV**.
2. Select your CSV file.
3. Choose whether to **auto-generate history** from the CSV rows. Enable this option if your CSV represents a single conversation in chronological order and you want OCS to construct the history column automatically from preceding rows. Leave it disabled if your CSV includes its own history column or the rows are not a sequential conversation.
4. Click **Upload**.

For column naming conventions, dot-notation for nested fields, and JSON structure examples, see the [CSV Format](../../tech-hub/evaluations/dataset-structure.md#csv-format) reference.
