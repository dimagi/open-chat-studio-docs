You need to update the changelog and documentation in this repository based on a merged PR from the open-chat-studio repository.

## PR Information
- **PR Number:** #${PR_NUMBER}
- **PR Title:** ${PR_TITLE}
- **PR URL:** ${PR_URL}
- **Author:** ${PR_AUTHOR}
- **Merged Date:** ${PR_MERGED_AT}
- **Labels:** ${PR_LABELS}
- **Is Widget Change:** ${IS_WIDGET_CHANGE}
- **Base Branch:** ${BASE_BRANCH}

## PR Description
```
${PR_BODY}
```

## Important Context
${CONTEXT_MESSAGE}

## Your Tasks

### Task 1: Update Changelog

**IMPORTANT: The changelog file to update depends on whether this is a widget change:**

${CHANGELOG_INSTRUCTIONS}

**General Changelog Guidelines (both types):**
- Be concise but informative
- Focus on user-facing changes
- Use active voice (e.g., "Added support for..." not "Support was added for...")
- Don't include internal implementation details unless they affect users
- Match the style and tone of existing changelog entries
- If the PR is purely internal/refactoring with no user impact, you can skip the changelog entry
- **However:** Still proceed to Task 2 to check if documentation updates are needed
- If both changelog AND docs are skipped, do not create a commit - the workflow will detect no changes and skip PR creation

### Task 2: Update Documentation

After updating the changelog, analyze whether this PR requires documentation updates:

1. **Check if documentation is needed:**
   - New features → Need user guides, how-tos, or concept docs
   - API changes → Update API documentation
   - Configuration changes → Update setup/configuration docs
   - Behavior changes → Update relevant user guides
   - Bug fixes → Usually no docs needed unless it changes behavior
   - Internal/refactoring → Skip documentation updates

2. **If documentation IS needed:**
   - Use the "mkdocs-technical-writer" agent to handle the documentation updates
   - Provide the agent with:
     * What changed (from the PR)
     * What documentation needs to be created or updated
     * Context from the PR description
   - The agent will find the right place in the docs structure and update accordingly
   - Review the agent's output to ensure quality

3. **If documentation is NOT needed:**
   - Simply skip this task and proceed to commit

### Task 3: Commit Changes

After completing the above tasks, commit your changes with the message:
"update changelog and docs from OCS PR #${PR_NUMBER}"

**IMPORTANT:** Do NOT create a pull request - just commit the changes to this branch. The workflow will create the PR.

## Important Guidelines

- Focus on user-facing changes
- Be clear and concise in both changelog and documentation
- Match the style of existing content
- If unsure whether docs are needed, err on the side of including them for NEW features
- For CHANGE and BUG types, docs updates are usually optional unless behavior significantly changes
