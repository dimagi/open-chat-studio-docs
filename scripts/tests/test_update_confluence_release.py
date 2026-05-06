"""Tests for the Confluence release table update script."""

import json
import textwrap

import pytest

from scripts.update_confluence_release import (
    build_table_row,
    extract_date_from_tag,
    get_release_info,
    insert_row_after_header,
    release_markdown_to_confluence_html,
)

# ---------------------------------------------------------------------------
# Minimal Confluence page fixture — header row + one data row
# ---------------------------------------------------------------------------
SAMPLE_PAGE_CONTENT = textwrap.dedent("""\
    <p>Intro paragraph</p>
    <ac:structured-macro ac:name="table-filter"><ac:rich-text-body>
    <table><colgroup><col /><col /><col /></colgroup>
    <tbody>
    <tr>
    <th data-highlight-colour="#e3fcef">
    <p><strong>Release date to users</strong></p></th>
    <th data-highlight-colour="#e3fcef">
    <p><strong>Description of the change</strong></p></th>
    <th data-highlight-colour="#e3fcef">
    <p><strong>Link</strong></p></th></tr>
    <tr>
    <td data-highlight-colour="#ffffff">
    <p><time datetime="2026-04-06" /></p></td>
    <td data-highlight-colour="#ffffff">
    <h3>Bug Fixes</h3>
    <ul><li><p>Fixed a thing</p></li></ul></td>
    <td>
    <p><a href="https://github.com/dimagi/open-chat-studio-docs/releases/tag/v2026.04.06">link</a></p></td></tr>
    </tbody></table></ac:rich-text-body></ac:structured-macro>""")


# ---------------------------------------------------------------------------
# extract_date_from_tag
# ---------------------------------------------------------------------------
class TestExtractDateFromTag:
    def test_standard_tag(self):
        assert extract_date_from_tag("v2026.04.13") == "2026-04-13"

    def test_tag_without_v_prefix(self):
        assert extract_date_from_tag("2026.04.13") == "2026-04-13"

    def test_invalid_tag_raises(self):
        with pytest.raises(ValueError, match="Cannot extract date"):
            extract_date_from_tag("release-1.0")


# ---------------------------------------------------------------------------
# release_markdown_to_confluence_html
# ---------------------------------------------------------------------------
class TestMarkdownToConfluenceHtml:
    def test_headings_and_lists(self):
        md = textwrap.dedent("""\
            ### New Features
            - Added feature X
            - Added feature Y

            ### Bug Fixes
            - Fixed issue Z
        """)
        html = release_markdown_to_confluence_html(md)
        assert "<h3>New Features</h3>" in html
        assert "<h3>Bug Fixes</h3>" in html
        assert "<li>" in html

    def test_li_content_wrapped_in_p(self):
        md = "- Item one\n- Item two\n"
        html = release_markdown_to_confluence_html(md)
        assert "<li>\n<p>Item one</p></li>" in html
        assert "<li>\n<p>Item two</p></li>" in html

    def test_already_wrapped_li_not_double_wrapped(self):
        md = "- Item one\n\n- Item two\n"  # loose list → markdown wraps in <p>
        html = release_markdown_to_confluence_html(md)
        assert "<p><p>" not in html

    def test_links_preserved(self):
        md = "- See [docs](https://example.com) for details\n"
        html = release_markdown_to_confluence_html(md)
        assert '<a href="https://example.com">docs</a>' in html

    def test_inline_code_preserved(self):
        md = "- Use `end_session()` to end\n"
        html = release_markdown_to_confluence_html(md)
        assert "<code>end_session()</code>" in html

    def test_empty_body(self):
        assert release_markdown_to_confluence_html("") == "<p>No release notes.</p>"
        assert release_markdown_to_confluence_html("  ") == "<p>No release notes.</p>"

    def test_bold_text(self):
        md = "- Added **ElevenLabs** support\n"
        html = release_markdown_to_confluence_html(md)
        assert "<strong>ElevenLabs</strong>" in html


# ---------------------------------------------------------------------------
# build_table_row
# ---------------------------------------------------------------------------
class TestBuildTableRow:
    def test_row_structure(self):
        row = build_table_row(
            "2026-04-13",
            "<h3>New</h3><ul><li><p>Thing</p></li></ul>",
            "https://github.com/dimagi/open-chat-studio-docs/releases/tag/v2026.04.13",
        )
        assert '<time datetime="2026-04-13" />' in row
        assert '<td data-highlight-colour="#ffffff">' in row
        assert "<h3>New</h3>" in row
        assert "v2026.04.13" in row
        assert row.startswith("<tr>")
        assert row.endswith("</td></tr>")


# ---------------------------------------------------------------------------
# insert_row_after_header
# ---------------------------------------------------------------------------
class TestInsertRowAfterHeader:
    def test_row_inserted_between_header_and_first_data_row(self):
        new_row = "<tr><td>NEW</td></tr>"
        result = insert_row_after_header(SAMPLE_PAGE_CONTENT, new_row)

        # The new row should appear after the header </tr> and before the
        # first data row
        header_end = result.index("</th></tr>") + len("</th></tr>")
        new_row_pos = result.index("<tr><td>NEW</td></tr>")
        old_first_row_pos = result.index('<td data-highlight-colour="#ffffff">')

        assert new_row_pos > header_end
        assert new_row_pos < old_first_row_pos

    def test_existing_content_preserved(self):
        new_row = "<tr><td>NEW</td></tr>"
        result = insert_row_after_header(SAMPLE_PAGE_CONTENT, new_row)
        assert "Intro paragraph" in result
        assert "table-filter" in result
        assert "Fixed a thing" in result

    def test_missing_header_raises(self):
        with pytest.raises(SystemExit):
            insert_row_after_header("<table><tbody><tr><td>no header</td></tr></tbody></table>", "")


# ---------------------------------------------------------------------------
# get_release_info (from event file)
# ---------------------------------------------------------------------------
class TestGetReleaseInfo:
    def test_reads_from_event_file(self, tmp_path, monkeypatch):
        event = {
            "release": {
                "body": "### New\n- Thing\n",
                "html_url": "https://github.com/example/releases/tag/v1",
                "tag_name": "v2026.04.13",
            }
        }
        event_file = tmp_path / "event.json"
        event_file.write_text(json.dumps(event))
        monkeypatch.setenv("GITHUB_EVENT_PATH", str(event_file))

        info = get_release_info()
        assert info["body"] == "### New\n- Thing\n"
        assert info["tag_name"] == "v2026.04.13"
        assert "github.com" in info["html_url"]

    def test_falls_back_to_env_vars(self, monkeypatch):
        monkeypatch.delenv("GITHUB_EVENT_PATH", raising=False)
        monkeypatch.setenv("RELEASE_BODY", "notes")
        monkeypatch.setenv("RELEASE_URL", "https://example.com")
        monkeypatch.setenv("RELEASE_TAG", "v2026.01.01")

        info = get_release_info()
        assert info["body"] == "notes"
        assert info["tag_name"] == "v2026.01.01"
