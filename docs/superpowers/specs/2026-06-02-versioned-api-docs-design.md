# Versioned API Docs Generation — Design

**Date:** 2026-06-02
**Branch:** sk/versioned-api-docs
**Status:** Approved

## Background

The OCS API is moving to a versioned scheme where `v1` is the current API. Today,
`src/ocs_docs/openapi_to_docs.py` fetches a **single** OpenAPI schema
(`.../main/api-schema.yml`) and emits one minified `.txt` file per tag directly into
`docs/api/`. The `update-api-docs` GitHub workflow runs this daily / on dispatch and
opens a PR.

Two hand-maintained pages live alongside the generated `.txt` files:

- `docs/api/index.md` — version-independent prose (overview, auth, error handling, rate
  limiting) **plus** a hardcoded "LLM Docs" list linking to each `.txt`.
- `docs/api/getting_started_with_oauth.md` — version-independent OAuth guide.

We need the generator (and surrounding workflow + docs structure) to support **multiple
API versions** and to produce a **per-version index page**.

## Goals

- Generate per-version API docs, with `v1` as the first/current version.
- Each version gets its own folder and a generated index page.
- The top-level API index lists the available versions without losing its hand-written
  prose.
- The generation pipeline discovers versions automatically from a directory of schema
  files, so adding `v2` requires no generator code change.

## Non-Goals

- Changing the *content/format* of the per-tag `.txt` LLM docs (kept as-is).
- Auto-editing `mkdocs.yml` nav (generators must not rewrite nav).
- Building a version switcher UI / redirects between versions.
- Defining the upstream OCS schema directory path (parameterized; OCS owns that).

## Key Decisions (resolved during brainstorming)

| Question | Decision |
|----------|----------|
| How are versioned schemas exposed? | One schema file per version, inside a **directory** OCS publishes. |
| How does the generator discover versions? | Iterate `*.yml`/`*.yaml` files in a local schema directory; each file = one version. |
| How does the workflow get that directory? | OCS publishes a schema dir; the workflow lists + downloads it (GitHub contents API). |
| Output layout? | **Subfolder per version** under `docs/api/`. |
| Per-version index content? | Title + per-tag LLM-doc links **plus** an endpoint summary table grouped by tag. |
| Top-level index handling? | Hand-maintained prose; generator injects a versions list **between HTML-comment markers**. |
| Nav? | Unchanged — version indexes reachable via the top-level versions list, not added to nav. |
| Upstream schema dir path? | Not finalized — **parameterized** (`API_SCHEMA_DIR`, default `api-schema/`). |

## Architecture

### Schema discovery — directory mode

`openapi_to_docs.py` gains a directory mode:

- If the input path is a **directory**, iterate its `*.yml`/`*.yaml` files. Each file is
  one API version; the **version label is the filename stem** (`v1.yml` → `v1`).
- Files are processed in a **numeric-aware sorted order** so `v10` sorts after `v2`
  (not lexically before it).
- If the input path is a **single file or URL**, behave exactly as today (single-schema
  mode), for ad-hoc/manual use.

A new orchestration function:

```python
def convert_versioned_docs(schema_dir: str | Path, output_dir: str | Path) -> list[str]:
    """For each schema file in schema_dir, generate docs into output_dir/<version>/,
    then write the per-version index and update the top-level versions list.
    Returns the list of generated file paths."""
```

It reuses the existing `OpenAPIToMarkdownConverter` per version, pointing each at
`output_dir/<version>/`. The existing `convert_openapi_to_markdown` single-schema
function and the converter class are left intact.

### Output layout

```
docs/api/
  index.md                       # hand-maintained prose + marker-injected versions list
  getting_started_with_oauth.md  # hand-maintained, version-independent
  v1/
    index.md                     # GENERATED
    channels.txt                 # GENERATED (one per tag, current format)
    chat.txt
    experiment_sessions.txt
    experiments.txt
    files.txt
    openai.txt
    participants.txt
```

The 7 existing root `.txt` files are **moved into `v1/`**; the stale root copies are
deleted.

