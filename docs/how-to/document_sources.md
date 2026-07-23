---
title: Set Up Document Sources
---
# Set Up Document Sources

Document sources let OCS automatically fetch and index content from an external system on a schedule. This keeps your indexed collection up to date without manual uploads.

OCS currently supports two document source types: **[GitHub](#github)** and **[Confluence](#confluence)**. Decide which one you need before you start, since the authentication provider and configuration fields differ for each.

For a conceptual overview, see [Indexed Collection for RAG](../concepts/collections/indexed.md#document-sources-for-indexed-collections).

## Prerequisites

- An [indexed collection](../concepts/collections/indexed.md) already created in OCS.
- An [authentication provider](../concepts/team/authentication_providers.md) configured for your chosen source type.

## Add a Document Source

1. Navigate to your indexed collection and open the **Document Sources** tab.
2. Click **Add document source** and select the source type: [GitHub](#github) or [Confluence](#confluence).
3. Complete the configuration fields for your chosen source (see below).
4. Click **Save**.

OCS runs an initial sync immediately and you can [monitor the sync status](#monitoring-sync-status).

---

## Confluence

Load pages from a Confluence site. You can filter which pages are loaded by space, label, CQL query, or individual page IDs.

### Authentication

Use a [Basic Auth](../concepts/team/authentication_providers.md#basic-auth) authentication provider. Set your Atlassian username as the **username** and your Atlassian API key as the **password**.

### Configuration

| Field     | Description                                                               |
|-----------|---------------------------------------------------------------------------|
| Site URL  | The URL of your Confluence site (e.g. `https://yoursite.atlassian.net/wiki`) |
| Max Pages | The maximum number of pages to load                                       |
| Space Key | Load all pages from this space                                            |
| Label     | Load pages that have this label                                           |
| CQL       | A CQL query to select which pages to load                                 |
| Page IDs  | Load only these specific pages (comma-separated IDs)                      |

!!! note
    Only one of **Space Key**, **Label**, **CQL**, and **Page IDs** can be used at a time.

---

## GitHub

Load files from a GitHub repository. You can filter by path prefix or filename patterns.

### Authentication

Use a [Bearer Token](../concepts/team/authentication_providers.md#bearer-token) authentication provider with a GitHub personal access token.

### Configuration

| Field          | Description                                                          |
|----------------|----------------------------------------------------------------------|
| Repository URL | GitHub repository URL (e.g. `https://github.com/user/repo`)          |
| Branch         | Git branch to sync from                                              |
| File Pattern   | File patterns to include. Prefix with `!` to exclude matching files. |
| Path Filter    | Optional path prefix to filter files (e.g. `docs/`)                  |

---

## Monitoring Sync Status

OCS tracks the history of every sync run for each document source. Use the sync logs to confirm that syncs are completing successfully and to diagnose problems when they are not.

Each document source displays a status indicator showing the outcome of the most recent sync:

- **Error** — the last sync failed before it could process any files. The indicator is shown in red. Open the sync log for details.
- **Completed with errors** — the sync finished, but one or more files failed to process. Every other file still synced and is searchable in the collection. Open the sync log to see how many files failed and which ones.
- **Success** — the last sync completed without errors.
- **In progress** — a sync is currently running. The indicator animates to show activity.

While a sync is in progress, the collection's file list updates live, showing a running count of how many files have synced so far. You don't need to wait for the sync to finish or refresh the page to see files as they're added.

## Filtering Synced Files by Metadata

Each file added by a document source carries metadata — for example, the Confluence space or label it came from, or its path in the GitHub repository. On your collection's **Files** tab, you can filter the file list by this metadata to quickly find specific synced content, in addition to the free-text search box.

When building a metadata filter, choose a metadata field, an operator, and a value. The **contains** operator matches when the field's value includes the text you enter — this also works for fields that hold a list of values (such as a list of Confluence labels or tags), matching if any item in the list includes your text. For example, a filter of `tags contains "urgent"` matches any file whose `tags` metadata includes `"urgent"`.

!!! note
    `contains` checks for one value at a time — it does not split a comma-separated value into multiple matches. To match several values, add a separate filter for each one.

## Troubleshooting

### Sync shows Error status

Open the sync log for the failed run. Common causes:

- Authentication credentials have expired or been revoked — update your authentication provider.
- The Confluence space key or GitHub repository URL has changed — update the configuration field.
- The Max Pages limit was reached before all pages were loaded — increase the limit or narrow your filter.

### Sync shows "Completed with errors" status

A single file that fails to process no longer stops the whole sync — the rest of the files still sync and are indexed normally. Open the sync log to see the failed-files count and the details for each failed file (for example, a file type OCS couldn't parse, or a page that couldn't be retrieved). Fix the underlying issue if possible, then trigger a new sync to retry those files.

### Pages are not updating after a sync

Check that the correct Space Key, Label, CQL, or Page IDs are set. Only one filter field can be active at a time — if multiple are filled in, only one will be used.
