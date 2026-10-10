<!-- This template will be used for manual creations of PRs (human and AI) -->
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
<!-- Summarize the actual updates in this PR to make it easier to review the PR -->

### Affected pages / sections
- Pages:
- Folders:
  - [ ] `docs/tutorials/`
  - [ ] `docs/how-to/`
  - [ ] `docs/concepts/`
  - [ ] `docs/tech-hub/`
  - [ ] `docs/chat_widget/`
- Tooling/processes:

### Out of scope for this PR
<!-- List related work this PR deliberately does not address. Reviewers and AI agents should not raise these. -->

## Validation
- [ ] Examples and UI features/behavior were manually checked.
- [ ] Internal links and cross-references were manually reviewed for user value.
- [ ] Terminology matches current OCS naming and behavior.
- Validation commands run (tick only those you ran):
  - [ ] `uv run zensical build --clean`
  - [ ] `uv run prek run --all-files`
  - [ ] `uv run pytest scripts/tests`

## Risks / Notes / Decisions
<!-- Call out anything reviewers should pay special attention to. -->
<!-- Examples:
- Additional work to be done
- Monitoring of GitHub workflows after release
-->
