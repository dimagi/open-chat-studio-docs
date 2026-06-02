"""Tests for the OpenAPI-to-markdown versioned docs generator."""

from pathlib import Path

import pytest

from src.ocs_docs.openapi_to_docs import (
    OpenAPIToMarkdownConverter,
    discover_version_schemas,
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
