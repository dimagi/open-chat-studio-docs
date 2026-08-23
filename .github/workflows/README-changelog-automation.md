# Changelog and User Doc Automation with Claude

This page is for maintainers of the [user documentation and changelog process](https://developers.openchatstudio.com/developer_guides/user_docs/) that keeps user-facing documentation and changelog entries aligned after code PRs are merged in the OCS repo.

`update-changelog.yml` and the dispatch workflow in the [OCS repo](https://github.com/dimagi/open-chat-studio/tree/main/.github/workflows) work together: the source workflow sends PR context to this docs repo, where `update-changelog.yml` runs the pipeline below.

## Pipeline

| Stage | What happens |
|---|---|
| **1. Trigger** | An OCS PR merges, or a maintainer runs it manually — see the workflow's header comment for exact trigger conditions. |
| **2. Classify & branch** | Detects whether the PR touches `components/` (widget) to pick the base branch (`main` or `widget-develop`), then creates a working branch `changelog-pr-<pr>-<run>`. |
| **3. Build instructions** | Renders [`changelog-instructions.md`](../templates/changelog-instructions.md) with the PR's title/body/author/widget-flag, pulling in the matching changelog-section template. |
| **4. Run Claude** | Claude updates the changelog directly, invoking [`zensical-technical-writer`](../../.claude/agents/zensical-technical-writer.md) if the PR also needs docs changes. |
| **5. Open PR** | Workflow (not Claude) opens the PR, titled by what changed (Changelog / Changelog + Docs / `[Widget]` prefix). |

## Maintenance Notes

Where to make changes:

- **Prompt and task logic** — `.github/templates/changelog-instructions.md` and the `main-changelog-section.md` / `widget-changelog-section.md` templates it pulls in (Pipeline stage 3 above).
- **Documentation-writing behavior** — `.claude/agents/zensical-technical-writer.md` (Pipeline stage 4 above). This agent is shared with the manual `/write-docs` command — see [README-claude-workflows.md#github-workflows](README-claude-workflows.md#github-workflows) for how it's used elsewhere.

Behavior changes often require touching both `.github/templates/` and `.claude/agents/` together.

### Repositories in Scope

Troubleshooting and process changes can involve both repositories:

- **Source repo:** `dimagi/open-chat-studio` (dispatch workflow source)
- **Receiving repo:** this docs repo

### Required Secrets

See the Requirements: line in the workflow file's header comment.

## Troubleshooting

See [README-claude-workflows.md#troubleshooting](README-claude-workflows.md#troubleshooting) for
issues common to all Claude workflows (auth failures, fork PRs, output quality).

Specific to`update-changelog.yml`:

- **Manual trigger:** Open GitHub Actions, select `Update Changelog and Docs from OCS PR`, and enter the OCS PR number. Safe to rerun for the same PR.
- **No PR created:** Check workflow runs in both repositories.
- **Unexpected target branch or classification:** Check workflow logs in the source and receiving repos to verify how the PR was classified.
- **widget-develop branch missing:** Handled automatically — the workflow creates it from `main` before pushing. If that push fails (e.g. branch protection), create it manually: `git checkout -b widget-develop main && git push origin widget-develop`. See [Developer guide with details on branching and app/widget release flow](https://developers.openchatstudio.com/developer_guides/user_docs/)
