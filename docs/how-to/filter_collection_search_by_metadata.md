---
title: Filter Collection Search by Metadata
---
# Filter Collection Search by Metadata

Metadata filters limit an LLM node's collection search to rows whose metadata matches values you set.
Use them when several chatbots share one [indexed collection](../concepts/collections/indexed_collections/index.md) and each chatbot should see only its own content.

## Prerequisites

- An [indexed collection](../concepts/collections/indexed_collections/index.md) with a [local index](../concepts/collections/indexed_collections/local_and_remote_indexes.md#local-index).
  Remote (OpenAI-hosted) indexes ignore metadata filters.
- Rows that carry metadata. Rows imported from a CSV or TSV file carry the columns you chose to store as metadata.
- A chatbot with an [LLM node](../concepts/pipelines/nodes.md#llm-node) that is linked to the collection.

## Add metadata filters

1. Open the chatbot and select the LLM node.
2. In the node's collection settings, select the indexed collection.
   The **Metadata Filters** setting appears after you select the collection.
3. Add a filter.
   Enter the metadata name in the key field and the value to match in the value field.
4. Add more filters if needed.
5. Save the chatbot.

Each key must be unique and not blank.
OCS rejects blank and duplicate keys when you save.

## Example

A team imports one sheet with the metadata column `district` and rows for several districts.
The team runs one chatbot per district.
For the Khayelitsha chatbot, you add one filter with the key `district` and the value `Khayelitsha`.
The chatbot's search returns only rows whose `district` metadata is `Khayelitsha`.

## Expected outcome

- A row is returned only if its metadata matches **every** filter.
- Matching is exact and case-sensitive.
  `Khayelitsha` does not match `khayelitsha`.
- If no row matches, the search tool tells the model which filters it applied.
  The model can then tell the participant that nothing matched instead of guessing.

## Common issues

- **No results are returned.**
  Check that the key and value match the metadata exactly, including capitalization.
- **The setting is not visible.**
  Select an indexed collection on the node first.
- **Filters have no effect.**
  The collection uses a remote index, which ignores filters.
  Use a local index instead.
- **Results differ from an unfiltered search.**
  Filtered searches match on words only and do not search by meaning.
  See [Metadata Filters Reference](../tech-hub/collections/metadata-filters.md#how-filtered-search-works).
