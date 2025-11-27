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


## LLM Docs

The following documents are a simplified version of the API for consumption by LLMs:

* [Channels](./channels.txt){:target="_blank"}
* [Chat](./chat.txt){:target="_blank"}
* [Sessions](./experiment_sessions.txt){:target="_blank"}
* [Experiments](./experiments.txt){:target="_blank"}
* [Files](./files.txt){:target="_blank"}
* [OpenAI](./openai.txt){:target="_blank"}
* [Participants](./participants.txt){:target="_blank"}
