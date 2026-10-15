---
title: Citations
description: How the Generate Citations setting adds source links to chatbot answers that use indexed collections
---
# Citations

A citation is a link, shown with a chatbot's answer, to a file that the answer came from.
Citations only apply to [indexed collections](./index.md).
They let participants check where an answer came from, and open the source to read more.

## When should I use this?

- A **policy assistant** where staff must confirm the answer against the official policy document
- A **support chatbot** that links participants to the full product documentation page
- A **research tool** where readers need to trace each answer back to the report it came from

Turn citations off when source links would confuse participants or reveal file names you don't want to share.

## Turning citations on or off

Citations are controlled by the **Generate Citations** toggle in the settings of each [LLM node](../../pipelines/nodes.md#llm-node) that uses an indexed collection.
The setting applies to every indexed collection selected on that node.

Turning citations off does not stop the chatbot from searching the collection.
The chatbot still answers from your files, but the answer has no source links.

## What a citation links to

What a participant sees depends on how the file got into the collection.

| How the file was added | Citation text | Citation link |
|------------------------|---------------|---------------|
| Uploaded to the collection | The file name | A download link for the file stored in OCS |
| [GitHub document source](../../../tech-hub/collections/document_sources.md#github) | The file's path in the repository | A download link for the copy stored in OCS |
| [Confluence document source](../../../tech-hub/collections/document_sources.md#confluence) | The page title | The Confluence page |

Uploaded and GitHub files link to the copy stored in OCS, so participants can download them without access to the repository.
Confluence citations link to the original page, so participants need access to that Confluence space to open it.

## See also

- [Indexed Collections](./index.md): what an indexed collection is and how to link it to a chatbot.
- [Document Sources](./document_sources.md): sync files from GitHub or Confluence.
- [Local and Remote Indexes](./local_and_remote_indexes.md): choose where your files are indexed.
