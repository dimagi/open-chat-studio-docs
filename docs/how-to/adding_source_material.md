### Add your source material
Select the *Source Material* tab on the left-hand menu and click *Add new*

### Select the source material for your bot
Once you’ve created your source material, it should appear in the list of source materials when editing your bot.

### Reference the source material in your prompt
To reference the source material, include the `{source_material}` [prompt variable][prompt_variables_concept] in your prompt. Be mindful of its placement—it’s best to include it in a separate section rather than within a sentence.

Example prompt:

```
You are a friendly bot. Be sure to reference the source material before answering the user's query: 

### Source material
{source_material}
```


!!! info "Assistant"
    Assistants do not support this method of adding knowledge. Instead, you must upload files to serve as the source material.


### See also
- [Source Material][source_material_concept]

[source_material_concept]: ../conceptual_guide/source_material.md
[prompt_variables_concept]: ../conceptual_guide/prompt_variables.md
[assistants]: https://platform.openai.com/docs/assistants/overview