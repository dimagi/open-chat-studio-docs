# Search and Get Prompt Help in the Pipeline Editor

This guide explains how to find text across the nodes of a pipeline, refer to enabled tools by name in an LLM prompt, and ask an AI assistant to review a prompt.

## Prerequisites

- A [pipeline](../concepts/pipelines/index.md) with at least one [node](../concepts/pipelines/nodes.md).
- For prompt help: your server administrator has configured the system agent models (`SYSTEM_AGENT_MODELS_HIGH`, `SYSTEM_AGENT_MODELS_LOW`, and `SYSTEM_AGENT_API_KEYS`).

## Find text in a pipeline

Find in pipeline searches the text written on every node: prompts, code, templates, router keywords, node names, and node IDs.
Hidden fields and select fields are not searched.

1. Select the magnifying glass button next to the add and test buttons on the canvas, or press **Ctrl+F** (**Cmd+F** on macOS).
2. Type the text to find.
3. Choose a result with the arrow keys and **Enter**, or click it.

The editor selects the node, brings it into view, opens its editor, and briefly highlights the matching field.
Results are ordered by canvas position, from left to right and then top to bottom.

Find in pipeline also works when you view a published version.

!!! note

    When your cursor is inside an input or code editor, **Ctrl+F** opens that editor's own search instead.
    Click the canvas first to open Find in pipeline.

## Refer to tools by name in an LLM prompt

While you write the prompt of an LLM node, the editor suggests the names of the [tools](../concepts/tools/index.md) enabled on that node.
These include agent tools, custom actions, MCP tools, file search, and attach-media.

1. Enable the tool on the LLM node.
2. In the prompt, start typing the tool name.
3. Press **Enter** to insert the suggested name.

The name is inserted as plain text, so the prompt refers to the tool exactly as the model sees it.
A suggestion appears when what you type matches the start of the name or the start of any part of the name separated by `-` or `_`.
For example, with One-off Reminder enabled, typing `one` or `remind` suggests `one-off-reminder`.

Built-in provider tools, such as web search and code execution, are not suggested because they have no name the model can refer to.
File search is suggested only for local collection indexes, not remote ones.

## Ask for prompt help

The LLM node and the [Router node](../concepts/pipelines/router_nodes.md) prompt editors have a **Help** button.
It asks an AI assistant to review the prompt and suggest a revision.

1. Open the node and select **Help** in the prompt editor.
2. Optionally, enter an instruction, such as "make it formal".
3. Select **Improve**.
4. Review the revised prompt, shown as a diff with short notes on each change.
5. Edit the revision if needed, then accept or reject it.

The revision keeps exactly the same [prompt variables](../concepts/prompt_variables.md) as the original and uses only variables allowed for that node type.
If the assistant cannot produce a valid revision, it returns the original prompt with a note that explains why.

## Common issues

- **Help is unavailable or returns an error.** Ask your server administrator to confirm the system agent models are configured.
- **Find in pipeline does not match a field.** Hidden fields and select fields are not searched.
- **A tool name is not suggested.** Check that the tool is enabled on that node and is not a built-in provider tool or a remote file search index.

## See also

- [Node Types](../concepts/pipelines/nodes.md)
- [Prompt](../concepts/llm.md#prompt)
