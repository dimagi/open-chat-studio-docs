---
title: Document Sources Reference
description: Configuration, authentication, sync behavior, and troubleshooting for GitHub and Confluence document sources
---
# Document Sources Reference

Fields, authentication, sync behavior, and troubleshooting for GitHub and Confluence [document sources](../../concepts/collections/indexed_collections/document_sources.md).
To add a source or read its sync log, follow the guide to [set up and manage document sources](../../how-to/document_sources.md).

## Quick reference

| Source | Authentication provider | A file is re-synced when | Source link shown with answers |
|--------|-------------------------|--------------------------|----------|
| [GitHub](#github) | [Bearer Token](../../concepts/team/authentication_providers.md#bearer-token) | Its commit hash (`sha`) changes | Link to the file in the repository |
| [Confluence](#confluence) | [Basic Auth](../../concepts/team/authentication_providers.md#basic-auth) | The page's last-modified time changes | Page title, linked to the page |

## Shared behavior

These rules apply to every document source type.
For when syncs start and what they change, see [How syncing works](../../concepts/collections/indexed_collections/document_sources.md#how-syncing-works).

- **One sync at a time.** If a sync is running, a second request is refused with a message.
  A sync that has run for more than two hours is treated as stalled, and the next request replaces it.
- **Removed files.** A file that failed to process is not treated as removed.
- **Chunking.** Synced files use a fixed chunk size and overlap that you can't change per source.
  See [Chunking and Optimization](local-index-optimization.md#chunking-and-optimization) for the values.
- **File limit.** The collection page shows a limit of 1000 files and disables **Add Files** and **Add Document Source** when it is reached.
  A sync does not stop at this limit.
- **Failure details.** The sync log lists at most 50 failed files per sync, followed by a count of the rest.

## GitHub

Loads files from a repository on `github.com`.

### Authentication

Use a [Bearer Token](../../concepts/team/authentication_providers.md#bearer-token) authentication provider that holds a GitHub personal access token.
The token needs read access to the repository's contents.

### Configuration

| Field | Description |
|-------|-------------|
| **Repository URL** | The repository address, for example `https://github.com/user/repo`. Only `https://github.com` URLs are accepted. |
| **Branch** | The branch to sync from. Defaults to `main`. |
| **File Pattern** | Comma-separated patterns to include, for example `*.md, *.txt`. Prefix a pattern with `!` to exclude matches, for example `!test_*`. Defaults to `*.md`. |
| **Path Filter** | An optional path prefix, for example `docs/`. Only files whose full path starts with it are loaded. |

File patterns match against the full path of each file, including folders.

### Behavior

- Files larger than 50 MB (the default maximum file size) are skipped without an error.
- Empty files are skipped without an error.
- If GitHub truncates the file listing for a very large repository, the sync fails and the collection stays as it was.
  Narrowing **Path Filter** doesn't help, because the truncation happens before filtering.
- A network error, rate limit, or server error from GitHub fails the sync instead of skipping a file.
  Existing files are kept.

## Confluence

Loads pages from an Atlassian Confluence site.
OCS indexes each page as text converted from the page's HTML.

### Authentication

Use a [Basic Auth](../../concepts/team/authentication_providers.md#basic-auth) authentication provider.
Enter your Atlassian username as the **username** and an Atlassian API key as the **password**.

### Configuration

| Field | Description |
|-------|-------------|
| **Confluence Site URL** | The site address, for example `https://yoursite.atlassian.net/wiki`. |
| **Space Key** | Load all pages from this Confluence space. |
| **Label** | Load pages that have this label. |
| **CQL Query** | Load pages that match this Confluence Query Language query. |
| **Page IDs** | Load only these pages. Enter comma-separated numeric IDs. |
| **Max Pages** | The most pages a sync loads. Accepts 1 to 10000. Defaults to 1000. |

Fill in exactly one of **Space Key**, **Label**, **CQL Query**, and **Page IDs**.
OCS refuses to save the source if none or more than one is filled in.

### Behavior

- Pages with no text are skipped without an error.
- When a space, label, or query matches more pages than **Max Pages**, the sync stops at the limit.
  OCS shows no warning or error, so pages beyond the limit are silently missing.

## Troubleshooting

### The source shows "Last Sync (with errors)" and the sync log says Failed

The sync stopped before it finished.
[Read the sync log](../../how-to/document_sources.md#read-the-sync-log) to see the error message.
Common causes:

- The authentication provider's credentials have expired or been revoked.
  Update the provider.
- The repository URL, branch, space key, or site URL has changed.
  Edit the source.
- GitHub truncated the listing of a very large repository.
  Sync a smaller repository or branch.
- GitHub or Confluence returned a rate limit or server error.
  Wait, then start the sync again.

### The sync log says "Completed with errors"

Some files failed and the rest synced normally.
[Read the sync log](../../how-to/document_sources.md#read-the-sync-log) to see each failed file and the reason, for example a file type OCS can't parse.
Fix the cause, then [retry the failed files](../../how-to/document_sources.md#retry-failed-files).

### Pages or files are missing from the collection

- **Confluence:** the source may have more pages than **Max Pages**.
  Raise the limit or use a narrower **Space Key**, **Label**, or **CQL Query**.
- **GitHub:** check that the files match **File Pattern** and **Path Filter**, and that none is empty or over 50 MB.
- Check that the sync log shows the expected **Added** count.

## See also

- [Document Sources](../../concepts/collections/indexed_collections/document_sources.md): the concept and when to use it.
- [Set Up and Manage Document Sources](../../how-to/document_sources.md): add a source and read the sync log.
