# Versioned API Docs Generation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `openapi_to_docs.py` generate per-version API docs (one folder per version) with a generated index page per version, and inject a versions list into the hand-maintained top-level `docs/api/index.md`.

**Architecture:** Add a "directory mode" to the generator: given a directory of OpenAPI schema files (one per version, e.g. `v1.yml`), iterate them, reuse the existing `OpenAPIToMarkdownConverter` to write each version's per-tag `.txt` files into `docs/api/<version>/`, generate a per-version `index.md` (links + endpoint summary table), and inject a versions list between HTML-comment markers in the top-level index. The `update-api-docs` workflow fetches the schema directory from OCS via the GitHub contents API.

**Tech Stack:** Python 3.13, `uv`, `pytest`, `requests`, `pyyaml`, Zensical (MkDocs-compatible), GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-06-02-versioned-api-docs-design.md`

---

## File Structure

- `src/ocs_docs/openapi_to_docs.py` — **Modify.** Add module-level helpers for version discovery, per-version index generation, and top-level marker injection; add `convert_versioned_docs()`; extend the `__main__` CLI to detect directory input. The existing `OpenAPIToMarkdownConverter` class and `convert_openapi_to_markdown()` stay intact and are reused per version.
- `scripts/tests/test_openapi_to_docs.py` — **Create.** Unit tests for directory mode, per-version index content, and marker injection (including the missing-markers error and idempotency).
- `docs/api/index.md` — **Modify.** Remove the hardcoded "LLM Docs" list (lines 55-66); add a `## Versions` section bounded by `<!-- api-versions:start -->` / `<!-- api-versions:end -->`.
- `docs/api/v1/*.txt` — **Create (git mv).** The 7 existing root `.txt` files move into `v1/`.
- `docs/api/*.txt` (root) — **Delete.** Stale root copies removed by the `git mv`.
- `docs/api/v1/index.md` — **Create (generated).** Produced by running the generator; committed.
- `.github/workflows/update-api-docs.yml` — **Modify.** List + download the OCS schema directory into a temp dir, then run the generator against that dir.

---

## Task 1: Version discovery (directory mode helper)

**Files:**
- Modify: `src/ocs_docs/openapi_to_docs.py` (add module-level helpers after the constants block, ~line 22)
- Test: `scripts/tests/test_openapi_to_docs.py`

- [ ] **Step 1: Write the failing test**

Create `scripts/tests/test_openapi_to_docs.py`:

```python
"""Tests for the OpenAPI-to-markdown versioned docs generator."""

from pathlib import Path

import pytest

from src.ocs_docs.openapi_to_docs import (
    discover_version_schemas,
)


def _write(path: Path, text: str = "openapi: 3.0.0\ninfo:\n  title: T\n  version: '1'\npaths: {}\n"):
    path.write_text(text, encoding="utf-8")


def test_discover_version_schemas_sorts_numerically(tmp_path):
    # Created out of order and including a non-schema file
    _write(tmp_path / "v2.yml")
    _write(tmp_path / "v10.yaml")
    _write(tmp_path / "v1.yml")
    (tmp_path / "README.md").write_text("ignore me", encoding="utf-8")

    result = discover_version_schemas(tmp_path)

    assert [version for version, _ in result] == ["v1", "v2", "v10"]
    assert all(isinstance(path, Path) for _, path in result)


def test_discover_version_schemas_empty_dir_raises(tmp_path):
    with pytest.raises(ValueError, match="No schema files"):
        discover_version_schemas(tmp_path)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py -v`
Expected: FAIL with `ImportError` / `cannot import name 'discover_version_schemas'`.

- [ ] **Step 3: Write minimal implementation**

In `src/ocs_docs/openapi_to_docs.py`, add after the constants block (after line 21):

