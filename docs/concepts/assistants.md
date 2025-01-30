# OpenAI Assistants

## Syncing with OpenAI
The in-sync status with OpenAI is automatically checked each time a user visits the edit screen of an assistant. If the assistant in OCS has the identical configurations and files with the assistant in Open AI, the an in-sync status will appear under the assistant id:
![In Sync Status](images/open_ai_assistant_in_sync_status.png)

Otherwise, a warning will be displayed explaining what is out of sync. For example, in the image below, there are files uploaded in OpenAI that are not uploaded in OCS. This may result in unexpected behavior from the assistant. To resolve, upload the listed files in the edit screen.
![Sync Warning](images/open_ai_assistant_out_of_sync_warning.png)

!!! warning "Assistants in versioned experiments"

    Although an assistant cannot be modified in OCS once an experiment is released that references that assistant, it can still be modified in OpenAI. A new assistant in OpenAI will be created at the time of the experiment's release, and *it is recommended not to modify that assistant to maintain the expected functionality of the released experiment*.


## Archiving

* **Goal: Archiving an assistant in OCS deletes the associated assistant in OpenAI.** This is an easy way to stop incurring costs and ensure that the assistant is closed for all experiments and pipelines that reference it within a project.
- OCS first checks if any published or unreleased experiments and pipelines reference the assistant. If so, the archival process is blocked, and a modal appears listing those experiments and pipelines preventing the archival. If only released versions reference the assistant, they are archived automatically.
- If any published or unreleased experiments reference the assistant, they are listed under the *“Experiments”* section of the modal. For published experiments, navigate to those versions and archive them. For unreleased versions, you must navigate to the version and either (1) remove the assistant reference or (2) archive the experiment.
- If a pipeline that references an assistant is not referenced by an experiment, the pipeline must be archived. These pipelines are listed under the *“Pipelines”* section of the modal. Navigate to the pipeline and either archive it or remove the assistant reference to unblock the assistant archival.
- If a pipeline references an assistant and that pipeline is used by a published experiment, you must archive the experiment. These experiments are listed under the *“Experiments Referencing Pipeline”* section of the modal. The links direct you to the experiments where the pipeline is used. Navigate to the version listed in the modal and archive it.

!!! info "Archiving an assistant with versions"
    If the assistant you are trying to archive has versions, the same checks apply to all versions of the assistant and are displayed together in the modal. Once confirmed, all assistant versions will be archived.
