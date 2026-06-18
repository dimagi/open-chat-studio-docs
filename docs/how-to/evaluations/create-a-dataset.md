# Create a Dataset

This guide walks you through each method for populating an evaluation dataset. Before you start, read [Evaluation Datasets](../../concepts/evaluations/dataset.md) to understand evaluation levels and when to use each creation method.

## Prerequisites

- A team with at least one chatbot.
- An existing dataset, or permission to create one. Datasets are created from the **Evaluations/Datasets** section in the left navigation.

## Create Dataset

1. Click the **Add new** button to view the Create Dataset view
2. Choose the **Evaluation level** (message-level or session-level) — this cannot be changed later and determines which creation methods/modes are available to you.

---
## The Dataset creation modes

1. [Clone from sessions](#clone-from-sessions)
2. [Import from annotation queue](#import-from-an-annotation-queue)
3. [Create manually](#create-manually)
4. [Upload CSV file](#upload-csv-file)

!!! note

    Open Chat Studio will show you the creation modes you can use based on the Evaluation level you have chosen.

### Clone from Sessions

Cloning turns real past conversations into dataset rows automatically. Use this method when you want to evaluate chatbot behavior against actual user interactions.

Rows created by cloning keep a link back to their original session in OCS. This link lets you navigate directly from a dataset row to the original conversation when reviewing evaluation output. It also makes those sessions eligible for import into an annotation queue for human review. Rows added by manual entry or CSV upload do not have a session link and are not eligible for annotation queue import.

!!! warning

    Modifying or updating a cloned message row will break the link to its original session.

Based on the evaluation level you have chosen, the system will clone either the message pairs (one row per message pair) or the sessions (one row is created per session). For details of the cloning field mappings, see [Tech Hub dataset structure](../../tech-hub/evaluations/dataset-structure.md).

#### Steps for a message-level dataset

1. Name the new dataset
2. Select at least one session, from the list shown, you want to clone from.
3. You can filter the list of sessions by details like: chatbot, date range, version, etc.
4. Click the **View Session** button to see more details to understand if this data is useful or not
5. Choose how much of each session to include:
    - **Filtered messages** — clones only the messages that match the active filter parameters.
    - **All messages** — clones every message in the selected sessions.
6. Click **Create Dataset** to create the dataset rows.

### Steps for a session-level dataset

1. Name the dataset
2. Select the sessions you want to clone from. You don't have to select a session if you want to auto-populate later.
3. You can search and filter by chatbot, date range, tags, or other session attributes.
4. Click **Create Dataset** to create the dataset rows.

---

### Import from an Annotation Queue

Use this method to populate a **session-level** dataset from sessions that have already been curated in an [annotation queue](../../concepts/annotations/queues.md). This is useful when your team has reviewed a set of conversations and you want to run automated scoring against the same set.

1. Select from your existing annotation queues. Archived queues are excluded from the list.
2. Select queue that contains session items.
3. Click **Import**.

Each session item in the queue becomes one row in the dataset, using the same field mapping as [session-level cloning](../../tech-hub/evaluations/dataset-structure.md#session-level-datasets).

Imports are idempotent — sessions already present in the dataset are skipped. You can re-run the import after adding new items to the annotation queue, and only the new sessions will be added.

---

### Create Manually

Use this method to write individual test cases by hand for a **message-level** dataset. This is particularly useful for testing specific behaviors or edge cases that have not appeared in real conversations yet.

1. Open the dataset and select the **Create manually** mode.
2. Enter a **Human Message** (required).
3. Enter an **AI Response** (required).
4. Optionally, enter **History** — previous turns that provide context for this message pair. See [History Syntax](../../tech-hub/evaluations/dataset-structure.md#history-syntax) for the required format.
5. Optionally, add any **Context** key-value pairs.
6. Click **Create Dataset**.

Repeat for each test case you want to add.

---

### Upload CSV file

Use this method to bulk-load message pairs from a file for a **message-level** dataset. This is the fastest way to migrate an existing test suite or import data prepared outside OCS.

1. Open the dataset and click **Browse** to select your CSV file.
2. Map the CSV columns to the dataset fields
3. Choose whether to **auto-generate history** from the CSV rows. Enable this option if your CSV represents a single conversation in chronological order and you want OCS to construct the history column automatically from preceding rows. Leave it disabled if your CSV includes its own history column or the rows do not form a sequential conversation.
4. Click **Create Dataset**.

For column naming conventions, dot-notation for nested fields, and JSON structure examples, see the [CSV Format](../../tech-hub/evaluations/dataset-structure.md#csv-format) reference.
