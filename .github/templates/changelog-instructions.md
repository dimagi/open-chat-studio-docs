You need to update the changelog and documentation in this repository based on a merged PR from the open-chat-studio repository.

## PR Information
- **PR Number:** #${PR_NUMBER}
- **PR Title:** ${PR_TITLE}
- **PR URL:** ${PR_URL}
- **Author:** ${PR_AUTHOR}
- **Merged Date:** ${PR_MERGED_AT}
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

### Task 2: Update Documentation

#### Decide: does this PR need documentation updates?

| PR type                  | Docs needed?                                         |
|--------------------------|------------------------------------------------------|
| New feature              | Yes                                                  |
| UI changes               | Yes                                                  |
| Configuration changes    | Yes                                                  |
| Behavior changes         | Yes                                                  |
| API changes              | No — skip this task and proceed to commit            |
| Bug fix                  | Usually no — only if behavior or UI visibly changes  |
| Internal / refactoring   | No — skip this task and proceed to commit            |

**When in doubt:** If the PR introduces a new feature and you're unsure whether docs are needed, include them.

#### If yes: act

Invoke the `zensical-technical-writer` agent via the `Task` tool. Give it facts about the change — **do not prescribe a page type or folder**. The agent is a documentation specialist; it will read the existing docs structure and decide the correct page type and location.

Write your prompt like this:

> "Update the documentation for a change to Open Chat Studio.
> **PR URL:** ${PR_URL}
> **What changed:** [1–2 sentences describing the change]
> **Who is affected:** [end users / advanced users / developers / widget integrators]
> **Nature of change:** [new feature / UI change / config change / behavior change / bug fix with visible impact]
> **PR description excerpt:** [paste the most relevant section of the PR body]"

Review the agent's output before committing.

#### If no: skip

Proceed to Task 3. If the changelog was also skipped, do not create a commit — see Task 3 for details.

### Task 3: Commit Changes

If both the changelog and docs were skipped, do not create a commit — the workflow will detect no changes and skip PR creation automatically.

Otherwise, commit your changes with the message:
"update changelog and docs from OCS PR #${PR_NUMBER}"

**IMPORTANT:** Do NOT create a pull request - just commit the changes to this branch. The workflow will create the PR.
