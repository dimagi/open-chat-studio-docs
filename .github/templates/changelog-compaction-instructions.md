You are compacting the Open Chat Studio changelog at `${CHANGELOG_FILE}` to keep its
length manageable. Recent history stays verbatim; older history is condensed into a
single summary per month.

## Retention rule

- **Keep verbatim** every entry dated on or after **${CUTOFF_HUMAN}**. These are the
  three most recent months (${KEEP_MONTHS}) — do not touch their headings or bullets.
- **Summarize** every entry dated *before* **${CUTOFF_HUMAN}**.

## How to summarize an older month

For each calendar month earlier than the cutoff, replace all of its per-day sections
(e.g. `## May 18, 2026`, `## May 15, 2026`, …) with a **single** section headed by the
month and year only. Use the **abbreviated month** form to match the file's existing
day headings (`## Jun 22, 2026` → `## Jun 2026`, `## Apr 8, 2026` → `## Apr 2026`):

```markdown
## May 2026
```

Under that heading, write a concise summary (typically 1–4 sentences, prose) of what
changed that month. Guidelines:

- Lead with the most significant user-facing changes (new features, behaviour changes).
- Group related items rather than listing every bullet.
- **Always preserve** breaking changes, deprecations, removal/sunset dates, and
  `**MIGRATION**` notes explicitly — these must not be lost in summarization.
- Match the existing tone: active voice, user-facing framing, no internal detail.
- Keep meaningful inline links (e.g. to deprecation successors or guides) where they
  add value.

## Hard constraints

- Preserve the YAML frontmatter, the `# Changelog` title, the `!!! info` admonition, and
  the trailing `---` plus the "older entries … GitHub release notes" footer line exactly.
- Keep all sections in reverse chronological order (newest first).
- **Idempotency:** a month already collapsed to a `## <Month> <Year>` heading (no day in
  the heading) is already summarized — leave it unchanged. Only collapse months that
  still have per-day sections and fall before the cutoff.
- Edit **only** `${CHANGELOG_FILE}`. Do not create a commit or a pull request — the
  workflow handles that.
