# Add a Knowledge Base

Adding knowledge to your bot depends on the type of bot you are building.

## Base LLM and Pipeline
### Add your source material
Select the *Source Material* tab on the left-hand menu and click *Add new*

### Select the source material for your bot
Once you’ve created your source material, it should appear in the list of source materials when editing your bot.

### Reference the source material in your prompt
To reference the source material, include the `{source_material}` [prompt variable][prompt_variables_concept] in your prompt. Be mindful of its placement—it’s best to include it in a separate section rather than within a sentence.

Example prompt:

```text
You are a friendly bot. Be sure to reference the source material before answering the user's query:

### Source material
{source_material}
```

## Assistant (Removed)

Assistant-type bots have been [removed](../concepts/assistants.md), so files can no longer be added to an assistant's *file_search* or *code_interpreter* tools. To give an LLM node the same file search knowledge, put the files in an [Indexed Collection](../concepts/collections/indexed.md) — the [migration guide](assistants_migration.md) walks through moving an assistant's files across.

### See also
- [Source Material][source_material_concept]

[source_material_concept]: ../concepts/source_material.md
[prompt_variables_concept]: ../concepts/prompt_variables.md
