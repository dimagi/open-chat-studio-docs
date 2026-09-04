# GitHub Workflows Guidelines

## Security First

- Enforce the Principle of Least Privilege by starting with the most restrictive `permissions:` to modify permissions for the GITHUB_TOKEN
- Store untrusted values in an intermediate env var, like `TITLE: ${{ github.event.pull_request.title }}`.
- Never interpolate ${{ }} directly into a `run:` script
- Set `persist-credentials: false` on checkout unless the job runs git against the remote after it.
- Set workflow-level timeouts to avoid runaway jobs
- Use GitHub’s concurrency controls to limit parallel runs

### GitHub App token

- The [`actions/create-github-app-token`](https://github.com/actions/create-github-app-token/blob/main/README.md) is used to mint a short-lived installation access token for the `ocs-agent` GitHub App.
- By default, the token inherits all of the installation's permissions, so explicitly list the permissions that are required for the action.
- The workflow's `permissions:` block only governs the default GITHUB_TOKEN. Wherever a step uses the `ocs-agent` token instead, that token's own permissions apply — the `permissions:` block has no effect on it.

## Workflows using `claude-code-action`

Many workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action).

### References

- [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action):
  [security.md](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) for
  actor checks, bot triggers, prompt injection and forks;
- [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) — flags `claude_args` passes through

### Security

Treat anything Claude reads from an issue, PR, comment, or fetched page as untrusted; keep those workflows' tool lists minimal.

Use these `claude_args` flags:
- `--allowedTools` lists tools Claude can execute without prompting for permission. Claude does not have access to execute arbitrary Bash commands by default so they must be explicitly listed.
- `--max-turns` limit the number of conversation turns

## Testing

```bash
uv run prek run actionlint --all-files
```
