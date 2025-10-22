# Changelog and Documentation Automation with Claude

This directory contains GitHub Actions workflows that use Claude AI to automatically generate changelog entries **and update documentation** from merged PRs in the main open-chat-studio repository.

## How It Works

### 1. Dispatch Workflow (open-chat-studio repo)

File: `.github/workflows/docs-changelog-dispatch.yml`

When a PR is merged to `main`:
- Captures the full PR information (title, description, labels, author, etc.)
- Sends a repository dispatch event to the docs repository with all PR metadata

### 2. Claude-Powered Update Workflow (open-chat-studio-docs repo)

File: `.github/workflows/update-changelog.yml`

This workflow uses Claude AI to intelligently update both changelog and documentation:

1. **Receives the repository dispatch event** with PR information
2. **Creates a new branch** for the updates
3. **Invokes Claude AI** with detailed instructions to:

   **For Changelog:**
   - Read and understand the existing changelog format
   - Analyze the PR title, description, and labels
   - Determine the appropriate changelog type (NEW, CHANGE, BUG, or MIGRATION)
   - Write a clear, concise changelog entry matching the project's style
   - Update `docs/changelog.md` with the new entry under the correct date

   **For Documentation:**
   - Analyze if the PR introduces changes that require documentation updates
   - For new features: Create user guides, how-tos, or concept documentation
   - For API changes: Update API documentation
   - For behavior changes: Update relevant user guides
   - Use the `mkdocs-technical-writer` agent to handle documentation updates
   - Skip documentation for internal changes or simple bug fixes

4. **Claude commits all changes** to the branch
5. **Creates a PR** with both changelog and documentation updates, including `@claude` for review

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

### For Changelog:
- **Intelligent Analysis**: Claude reads the PR description and understands the context of changes
- **Consistent Style**: Claude matches the tone and format of existing changelog entries
- **Smart Categorization**: Automatically determines if a change is NEW, CHANGE, BUG, or MIGRATION
- **Context-Aware**: Can skip internal/refactoring PRs that don't affect users

### For Documentation:
- **Comprehensive Coverage**: Automatically identifies what documentation needs updating based on PR content
- **Proper Structure**: Uses the mkdocs-technical-writer agent to place docs in the right location
- **User-Focused**: Creates documentation that serves both technical and non-technical audiences
- **Smart Decisions**: Knows when documentation is needed vs when it can be skipped
- **Consistency**: Follows existing documentation patterns and MkDocs structure

### Overall:
- **Zero Manual Work**: Developers don't need to write changelog or documentation updates manually
- **Quality Review**: The generated PR includes `@claude` for additional review and refinement
- **Iterative Improvement**: Can refine both changelog and docs by commenting on the PR

## Manual Triggering

The `update-changelog.yml` workflow can also be triggered manually via the GitHub Actions UI:

1. Go to Actions → "Update Changelog and Docs from OCS PR"
2. Click "Run workflow"
3. Enter the PR number from the open-chat-studio repository
4. Claude will fetch the PR details and generate both changelog and documentation updates as needed

## Required Secrets

The workflows require two secrets:

1. **`OCS_DOCS_PAT`**: GitHub Personal Access Token with:
   - `repo` scope (for repository dispatch and PR creation)
   - `workflow` scope (for triggering workflows)
   - Access to both repositories

2. **`ANTHROPIC_API_KEY`**: API key for Claude AI
   - Required for the Claude Code action to generate changelog entries

## How Claude Decides

### For Changelog Entries:

Claude uses the following criteria to generate changelog entries:

1. **PR Title & Labels**: Looks for keywords like "fix", "add", "update", "migrate"
2. **User Impact Section**: Prioritizes information from the "User Facing Changes" section of the PR template
3. **Description Content**: Analyzes the PR description to understand what changed
4. **Existing Patterns**: Reads existing changelog entries to match style and detail level
5. **Internal Changes**: Can skip purely internal refactoring that doesn't affect users

### For Documentation Updates:

Claude analyzes the PR to determine if documentation is needed:

1. **New Features** → Creates user guides, how-tos, or concept documentation
2. **API Changes** → Updates API reference documentation
3. **Configuration Changes** → Updates setup/configuration docs
4. **Behavior Changes** → Updates relevant user guides and tutorials
5. **Bug Fixes** → Usually skips (unless behavior significantly changes)
6. **Internal/Refactoring** → Skips documentation updates

When documentation is needed, Claude:
- Uses the **mkdocs-technical-writer** agent for quality documentation
- Analyzes existing docs structure to find the right placement
- Follows MkDocs best practices and Open Chat Studio's documentation style
- Creates or updates files as needed
- Can update navigation in `mkdocs.yml` if necessary

## Troubleshooting

### No PR created in docs repo

1. Check that the PR was merged (not just closed)
2. Verify both `OCS_DOCS_PAT` and `ANTHROPIC_API_KEY` secrets are configured
3. Check the workflow runs in both repositories for errors
4. Look at the Claude step output to see if it determined the change was internal-only

### Poor changelog quality

1. Review the generated PR - `@claude` is mentioned for easy follow-up review
2. Comment on the PR with `@claude` to request improvements
3. Add more detail to future PR descriptions in the "User Facing Changes" section

### Missing or incomplete documentation

1. Check if the PR had sufficient details in the "User Facing Changes" section
2. Review the generated PR and comment with `@claude` to request additional documentation
3. For complex features, you may need to manually add more context or examples
4. Use `@claude` to ask for specific documentation sections (e.g., "add a troubleshooting section")

### Documentation in wrong location

1. Comment on the PR with `@claude` explaining where it should be
2. Claude can move/reorganize documentation based on your feedback
3. The mkdocs-technical-writer agent follows existing patterns, so inconsistent structure may confuse it

### Incorrect date format

The workflow uses the PR merge timestamp. Dates are formatted as "MMM D, YYYY" (e.g., "Oct 22, 2025").

### Duplicate entries

If multiple PRs are merged quickly, they create separate changelog PRs. You can:
- Merge them individually (recommended)
- Ask `@claude` to combine them in one of the PRs
- Manually merge and close the others

## Best Practices for Better Results

To help Claude generate high-quality changelog entries and documentation:

### In Your PRs:

1. **Write Clear PR Titles**: Use descriptive titles that explain what changed
   - ✅ "Add parallel pipeline execution support"
   - ❌ "Fix issue #123"

2. **Fill Out User Facing Changes**: This is the most important section
   - Describe what changed from the user's perspective
   - Include screenshots or examples for UI changes
   - Mention any breaking changes or migrations needed

3. **Use Labels**: Add appropriate labels (feature, bug, enhancement, etc.)
   - Labels help Claude categorize the change correctly

4. **Link to Related Issues**: Include context about why the change was made
   - Helps Claude understand the full story

5. **Document Complex Features**: For significant features, provide:
   - Use cases and examples
   - Configuration options
   - Known limitations

### After the PR is Created:

1. **Review the Generated PR**: Claude generates a PR with both changelog and docs
2. **Provide Feedback**: Use `@claude` to request improvements or additions
3. **Iterate**: Claude can refine based on your comments
4. **Merge When Ready**: Once satisfied, merge the docs PR

Following these practices will result in better automated documentation and save everyone time! 🎉
