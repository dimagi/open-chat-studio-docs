---
title: Import CSV/TSV Rows into a Collection
---

# Import CSV/TSV Rows into a Collection

This guide shows you how to import a `.csv` or `.tsv` file into an indexed collection.
Each row becomes its own searchable record, instead of the whole file being chunked as plain text.
Use this when your chatbot needs to look up individual rows, such as matching a participant's input against a product list or reference table.

For a conceptual overview, see [Importing CSV/TSV rows](../concepts/collections/indexed.md#importing-csvtsv-rows).

## Prerequisites

- An [indexed collection](../concepts/collections/indexed.md) using a **[Local Index](../concepts/collections/indexed.md#local-index)**. Remote (OpenAI) indexes do their own chunking and do not accept CSV/TSV row import.
- A `.csv` or `.tsv` file, within the standard file upload size limit.

## Import a file

1. Open your indexed collection and click **Add Files**.
2. Select **Import CSV/TSV rows**.
3. Choose your `.csv` or `.tsv` file.
4. In the dialog, tick the columns you want to keep as metadata on each row's record. You can keep up to 16 metadata columns.
5. Review the preview — it shows the detected headers, the number of rows found, and the first five rows rendered as they will be indexed.
6. Click **Import** to upload the file and start indexing.

Each row is indexed as one chunk, rendered as the sheet name followed by `column: value` lines for the metadata columns you chose.

!!! note "Row numbers count from the first data row"
    Row numbers in the preview, the chunks page, and search results count data rows starting at 1.
    "Row 4" is the fifth line of the file once the header row is counted.

## Viewing imported rows

On the file's chunks page, each imported row appears as its own chunk, showing its row number and the metadata you chose to keep.

When your chatbot searches the collection, search results include the row number and the chosen metadata alongside the row's text.
This lets a chatbot answer questions like "find the record like this one" against the sheet.

## File requirements

- Headers must be unique and non-blank.
- Every row must have the same number of cells as the header row. A row with a different number of cells (a ragged row) is rejected, and its row number is reported.
- Files must be UTF-8 encoded. A byte-order mark at the start of the file is handled automatically.
- The delimiter for `.csv` files is detected automatically. `.tsv` files must be tab-separated.

## Limits

- A single import can hold up to 10,000 rows.
- Each row must be under 2,000 tokens once rendered as `column: value` lines.

Both limits are checked when you preview the file, so an oversized row is reported before indexing starts rather than partway through.
Self-hosted operators who need different limits can override the application settings — see [Local Index Optimization](../tech-hub/local-index-optimization.md#csvtsv-row-import-limits).

## Common issues

### Some rows did not import

If some rows in the file fail to embed, the rest of the sheet still indexes.
The failed rows are listed on the file's status tooltip in the collection's file list.

The file is still marked **completed**, since most of its rows indexed successfully, so **Retry Failed Uploads** does not pick it up.
To recover the missing rows, delete the file and import it again.

If every row in a batch fails, the whole file fails and stays retryable, so **Retry Failed Uploads** picks it up as usual.

### The file was rejected before importing

Check the [file requirements](#file-requirements) above.
A common cause is a ragged row, a non-unique or blank header, or a file that isn't UTF-8 encoded.
The error message reports the row number where the problem was found.

## See also

- [Indexed Collection for RAG](../concepts/collections/indexed.md) — how indexed collections and local indexes work
- [Local Index Optimization](../tech-hub/local-index-optimization.md) — chunking configuration and row import limits