```python
def _natural_sort_key(version: str) -> tuple[int | str, ...]:
    """Split a version label into text/number chunks so 'v10' sorts after 'v2'."""
    return tuple(int(chunk) if chunk.isdigit() else chunk for chunk in re.split(r"(\d+)", version))


def discover_version_schemas(schema_dir: str | Path) -> list[tuple[str, Path]]:
    """Find per-version schema files in a directory.

    Each YAML file is one API version; the version label is the filename stem
    (``v1.yml`` -> ``v1``). Returned in numeric-aware sorted order.

    Returns:
        List of (version_label, schema_path) tuples.

    Raises:
        ValueError: if the directory contains no YAML schema files.
    """
    directory = Path(schema_dir)
    schema_files = sorted(
        (p for p in directory.iterdir() if p.suffix.lower() in YAML_EXTENSIONS),
        key=lambda p: _natural_sort_key(p.stem),
    )
    if not schema_files:
        raise ValueError(f"No schema files (*.yaml/*.yml) found in directory: {directory}")
    return [(p.stem, p) for p in schema_files]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py -v`
Expected: PASS (both tests).

- [ ] **Step 5: Commit**

```bash
git add src/ocs_docs/openapi_to_docs.py scripts/tests/test_openapi_to_docs.py
git commit -m "feat: discover per-version OpenAPI schema files in a directory"
```

---

## Task 2: Per-version index page generation

**Files:**
- Modify: `src/ocs_docs/openapi_to_docs.py` (add a method to `OpenAPIToMarkdownConverter`)
- Test: `scripts/tests/test_openapi_to_docs.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/tests/test_openapi_to_docs.py`:

```python
from src.ocs_docs.openapi_to_docs import OpenAPIToMarkdownConverter

SAMPLE_SCHEMA = {
    "openapi": "3.0.0",
    "info": {"title": "Dimagi Chatbots", "version": "1", "description": "Experiments with LLMs"},
    "tags": [{"name": "Channels", "description": "Manage channels"}],
    "paths": {
        "/api/channels/": {
            "get": {"tags": ["Channels"], "summary": "List channels", "responses": {"200": {"description": "ok"}}},
            "post": {"tags": ["Channels"], "summary": "Create channel", "responses": {"201": {"description": "made"}}},
        }
    },
}


def test_generate_version_index_has_links_and_table():
    converter = OpenAPIToMarkdownConverter(SAMPLE_SCHEMA)

    index_md = converter.generate_version_index("v1")

    # Heading + API info
    assert "# v1" in index_md
    assert "Dimagi Chatbots" in index_md
    # LLM-doc link to the tag .txt file (relative, new-tab attribute preserved)
    assert "[Channels](./channels.txt){:target=\"_blank\"}" in index_md
    assert "Manage channels" in index_md
    # Endpoint summary table: header + both endpoints
    assert "| Method | Path | Summary |" in index_md
    assert "| GET | `/api/channels/` | List channels |" in index_md
    assert "| POST | `/api/channels/` | Create channel |" in index_md
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py::test_generate_version_index_has_links_and_table -v`
Expected: FAIL with `AttributeError: 'OpenAPIToMarkdownConverter' object has no attribute 'generate_version_index'`.

- [ ] **Step 3: Write minimal implementation**

Add this method to `OpenAPIToMarkdownConverter` (e.g. after `convert_to_text_files`, ~line 119):

