---
title: Set Up and Manage Document Sources
---
# Set Up and Manage Document Sources

Document sources fetch and index content from GitHub or Confluence, so your indexed collection stays current without manual uploads.
This guide covers adding a source, running syncs, and reading the sync status and logs.
For the idea behind document sources, see [Document Sources](../concepts/collections/indexed_collections/document_sources.md).

## Prerequisites

- An [indexed collection](../concepts/collections/indexed_collections/index.md).
  You can't add document sources to a media collection.
- An [authentication provider](../concepts/team/authentication_providers.md) of the type your source needs: Bearer Token for GitHub, Basic Auth for Confluence.
- The details of the source content to load, such as a GitHub repository URL or a Confluence space key.

## Set up a document source

1. Open your indexed collection from **Collections** in the sidebar.
2. Click **Add Document Source** and choose **GitHub Repository** or **Confluence**.
3. In **Auth provider**, choose the authentication provider.
   The list shows only providers of the type this source accepts.
4. Fill in the source fields.
   The [reference](../tech-hub/document_sources.md) describes every field for [GitHub](../tech-hub/document_sources.md#github) and [Confluence](../tech-hub/document_sources.md#confluence).
5. Turn on **Auto Sync** if OCS should also sync the source once a week.
6. Click **Save**.

A sync starts right away.
The source appears above the **Files** list with a status line, and the files appear as they sync.
You don't need to refresh the page.

For example, a support team can add a GitHub source with the file pattern `*.md` and the path filter `docs/`.
The chatbot then answers from the repository's documentation, and each weekly sync picks up edits.

## Manage a document source

Each source has icon buttons beside its name.

| Button | What it does |
|--------|--------------|
| Circular arrows (**Sync Document Source**) | Starts a sync now. It is hidden while a sync is running. |
| Pencil | Opens the source's fields. Saving starts a sync. |
| List (**View Sync Logs**) | Opens the sync log. |
| Trash | Deletes the source and the files it synced, after you confirm. |

### Read the sync status

The line under the source name shows the state of the latest sync:

- **Not yet synced**: no sync has run.
- **Syncing**: a sync is running, with the date of the previous sync.
- **Last Sync**: the last sync finished without errors.
- **Last Sync (with errors)**: the last sync failed, or finished but some files failed.
  The red dot is the same for both, so open the sync log to tell them apart.

While a sync runs, the file list shows how many files have synced so far.

### Read the sync log

1. Click **View Sync Logs** to open the log, newest first.
2. Check each entry's badge: **Success**, **Completed with errors**, **Failed**, or **In Progress**.
3. Check the counts for **Added**, **Updated**, **Removed**, and **Failed** files.
4. Click **View Error** on a failed run, or **View failed files** on a run that completed with errors, to read the details.

Select **Show errors only** to hide everything except failed runs.
Runs that completed with errors stay hidden by that filter.

### Retry failed files

Fix the cause shown in the log, then start another sync.
If files still show a failed status in the file list, click **Retry Failed Uploads** at the top of the collection page.

## Common issues

- **A sync is already in progress.**
  Wait for it to finish, then try again.
- **The sync failed.**
  Check the message in **View Error**, then see [Troubleshooting](../tech-hub/document_sources.md#troubleshooting).
- **Pages are missing from a Confluence source.**
  The source may have reached **Max Pages**.
  See [Troubleshooting](../tech-hub/document_sources.md#troubleshooting).

## See also

- [Document Sources reference](../tech-hub/document_sources.md): fields, authentication, and sync behavior for each source.
- [Authentication Providers](../concepts/team/authentication_providers.md): create the credentials a source needs.
