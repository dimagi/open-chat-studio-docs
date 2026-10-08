---
title: Import CSV/TSV Rows into a Collection
---

# Import CSV/TSV Rows into a Collection

This guide shows you how to import a `.csv` or `.tsv` file into an indexed collection.
Each row becomes its own searchable record.
Regular file upload doesn't accept CSV or TSV files, so row import is how you add them.
Use this when your chatbot needs to look up individual rows, such as matching a participant's input against a product list or reference table.

For a conceptual overview, see [Importing CSV/TSV rows](../concepts/collections/indexed_collections/local_and_remote_indexes.md#importing-csvtsv-rows).

## Prerequisites

- An [indexed collection](../concepts/collections/indexed_collections/index.md) using a **[Local Index](../concepts/collections/indexed_collections/local_and_remote_indexes.md#local-index)**. Remote (OpenAI) indexes don't offer row import.
- A `.csv` or `.tsv` file, within the standard file upload size limit.

## Import a file

1. Open your indexed collection and click **Add Files**.
2. Select **Import CSV/TSV rows**.
3. Choose your `.csv` or `.tsv` file. A preview loads as soon as you choose it.
4. Check the preview. It shows the number of rows found and the first five rows as they will be indexed. If a row is too long, the preview names it and **Import** is disabled.
5. Under **Store as metadata**, tick the columns you want stored with each row. You can tick up to 16.
6. Click **Import** to upload the file and start indexing.

Each row is indexed as one chunk.
The chunk text is the file name followed by one `column: value` line for every column, whether or not you ticked it.

!!! note "Row numbers count from the first data row"
    Row numbers in the preview, the chunks page, and search results count data rows starting at 1.
    "Row 4" is the fifth line of the file once the header row is counted.
    Blank rows are skipped but keep their place in the count, so the numbers can have gaps.

## Viewing imported rows

On the file's chunks page, each imported row appears as its own chunk, showing its row number and the metadata you chose to keep.

When your chatbot searches the collection, each matching row comes back with its row number and the metadata you chose.
The collection's **Index Inspector** page (the search icon) doesn't show the row number or metadata.

## File requirements

- Headers must be unique and non-blank.
- Every row must have the same number of cells as the header row. A row with a different number of cells (a ragged row) is rejected, and its row number is reported.
- The file must have at least one data row.
- UTF-8 is tried first, with or without a byte-order mark. If the file isn't UTF-8, OCS tries to detect its encoding and rejects the file only if detection fails.
- The delimiter for `.csv` files is detected automatically from comma, semicolon, tab and pipe. `.tsv` files must be tab-separated.

## Limits

- A single import can hold up to 10,000 rows.
- Each row can be at most 2,000 tokens once rendered as `column: value` lines.

Both limits are checked when you preview the file, so an oversized row is reported before indexing starts.
Self-hosted operators who need different limits can override the application settings — see [Local Index Optimization](../tech-hub/collections/local-index-optimization.md#csvtsv-row-import-limits).

## Common issues

### Some rows did not import

If some rows in the file fail to embed, the rest of the sheet still indexes.
The failed rows are listed on the file's status tooltip in the collection's file list. A long list is cut short.

The file is still marked **completed** if at least one row indexed, so **Retry Failed Uploads** does not pick it up.
To recover the missing rows, delete the file and import it again.

If every row in a batch fails, the whole file fails and stays retryable, so **Retry Failed Uploads** picks it up as usual.

### The file was rejected before importing

Check the [file requirements](#file-requirements) above.
Common causes are a ragged row, a duplicate or blank header, or an encoding OCS couldn't detect.
For a ragged row, the error message reports its row number.

## See also

- [Indexed Collections](../concepts/collections/indexed_collections/index.md) — how indexed collections work
- [Local and Remote Indexes](../concepts/collections/indexed_collections/local_and_remote_indexes.md) — how local indexes work
- [Local Index Optimization](../tech-hub/collections/local-index-optimization.md) — chunking configuration and row import limits
