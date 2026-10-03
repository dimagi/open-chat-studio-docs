---
title: Document Sources
---
# Document Sources

A document source connects an [indexed collection](./index.md) to an external system, such as a Confluence space or a GitHub repository.
OCS fetches the content from that system and indexes it for you, so you don't upload files by hand.
Document sources work with both [local and remote indexes](./local_and_remote_indexes.md).

## When should I use this?

Use a document source when your content already lives in a system that people keep up to date.

Common examples include:

- A **product documentation** repository on GitHub that your support chatbot should answer from
- A **policy or FAQ space** in Confluence that your HR assistant should search
- Any collection where manual re-uploads would leave the chatbot with outdated answers

If your files rarely change, [upload them directly](../index.md#adding-a-collection-to-a-chatbot) instead.

## Supported sources

- **GitHub**: files from a repository, filtered by branch, folder, and file name pattern.
- **Confluence**: pages from a Confluence site, selected by space, label, query, or page ID.

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
- [Document Sources reference](../../../tech-hub/document_sources.md): configuration fields, authentication, and troubleshooting for each source.
- [Authentication Providers](../../team/authentication_providers.md): the credentials a source uses to connect.
