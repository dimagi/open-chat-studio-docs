#!/usr/bin/env python3
"""Update the Confluence release table with a new GitHub release entry.

Reads release information from environment variables, fetches the target
Confluence page, converts the release markdown to Confluence storage format,
inserts a new row at the top of the release table, and writes the updated page
back.

Required environment variables:
    CONFLUENCE_BASE_URL: e.g. https://dimagi.atlassian.net
    CONFLUENCE_EMAIL: Service account email
    CONFLUENCE_API_TOKEN: Atlassian API token
    CONFLUENCE_PAGE_ID: Target page ID
    RELEASE_URL: URL to the GitHub release
    RELEASE_TAG: Release tag (e.g. v2026.04.13)
    RELEASE_BODY: Release notes in markdown (optional)
"""

import os
import re
import sys

import markdown
import requests


def get_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Error: {name} environment variable is required", file=sys.stderr)
        sys.exit(1)
    return value


def get_release_info() -> dict:
    """Get release information from environment variables."""
    return {
        "body": os.environ.get("RELEASE_BODY", ""),
        "html_url": get_env("RELEASE_URL"),
        "tag_name": get_env("RELEASE_TAG"),
    }


def extract_date_from_tag(tag_name: str) -> str:
    """Extract a YYYY-MM-DD date from a release tag like v2026.04.13."""
    match = re.match(r"v?(\d{4})\.(\d{2})\.(\d{2})", tag_name)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    raise ValueError(f"Cannot extract date from tag: {tag_name}")


def get_confluence_page(base_url: str, page_id: str, auth: tuple) -> dict:
    """Fetch the current Confluence page content and version number."""
    url = f"{base_url}/wiki/api/v2/pages/{page_id}"
    params = {"body-format": "storage"}
    response = requests.get(url, params=params, auth=auth)
    response.raise_for_status()
    data = response.json()
    return {
        "title": data["title"],
        "version": data["version"]["number"],
        "content": data["body"]["storage"]["value"],
    }


def update_confluence_page(
    base_url: str, page_id: str, auth: tuple, title: str, content: str, version: int
) -> dict:
    """Update the Confluence page, incrementing the version number."""
    url = f"{base_url}/wiki/api/v2/pages/{page_id}"
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content,
        },
        "version": {"number": version + 1},
    }
    response = requests.put(url, json=payload, auth=auth)
    response.raise_for_status()
    return response.json()


def release_markdown_to_confluence_html(md_text: str) -> str:
    """Convert GitHub release markdown to Confluence storage format HTML.

    Produces XHTML compatible with the existing table style: <h3> section
    headings, <ul> lists with each <li> wrapping content in a <p> tag.
    """
    if not md_text.strip():
        return "<p>No release notes.</p>"

    html = markdown.markdown(md_text, extensions=["extra", "sane_lists"])

    # Wrap bare <li> content in <p> tags to match existing Confluence format.
    # The markdown library produces <li>text</li> for tight lists, but the
    # existing table rows use <li><p>text</p></li>.
    def _wrap_li(match: re.Match) -> str:
        content = match.group(1)
        if "<p>" in content:
            return match.group(0)
        return f"<li>\n<p>{content.strip()}</p></li>"

    html = re.sub(r"<li>(.*?)</li>", _wrap_li, html, flags=re.DOTALL)

    return html


def build_table_row(date_str: str, description_html: str, release_url: str) -> str:
    """Build a Confluence storage format table row matching the existing style."""
    return (
        "<tr>\n"
        '<td data-highlight-colour="#ffffff">\n'
        f'<p><time datetime="{date_str}" /></p></td>\n'
        '<td data-highlight-colour="#ffffff">\n'
        f"{description_html}</td>\n"
        "<td>\n"
        f'<p><a href="{release_url}">{release_url}</a></p></td></tr>'
    )


def insert_row_after_header(page_content: str, new_row: str) -> str:
    """Insert a new table row immediately after the header row.

    The header row is identified by its closing </th></tr> sequence.
    The new row is inserted right after it, placing the newest release
    at the top of the table.
    """
    # Match the closing of the last <th> in the header row followed by </tr>
    pattern = r"</th>\s*</tr>"
    match = re.search(pattern, page_content)
    if not match:
        print("Error: could not find header row in table", file=sys.stderr)
        sys.exit(1)

    insert_pos = match.end()
    return page_content[:insert_pos] + "\n" + new_row + "\n" + page_content[insert_pos:]


def main():
    base_url = get_env("CONFLUENCE_BASE_URL")
    email = get_env("CONFLUENCE_EMAIL")
    api_token = get_env("CONFLUENCE_API_TOKEN")
    page_id = get_env("CONFLUENCE_PAGE_ID")

    release = get_release_info()
    date_str = extract_date_from_tag(release["tag_name"])

    auth = (email, api_token)

    print(f"Fetching Confluence page {page_id}...")
    page = get_confluence_page(base_url, page_id, auth)
    print(f"Current page version: {page['version']}")

    description_html = release_markdown_to_confluence_html(release["body"])
    new_row = build_table_row(date_str, description_html, release["html_url"])
    updated_content = insert_row_after_header(page["content"], new_row)

    print("Updating Confluence page...")
    result = update_confluence_page(
        base_url, page_id, auth, page["title"], updated_content, page["version"]
    )
    print(f"Page updated to version {result['version']['number']}")


if __name__ == "__main__":
    main()
