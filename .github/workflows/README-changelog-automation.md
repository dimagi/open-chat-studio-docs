# Changelog Automation with Claude

This directory contains GitHub Actions workflows that use Claude AI to automatically generate and update changelog entries from merged PRs in the main open-chat-studio repository.

## How It Works

### 1. Dispatch Workflow (open-chat-studio repo)

File: `.github/workflows/docs-changelog-dispatch.yml`

When a PR is merged to `main`:
- Captures the full PR information (title, description, labels, author, etc.)
- Sends a repository dispatch event to the docs repository with all PR metadata

### 2. Claude-Powered Update Workflow (open-chat-studio-docs repo)

File: `.github/workflows/update-changelog.yml`

This workflow:
1. Receives the repository dispatch event with PR information
2. Creates a new branch for the changelog update
3. Invokes Claude AI with detailed instructions to:
   - Read and understand the existing changelog format
   - Analyze the PR title, description, and labels
   - Determine the appropriate changelog type (NEW, CHANGE, BUG, or MIGRATION)
   - Write a clear, concise changelog entry matching the project's style
   - Update `docs/changelog.md` with the new entry under the correct date
4. Claude commits the changes to the branch
5. Creates a PR for review with `@claude` mentioned for further review

## Changelog Format

Changelog entries follow this format:

```markdown
## [Date]
* **[TYPE]** [Description]
```

Example:
```markdown
## Oct 22, 2025
* **NEW** Added support for parallel pipeline execution
* **BUG** Fixed issue with session timeout handling
```

### Changelog Types

- **NEW**: New features or functionality
- **CHANGE**: Modifications to existing features
- **BUG**: Bug fixes
- **MIGRATION**: Migration-related changes or breaking changes

## Benefits of Using Claude

- **Intelligent Analysis**: Claude reads the PR description and understands the context of changes
- **Consistent Style**: Claude matches the tone and format of existing changelog entries
- **Smart Categorization**: Automatically determines if a change is NEW, CHANGE, BUG, or MIGRATION
- **Context-Aware**: Can skip internal/refactoring PRs that don't affect users
- **Quality Review**: The generated PR includes `@claude` for additional review

## Manual Triggering

The `update-changelog.yml` workflow can also be triggered manually via the GitHub Actions UI:

1. Go to Actions → "Update Changelog from OCS PR"
2. Click "Run workflow"
3. Enter the PR number from the open-chat-studio repository
4. Claude will fetch the PR details and generate the changelog entry

## Required Secrets

The workflows require two secrets:

1. **`OCS_DOCS_PAT`**: GitHub Personal Access Token with:
   - `repo` scope (for repository dispatch and PR creation)
   - `workflow` scope (for triggering workflows)
   - Access to both repositories

2. **`ANTHROPIC_API_KEY`**: API key for Claude AI
   - Required for the Claude Code action to generate changelog entries

## How Claude Decides

Claude uses the following criteria to generate changelog entries:

1. **PR Title & Labels**: Looks for keywords like "fix", "add", "update", "migrate"
2. **User Impact Section**: Prioritizes information from the "User Impact" section of the PR template
3. **Description Content**: Analyzes the PR description to understand what changed
4. **Existing Patterns**: Reads existing changelog entries to match style and detail level
5. **Internal Changes**: Can skip purely internal refactoring that doesn't affect users

## Troubleshooting

### No PR created in docs repo

1. Check that the PR was merged (not just closed)
2. Verify both `OCS_DOCS_PAT` and `ANTHROPIC_API_KEY` secrets are configured
3. Check the workflow runs in both repositories for errors
4. Look at the Claude step output to see if it determined the change was internal-only

### Poor changelog quality

1. Review the generated PR - `@claude` is mentioned for easy follow-up review
2. Comment on the PR with `@claude` to request improvements
3. Add more detail to future PR descriptions in the "User Impact" section

### Incorrect date format

The workflow uses the PR merge timestamp. Dates are formatted as "MMM D, YYYY" (e.g., "Oct 22, 2025").

### Duplicate entries

If multiple PRs are merged quickly, they create separate changelog PRs. You can:
- Merge them individually (recommended)
- Ask `@claude` to combine them in one of the PRs
- Manually merge and close the others
