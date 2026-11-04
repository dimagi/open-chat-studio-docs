# Creating and Publishing Chatbot Versions

These steps explain how to create and publish chatbot versions, so you can keep editing without affecting participants.
They illustrate the [Versioning](../concepts/versioning.md) feature.

When a chatbot is first created, it has two versions: a published version and an unreleased version, as shown below.

![Chatbot Version Table](images/version_table_after_exp_creation.png)

## Step 1: Edit your chatbot

Open your chatbot and make your changes in the [pipeline editor](../concepts/pipelines/index.md).
All edits apply to the unreleased version.

## Step 2: Create a new version

When you have tested the chatbot and are ready to publish it to your participants, create a new version.
To do this, click the **Create Version** button in the versions table.

## Step 3: Review and save the version

You will be taken to the create new version page, which shows you the difference between the most recent version and the unreleased version.
The most recent version may be different from the currently published version.

Pressing the **Create** button saves the current configuration of the chatbot and allocates it a version number.

Here you can:

- Add a description to help identify what changed.
- Check **Set as Published Version** to make this version live immediately.
  If you skip this checkbox, the version is saved but not yet published.
  You can publish it later in Step 5.

![Create new Chatbot Version View](images/version_create_view.png)

## Step 4: Confirm and test the version

You will be directed back to the versions table.
It may take a few minutes for the new version to be fully available and listed in the table.
From the table, you can select which Chatbot version you want to open a web chat with for testing.

## Step 5: Publish the version

Click **View Details** on any version to see its summary and set it as published or archive it.
Click the **Set as Published Version** button at the bottom of the dialog.

![Chatbot Version Action Buttons](images/version_details_action_button.png)

## Step 6: Check what version is published

To see which version is currently published, look for the green version badge.
It is next to the chatbot name at the top of the chatbot home screen.
In the example below, "v2" is the published version.
You can also confirm this in the table by looking for the checkmark in the published row.

![Chatbot version table showing published version badge](images/version_table_after.png)

## Step 7: Revert to a previous version

If you need to go back to an older configuration, click **Revert**.

A confirmation modal opens showing the differences between your current working state and the target version.
See [The revert confirmation modal](../concepts/versioning.md#the-revert-confirmation-modal) for details.

!!! warning "Check for unreleased changes before reverting"
    If your working state has unsaved edits, the modal warns that reverting permanently overwrites them.
    Create a new version first to keep them.

After reviewing the diff, click **Revert to vN** (where N is the version number).
This replaces your working state with a copy of the selected version.
The reverted configuration becomes your new unreleased version, which you can edit or publish following Steps 2–5 above.

## Next steps

[Deploy your chatbot to a channel](../how-to/channels/deploy_to_different_channels.md) so participants can use the published version.

## See also

- [Versioning](../concepts/versioning.md)
- [Configure an LLM Node](configure_llm_node.md)