```python
    def generate_version_index(self, version: str) -> str:
        """Generate the markdown index page for a single API version.

        Includes the API title/version/description, a per-tag list linking to each
        tag's ``.txt`` LLM doc, and an endpoint summary table grouped by tag.
        """
        tag_groups = self._group_endpoints_by_tag()

        lines = [
            f"# {version}",
            "",
            f"**{self.base_info['title']}** API version `{self.base_info['version']}`.",
            "",
        ]
        if self.base_info.get("description"):
            lines += [self.base_info["description"], ""]

        # LLM-doc links per tag
        lines += ["## LLM Docs", "", "Simplified per-tag references for LLM consumption:", ""]
        for tag in sorted(tag_groups):
            filename = self._generate_tag_filename(tag)
            tag_info = self._get_tag_info(tag) or {}
            suffix = f" — {tag_info['description']}" if tag_info.get("description") else ""
            lines.append(f"* [{tag}](./{filename}.txt){{:target=\"_blank\"}}{suffix}")
        lines.append("")

        # Endpoint summary table grouped by tag
        lines += ["## Endpoints", ""]
        for tag in sorted(tag_groups):
            lines += [f"### {tag}", "", "| Method | Path | Summary |", "| --- | --- | --- |"]
            for endpoint in tag_groups[tag]:
                method = endpoint["method"].upper()
                path = endpoint["path"]
                summary = endpoint["operation"].get("summary", "")
                lines.append(f"| {method} | `{path}` | {summary} |")
            lines.append("")

        return "\n".join(lines)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py::test_generate_version_index_has_links_and_table -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ocs_docs/openapi_to_docs.py scripts/tests/test_openapi_to_docs.py
git commit -m "feat: generate per-version API index page with links and endpoint table"
```

---

## Task 3: Top-level index versions-list marker injection

**Files:**
- Modify: `src/ocs_docs/openapi_to_docs.py` (add module-level function)
- Test: `scripts/tests/test_openapi_to_docs.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/tests/test_openapi_to_docs.py`:

```python
from src.ocs_docs.openapi_to_docs import inject_versions_list

INDEX_WITH_MARKERS = """# API

Some hand-written prose about auth.

## Versions

<!-- api-versions:start -->
old content to be replaced
<!-- api-versions:end -->

More prose after.
"""


def test_inject_versions_list_replaces_between_markers(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text(INDEX_WITH_MARKERS, encoding="utf-8")

    inject_versions_list(index_path, ["v1", "v2"])

    result = index_path.read_text(encoding="utf-8")
    assert "Some hand-written prose about auth." in result
    assert "More prose after." in result
    assert "old content to be replaced" not in result
    assert "* [v1](v1/index.md)" in result
    assert "* [v2](v2/index.md)" in result


def test_inject_versions_list_is_idempotent(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text(INDEX_WITH_MARKERS, encoding="utf-8")

    inject_versions_list(index_path, ["v1"])
    first = index_path.read_text(encoding="utf-8")
    inject_versions_list(index_path, ["v1"])
    second = index_path.read_text(encoding="utf-8")

    assert first == second


def test_inject_versions_list_missing_markers_raises(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text("# API\n\nNo markers here.\n", encoding="utf-8")

    with pytest.raises(ValueError, match="api-versions"):
        inject_versions_list(index_path, ["v1"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py -k inject -v`
Expected: FAIL with `ImportError` / `cannot import name 'inject_versions_list'`.

- [ ] **Step 3: Write minimal implementation**

Add at module level in `src/ocs_docs/openapi_to_docs.py` (after `discover_version_schemas`):

```python
VERSIONS_MARKER_START = "<!-- api-versions:start -->"
VERSIONS_MARKER_END = "<!-- api-versions:end -->"


def inject_versions_list(index_path: str | Path, versions: list[str]) -> None:
    """Replace the content between the version markers in the top-level API index.

    Only the text between ``VERSIONS_MARKER_START`` and ``VERSIONS_MARKER_END`` is
    rewritten; all surrounding hand-written prose is preserved. Idempotent.

    Raises:
        ValueError: if either marker is missing from the file.
    """
    path = Path(index_path)
    content = path.read_text(encoding="utf-8")

    if VERSIONS_MARKER_START not in content or VERSIONS_MARKER_END not in content:
        raise ValueError(
            f"Missing api-versions markers in {path}. Expected both "
            f"'{VERSIONS_MARKER_START}' and '{VERSIONS_MARKER_END}'."
        )

    block_lines = [VERSIONS_MARKER_START]
    block_lines += [f"* [{version}]({version}/index.md)" for version in versions]
    block_lines.append(VERSIONS_MARKER_END)
    replacement = "\n".join(block_lines)

    pattern = re.compile(
        re.escape(VERSIONS_MARKER_START) + r".*?" + re.escape(VERSIONS_MARKER_END),
        re.DOTALL,
    )
    path.write_text(pattern.sub(replacement, content), encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py -k inject -v`
