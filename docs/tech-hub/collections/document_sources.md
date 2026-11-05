---
title: Document Sources Reference
description: Shared sync behavior and troubleshooting for GitHub and Confluence document sources
---
# Document Sources Reference

Sync behavior shared by all [document sources](../../concepts/collections/indexed_collections/document_sources.md), and troubleshooting for GitHub and Confluence sources.
Use it to understand what a sync changes and why a sync fails or files are missing.
To add a source or read its sync log, follow the guide to [set up and manage document sources](../../how-to/collections/document_sources.md).

## Quick reference

| Source | Authentication provider | A file is re-synced when | [Citation](../../concepts/collections/indexed_collections/citations.md) text and link |
|--------|-------------------------|--------------------------|--------------------------------------------------------------------------|
| [GitHub](github_document_source.md) | [Bearer Token](../../concepts/team/authentication_providers.md#bearer-token) | Its content hash (`sha`) changes | File path in the repository, linked to a download copy stored in OCS |
| [Confluence](confluence_document_source.md) | [Basic Auth](../../concepts/team/authentication_providers.md#basic-auth) | The page's last-modified time changes | Page title, linked to the Confluence page |

## Shared behavior

These rules apply to every document source type.
For when syncs start and what they change, see [How syncing works](../../concepts/collections/indexed_collections/document_sources.md#how-syncing-works).

- **One sync at a time.** If a sync is running, a second request is refused with a message.
  A sync that has run for more than two hours is treated as stalled, and the next request replaces it.
- **Removed files.** A sync removes any previously synced file that the source no longer returns.
  This includes a file the source now skips, for example because it became empty, too large, or restricted.
  A file that failed to process is not treated as removed.
- **Chunking.** Synced files use a fixed chunk size and overlap that you can't change per source, in both local and remote indexes.
  See [Chunking and Optimization](local-index-optimization.md#chunking-and-optimization) for the values.
- **File limit.** A sync does not check the collection's 1000-file limit, so it can take a collection past it.
- **Failure details.** The sync log lists at most 50 failed files per sync, followed by a count of the rest.

## Source references

- [GitHub](github_document_source.md): files from a repository on `github.com`.
- [Confluence](confluence_document_source.md): pages from an Atlassian Confluence Cloud site.

## Troubleshooting

### The source shows **Last Sync (with errors)** and the sync log says **Failed**

The sync stopped before it finished.
[Read the sync log](../../how-to/collections/document_sources.md#read-the-sync-log) to see the error message.
Common causes:

- The authentication provider's credentials have expired or been revoked.
  Update the provider.
- The repository URL, branch, space key, or site URL has changed.
  Edit the source.
- GitHub truncated the listing of a very large repository.
  Sync a smaller repository or branch.
- GitHub or Confluence returned a rate limit or server error.
  Wait, then start the sync again.

### The sync log says **Completed with errors**

Some files failed and the rest synced normally.
[Read the sync log](../../how-to/collections/document_sources.md#read-the-sync-log) to see each failed file and the reason, for example a file type OCS can't parse.
Fix the cause, then [retry the failed files](../../how-to/collections/document_sources.md#retry-failed-files).

### Pages or files are missing from the collection

- **Confluence:** the source may have more pages than **Max Pages**.
  Raise the limit or use a narrower **Space Key**, **Label**, or **CQL Query**.
  Also check whether the pages are restricted, archived, or not visible to the authentication provider's account.
- **GitHub:** check that the files match **File Pattern** and **Path Filter**, and that none is empty or over 50 MB.
- Check that the sync log shows the expected **Added** count.

## See also

- [Document Sources](../../concepts/collections/indexed_collections/document_sources.md): the concept and when to use it.
- [Set Up and Manage Document Sources](../../how-to/collections/document_sources.md): add a source and read the sync log.
