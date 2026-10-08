---
title: Metadata Filters Reference
---
# Metadata Filters Reference

This page describes how the **Metadata Filters** setting of the LLM node changes collection search.
For setup steps, see [Filter Collection Search by Metadata](../../how-to/filter_collection_search_by_metadata.md).

## Settings

The **Metadata Filters** setting appears on the [LLM node](../../concepts/pipelines/nodes.md#llm-node) after you select an indexed collection.
Each filter has a key and a value, for example `district` = `Khayelitsha`.

| Rule | Behavior |
|---|---|
| Keys | Must not be blank or duplicated. OCS rejects the node otherwise. |
| Matching | A row or chunk must match every filter. |
| Case | Exact and case-sensitive. |
| Remote indexes | Ignore the setting. |

## How filtered search works

When at least one filter is set, the search differs from an unfiltered search:

- **Lexical search only.**
  The search uses full-text matching.
  OCS does not embed the query and does not combine vector and lexical results, whatever the hybrid search setting is.
- **Any query word matches.**
  A row matches if it contains at least one word of the query.
  An unfiltered search does not work this way.
- **Words split on punctuation.**
  OCS splits the query into words at punctuation.
- **Queries without searchable words.**
  If the query is empty, contains only punctuation, or contains only stopwords, the search returns the first matching rows in index order.
- **Reranking still runs.**
  OCS reranks the filtered results.

## When no row matches

The search tool tells the model which filters it applied.
The model can report that no matching content exists for those filters.

## See also

- [Indexed Collections](../../concepts/collections/indexed_collections/index.md)
- [Local Index Optimization](local-index-optimization.md)
