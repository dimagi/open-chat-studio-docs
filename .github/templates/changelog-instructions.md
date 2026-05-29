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

#### Decide: does this PR need documentation updates?

| PR type                  | Docs needed?                                          |
|--------------------------|-------------------------------------------------------|
| New feature              | Yes — concept and/or how-to pages                    |
| UI changes / demo        | Yes — update relevant user guides or how-tos         |
| Configuration changes    | Yes — update how-to pages with code examples in tech hub    |
| Behavior changes         | Yes — update relevant user guides                    |
| API changes              | Yes — update API documentation                       |
| Bug fix                  | Usually no — only if behavior or UI visibly changes  |
| Internal / refactoring   | No — skip this task and proceed to commit            |

#### If yes: act

Invoke the `zensical-technical-writer` agent via the `Task` tool. Write your prompt to the agent like this:

> "Update the documentation for a change to Open Chat Studio.
> **What changed:** [1–2 sentences from the PR]
> **Doc type affected:** [concept / how-to / configuration / tech hub / API]
> **PR description excerpt:** [paste the most relevant section]"

The agent will find the right place in the docs structure and update accordingly. Review its output before committing.

### Task 3: Commit Changes

After completing the above tasks, commit your changes with the message:
"update changelog and docs from OCS PR #${PR_NUMBER}"

**IMPORTANT:** Do NOT create a pull request - just commit the changes to this branch. The workflow will create the PR.

## Important Guidelines

- Focus on user-facing changes
- Be clear and concise in both changelog and documentation
- Match the style of existing content
