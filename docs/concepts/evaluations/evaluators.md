# Evaluators

**Evaluators** define the logic for analyzing messages and generating evaluation metrics. Each evaluator takes individual messages from a dataset and optionally a generated response, then outputs structured results in a table.

## Evaluator Types

### LLM Evaluator
The LLM Evaluator uses language models to evaluate responses based on a custom prompt. This can be used as an LLM-as-judge to evaluate the performance of a chatbot, or to gain insight properties of both the user and assistant messages.


**Example prompt:**
```
Rate the helpfulness and accuracy of this response on a scale of 1-5:

User question: {input.content}
Expected answer: {output.content}
Generated answer: {generated_response}

Consider the conversation context: {context.topic}
```

**Template Variables:**
The following variables are available to be used in the LLM prompt.

- `{input.content}`: The human message content
- `{output.content}`: The expected AI response content
- `{generated_response}`: The generated response from your chatbot (if generation enabled)
- `{context.[parameter]}`: Access any context variables, e.g., `{context.topic}`
- `{full_history}`: Complete conversation history as formatted text

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
