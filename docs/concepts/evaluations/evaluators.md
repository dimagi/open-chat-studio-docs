# Evaluators

**Evaluators** define the logic for analyzing messages and generating evaluation metrics. Each evaluator takes individual messages from a dataset and optionally a generated response, then outputs structured results in a table.

Each evaluator has an **evaluation mode** — either **message-level** or **session-level** — that must match the dataset it is used with. When configuring an evaluation run, evaluators whose mode is incompatible with the selected dataset are automatically disabled.

## Evaluator Types

### LLM Evaluator
The LLM Evaluator uses language models to evaluate responses based on a custom prompt. This can be used as an LLM-as-judge to evaluate the performance of a chatbot, or to gain insight properties of both the user and assistant messages.


**Example prompt:**
```
Rate the helpfulness and accuracy of this response on a scale of 1-5:

User question: {input.content}
Reference answer: {output.content}
Generated answer: {generated_response}

Consider the conversation context: {context.topic}
```

**Template Variables:**

The available variables depend on the evaluator's evaluation mode.

##### Message-level variables

| Variable | Description |
|---|---|
| `{input.content}` | The human message content |
| `{output.content}` | The dataset message's AI response content. This may be an expected/reference answer (for manually created datasets) or the actual AI response (for session-cloned datasets). |
| `{generated_response}` | The generated response from your chatbot (if generation is enabled) |
| `{context.[parameter]}` | Any context variable, e.g. `{context.topic}` |
| `{full_history}` | Complete conversation history as formatted text |

##### Session-level variables

In session-level mode, `{input.content}` and `{output.content}` are empty. Use the following variables instead:

| Variable | Description |
|---|---|
| `{summary}` | The session snapshot — the full conversation context captured at the time of the last AI message |
| `{context.[parameter]}` | Any context variable, e.g. `{context.current_datetime}` |

!!! note
    Generation is not available for session-level datasets, so `{generated_response}` is not applicable in session-level prompts.

See [Evaluation Datasets](dataset.md) for how data is mapped into these fields.

#### Output Schema

The output schema defines the metrics that the LLM should attempt to output. Each item in the schema will become a column in the output table. You can specify the data type for each field to ensure structured, validated output.

**Available Types:**

- **string**: Text output (default behavior)
- **integer**: Whole numbers (e.g., counts, ratings)
- **float**: Decimal numbers (e.g., confidence scores, percentages)
- **choices (enum)**: Predefined options from a list

The system automatically validates the LLM's output against the specified types using a dynamically generated schema. If the output doesn't match the expected format, the system will retry up to 3 times before failing, ensuring reliable structured data.

**Example Output Schema:**

| Column Name | Type | Description |
|-------------|------|-------------|
| expected_helpfulness | integer | The helpfulness, on a scale of 1-5 of the expected assistant message |
| actual_helpfulness | integer | The helpfulness, on a scale of 1-5 of the actual assistant message |
| user_sentiment | choices | The sentiment of the user message (options: positive, neutral, negative) |
| confidence_score | float | Confidence in the evaluation, from 0.0 to 1.0 |

#### Tag Rules

Tag Rules let you automatically apply tags to sessions or messages when an evaluator output field matches a condition. This makes it easy to surface and filter results — for example, flagging all sessions where the evaluator detected negative sentiment, or marking messages that scored below a threshold.

Tag Rules are available only on LLM evaluators. They run automatically on every non-preview evaluation run. Preview runs do not trigger tag application.

**How tags are applied**

The target of the tag depends on the evaluator's mode:

- **Message mode**: the tag is applied to the specific chat message being evaluated.
- **Session mode**: the tag is applied to the session's chat.

Each tag application is recorded in an audit log and displayed in the **Applied Tags** column on the run results page.

**Defining a rule**

Each rule has three parts:

| Field | Description |
|-------|-------------|
| Output field | The output schema field whose value is tested |
| Tag name | The tag to apply when the condition is met |
| Condition | The value or range that triggers the tag |

The condition options vary by the type of the output field:

| Output field type | Condition behaviour |
|-------------------|---------------------|
| choices (enum) | Apply the tag when the field equals one of the defined choice values (e.g. `sentiment == "negative"`) |
| integer / float | Apply the tag when the field equals a specific value, or falls within a `min..max` range |
| string | Apply the tag when the field equals a specific value |

**Example Tag Rules**

Given the output schema from the example above, you could define the following rules:

| Output field | Tag name | Condition |
|---|---|---|
| user_sentiment | negative-sentiment | equals `negative` |
| expected_helpfulness | low-helpfulness | range `1..2` |
| confidence_score | low-confidence | range `0.0..0.4` |

With these rules, any evaluation run will automatically tag messages or sessions that meet the conditions, without requiring manual review of every row.

### Python Evaluator

The Python Evaluator allows custom code execution against each message.

The code **must** define a `main` function which takes the `input`, `output`, `full_history`, and `generated_response`. It should return a `dict` whose keys will become columns in the output table.

**Function Arguments:**

| Argument | Type | Description | Example |
|----------|------|-------------|---------|
| `input` | dict | The human message data with `content` and `role` keys | `{'content': 'What is 2+2?', 'role': 'human'}` |
| `output` | dict | The expected AI response with `content` and `role` keys | `{'content': '2+2 equals 4', 'role': 'ai'}` |
| `context` | dict | Additional metadata and variables | `{'topic': 'math', 'difficulty': 'easy', 'user_id': '123'}` |
| `full_history` | str | Complete conversation history | `"user: Hello\nassistant: Hi there!\nuser: What is 2+2?"` |
| `generated_response` | str | AI-generated response being evaluated | `"The answer is 4. Is there anything else I can help with?"` |


**Example:**

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
