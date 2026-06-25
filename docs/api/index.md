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

## Pagination

List endpoints use **cursor-based pagination**. Each response wraps the records in a
`results` array alongside `next` and `previous` links:

```json
{
  "count": 1432,
  "next": "https://openchatstudio.com/api/sessions/?cursor=cD0yMDI2LTA2LTEw",
  "previous": null,
  "results": [ ... ]
}
```

To page through a full result set, follow the `next` link until it is `null`. The
`previous` link returns the prior page (or `null` on the first page). Do not construct
cursor values yourself — always use the links returned by the API, as their format may
change.

### Total count

On the **first page** of a cursor-paginated response, the `count` field reports the total
number of records matching your query, which is useful for showing progress while syncing
a large data set. To keep paging fast, `count` is **omitted on subsequent (cursor-following)
pages** — treat it as optional and do not rely on it being present after the first page.

The following list endpoints are cursor-paginated and include the first-page `count`:

- `GET /api/sessions/`
- `GET /api/participants/`
- `GET /api/experiments/`
- `GET /api/v2/chatbots/`

## Versions

The API is versioned. Select a version below for its endpoint reference and simplified
LLM docs:

<!-- api-versions:start -->
* [v1](v1/index.md)
* [v2](v2/index.md)
<!-- api-versions:end -->
