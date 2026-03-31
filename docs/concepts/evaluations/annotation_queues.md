# Annotation Queues

**Annotation queues** are a structured way to collect human feedback on chat sessions. They allow team members to review conversation sessions, add annotations, and build labeled datasets for quality assurance or model improvement.

## Overview

An annotation queue is a curated list of chat sessions assigned to one or more reviewers. Reviewers work through the sessions in the queue, reading the conversation content and recording their judgments or labels. Administrators control which sessions are included in a queue and who can review it.

Annotation queues are separate from [Evaluations](./index.md), which use automated evaluators. Queues focus on human review, while evaluations focus on programmatic or LLM-based scoring.

## Roles and Permissions

Two roles interact with annotation queues:

| Action | Super Admin | Annotation Reviewer |
|---|---|---|
| Create and manage queues | Yes | No |
| Add sessions to a queue | Yes | No |
| Assign reviewers to a queue | Yes | No |
| View assigned queues | Yes | Yes |
| View and change queue items | Yes | Yes |
| Add annotations | Yes | Yes |
| View aggregate results | Yes | Yes |
| Export results | Yes | No |

### The Annotation Reviewer role

The **Annotation Reviewer** role grants scoped access limited to annotation queues. Users with this role:

- Can view and annotate only the queues they have been explicitly assigned to.
- Cannot manage queues, add sessions, or export results.
- Cannot access other parts of the application such as experiments, pipelines, or settings.

This role is suited for external reviewers or team members who should only see the conversations relevant to their annotation work.

!!! note "Assigning reviewers"
    Reviewers must be assigned to a specific queue by a Super Admin before they can see it. Being an Annotation Reviewer does not grant access to all queues — only to the queues they are assigned to.

See [User Groups](../team/groups.md) for the full permissions table and instructions on assigning roles.

## Adding Sessions to a Queue

When adding sessions to an annotation queue, you can choose from three selection modes. Open the session list for the relevant experiment, apply any filters you need, and then use the **Add to queue** action to open the selection dialog.

### Selection modes

#### Selected only (default)

Add only the sessions you have individually checked. Use the checkboxes in the session list to mark the sessions you want, then confirm the selection.

This mode is the default and is appropriate when you have a small, specific set of sessions in mind.

#### All matching filters

Add every session that currently matches the active filter criteria. This is a bulk operation — all sessions returned by the current filter will be added to the queue, not just those visible on the current page.

Use this mode when you want to capture a complete filtered set, such as all sessions from a specific date range, channel, or participant.

!!! warning "Confirmation required"
    A confirmation modal is shown before sessions are added when using this mode. Review the session count before confirming, as the operation cannot be selectively undone.

#### Sample

Add a random percentage of sessions from those matching the current filter. A slider lets you choose what proportion to include, from a small fraction up to 100%.

Use this mode when you want a statistically representative sample rather than a complete set — for example, sampling 10% of last month's sessions for a spot-check.

!!! warning "Confirmation required for large samples"
    If the sampled set would include more than 200 sessions, a confirmation modal is shown before the sessions are added.

### Summary of selection modes

| Mode | Sessions added | Best for |
|---|---|---|
| Selected only | Individually checked sessions | Small, hand-picked sets |
| All matching filters | All sessions matching the active filter | Complete filtered sets |
| Sample | A random percentage of filter-matching sessions | Representative sampling |

## Workflow

A typical annotation workflow looks like this:

1. A Super Admin creates an annotation queue and gives it a name and description.
2. The admin adds sessions to the queue using one of the three selection modes.
3. The admin assigns one or more Annotation Reviewers to the queue.
4. Reviewers log in, navigate to their assigned queues, and work through the sessions.
5. Reviewers add annotations to each session.
6. The admin monitors progress and exports results when annotation is complete.
