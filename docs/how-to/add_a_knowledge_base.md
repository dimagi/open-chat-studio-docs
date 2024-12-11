Adding knowledge to your bot depends on the type of bot you are building.

## Base LLM and Pipeline
#### Add your source material
Select the *Source Material* tab on the left-hand menu and click *Add new*

#### Select the source material for your bot
Once you’ve created your source material, it should appear in the list of source materials when editing your bot.

#### Reference the source material in your prompt
To reference the source material, include the `{source_material}` [prompt variable][prompt_variables_concept] in your prompt. Be mindful of its placement—it’s best to include it in a separate section rather than within a sentence.

Example prompt:

```
You are a friendly bot. Be sure to reference the source material before answering the user's query: 

### Source material
{source_material}
```

## Assistant
To add knowldege to your assistant, you must upload files to serve as the source material. When creating or editing your assistant, select the *file_search* or *code_interpreter* checkboxes to allow the assistant to read files.

- [File search][file_search]: This allows the bot to search and reference information provided in uploaded files.
- [Code Interpreter][code_interpreter]: This allows the bot to write and execute code to accomplish tasks.


### See also
- [Source Material][source_material_concept]

[source_material_concept]: ../concepts/source_material.md
[prompt_variables_concept]: ../concepts/prompt_variables.md
[assistants]: https://platform.openai.com/docs/assistants/overview
[file_search]: https://platform.openai.com/docs/assistants/tools/file-search
[code_interpreter]: https://platform.openai.com/docs/assistants/tools/code-interpreter
