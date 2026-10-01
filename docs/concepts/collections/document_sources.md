---
title: Document Sources
---
# Document Sources

Instead of uploading files manually, you can connect OCS to an external document source — such as a Confluence space or GitHub repository — and have it fetch and index content automatically on a schedule. This keeps your OCS [indexed collection](./indexed.md) (for both remote and local indexes) current without manual uploads.

!!! note "Document-source updates reach published chatbots automatically"
    When a document-source sync runs and updates the collection's content, those changes are applied to your published chatbot without requiring a republish. See [Collections and published chatbots](./index.md#collections-and-published-chatbots) for more detail.

Currently supported sources: **Confluence** and **GitHub**.

For configuration steps, authentication setup, and how to monitor sync status, see [Set Up Document Sources](../../how-to/document_sources.md).

If a file fails to sync, the rest of the source's files still sync and remain searchable — only the failed file is skipped. See [Monitoring Sync Status](../../how-to/document_sources.md#monitoring-sync-status) for how to see which files failed and why.