Expected: PASS (all three tests).

- [ ] **Step 5: Commit**

```bash
git add src/ocs_docs/openapi_to_docs.py scripts/tests/test_openapi_to_docs.py
git commit -m "feat: inject versions list between markers in top-level API index"
```

---

## Task 4: `convert_versioned_docs` orchestration

**Files:**
- Modify: `src/ocs_docs/openapi_to_docs.py` (add module-level function after `convert_openapi_to_markdown`, ~line 467)
- Test: `scripts/tests/test_openapi_to_docs.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/tests/test_openapi_to_docs.py`:

```python
import yaml

from src.ocs_docs.openapi_to_docs import convert_versioned_docs


def test_convert_versioned_docs_end_to_end(tmp_path):
    # Schema directory with a single version
    schema_dir = tmp_path / "schemas"
    schema_dir.mkdir()
    (schema_dir / "v1.yml").write_text(yaml.safe_dump(SAMPLE_SCHEMA), encoding="utf-8")

    # Output dir with a top-level index containing markers
    output_dir = tmp_path / "api"
    output_dir.mkdir()
    (output_dir / "index.md").write_text(
        "# API\n\n## Versions\n\n"
        "<!-- api-versions:start -->\n<!-- api-versions:end -->\n",
        encoding="utf-8",
    )

    generated = convert_versioned_docs(schema_dir, output_dir)

    # Per-version folder, index, and tag txt exist
    assert (output_dir / "v1" / "index.md").exists()
    assert (output_dir / "v1" / "channels.txt").exists()
    # Top-level index links the version
    index_text = (output_dir / "index.md").read_text(encoding="utf-8")
    assert "* [v1](v1/index.md)" in index_text
    # Return value lists generated files
    assert any(name.endswith("v1/index.md") for name in generated)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py::test_convert_versioned_docs_end_to_end -v`
Expected: FAIL with `ImportError` / `cannot import name 'convert_versioned_docs'`.

- [ ] **Step 3: Write minimal implementation**

Add at module level in `src/ocs_docs/openapi_to_docs.py` (after `convert_openapi_to_markdown`):

```python
def convert_versioned_docs(schema_dir: str | Path, output_dir: str | Path) -> list[str]:
    """Generate per-version API docs from a directory of schema files.

    For each ``*.yml``/``*.yaml`` file in ``schema_dir`` (one per version), writes the
    per-tag ``.txt`` files and a generated ``index.md`` into ``output_dir/<version>/``,
    then injects the versions list into ``output_dir/index.md`` between its markers.

    Returns:
        List of generated file paths (tag docs + per-version index pages).
    """
    output_path = Path(output_dir)
    versions = discover_version_schemas(schema_dir)

    generated_files: list[str] = []
    for version, schema_path in versions:
        version_dir = output_path / version
        converter = OpenAPIToMarkdownConverter(schema_path)

        generated_files.extend(converter.convert_to_text_files(version_dir))

        index_file = version_dir / "index.md"
        index_file.write_text(converter.generate_version_index(version), encoding="utf-8")
        generated_files.append(str(index_file))

    inject_versions_list(output_path / "index.md", [version for version, _ in versions])

    return generated_files
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py::test_convert_versioned_docs_end_to_end -v`
Expected: PASS.

- [ ] **Step 5: Run the full test file**

Run: `uv run pytest scripts/tests/test_openapi_to_docs.py -v`
Expected: PASS (all tests so far).

- [ ] **Step 6: Commit**

