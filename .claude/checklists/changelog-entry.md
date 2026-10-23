# Changelog Entry Checklist

Check only the entry added in this PR.

- [ ] One line, under 700 characters (markdownlint fails at 750).
- [ ] Main (`docs/changelog.md`): under a date heading such as "Oct 9, 2026" (no leading zero), newest first, with one prefix: `**NEW**`, `**CHANGE**`, `**BUG**`, `**MIGRATION**`.
- [ ] Widget (`docs/chat_widget/changelog.md`): a bullet with no prefix under a version heading such as `v0.13.0 (2026-09-16)`.
- [ ] The prefix fits: `MIGRATION` when the reader must act, `CHANGE` for altered behaviour, `NEW` for added capability.
- [ ] A breaking or position-dependent change (renamed, removed, reordered) says what the reader must do.
- [ ] Gated changes name the gate: feature flag, team, or self-hosted only.
- [ ] Bold UI labels, backticked identifiers and flag names match the docs changes in this PR.
- [ ] Links point to an existing file and heading.
- [ ] No internal details (PR numbers, module names) and no mannered prose (see `AGENTS.md`).
