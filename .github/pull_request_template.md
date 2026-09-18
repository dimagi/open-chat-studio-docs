<!-- Classify by using a prefix i.e.: [Docs], [AgentOps] [DevOps] [Dev Tooling] or [Widget Docs]-->

## Summary: what and why
<!-- Briefly in 1 sentence describe the goal, reason or impact -->

### Context
<!-- Explain the gap, user problem, issue or product change that prompted this PR. -->
<!-- Examples:
- The current docs are outdated or incorrect and should align with current product behavior or release state
- A workflow is missing or unclear.
- Existing guidance leads to confusion or incorrect setup.
- The automated processes or tooling need fixes/enhancements for accuracy/maintainability
-->
Related issue: #xyz

## Changes

### Scope
Added / revised / separated / simplified
<!-- Summarize the actual update.
- Updated examples, screenshots, navigation, or configuration
- Fixed terminology, accuracy, duplication or cross-references
- Clarified workflow or product behavior
-->

### Affected pages / sections
<!-- List the page(s), section(s), or folders affected. -->
- Page(s) / section(s):
- Folder(s):
  - [ ] `docs/tutorials/`
  - [ ] `docs/how-to/`
  - [ ] `docs/concepts/`
  - [ ] `docs/tech-hub/`
  - [ ] `docs/chat_widget/` — base must be `widget-develop`, not `main`, and must not be mixed with the folders above  
- Automated process(s):

### Decisions and what not addressed in this PR
<!-- Useful to constrain what AI agent PR reviews cover to keep PR scope from growing. -->

## Validation
- [ ] This follows the relevant page-type contract.
- [ ] Examples and UI features/behaviour were manually checked.
- [ ] Internal links and cross-references were manually reviewed for user value.
- [ ] Terminology matches current OCS naming and behavior.
- [ ] Validation commands run are listed below:
  - [ ] `uv run zensical build --clean`
  - [ ] `uv run prek run markdownlint-cli2 --all-files`
  - [ ] `uv run prek run --all-files`
  - [ ] `uv run pytest scripts/tests`

## Risks / notes
<!-- Call out anything reviewers should pay special attention to. -->
<!-- Examples:
- Additional work to be done
- Monitoring of GitHub workflows needed
-->
