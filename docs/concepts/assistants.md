# OpenAI Assistants

## Archiving

* **Goal: Archiving an assistant in OCS deletes the associated assistant in OpenAI.** This is an easy way to stop incurring costs and ensure that the assistant is closed for all experiments and pipelines that reference it within a project.
- OCS first checks if any published or unreleased experiments and pipelines reference the assistant. If so, the archival process is blocked, and a modal appears listing those experiments and pipelines preventing the archival. If only released versions reference the assistant, they are archived automatically.
- If any published or unreleased experiments reference the assistant, they are listed under the *“Experiments”* section of the modal. For published experiments, navigate to those versions and archive them. For unreleased versions, you must navigate to the version and either (1) remove the assistant reference or (2) archive the experiment.
- If a pipeline that references an assistant is not referenced by an experiment, the pipeline must be archived. These pipelines are listed under the *“Pipelines”* section of the modal. Navigate to the pipeline and either archive it or remove the assistant reference to unblock the assistant archival.
- If a pipeline references an assistant and that pipeline is used by a published experiment, you must archive the experiment. These experiments are listed under the *“Experiments Referencing Pipeline”* section of the modal. The links direct you to the experiments where the pipeline is used. Navigate to the version listed in the modal and archive it.

!!! info "Archiving an assistant with versions"
    If the assistant you are trying to archive has versions, the same checks apply to all versions of the assistant and are displayed together in the modal. Once confirmed, all assistant versions will be archived.
