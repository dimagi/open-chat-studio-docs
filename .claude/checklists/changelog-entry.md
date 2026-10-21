# Changelog Entry Checklist

- [ ] One entry added, as one line of 1-2 sentences, under 700 characters (markdownlint fails at 750).
- [ ] Main changelog (`docs/changelog.md`): under a date heading ("Oct 9, 2025", no leading zero), newest date first, with one prefix: `**NEW**`, `**CHANGE**`, `**BUG**`, `**MIGRATION**`.
- [ ] Widget changelog (`docs/chat_widget/changelog.md`): under a version heading, with no date and no prefix.
- [ ] Active voice: "Added support for..." not "Support was added for...".
- [ ] A user can tell what changed and whether they need to act; internal details only if they affect users.
- [ ] Detail better suited to a docs page (many options, limits or UI elements) is linked, not listed, and the link target exists.
- [ ] Matches the style and tone of existing entries and is consistent with the docs changes in the same PR.
- [ ] No mannered prose (see `AGENTS.md`): no metaphor or flourish where a literal phrase says it directly.
