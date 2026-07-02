# Versioning

Versioning keeps your live chatbot stable while you make changes. You can edit and test your chatbot without impacting your users. For more details, see the tutorial on [creating and publishing versions](../tutorials/versioning_steps.md).

Versioning tracks the history of your chatbot's configuration so you can review what changed, and roll back to a previous version if needed.

## Terminology

* *Unreleased Version*. This is the version of the chatbot you are currently editing. It is a draft that has not been versioned or published.

* *Published Version*. This is the version that users will interact with — through the web, WhatsApp, or any other channel you have set up, including the public link.

## What is a Chatbot Version?

Once a version is created, it cannot be edited or modified. This ensures that the users' experience remains stable even if chatbot editors are changing the unreleased version.

### What is frozen — and what is live

Most of a published version's configuration is frozen at publish time. One exception is **collection content**:

- Changes to files in a linked [media collection](collections/media.md) — such as adding, removing, or replacing files — are reflected immediately in the published bot.
- Scheduled [document-source syncs](collections/indexed.md#document-sources-for-indexed-collections) to a linked RAG index collection are also applied to the published bot as they run.

The collection *structure* (which collections are linked to which nodes) remains part of the frozen version. Only the *content* of those collections is treated as a live shared resource.

!!! note "What this means for drift detection"
    Because collection content is live, adding files to a collection or waiting for a document-source sync no longer marks your bot as having unpublished changes. Only changes to the bot's pipeline configuration and settings are tracked as pending changes.

!!! warning "Existing published bots"
    This live-collection behaviour applies to bots republished after this change was introduced (2026-06-03). Bots that were published before retain their previous frozen collection snapshot until the next time they are republished.

## Chatting to the unreleased version
For testing, if you want to chat with the unreleased draft chatbot, go to the chatbot home page and click the speech bubble icon in the top-right corner. In the dropdown, select "Unreleased Version" instead of "Published Version" to open a web chat.

When chatting with an unpublished version, a banner will appear indicating that it is not the published version and showing the version number.

![Web chat unpublished version banner](images/version_web_chat.png)

Only bot editors can chat with the unreleased version because it is not available through [channels](channels.md).

!!! note "Behavior before versioning"
    Previously, all channels always used the unreleased version.

## Changing the Published Version

The published version can be selected from any of the Chatbot versions, enabling rollback to a previous version.
Only one version can be the published version at a time.

To publish a version, follow the tutorial on [creating and publishing versions](../tutorials/versioning_steps.md).

## Reverting to a Previous Version

Reverting replaces your current working (unreleased) state with a copy of an older version's configuration. The older version itself is not modified — a fresh copy becomes your new working state, ready to edit or publish.

### The revert confirmation modal

When you click **Revert** on a version, a confirmation modal opens instead of a plain confirm dialog. The modal shows a field- and node-level diff so you can see exactly what will change before committing. Added fields are highlighted and removed fields are marked, giving you a clear picture of the differences between your current working state and the target version.

### Warning for unreleased changes

If your current working version contains changes that have not yet been released (that is, they do not belong to any saved version), a warning appears in the modal. The warning tells you that reverting will overwrite those unreleased changes permanently. Review the diff carefully before confirming if you see this warning.

!!! warning "Unreleased changes are permanently lost on revert"
    Once you confirm a revert, any edits in the unreleased working state that are not part of a saved version cannot be recovered. Create a new version first if you want to preserve those changes.

## Versioning for OpenAI Assistants

!!! info "Versioning chatbots that use OpenAI Assistants"
    Yes, this is supported. When a new version is saved for a chatbot that uses an OpenAI Assistant, a snapshot copy of that assistant is automatically created — no extra setup needed. The original assistant remains available and can still be updated in the unreleased version.

!!! warning "Modifying Assistants in OpenAI referenced by released versions"

    As mentioned above, the copied assistant will be read-only in OCS, however, in OpenAI changes can still be made to that copy of the assistant. *We recommend advising your team to not modify this assistant if it references a released version.* This can cause unexpected behavior to the version and to its end users. To ensure that the released version acts as expected this assistant should remain as-is.
