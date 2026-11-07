# GitHub Workflows Guidelines

## Security First

- Enforce the Principle of Least Privilege: set `permissions: {}` at workflow level and grant each job only the `GITHUB_TOKEN` permissions it needs.
- Never interpolate `${{ }}` into a `run:` script; pass it via `env:` (e.g. `TITLE: ${{ github.event.pull_request.title }}`) and use `"$TITLE"`.
- Set `persist-credentials: false` on checkout unless the job runs git against the remote after it.
- For multi-line `$GITHUB_OUTPUT` values, use a random delimiter `(EOF_$(openssl rand -hex 16))` and add an echo before the closing delimiter, so the value always ends with a newline.
- Set `timeout-minutes` on every job; add a step-level one on the `claude-code-action` step.
- Optional: use GitHub’s concurrency controls to limit parallel runs.

### GitHub App token

- The [`actions/create-github-app-token`](https://github.com/actions/create-github-app-token/blob/main/README.md) is used to mint a short-lived installation access token for the `ocs-agent` GitHub App.
- By default, the token inherits all of the installation's permissions, so explicitly list the permissions that are required for the action.
- Leave `owner` and `repositories` unset for a current-repository token. For other repositories, list them in `repositories`; never set `owner` alone.
- The workflow's `permissions:` block only governs the default GITHUB_TOKEN. Wherever a step uses the `ocs-agent` token instead, that token's own permissions apply — the `permissions:` block has no effect on it.

## Workflows that call reusable workflows

- Grant the calling job only the permissions the called workflow needs.
- Pass secrets by name under `secrets:`. Never use `secrets: inherit`.

## Workflows using `claude-code-action`

Many workflows use [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action).

### Security

Treat anything Claude reads from an issue, PR, comment, or fetched page as untrusted; keep those workflows' tool lists minimal.

Do deterministic checks (trigger, base branch, changed paths) in shell or `if:` before the Claude step. Give the agent a pass/fail check such as build or lint; if it reads untrusted content, run the check in the workflow and pass only the output.

Render prompt templates with `envsubst` limited to named variables, such as `envsubst '${PR_NUMBER} ${REPO}'`.

Guidance, not requirements:

- If Claude edits files, check the changed paths after the Claude step and fail the job on any path outside the expected set (count a rename as a delete plus an add).
- If the workflow reads untrusted content, avoid giving the Claude job a write token or a push step. Run the push, PR-creation and comment steps in a separate job with its own token and no Claude step. Workflows that need write access by design, such as `claude.yml`, can keep it.

Use these `claude_args` flags:

- `--allowedTools` lists tools Claude can execute without prompting for permission. Claude does not have access to execute arbitrary Bash commands by default so they must be explicitly listed.
- `--max-turns` (optional) limits the number of conversation turns. If you set it, use about 1.5-2x the highest `num_turns` seen across recent successful runs (find it in the raw job log). Re-check it if a run ends early with no result.
- Keep each `--allowedTools` / `--disallowedTools` value on one line, as in the action's configuration docs
- Give each domain its own `WebFetch` entry (`WebFetch(domain:github.com),WebFetch(domain:pypi.org)`); the action splits tool lists on every comma, so `WebFetch(domain:a,domain:b)` breaks into fragments.

### References

- [`claude-code-action` security.md](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) — actor checks, bot triggers, prompt injection and forks
- [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) — flags `claude_args` passes through

## Testing

```bash
uv run prek run actionlint --all-files
```
