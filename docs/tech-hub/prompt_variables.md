# Prompt Variables Reference

[Prompt variables](../concepts/prompt_variables.md), such as `{participant_data}`, insert data into your prompts.
This page covers three advanced topics:

- [Nested data access](#nested-data-access): insert one value instead of a whole variable.
- [Prompt variables vs. template variables](#prompt-variables-vs-template-variables): which syntax to use in each node type.
- [Remote context](#remote-context): use data that your website or app sends with each message.

For the list of available variables and what each one contains, see [Prompt Variables](../concepts/prompt_variables.md).

## Nested data access

These prompt variables hold structured data.
You can insert one value from them instead of the whole object:

- `{participant_data}` — see [Participant Data](../concepts/participant_data.md)
- `{temp_state}` — see [Temporary State](python_node.md#temporary-state)
- `{session_state}` — see [Session State](python_node.md#session-state)

Use dot notation to access nested values, separating each level of nesting with a period.
For example, if a participant's data looks like this:

```json
{
  "name": "John Doe",
  "address": {
    "street": "123 Main St"
  },
  "tasks": [
    {
      "name": "Fix the roof"
    }
  ]
}
```

Use these placeholders to insert specific values:

```text
{participant_data.name}
{participant_data.address.street}
{participant_data.tasks[0].name}
```

To access an item in a list, put its position in square brackets.
The first item is `[0]`, the second is `[1]`, and so on.

If a value does not exist, the prompt shows nothing in its place and no error occurs.

## Prompt variables vs. template variables

OCS uses two different variable syntaxes, depending on where you write the text.
Each place has its own set of variables, and the sets are not interchangeable.
Use the syntax and variables that match the field you are editing.

- **LLM node prompt:** Single braces, for example `{participant_data.name}`.
  See [Prompt Variables](../concepts/prompt_variables.md).
- **Router node prompt:** Single braces, with fewer variables available, plus the router-only `{routes}` and `{routes_list}`.
  See [Variables you can use in the prompt](../how-to/routers/llm_router.md#variables-you-can-use-in-the-prompt).
- **Render a Template and Send an Email nodes:** Jinja2 syntax with double braces, for example `{{ participant_data.name }}`.
  See [Render a Template and Send an Email Nodes](template_and_email_nodes.md).
- **LLM evaluator prompt:** Single braces with its own variables, for example `{input.content}`.
  See [Evaluator Reference](evaluations/evaluator-reference.md#template-variables).

## Remote context

Remote context is data that your website or app sends to OCS along with a participant's message.
For example, you can send the page the participant is viewing, or a product ID.
OCS stores this data in session state under the `remote_context` key, so you can read it in a prompt as `{session_state.remote_context}`.

There are two ways to send remote context:

- **Chat API** — include a `context` object when you send a message.
  See the [Chat API documentation](../api/v1/chat.txt).
- **Chat widget** — set the widget's `pageContext` property.
  See [Page Context](../chat_widget/reference.md#page-context).

For example, if a message is sent with this context:

```json
{
  "page_url": "https://example.com/products/widget-x",
  "product_id": "widget-x",
  "category": "gadgets",
  "user_segment": "premium"
}
```

You can access each value in your prompt with dot notation:

```text
Current page: {session_state.remote_context.page_url}
Product ID: {session_state.remote_context.product_id}
User segment: {session_state.remote_context.user_segment}
```

!!! note "Remote context availability"

    The `remote_context` key is only present in session state when context is sent with a message.
    If no context is sent, the key does not exist and the variable shows nothing in the prompt.

## See also

- [Prompt Variables](../concepts/prompt_variables.md)
- [Participant Data](../concepts/participant_data.md)
- [Python Node](python_node.md)
- [OCS API Access](api_access.md)