```bash
git add src/ocs_docs/openapi_to_docs.py scripts/tests/test_openapi_to_docs.py
git commit -m "feat: add convert_versioned_docs orchestration for multi-version docs"
```

---

## Task 5: CLI directory-mode detection

**Files:**
- Modify: `src/ocs_docs/openapi_to_docs.py` (the `__main__` block, lines 470-486)
- Test: manual CLI check (no unit test — argparse glue)

- [ ] **Step 1: Update the `__main__` block**

Replace the body of the `try:` block in `if __name__ == "__main__":` so directory input routes to `convert_versioned_docs`:

```python
    try:
        if Path(args.schema).is_dir():
            generated_files = convert_versioned_docs(args.schema, args.output)
        else:
            generated_files = convert_openapi_to_markdown(args.schema, args.output)
        print(f"Generated {len(generated_files)} files in '{args.output}':")
        for file_path in generated_files:
            print(f"  - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
```

Also update the `schema` arg help text (line 474) to mention directories:

```python
    parser.add_argument(
        "schema",
        help="Path to an OpenAPI schema file/URL, or a directory of per-version schema files",
    )
```

- [ ] **Step 2: Smoke-test directory mode with a throwaway schema dir**

Build a temporary schema directory from the test fixture and run the CLI against it:

```bash
mkdir -p "$CLAUDE_JOB_DIR/tmp/schemas"
uv run python -c "import yaml, json; from scripts.tests.test_openapi_to_docs import SAMPLE_SCHEMA; open('$CLAUDE_JOB_DIR/tmp/schemas/v1.yml','w').write(yaml.safe_dump(SAMPLE_SCHEMA))"
mkdir -p "$CLAUDE_JOB_DIR/tmp/out"
printf '# API\n\n## Versions\n\n<!-- api-versions:start -->\n<!-- api-versions:end -->\n' > "$CLAUDE_JOB_DIR/tmp/out/index.md"
uv run python src/ocs_docs/openapi_to_docs.py "$CLAUDE_JOB_DIR/tmp/schemas" -o "$CLAUDE_JOB_DIR/tmp/out"
```

Expected: prints generated files including `.../out/v1/index.md` and `.../out/v1/channels.txt`; exit code 0.

- [ ] **Step 3: Commit**

```bash
git add src/ocs_docs/openapi_to_docs.py
git commit -m "feat: route directory input to versioned docs generation in CLI"
```

---

## Task 6: Migrate `docs/api/` — markers + move v1 files

**Files:**
- Modify: `docs/api/index.md` (replace lines 55-66 hardcoded LLM-docs list)
- git mv: `docs/api/*.txt` → `docs/api/v1/*.txt`
- Create: `docs/api/v1/index.md` (generated)

- [ ] **Step 1: Edit `docs/api/index.md` — replace the LLM Docs section with a Versions section**

Replace this block (currently lines 55-66):

```markdown
## LLM Docs

The following documents are a simplified version of the API for consumption by LLMs:

* [Channels](./channels.txt){:target="_blank"}
* [Chat](./chat.txt){:target="_blank"}
* [Sessions](./experiment_sessions.txt){:target="_blank"}
* [Experiments](./experiments.txt){:target="_blank"}
* [Files](./files.txt){:target="_blank"}
* [OpenAI](./openai.txt){:target="_blank"}
* [Participants](./participants.txt){:target="_blank"}
```

with:

```markdown
## Versions

The API is versioned. Select a version below for its endpoint reference and simplified
LLM docs:

<!-- api-versions:start -->
<!-- api-versions:end -->
```

- [ ] **Step 2: Move the existing root `.txt` files into `v1/`**

Run:

```bash
mkdir -p docs/api/v1
git mv docs/api/channels.txt docs/api/v1/channels.txt
git mv docs/api/chat.txt docs/api/v1/chat.txt
git mv docs/api/experiment_sessions.txt docs/api/v1/experiment_sessions.txt
git mv docs/api/experiments.txt docs/api/v1/experiments.txt
git mv docs/api/files.txt docs/api/v1/files.txt
git mv docs/api/openai.txt docs/api/v1/openai.txt
git mv docs/api/participants.txt docs/api/v1/participants.txt
```

