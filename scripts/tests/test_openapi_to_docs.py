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
