<!-- This template will be used for manual creations of PRs -->
<!-- Manually classify if useful with a prefix e.g. [Docs], [AgentOps], [DevOps], [Dev Tooling] or [Widget] -->

## Summary: what and why
<!-- Briefly in 1 sentence describe the goal, reason or impact -->

### Context
<!-- Explain the gap, user problem, issue or product change that prompted this PR. -->
<!-- Examples:
- The current docs are outdated or incorrect and should align with current product
- Existing guidance leads to confusion or incorrect setup.
- The automated processes or tooling need fixes/enhancements for accuracy/maintainability
-->
Related issue:

## Changes

### Scope
<!-- Summarize the actual updates to provide information to the reviewer to make it easier to review the PR -->

### Affected pages / sections

### Out of scope for PR
<!-- Useful to constrain what AI agents surface in PR reviews -->

## Validation manually done
- [ ] Changes follow the relevant page-type contract.
- [ ] Examples and UI features/behavior were manually checked.
- [ ] Internal links and cross-references were manually reviewed for user value.
- [ ] Terminology matches current OCS naming and behavior.
- [ ] Validation commands run are listed below:
  - [ ] `uv run zensical build --clean`
  - [ ] `uv run prek run markdownlint-cli2 --all-files`
  - [ ] `uv run prek run --all-files`
  - [ ] `uv run pytest scripts/tests`

## Risks / Notes / Decisions
<!-- Call out anything reviewers should pay special attention to. -->
<!-- Examples:
- Additional work to be done
- Monitoring of GitHub workflows after release
-->
