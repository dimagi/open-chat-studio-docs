# Prompt Variables Reference

This page covers the syntax for reading a single value out of a [prompt variable](../concepts/prompt_variables.md).
It also covers how to read data that your website or app sends with each message.
Finally, it explains how prompt variables differ from the template variables used in other nodes.

For the list of available prompt variables and what each one contains, see [Prompt Variables](../concepts/prompt_variables.md).

## Nested data access

The following prompt variables hold structured data, so you can reference a single value inside them instead of inserting the whole object:

- `{participant_data}` — see [Participant Data](../concepts/participant_data.md)
- `{temp_state}` (pipelines only) — see [Temporary State](python_node.md#temporary-state)
- `{session_state}` (pipelines only) — see [Session State](python_node.md#session-state)

Use dot notation to access nested values.
Separate each level of nesting with a period.
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

You can access specific values with these prompt variables:

```text
{participant_data.name}
{participant_data.address.street}
{participant_data.tasks[0].name}  # lists are zero-indexed
```

To access an item in a list, put its position in square brackets.
The first item is `[0]`, the second is `[1]`, and so on.

## Remote context

Remote context is data that your website or app sends to OCS along with a participant's message.
For example, you can send the page the participant is viewing, or a product ID.
OCS stores this data in session state under the `remote_context` key, so you can read it in a prompt:

```text
{session_state.remote_context}
```

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
    If no context is sent, the key does not exist.

## Prompt variables vs. template variables

OCS uses two different variable syntaxes, depending on where you write the text.
Each place has its own set of variables, and the sets are not interchangeable.
Use the syntax and variables that match the field you are editing.

| Where you write it | Syntax | Example | Reference |
|---|---|---|---|
| LLM node prompt, Router node prompt | Single braces | `{participant_data.name}` | This page and [Prompt Variables](../concepts/prompt_variables.md) |
| Render a Template node, Send an Email node | Jinja2, double braces | `{{ participant_data.name }}` | [Render a Template and Send an Email Nodes](template_and_email_nodes.md) |
| LLM evaluator prompt | Single braces | `{input.content}` | [Evaluator Reference](evaluations/evaluator-reference.md#template-variables) |

## See also

- [Prompt Variables](../concepts/prompt_variables.md)
- [Participant Data](../concepts/participant_data.md)
- [Python Node](python_node.md)
- [OCS API Access](api_access.md)
