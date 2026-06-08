# Open Chat Studio Documentation

User documentation site for [Open Chat Studio](https://github.com/dimagi/open-chat-studio).
Built with [Zensical](https://zensical.org/) (MkDocs-compatible), Python 3.13+, managed with `uv`.

## Commands

```bash
uv sync                                  # Install / sync dependencies
uv run zensical serve                    # Local dev server (auto-reload)
uv run zensical build --clean --strict   # Same build CI runs — fails on broken refs
uv run pytest scripts/tests              # Run the (small) test suite for scripts/
```

Do **not** invoke `mkdocs` directly — the project uses Zensical, which reads `mkdocs.yml`
for compatibility but ships its own CLI.

## Architecture

- `docs/` — All site content (markdown). Navigation declared in `mkdocs.yml`.
- `mkdocs.yml` — Site config (theme, plugins, nav). Zensical-compatible MkDocs format.
- `overrides/` — Theme template overrides (Material for MkDocs).
- `src/ocs_docs/openapi_to_docs.py` — Converts the OCS OpenAPI schema into markdown
  under `docs/api/`. Run by the `update-api-docs` workflow; `docs/api/` is generated —
  do not hand-edit.
- `src/python_node/` — Source for Python-node API reference (rendered via `mkdocstrings`).
- `scripts/update_confluence_release.py` — Publishes release rows to a Confluence page
  (used by the `update-confluence` workflow).
- `.github/workflows/update-changelog.yml` — Listens for `repository_dispatch` from the
  OCS repo and opens a PR updating `docs/changelog.md` (or `docs/chat_widget/changelog.md`
  for widget PRs) using `.github/templates/changelog-instructions.md`.

## Page-Type Conventions

Each top-level docs folder has a strict content contract — keep content in the right place:

| Folder           | Audience              | Contains                                | Must not contain                  |
|------------------|-----------------------|-----------------------------------------|-----------------------------------|
| `tutorials/`     | First-time users      | Guided, end-to-end walkthroughs         | Advanced config, code, references |
| `how-to/`        | All users             | Task-focused step-by-steps              | Deep code snippets, architecture  |
| `concepts/`      | All users             | "What" and "why" explanations           | API/code, jargon                  |
| `tech-hub/`      | Developers / advanced | API refs, code, advanced config         | Concept recap (link instead)      |
| `chat_widget/`   | Widget integrators    | Widget-only reference and integration   | General OCS user content          |

Full guidelines: `.claude/agents/zensical-technical-writer.md`. Prefer the
`zensical-technical-writer` agent (via `/write-docs`) for non-trivial doc work.

## Branch Workflow

- **Default base = `main`.** Most doc changes target `main`.
- **Widget docs base = `widget-develop`.** Anything under `docs/chat_widget/` (and its
  assets) ships on the widget release cadence. Branch from and PR into `widget-develop`;
  release managers merge it back to `main` during the widget release.
- Don't mix widget and non-widget changes in one PR — they go to different bases.

## Changelog

`docs/changelog.md` (main) and `docs/chat_widget/changelog.md` (widget) use date-grouped
entries with category prefixes: `**NEW**`, `**CHANGE**`, `**BUG**`, `**MIGRATION**`.

Changelog updates are largely automated — the `update-changelog` workflow opens a PR
when an upstream OCS PR is merged. Manual edits are fine but should match the existing
style.

## Releases

Use `/create-release <tag> <title>` to draft a GitHub release from the diff of
`docs/changelog.md` since the last release. The command groups entries by category
and produces a markdown summary. Releases are created as drafts.

## Gotchas

- `zensical build --strict` (CI) fails on broken internal links — `serve` does not.
  Run the strict build locally before pushing if you've added cross-references.
- `docs/api/` is regenerated from OpenAPI by the `update-api-docs` workflow. Don't hand-edit.
- `uv` self-ignores `.venv/` and `.cache/` by dropping `.gitignore` files inside them,
  so the repo `.gitignore` doesn't need entries for those.

## Custom Tooling

- `/write-docs` — Launches `zensical-technical-writer` agent with proper context.
- `/create-release <tag> <title>` — Drafts a GitHub release from changelog diff.
- `/review-pr` — Project's PR review workflow.
- `documentation-pr-reviewer` agent — Specialised reviewer for docs PRs.
