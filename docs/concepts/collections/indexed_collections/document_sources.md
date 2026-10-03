---
title: Document Sources
---
# Document Sources

A document source is a saved set of instructions that tells OCS where to read content from, for example a GitHub or Confluence.
You add one or more document sources to an [indexed collection](./index.md).
OCS reads the matching content, splits it into chunks and indexes it, which is the same processing applied to files you upload yourself.
Document sources work with both [local and remote indexes](./local_and_remote_indexes.md).

## When should I use this?

Use a document source when your content already lives in a system that people keep up to date.

Common examples include:

- A **product documentation** repository on GitHub that your support chatbot should answer from
- A **policy or FAQ space** in Confluence that your HR assistant should search
- Any content that changes often, where manual re-uploads would leave the chatbot giving outdated answers

### Document source or uploading files?

| | Document source | Uploading files to the collection |
|---|---|---|
| Where the content lives | In GitHub or Confluence, where your team edits it | Files you add to the indexed collection yourself |
| Keeping it current | OCS re-syncs it for you, and the chatbot uses the update without a republish | You replace the files by hand |
| Best for | Content that changes often or is owned by other people | Files that rarely change, or that don't exist in GitHub or Confluence |

You can use both in the same indexed collection: its page offers **Add Files** and **Add Document Source**, and both count toward the same file limit.
To upload files, create an indexed collection and use **Add Files**, as described in [adding a collection to a chatbot](../index.md#adding-a-collection-to-a-chatbot).

## Supported sources

- **[GitHub](../../../tech-hub/document_sources.md#github)**: files from a repository, filtered by branch, folder, and file name pattern.
- **[Confluence](../../../tech-hub/document_sources.md#confluence)**: pages from a Confluence site, selected by space, label, query, or page ID.

See the [Document Sources reference](../../../tech-hub/document_sources.md) for what each source needs and how it behaves.

## How syncing works

A *sync* is one run that fetches content from the source and updates the collection.

- OCS starts a sync when you save a new or edited document source.
- You can start a sync at any time from the document source on the collection page.
- If you turn on **Auto Sync**, OCS also syncs the source once a week.
- Each sync adds new files, updates changed files, and removes files that no longer exist in the source.
- If one file can't be processed, only that file is skipped.
  The remaining files still sync and stay searchable.

## Syncs and published chatbots

!!! note "Document-source updates reach published chatbots automatically"
    When a sync updates the collection's content, the changes apply to your published chatbot without a republish.
    See [Collections and published chatbots](../index.md#collections-and-published-chatbots).

[Snapshots](./index.md#snapshots) are different.
A snapshot is a fixed copy of a collection, so syncs never change it.

## See also

- [Set Up and Manage Document Sources](../../../how-to/document_sources.md): add a source, run syncs, and read sync logs.
- [Document Sources reference](../../../tech-hub/document_sources.md): configuration fields, authentication, and troubleshooting for each source type.
