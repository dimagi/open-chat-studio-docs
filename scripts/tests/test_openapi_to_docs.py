"""Tests for the OpenAPI-to-markdown versioned docs generator."""

from pathlib import Path

import pytest
import yaml

from src.ocs_docs.openapi_to_docs import (
    OpenAPIToMarkdownConverter,
    convert_versioned_docs,
    discover_version_schemas,
    inject_versions_list,
)

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


def test_generate_version_index_escapes_pipes_in_summary():
    schema = {
        "openapi": "3.0.0",
        "info": {"title": "T", "version": "1"},
        "tags": [{"name": "Channels"}],
        "paths": {
            "/api/x/": {
                "get": {"tags": ["Channels"], "summary": "List a | b channels", "responses": {"200": {"description": "ok"}}},
            }
        },
    }
    index_md = OpenAPIToMarkdownConverter(schema).generate_version_index("v1")
    assert r"| GET | `/api/x/` | List a \| b channels |" in index_md


def test_generate_version_index_collapses_multiline_tag_description():
    schema = {
        "openapi": "3.0.0",
        "info": {"title": "T", "version": "1"},
        "tags": [{"name": "Chat", "description": "\n        The Chat API.\n        Use it well.\n    "}],
        "paths": {
            "/api/chat/": {
                "get": {"tags": ["Chat"], "summary": "List", "responses": {"200": {"description": "ok"}}},
            }
        },
    }
    index_md = OpenAPIToMarkdownConverter(schema).generate_version_index("v1")
    assert "[Chat](./chat.txt){:target=\"_blank\"} — The Chat API. Use it well." in index_md
    # No raw newline inside the bullet, no trailing space before newline
    for line in index_md.splitlines():
        assert not line.endswith(" ")


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


def test_inject_versions_list_reversed_markers_raises(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text(
        "# API\n\n<!-- api-versions:end -->\n<!-- api-versions:start -->\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="api-versions"):
        inject_versions_list(index_path, ["v1"])


def test_response_empty_description_emits_no_trailing_space():
    converter = OpenAPIToMarkdownConverter(
        {"openapi": "3.0.0", "info": {"title": "T", "version": "1"}, "paths": {}}
    )

    lines = converter._generate_endpoint_section_minified(
        "delete", "/api/x/", {"responses": {"204": {"description": ""}, "200": {}}}
    )

    assert "    204:" in lines
    assert "    200:" in lines
    # Neither code must have a trailing space
    assert "    204: " not in lines
    assert "    200: " not in lines


def test_endpoint_security_handles_optional_requirement():
    # An empty requirement object ({}) means auth is optional; it must not crash.
    schema = {
        "openapi": "3.0.0",
        "info": {"title": "T", "version": "1"},
        "paths": {
            "/api/me/": {
                "get": {
                    "tags": ["Me"],
                    "summary": "Current user",
                    "security": [{}, {"apiKeyAuth": []}, {"tokenAuth": ["read"]}],
                    "responses": {"200": {"description": "ok"}},
                }
            }
        },
    }
    converter = OpenAPIToMarkdownConverter(schema)
    doc = converter._generate_tag_documentation("Me", converter._group_endpoints_by_tag()["Me"])

    assert "(optional - no authentication required)" in doc
    assert "apiKeyAuth" in doc
    assert "Required scopes: read" in doc


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