- [ ] **Step 3: Generate the v1 index + populate the versions list from the real schema**

Download the current single schema as `v1.yml`, run the generator against the dir, which (re)writes `docs/api/v1/*.txt`, creates `docs/api/v1/index.md`, and fills the markers in `docs/api/index.md`:

```bash
mkdir -p "$CLAUDE_JOB_DIR/tmp/schemas"
curl -sSL https://raw.githubusercontent.com/dimagi/open-chat-studio/refs/heads/main/api-schema.yml \
  -o "$CLAUDE_JOB_DIR/tmp/schemas/v1.yml"
uv run python src/ocs_docs/openapi_to_docs.py "$CLAUDE_JOB_DIR/tmp/schemas" -o docs/api/
```

Expected: `docs/api/v1/index.md` created; `docs/api/index.md` versions block now contains `* [v1](v1/index.md)`.

- [ ] **Step 4: Verify the strict build passes (no broken links)**

Run: `uv run zensical build --clean --strict`
Expected: build succeeds. If it fails on the version index page being absent from nav (not just INFO), STOP and add a nav entry under `OCS API` in `mkdocs.yml` for `api/v1/index.md`, then re-run.

- [ ] **Step 5: Commit**

```bash
git add docs/api
git commit -m "docs: migrate API docs to versioned layout (v1) with generated index"
```

---

## Task 7: Update the `update-api-docs` workflow

**Files:**
- Modify: `.github/workflows/update-api-docs.yml` (the "Generate API documentation" step)

- [ ] **Step 1: Replace the generate step with fetch-directory + generate**

Replace the single step:

```yaml
      - name: Generate API documentation
        run: uv run python src/ocs_docs/openapi_to_docs.py https://raw.githubusercontent.com/dimagi/open-chat-studio/refs/heads/main/api-schema.yml -o docs/api/
```

with:

```yaml
      - name: Fetch OpenAPI schema directory
        env:
          # Path to the per-version schema directory in the OCS repo.
          # Change this one line once OCS finalizes the location.
          API_SCHEMA_DIR: api-schema
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          mkdir -p schemas
          gh api "repos/dimagi/open-chat-studio/contents/${API_SCHEMA_DIR}?ref=main" \
            --jq '.[] | select(.name | test("\\.ya?ml$")) | .download_url' \
          | while read -r url; do
              echo "Downloading $url"
              curl -sSL "$url" -O --output-dir schemas
            done
          echo "Fetched schema files:"
          ls -1 schemas

      - name: Generate API documentation
        run: uv run python src/ocs_docs/openapi_to_docs.py schemas -o docs/api/
```

- [ ] **Step 2: Validate the workflow YAML parses**

Run: `uv run python -c "import yaml; yaml.safe_load(open('.github/workflows/update-api-docs.yml'))"`
Expected: no output, exit code 0.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/update-api-docs.yml
git commit -m "ci: fetch versioned schema directory from OCS for API docs generation"
```

---

## Task 8: Final verification

**Files:** none (verification only)

- [ ] **Step 1: Run the full test suite**

Run: `uv run pytest scripts/tests -v`
Expected: PASS (including the existing Confluence tests and all new generator tests).

- [ ] **Step 2: Run the strict build**

Run: `uv run zensical build --clean --strict`
Expected: build succeeds with no broken-link errors.

- [ ] **Step 3: Confirm generated artifacts are present and correct**

Run: `ls docs/api docs/api/v1 && grep -n "api-versions" docs/api/index.md`
Expected: `docs/api/v1/` contains `index.md` + the 7 `.txt` files; `docs/api/index.md` contains both markers with `* [v1](v1/index.md)` between them.
