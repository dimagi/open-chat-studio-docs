# GitHub Workflows Guidelines

For AI coding agents working in `.github/workflows/`. Many workflows run the
`anthropics/claude-code-action` custom action. Operator docs, and how `.claude/commands` and `.claude/agents` fit in, are in [README-claude-workflows.md](README-claude-workflows.md).

## Reference docs

- [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action):
  [security.md](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) for
  actor checks, bot triggers, prompt injection and forks;
  [configuration.md](https://github.com/anthropics/claude-code-action/blob/main/docs/configuration.md)
  for `claude_args` and the tool flags
- [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) — flags `claude_args` passes through

## Rules

Getting `permissions:` or the Claude tool list wrong is how a hostile issue body, PR body, or release note takes unintended action — treat changes to either as security-sensitive.

### Any workflow

- Start from `permissions: {}`, granting scopes per job, and trace whether each is really consumed
  by the default `GITHUB_TOKEN` — a step passing its own `token:`/`github_token:`/`GH_TOKEN:` never
  touches it. `token:` is the key `actions/checkout` and `peter-evans/create-pull-request` use.
- `permissions:` is bypassed wherever the custom `ocs-agent` GitHub App mints an installation token:
  its writes come from the App's own grant (org Settings → GitHub Apps) and land as `ocs-agent[bot]`.
- Set `persist-credentials: false` on checkout unless the job runs git against the remote after it.

### Workflows using `claude-code-action`

- `--allowedTools` lists tools Claude can call without being denied — there are no permission prompts in GitHub Actions. Never infer a workflow is read-only from this list.
- Bash is the exception, and why the list matters: this action disables Bash by default, so a
  workflow's `Bash(...)` patterns are that run's entire shell surface.
- Treat anything Claude reads from an issue, PR, comment, or fetched page as untrusted; keep those workflows' tool lists minimal.

## Local testing

Run before committing workflow changes:

```bash
uv run prek run actionlint --all-files
```
