# API

Open Chat Studio provides a REST API that enables you to create chat sessions, send messages, manage experiments, and access session data programmatically.

## API Schema and Docs

See the following links for documentation on the API endpoints:

* [API docs](https://openchatstudio.com/api/docs/)
* [OpenAPI Schema](https://openchatstudio.com/api/schema/)

## Overview

The API is organized around REST principles and uses standard HTTP methods and status codes. All API endpoints return JSON responses and require authentication.

**Base URL:** `https://openchatstudio.com/api/`

## Authentication

The API supports multiple authentication methods:

- **API Key Authentication:** Include your API key in the `X-api-key` header
- **Token Authentication:** Use Bearer token authentication in the `Authorization` header  
- **Cookie Authentication:** Session-based authentication using cookies (for web integrations)
- **OAuth2 Authentication:** OAuth2 authentication using scopes. See the [getting started page](getting_started_with_oauth.md) on how to get started.

## Error Handling

The API uses standard HTTP status codes:

- `200 OK`: Request successful
- `201 Created`: Resource created successfully  
- `202 Accepted`: Request accepted for processing
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Error responses include a JSON object with error details:

```json
{
  "detail": "Error description"
}
```

## Rate Limiting

To ensure optimal performance:
- Chat polling should not exceed once every 30 seconds
- API requests are subject to reasonable rate limits
- Use pagination for large data sets

## Page Context

The API supports passing arbitrary page context data when creating chat sessions. This contextual information is merged into the session state under the reserved `page_context` key, making it accessible to the chatbot's prompts and pipelines.

### Use Cases

Page context is particularly useful for:

- **Embedded Chat Widgets**: Pass information about the current web page to provide context-aware responses
- **E-commerce**: Share product IDs, prices, and inventory status
- **Customer Support**: Include account details, order information, or service status
- **Content Sites**: Provide article metadata, category information, or user preferences
- **Location-based Services**: Share geographic location or regional settings

### API Usage

#### Starting a Chat Session with Page Context

When creating a new chat session via the `/api/chat/start/` endpoint, include the `page_context` parameter:

```bash
curl -X POST https://openchatstudio.com/api/chat/start/ \
  -H "Content-Type: application/json" \
  -H "X-Embed-Key: your-embed-key" \
  -d '{
    "chatbot_id": "your-chatbot-id",
    "participant_remote_id": "user-123",
    "participant_name": "Jane Smith",
    "page_context": {
      "page_url": "https://example.com/products/widget-x",
      "product_id": "widget-x",
      "product_name": "Premium Widget X",
      "price": "$99.99",
      "category": "gadgets",
      "in_stock": true
    }
  }'
```

**Response:**

```json
{
  "session_id": "abc123...",
  "chatbot": {
    "id": "your-chatbot-id",
    "name": "Support Bot"
  },
  "participant": {
    "id": "user-123",
    "name": "Jane Smith"
  }
}
```

#### Creating an Experiment Session with Page Context

When creating a session via the `/api/sessions/` endpoint:

```bash
curl -X POST https://openchatstudio.com/api/sessions/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-token" \
  -d '{
    "experiment": "experiment-id",
    "participant": "participant-id",
    "page_context": {
      "referrer": "https://google.com",
      "utm_source": "email",
      "utm_campaign": "spring-sale",
      "user_segment": "premium"
    }
  }'
```

### Accessing Page Context in Chatbots

Once page context is set, the chatbot can access it in several ways:

#### In Prompts

Use session state variables to reference page context values:

```
You are a helpful customer support assistant.

Current page: {session_state.page_context.page_url}
Product: {session_state.page_context.product_name} ({session_state.page_context.product_id})
Price: {session_state.page_context.price}
In stock: {session_state.page_context.in_stock}

Provide assistance related to this product.
```

#### In Python Nodes

Access page context programmatically in pipeline Python nodes:

```python
from python_node import get_session_state_key

# Get the entire page context
page_context = get_session_state_key("page_context")

# Access specific values
product_id = get_session_state_key("page_context.product_id")
product_name = get_session_state_key("page_context.product_name")

# Use the context to customize behavior
if product_id:
    return f"I can help you with {product_name}!"
else:
    return "How can I assist you today?"
```

### Reserved Key Protection

The `page_context` key in session state is **reserved** and can only be set via the `page_context` API parameter. Attempts to set `session_state.page_context` directly through the `state` or `session_data` parameters will be rejected with a validation error.

**Invalid Request (will fail):**

```json
{
  "chatbot_id": "your-chatbot-id",
  "session_data": {
    "page_context": {
      "custom": "data"
    }
  }
}
```

**Valid Request:**

```json
{
  "chatbot_id": "your-chatbot-id",
  "page_context": {
    "custom": "data"
  }
}
```

### Best Practices

- **Keep it relevant**: Only include context that will be useful for the chatbot
- **Use consistent keys**: Standardize key names across your integration for easier prompt configuration
- **Sanitize data**: Validate and clean user-generated data before passing it as context
- **Consider privacy**: Avoid including sensitive personal information unless necessary
- **Document your schema**: Maintain documentation of your page context structure for prompt authors

### Related Documentation

- [Session State](../concepts/pipelines/nodes.md#session-state) - Learn about session state in pipelines
- [Prompt Variables](../concepts/prompt_variables.md#accessing-page-context) - Using page context in prompts
- [Chat Widget](../chat_widget/reference.md#page-context) - Setting page context from embedded widgets


## LLM Docs

The following documents are a simplified version of the API for consumption by LLMs:

* [Channels](./channels.txt){:target="_blank"}
* [Chat](./chat.txt){:target="_blank"}
* [Sessions](./experiment_sessions.txt){:target="_blank"}
* [Experiments](./experiments.txt){:target="_blank"}
* [Files](./files.txt){:target="_blank"}
* [OpenAI](./openai.txt){:target="_blank"}
* [Participants](./participants.txt){:target="_blank"}
