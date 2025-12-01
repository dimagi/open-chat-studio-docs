#!/usr/bin/env python3
"""
OpenAPI Schema to Markdown Documentation Converter

This module provides functionality to convert OpenAPI 3.x schemas into
self-contained text documents for each group of APIs (grouped by tag).
"""

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
import yaml

# Constants
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}
JSON_EXTENSIONS = {".json"}
YAML_EXTENSIONS = {".yaml", ".yml"}


class OpenAPIToMarkdownConverter:
    """Converts OpenAPI schemas to markdown documentation."""

    def __init__(self, schema: str | dict[str, Any] | Path):
        """
        Initialize the converter with an OpenAPI schema.

        Args:
            schema: OpenAPI schema as JSON/YAML string, dict, file path, or URL
        """
        if isinstance(schema, str | Path):
            self.schema = self._load_schema(schema)
        else:
            self.schema = schema

        self.base_info = self._extract_base_info()
        self.components = self.schema.get("components", {})
        self.schemas = self.components.get("schemas", {})

    def _load_schema(self, schema_path: str | Path) -> dict[str, Any]:
        """Load OpenAPI schema from file path, URL, or string content."""
        schema_str = str(schema_path)
        
        # Check if it's a URL
        parsed_url = urlparse(schema_str)
        if parsed_url.scheme in ('http', 'https'):
            try:
                response = requests.get(schema_str, timeout=30)
                response.raise_for_status()
                content = response.text
            except requests.RequestException as e:
                raise ValueError(f"Failed to fetch schema from URL: {e}") from e
        else:
            # Try as file path first
            path = Path(schema_path)
            if path.exists():
                content = path.read_text(encoding="utf-8")
            else:
                # Try to parse as JSON/YAML string
                try:
                    return json.loads(schema_str)
                except json.JSONDecodeError:
                    try:
                        return yaml.safe_load(schema_str)
                    except yaml.YAMLError as e:
                        raise ValueError("Invalid schema: not a valid file path, URL, JSON, or YAML") from e
        
        # Parse the content (from file or URL)
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            try:
                return yaml.safe_load(content)
            except yaml.YAMLError as e:
                raise ValueError("Invalid schema content: not valid JSON or YAML") from e

    def _extract_base_info(self) -> dict[str, Any]:
        """Extract basic API information from schema."""
        info = self.schema.get("info", {})
        servers = self.schema.get("servers", [])

        return {
            "title": info.get("title", "API Documentation"),
            "version": info.get("version", "1.0.0"),
            "description": info.get("description", ""),
            "servers": servers,
            "base_url": servers[0].get("url", "") if servers else "",
        }

    def convert_to_text_files(self, output_dir: str | Path = "api_docs") -> list[str]:
        """
        Convert OpenAPI schema to markdown files grouped by tags.

        Args:
            output_dir: Directory to save markdown files

        Returns:
            List of generated file paths
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Group endpoints by tags
        tag_groups = self._group_endpoints_by_tag()

        generated_files = []
        for tag, endpoints in tag_groups.items():
            filename = self._generate_tag_filename(tag)
            file_path = output_path / f"{filename}.txt"

            markdown_content = self._generate_tag_documentation(tag, endpoints)

            file_path.write_text(markdown_content, encoding="utf-8")
            generated_files.append(str(file_path))

        return generated_files

    def _group_endpoints_by_tag(self) -> dict[str, list[dict[str, Any]]]:
        """
        Group all endpoints by their tags.

        Returns:
            Dictionary mapping tag names to lists of endpoint info
        """
        tag_groups = {}
        paths = self.schema.get("paths", {})

        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.lower() in HTTP_METHODS:
                    tags = operation.get("tags", ["Untagged"])

                    # Handle endpoints with multiple tags
                    for tag in tags:
                        if tag not in tag_groups:
                            tag_groups[tag] = []

                        endpoint_info = {"method": method, "path": path, "operation": operation}
                        tag_groups[tag].append(endpoint_info)

        return tag_groups

    def _generate_tag_filename(self, tag: str) -> str:
        """Generate a clean filename for the tag."""
        # Clean up tag name for filename
        clean_tag = re.sub(r"[^a-zA-Z0-9_-]", "_", tag.lower())
        clean_tag = re.sub(r"_+", "_", clean_tag)
        return clean_tag.strip("_")

    def _generate_tag_documentation(self, tag: str, endpoints: list[dict[str, Any]]) -> str:
        """Generate markdown documentation for all endpoints in a tag."""
        lines = []

        # API header info
        lines.append(f"API: {self.base_info['title']} v{self.base_info['version']}")
        if self.base_info.get("description"):
            lines.append(f"Description: {self.base_info['description']}")
        lines.append("")

        # Tag info
        tag_info = self._get_tag_info(tag)
        if tag != "Untagged":
            lines.append(f"TAG: {tag}")
            if tag_info and tag_info.get("description"):
                lines.append(f"Description: {tag_info['description']}")
            lines.append("")

        lines.append("ENDPOINTS:")
        lines.append("")

        # Generate documentation for each endpoint
        for endpoint in endpoints:
            method = endpoint["method"]
            path = endpoint["path"]
            operation = endpoint["operation"]

            endpoint_lines = self._generate_endpoint_section_minified(method, path, operation)
            lines.extend(endpoint_lines)
            lines.append("")

        # Collect all schemas used in this tag
        schemas_used = self._collect_schemas_for_tag(endpoints)
        if schemas_used:
            lines.append("SCHEMAS:")
            lines.append("")

            for schema_name in sorted(schemas_used):
                schema_lines = self._format_schema_minified(schema_name)
                lines.extend(schema_lines)
                lines.append("")

        # Add security info if present
        security_schemes = self.schema.get("components", {}).get("securitySchemes", {})
        if security_schemes:
            lines.append("SECURITY:")
            for scheme_name, scheme in security_schemes.items():
                scheme_type = scheme.get("type", "unknown")
                if scheme_type == "apiKey":
                    location = scheme.get("in", "header")
                    key_name = scheme.get("name", "key")
                    lines.append(f"- API Key authentication ({location}: {key_name})")
                elif scheme_type == "http":
                    scheme_name_val = scheme.get("scheme", "bearer")
                    lines.append(f"- HTTP {scheme_name_val} authentication")
                elif scheme_type == "oauth2":
                    lines.append(f"- {scheme_name}")
                    for name, flow in scheme.get("flows", {}).items():
                        auth_url = flow.get("authorizationUrl", "")
                        token_url = flow.get("tokenUrl", "")
                        title = list(filter(None, re.split(r'(?=[A-Z])', name)))
                        title[0] = title[0].title()
                        name = ' '.join(title)
                        lines.append(f"  - {name} Flow (authorization url: {auth_url}, token url: {token_url})")
                else:
                    lines.append(f"- {scheme_name} ({scheme_type})")
            lines.append("")

        return "\n".join(lines)

    def _get_tag_info(self, tag: str) -> dict[str, Any] | None:
        """Get tag information from schema if available."""
        tags = self.schema.get("tags", [])
        for tag_info in tags:
            if tag_info.get("name") == tag:
                return tag_info
        return None

    def _generate_anchor(self, method: str, path: str) -> str:
        """Generate URL anchor for endpoint."""
        anchor = f"{method.lower()}-{path}"
        anchor = re.sub(r"[^a-zA-Z0-9_-]", "-", anchor)
        anchor = re.sub(r"-+", "-", anchor)
        return anchor.strip("-")

    def _generate_endpoint_section_minified(self, method: str, path: str, operation: dict[str, Any]) -> list[str]:
        """Generate minified markdown section for a single endpoint."""
        lines = []

        # Endpoint header
        lines.append(f"{method.upper()} {path}")

        # Summary
        if operation.get("summary"):
            lines.append(f"  Summary: {operation['summary']}")

        # Description (only if different from summary)
        description = operation.get("description")
        if description and description != operation.get("summary"):
            lines.append(f"  Description: {description}")

        # Parameters
        parameters = operation.get("parameters", [])
        if parameters:
            lines.append("  Parameters:")
            for param in parameters:
                name = param.get("name", "")
                location = param.get("in", "query")
                param_type = self._get_parameter_type_minified(param)
                required = " (required)" if param.get("required", False) else " (optional)"
                description = param.get("description", "No description")
                lines.append(f"    - {name} ({location}, {param_type}{required}): {description}")

        # Request Body
        request_body = operation.get("requestBody")
        if request_body:
            lines.append("  Request Body:")
            content = request_body.get("content", {})
            for media_type, media_content in content.items():
                lines.append(f"    Content: {media_type}")
                schema = media_content.get("schema", {})
                if schema:
                    schema_ref = self._get_schema_reference(schema)
                    lines.append(f"    Schema: {schema_ref}")

        # Responses
        responses = operation.get("responses", {})
        if responses:
            lines.append("  Responses:")
            for status_code, response in responses.items():
                description = response.get("description", "No description")
                lines.append(f"    {status_code}: {description}")

                content = response.get("content", {})
                for media_type, media_content in content.items():
                    lines.append(f"      Content: {media_type}")
                    schema = media_content.get("schema", {})
                    if schema:
                        schema_ref = self._get_schema_reference(schema)
                        lines.append(f"      Schema: {schema_ref}")

        # Security
        if security :=  operation.get("security", []):
            lines.append("  Security:")
            for security in security:
                key = next(iter(security))
                lines.append(f"    {key}")
                if value := security.get(key):
                    value = ', '.join(value)
                    lines.append(f"      - Required scopes: {value}")

        return lines

    def _get_parameter_type_minified(self, param: dict[str, Any]) -> str:
        """Extract simplified parameter type information."""
        schema = param.get("schema", {})
        return schema.get("type", "string")

    def _get_schema_reference(self, schema: dict[str, Any]) -> str:
        """Get schema reference name or type."""
        if "$ref" in schema:
            return schema["$ref"].split("/")[-1]
        elif schema.get("type") == "array" and "items" in schema:
            items = schema["items"]
            if "$ref" in items:
                return f"array of {items['$ref'].split('/')[-1]}"
            else:
                return f"array of {items.get('type', 'unknown')}"
        else:
            return schema.get("type", "Unknown")

    def _collect_schemas_for_tag(self, endpoints: list[dict[str, Any]]) -> set[str]:
        """Collect all schema references used in endpoints of this tag."""
        schemas = set()

        for endpoint in endpoints:
            operation = endpoint["operation"]

            # Check request body schemas
            request_body = operation.get("requestBody", {})
            content = request_body.get("content", {})
            for media_content in content.values():
                schema = media_content.get("schema", {})
                self._extract_schema_refs(schema, schemas)

            # Check response schemas
            responses = operation.get("responses", {})
            for response in responses.values():
                content = response.get("content", {})
                for media_content in content.values():
                    schema = media_content.get("schema", {})
                    self._extract_schema_refs(schema, schemas)

        return schemas

    def _extract_schema_refs(self, schema: dict[str, Any], refs: set[str]):
        """Recursively extract schema references."""
        if "$ref" in schema:
            ref_name = schema["$ref"].split("/")[-1]
            refs.add(ref_name)
        elif schema.get("type") == "array" and "items" in schema:
            self._extract_schema_refs(schema["items"], refs)
        elif schema.get("type") == "object" and "properties" in schema:
            for prop_schema in schema["properties"].values():
                self._extract_schema_refs(prop_schema, refs)

    def _format_schema_minified(self, schema_name: str) -> list[str]:
        """Format a schema definition in minified style."""
        lines = []
        schema = self.schemas.get(schema_name)

        if not schema:
            lines.append(f"{schema_name}: (not found)")
            return lines

        lines.append(f"{schema_name}:")

        if schema.get("type") == "object":
            properties = schema.get("properties", {})
            required = schema.get("required", [])

            for prop_name, prop_schema in properties.items():
                prop_type = self._get_schema_reference(prop_schema)
                required_marker = " (required)" if prop_name in required else ""
                lines.append(f"  - {prop_name}: {prop_type}{required_marker}")

        elif schema.get("type") == "array":
            items = schema.get("items", {})
            item_type = self._get_schema_reference(items)
            lines.append(f"  - array of {item_type}")

        elif schema.get("enum"):
            enum_values = ", ".join(map(str, schema["enum"]))
            lines.append(f"  - enum: [{enum_values}]")

        else:
            schema_type = schema.get("type", "unknown")
            lines.append(f"  - type: {schema_type}")

        return lines

    def _resolve_ref(self, ref: str) -> dict[str, Any]:
        """Resolve a $ref to the actual schema definition."""
        if ref.startswith("#/components/schemas/"):
            schema_name = ref.split("/")[-1]
            return self.schemas.get(schema_name, {})
        elif ref.startswith("#/"):
            # Handle other internal references
            parts = ref[2:].split("/")
            result = self.schema
            for part in parts:
                result = result.get(part, {})
            return result
        else:
            # External references not supported
            return {}

    def _get_type_info(self, schema: dict[str, Any]) -> str:
        """Get comprehensive type information including constraints."""
        if "$ref" in schema:
            resolved = self._resolve_ref(schema["$ref"])
            if resolved:
                schema_name = schema["$ref"].split("/")[-1]
                return f"{schema_name} (ref)"
            return "unknown (ref)"

        schema_type = schema.get("type", "unknown")
        type_info = [schema_type]

        # Add format
        if schema.get("format"):
            type_info.append(f"format: {schema['format']}")

        # Add constraints
        constraints = []
        if "minimum" in schema:
            constraints.append(f"min: {schema['minimum']}")
        if "maximum" in schema:
            constraints.append(f"max: {schema['maximum']}")
        if "minLength" in schema:
            constraints.append(f"minLen: {schema['minLength']}")
        if "maxLength" in schema:
            constraints.append(f"maxLen: {schema['maxLength']}")
        if "pattern" in schema:
            constraints.append(f"pattern: {schema['pattern']}")
        if schema.get("enum"):
            enum_values = ", ".join([str(v) for v in schema["enum"][:3]])
            if len(schema["enum"]) > 3:
                enum_values += "..."
            constraints.append(f"enum: [{enum_values}]")

        if constraints:
            type_info.append(f"({', '.join(constraints)})")

        return " ".join(type_info)


def convert_openapi_to_markdown(
    schema_path: str | dict[str, Any] | Path, output_dir: str | Path = "api_docs"
) -> list[str]:
    """
    Convenience function to convert OpenAPI schema to markdown files.

    Args:
        schema_path: Path to OpenAPI schema file, URL, schema dict, or schema string
        output_dir: Directory to save markdown files

    Returns:
        List of generated file paths
    """
    converter = OpenAPIToMarkdownConverter(schema_path)
    return converter.convert_to_text_files(output_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert OpenAPI schema to markdown documentation")
    parser.add_argument("schema", help="Path to OpenAPI schema file, URL, or schema content (JSON or YAML)")
    parser.add_argument("-o", "--output", default="api_docs", help="Output directory for markdown files")

    args = parser.parse_args()

    try:
        generated_files = convert_openapi_to_markdown(args.schema, args.output)
        print(f"Generated {len(generated_files)} markdown files in '{args.output}':")
        for file_path in generated_files:
            print(f"  - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
