---
title: GitHub Document Source Reference
---
# GitHub Document Source Reference

Authentication, configuration fields, and behavior of the GitHub [document source](../../concepts/collections/indexed_collections/document_sources.md).
Use it to check why a repository file is or is not synced.

OCS oads files from a repository on `github.com`.

## Authentication

Use a [Bearer Token](../../concepts/team/authentication_providers.md#bearer-token) authentication provider that holds a GitHub personal access token.
The token needs read access to the repository's contents.

## Configuration

| Field | Description |
|-------|-------------|
| **Repository URL** | The repository address, for example `https://github.com/user/repo`. Only `https://github.com` URLs are accepted. |
| **Branch** | The branch to sync from. Defaults to `main`. |
| **File Pattern** | Comma-separated patterns to include, for example `*.md, *.txt`. Prefix a pattern with `!` to exclude matches, for example `!test_*`. Defaults to `*.md`. If you clear the field, no files match. |
| **Path Filter** | An optional path prefix, for example `docs/`. Only files whose full path starts with it are loaded. |

File patterns match against the full path of each file, including folders.

## Behavior

- Files larger than 50 MB (the default maximum file size) are skipped without an error.
- Empty files are skipped without an error.
- If GitHub truncates the file listing for a very large repository, the sync fails and the collection stays as it was.
  Narrowing **Path Filter** doesn't help, because the truncation happens before filtering.
- A network error, rate limit, or server error from GitHub fails the sync instead of skipping a file.
  Existing files are kept.

## See also

- [Document Sources Reference](document_sources.md): behavior shared by all sources, and troubleshooting.
- [Set Up and Manage Document Sources](../../how-to/collections/document_sources.md): add a source and read the sync log.
- [Document Sources](../../concepts/collections/indexed_collections/document_sources.md): the concept and when to use it.
