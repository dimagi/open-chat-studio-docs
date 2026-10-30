# Source Material

Source Material lets you give your chatbot specific content, information, or data to use as a reference or knowledge base.
This is particularly useful for [LLM](llm.md)-based chatbots, because it helps tailor their responses to your needs or the chatbot's theme.

## How to use source material
- Content Integration: You can integrate specific documents or text into the chatbot.
  This could be health information in FAQ format, program-specific data, or other content you want your chatbot to reference.

- Contextual Relevance: This material gives the chatbot focused, relevant context.
  Your chatbot can then provide more accurate and tailored responses based on the Source Materials you've provided.

- Updating Information: Keep your Source Materials up-to-date.
  When program materials change (for example guidelines for counselling or home visits), update your Source Materials so your chatbot stays relevant and effective.

## Best Practices
- Relevance and Accuracy: Ensure the materials are relevant to the conversations your chatbot will engage in.

- Organization and Structure: Well-organized Source Materials make it easier for the chatbot to retrieve and use the information.
  Structure your content clearly and concisely, with labels for different sections.

## Deleting source material

You can't delete a Source Material while a chatbot still references it, in either a [published version](versioning.md) or the working draft.
Attempting to delete it shows a list of every chatbot that still references it, so you know what to update first.
[Collections](./collections/index.md) are protected in the same way.

To delete it, first clear the Source Material from each referencing [node](./pipelines/nodes.md), or delete the referencing chatbots, then try again.

## See also

- [Prompt variables](./prompt_variables.md)
- [Add a knowledge base](../how-to/add_a_knowledge_base.md)
- [Collections](./collections/index.md)
- [Versioning](versioning.md)
