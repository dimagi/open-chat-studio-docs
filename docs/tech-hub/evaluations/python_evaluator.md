# Python Evaluator

The Python Evaluator runs custom code against each message — useful for deterministic rules, custom string matching, or logic an LLM prompt can't reliably express. See [Evaluators](../../concepts/evaluations/evaluators.md#python-evaluator) for when to choose it over the [LLM Evaluator](../../concepts/evaluations/evaluators.md#llm-evaluator).

The code **must** define a `main` function which takes the `input`, `output`, `context`, `full_history`, and `generated_response` as arguments, plus a `**kwargs` catch-all. It should return a `dict` whose keys will become columns in the output table.

## Function Arguments

| Argument | Type | Description | Example |
|----------|------|-------------|---------|
| `input` | dict | The human message data with `content` and `role` keys | `{'content': 'What is 2+2?', 'role': 'human'}` |
| `output` | dict | The expected AI response with `content` and `role` keys | `{'content': '2+2 equals 4', 'role': 'ai'}` |
| `context` | dict | Additional metadata and variables | `{'topic': 'math', 'difficulty': 'easy', 'user_id': '123'}` |
| `full_history` | str | Complete conversation history | `"user: Hello\nassistant: Hi there!\nuser: What is 2+2?"` |
| `generated_response` | str | AI-generated response being evaluated | `"The answer is 4. Is there anything else I can help with?"` |
| `**kwargs` | dict | Catch-all for additional values passed by keyword — currently `participant_data` and `session_state` (see below) | `{'participant_data': {...}, 'session_state': {...}}` |

### Participant data and session state

`kwargs` also carries `participant_data` and `session_state` — the same values available to LLM evaluator prompts as [`{participant_data.[key]}` and `{session_state.[key]}`](../../concepts/evaluations/evaluators.md#template-variables). See [Dataset Structure](dataset-structure.md#dataset-fields) for where these values come from.

Read them with `kwargs.get(...)`, since they are keyword-only, not positional arguments:

```python
def main(input: dict, output: dict, context: dict, full_history: str, generated_response: str, **kwargs) -> dict:
    participant_data = kwargs.get("participant_data", {})
    session_state = kwargs.get("session_state", {})
    ...
```

!!! note
    Don't add `participant_data` or `session_state` to your function's parameter list. Open Chat Studio checks that the positional arguments match the five listed above exactly, so a function declaring either of them positionally will be rejected. They are passed by keyword so that evaluators written before this feature keep working unchanged.

## Example

```python
def main(input: dict, output: dict, context: dict, full_history: str, generated_response: str, **kwargs) -> dict:
    """Evaluates response quality based on accuracy, length, and politeness.
    """

    expected_answer = output['content'].lower()
    actual_answer = generated_response.lower()
    has_correct_answer = expected_answer in actual_answer

    response_length = len(generated_response.split())
    is_polite = any(word in actual_answer for word in ['please', 'thank', 'help', 'happy'])

    return {
        'correct_answer': has_correct_answer,
        'response_length': response_length,
        'politeness_score': 1.0 if is_polite else 0.0,
        'topic': context.get('topic', 'unknown')
    }
```
