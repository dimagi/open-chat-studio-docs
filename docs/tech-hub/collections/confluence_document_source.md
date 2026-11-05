---
title: Confluence Document Source Reference
---
# Confluence Document Source Reference

Authentication, configuration fields, and behavior of the Confluence [document source](../../concepts/collections/indexed_collections/document_sources.md).

Loads pages from an Atlassian Confluence site.
OCS indexes each page as text converted from the page's HTML.

## Authentication

Use a [Basic Auth](../../concepts/team/authentication_providers.md#basic-auth) authentication provider.
Enter your Atlassian username as the **username** and an Atlassian API key as the **password**.

## Configuration

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

## Behavior

- Pages with no text are skipped without an error.
- When a space, label, or query matches more pages than **Max Pages**, the sync stops at the limit.
  OCS shows no warning or error, so pages beyond the limit are silently missing.

## Troubleshooting

### Pages are missing from the collection

OCS also skips a page when it:

- is not current, for example an archived or trashed page
- has a read restriction, including one inherited from a parent page
- is forbidden or not found for the credentials (HTTP 403 or 404)

Pages with no text and pages beyond **Max Pages** are left out too, as described under [Behavior](#behavior).
To load pages beyond the limit, raise **Max Pages** or use a narrower **Space Key**, **Label**, or **CQL Query**.

## See also

- [Document Sources Reference](document_sources.md): behavior shared by all sources, and troubleshooting for failed syncs.
- [Set Up and Manage Document Sources](../../how-to/collections/document_sources.md): add a source and read the sync log.
- [Document Sources](../../concepts/collections/indexed_collections/document_sources.md): the concept and when to use it.
