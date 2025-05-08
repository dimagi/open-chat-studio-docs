#!/usr/bin/env python3

# /// script
# dependencies = [
#   "requests",
#   "anthropic",
# ]
# ///
"""
GitHub Release Summary Generator

This script fetches release information from a GitHub repository via the GitHub API,
identifies changes since the previous release by retrieving the diff,
uses an LLM API to generate a summary of those changes,
and then creates a new GitHub release with the summary as release notes.
"""

import os
import sys
import argparse
import json
import requests
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import re
import anthropic

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate a summary of changes from GitHub releases using an LLM and create a new release.')
    parser.add_argument('--repo', '-r', required=True, help='GitHub repository in the format "owner/repo"')
    parser.add_argument('--token', '-t', help='GitHub personal access token (can also use GITHUB_TOKEN env var)')
    parser.add_argument('--api-key', '-k', help='Anthropic API key (can also use ANTHROPIC_API_KEY env var)')
    parser.add_argument('--model', '-m', default='claude-3-5-haiku-20241022',
                        help='Anthropic model to use (default: claude-3-5-haiku-20241022)')
    parser.add_argument('--format', '-f', choices=['markdown', 'plain'], default='markdown',
                        help='Output format (default: markdown)')
    parser.add_argument('--tag', required=True, help='Tag name for the new release')
    parser.add_argument('--name', help='Name for the new release (defaults to tag name if not provided)')
    parser.add_argument('--target', help='Target commitish (branch/commit) for the new release (defaults to default branch)')
    parser.add_argument('--draft', action='store_true', help='Create release as a draft')
    parser.add_argument('--dry-run', action='store_true', help='Generate summary but do not create GitHub release')
    return parser.parse_args()

def get_github_token(args) -> str:
    """Get GitHub token from args or environment variable."""
    if args.token:
        return args.token

    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        sys.exit("Error: GitHub token not provided. Use --token or set GITHUB_TOKEN environment variable.")

    return token

def get_anthropic_api_key(args) -> str:
    """Get Anthropic API key from args or environment variable."""
    if args.api_key:
        return args.api_key

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        sys.exit("Error: Anthropic API key not provided. Use --api-key or set ANTHROPIC_API_KEY environment variable.")

    return api_key

def fetch_github_releases(repo: str, token: str) -> List[Dict]:
    """Fetch release information from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        releases = response.json()

        # Sort releases by published date (newest first)
        releases.sort(key=lambda x: x.get('published_at', ''), reverse=True)

        return releases
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error fetching releases from GitHub API: {e}")

def fetch_file_content(repo: str, token: str, path: str, ref: str) -> Optional[str]:
    """Fetch file content from a specific release tag."""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return None  # File doesn't exist in this release

        response.raise_for_status()
        content_data = response.json()

        # GitHub API returns content as base64-encoded
        import base64
        content = base64.b64decode(content_data['content']).decode('utf-8')
        return content
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch file content for {path} at {ref}: {e}")
        return None

def get_changelog_diff(repo: str, token: str, latest_tag: str, previous_tag: str) -> Dict[str, Dict[str, str]]:
    filename = 'docs/changelog.md'
    latest_content = fetch_file_content(repo, token, filename, latest_tag)
    previous_content = fetch_file_content(repo, token, filename, previous_tag)

    if latest_content and previous_content:
        import difflib
        diff = '\n'.join(difflib.unified_diff(
            previous_content.splitlines(),
            latest_content.splitlines(),
            fromfile=f"{filename} (previous)",
            tofile=f"{filename} (latest)",
            lineterm=''
        ))
        return diff
    return ""

def generate_llm_summary(
        changelog_diff: str,
        api_key: str,
        model: str,
        output_format: str
) -> str:
    """Generate a summary of changes using the Anthropic Claude API."""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are a technical writer preparing release notes. 
I'll provide you with information about a GitHub repository's changes since the previous release.

Changes between releases taken from the changelog markdown file:

{changelog_diff}

Based on this information, create a concise but comprehensive summary of the changes for the new release.
Focus on new features, improvements, bug fixes, and breaking changes.
Organize the summary into clear sections:
- Start with an overall summary of the release
- Then add the following sections to categorize the changes:
  - New Features (tagged with 'NEW' in the changelog)
  - Improvements (tagged with 'CHANGE' in the changelog)
  - Bug Fixes (tagged with 'BUG' in the changelog)

Format the output in {'markdown' if output_format == 'markdown' else 'plain text'}.
"""

    try:
        response = client.messages.create(
            model=model,
            max_tokens=1000,
            temperature=0.2,
            system="You are a release notes generator that provides concise, organized and informative summaries of software changes.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        sys.exit(f"Error generating summary with Anthropic API: {e}")

def create_github_release(repo: str, token: str, tag_name: str, name: str, body: str, target_commitish: str = None, draft: bool = False) -> Dict:
    """Create a new release on GitHub with the generated summary."""
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'tag_name': tag_name,
        'name': name if name else tag_name,
        'body': body,
        'draft': draft,
    }

    if target_commitish:
        data['target_commitish'] = target_commitish

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        new_release = response.json()

        return new_release
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error creating GitHub release: {e}")

def main():
    """Main entry point for the script."""
    args = parse_args()

    # Get required tokens
    github_token = get_github_token(args)
    anthropic_api_key = get_anthropic_api_key(args)

    # Fetch existing releases from GitHub
    releases = fetch_github_releases(args.repo, github_token)

    if not releases:
        sys.exit("Error: No existing releases found in the repository.")

    # Get the latest release
    previous_release = releases[0]

    # Prepare data for the new release we're creating
    new_release = {
        'tag_name': args.tag,
        'name': args.name if args.name else args.tag
    }

    print(f"Generating summary for new release: {new_release['name']} (compared to {previous_release['name']})")

    changelog_diff = ""
    try:
        changelog_diff = get_changelog_diff(
            args.repo,
            github_token,
            'HEAD',  # Current state
            previous_release['tag_name']  # Previous release
        )
    except Exception as e:
        print(f"Warning: Could not fetch file diffs: {e}")

    if not changelog_diff:
        sys.exit("No changelog diffs found.")

    # Generate summary using LLM
    summary = generate_llm_summary(
        changelog_diff,
        anthropic_api_key,
        args.model,
        args.format
    )

    # Print the generated summary
    print("\n=== Generated Release Notes ===\n")
    print(summary)
    print("\n==============================\n")

    if args.dry_run:
        print("Dry run mode - not creating GitHub release.")
        return

    # Create the new release on GitHub
    new_release = create_github_release(
        args.repo,
        github_token,
        args.tag,
        args.name,
        summary,
        args.target,
        args.draft,
    )

    print(f"Successfully created new GitHub release: {new_release['html_url']}")

if __name__ == "__main__":
    main()