### Generated per-version `index.md`

Each `docs/api/<version>/index.md` contains:

1. **Heading** — version label, plus the API `title`, `version`, and `description` from
   the schema `info` block.
2. **LLM Docs list** — a link to each `<tag>.txt` in this version's folder, annotated
   with the tag's description (from the schema `tags` block where available). This
   replaces the role of the old hardcoded list in the top-level index.
3. **Endpoint summary table**, grouped by tag, with columns **Method | Path | Summary**.
   Gives a human-readable overview alongside the link hub.

Links are relative within the version folder (e.g. `./channels.txt`), preserving the
existing `{:target="_blank"}` attribute pattern used today.

### Top-level `index.md` — marker injection

- Add a `## Versions` section bounded by:
  ```
  <!-- api-versions:start -->
  <!-- api-versions:end -->
  ```
- Remove the now-stale hardcoded "LLM Docs" list.
- The generator rewrites **only** the content between the markers — a list linking to
  each `v*/index.md`. All prose outside the markers (overview, auth, errors, rate
  limiting) is untouched.
- If the markers are **absent at runtime**, the generator raises a clear `ValueError`
  explaining that the markers must be present, rather than silently doing nothing.
- Injection is **idempotent** — re-running replaces the block in place rather than
  appending.

### `update-api-docs` workflow

Replace the single-URL fetch step with:

1. **List** the OCS schema directory via the GitHub contents API
   (`https://api.github.com/repos/dimagi/open-chat-studio/contents/${API_SCHEMA_DIR}?ref=main`),
   selecting `*.yml`/`*.yaml` entries.
2. **Download** each file's `download_url` into a temp `schemas/` directory.
3. **Run** the generator against that directory:
   `uv run python src/ocs_docs/openapi_to_docs.py schemas/ -o docs/api/`.

`API_SCHEMA_DIR` is an env var defaulting to `api-schema/`, marked as the single line to
change once OCS finalizes the path. The rest of the workflow (change detection, PR
creation) is unchanged.

### Nav

`mkdocs.yml` nav is unchanged: it keeps pointing at `api/index.md` and
`api/getting_started_with_oauth.md`. Version index pages are reachable from the
top-level versions list — the same way the `.txt` files are reachable today (orphan
markdown pages are logged at INFO by MkDocs/Zensical and do not fail `--strict`).

## Error Handling

- **Missing version markers** in `docs/api/index.md` → `ValueError` with guidance.
- **Empty / no schema files** in the directory → `ValueError` (nothing to generate).
- **Malformed schema file** → existing `_load_schema` error handling applies, surfaced
  per file so a bad `v2.yml` doesn't silently skip.

## Testing

Add `scripts/tests/test_openapi_to_docs.py` (matches the existing `scripts/tests`
convention; importing the converter from `src.ocs_docs.openapi_to_docs`). Using a small
inline OpenAPI schema dict and `tmp_path`:

- **Directory mode** creates `v1/index.md` and the per-tag `.txt` files.
- The per-version `index.md` contains the **endpoint summary table** and **links to the
  tag `.txt` files**.
- **Marker injection** replaces the versions block between markers and is **idempotent**
  across two runs.
- Marker injection **raises** when the markers are absent.

Then verify the strict build:

```bash
uv run pytest scripts/tests
uv run zensical build --clean --strict
```

## Migration Steps (summary)

1. Implement directory mode + `convert_versioned_docs` in `openapi_to_docs.py`.
2. Implement per-version `index.md` generation (links + endpoint table).
3. Implement top-level marker injection.
4. Edit `docs/api/index.md`: drop hardcoded LLM-docs list, add `## Versions` marker block.
5. Regenerate docs into `docs/api/v1/` from the v1 schema and delete the stale root
   `.txt` files (a plain `git mv` is acceptable if regeneration is not yet wired up).
6. Update `.github/workflows/update-api-docs.yml` to list + fetch the schema dir.
7. Add tests; run `pytest` + strict build.
