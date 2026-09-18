
<!-- Classify by prefixing the PR name with: [Docs], [AgentOps] [DevOps] or [Dev Tooling] -->

## Summary
<!-- Briefly describe the goal, reason or impact -->

### Context
<!-- Explain the gap, user problem, issue or product change that prompted this PR. -->
<!-- Examples:
- The current docs are outdated or incorrect and should align with current product behavior or release state
- A workflow is missing or unclear.
- A new feature needs documentation.
- Existing guidance leads to confusion or incorrect setup.
- The docs should align with current product behavior or release state
- The automated processes or tooling need fixes/enhancements for accuracy/maintainability
-->
This resolves: Issue #

## Affected pages / sections
<!-- List the page(s), section(s), or folders affected. -->
- Page(s) / section(s):
- Folder(s):
  - [ ] `docs/tutorials/`
  - [ ] `docs/how-to/`
  - [ ] `docs/concepts/`
  - [ ] `docs/tech-hub/`
  - [ ] `docs/chat_widget/`
- Automated process(s):

### What changed
<!-- Summarize the actual update. -->
- Added / revised / separated / simplified:
- Updated examples, screenshots, navigation, or configuration
- Fixed terminology, accuracy, duplication or cross-references
- Clarified workflow or product behavior

### Decisions and what not addressed in this PR
<!-- Useful to constrain what AI agent PR reviews cover to keep PR scope from growing. -->

## Validation
- [ ] This follows the relevant page-type contract.
- [ ] Examples and UI features/behaviour were manually checked.
- [ ] Internal links and cross-references were manually reviewed for user value.
- [ ] Terminology matches current OCS naming and behavior.
- [ ] I/Claude ran the relevant validation:
  - [ ] `uv run zensical build --clean`
  - [ ] `uv run prek run markdownlint-cli2 --all-files`
  - [ ] `uv run prek run --all-files`
  - [ ] `uv run pytest scripts/tests`

## Risks / notes
<!-- Call out anything reviewers should pay special attention to. -->
<!-- Examples:
- Additional work to be done
- Docs generated using /write-docs and not manually reviewed
- Cross-reference or nav updates may need follow-up
- Monitoring of GitHub workflows needed
-->
