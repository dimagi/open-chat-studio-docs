# Custom Actions

Custom Actions enable bots to communicate with external services via HTTP API calls. This feature allows you to extend the functionality of your bot by integrating it with other services.

This feature is analogous to the OpenAI's GPT Actions feature.

## Key points (summary)
- Custom Actions are backed by an OpenAPI schema describing the remote API.
- Each operation (endpoint + method) in the schema becomes an available "operation" which is configured on an Experiment, Assistant, or Node via a CustomActionOperation.
- Authentication is provided via an Authentication Provider (optional). If none is set, requests are made anonymously.
- CustomActionOperation instances are versioned when experiments/assistants are versioned; the CustomAction itself is not.
- Only HTTPS base URLs are supported; the OpenAPI schema is validated on save.

## Custom Action Fields

### Authentication Provider

If the external API requires authentication, create an Authentication Provider in Team Settings and attach it to the Custom Action. If no auth provider is configured the action will use an anonymous auth service.

See: docs/team/authentication_providers.md

### Base URL

The base URL is the root URL of the external service (for example: https://api.example.com). Only HTTPS URLs are supported.

### API Schema (OpenAPI)

Provide a JSON or YAML OpenAPI schema that describes the API. The platform parses the schema on save and extracts operations. The schema must be a valid OpenAPI document (FastAPI's /openapi.json works).

If the schema cannot be parsed the save will fail with a validation error.

## How Custom Actions work (detailed)

- The CustomAction model stores the server_url, api_schema, optional auth_provider, and derived operations. When a Custom Action is saved the OpenAPI schema is parsed and the available operations are computed and stored in-memory for the working version.

- Each operation in the OpenAPI spec is represented by an APIOperationDetails object. When you add a Custom Action to an Experiment/Assistant/Node you create a CustomActionOperation that references the CustomAction and selects a specific operation_id.

- CustomActionOperation is the object that is versioned and persisted with a snapshot of the operation schema when an Experiment/Assistant version is created. The CustomAction model itself is not versioned; this allows editing the action schema while keeping historical versions intact through the operation snapshotting.

- When running, each CustomActionOperation is converted into a "tool" that is passed to the LLM agent. The tool knows how to build and send the HTTP request for that operation (see apps.chat.agent.openapi_tool.FunctionDef.build_tool).

- API responses are returned to the LLM as text. If the remote response includes a Content-Disposition header indicating a file download, the file is downloaded and handled accordingly.

## Permissions, constraints, and usage notes

- A CustomActionOperation must be attached to exactly one holder: an Experiment, Assistant, or Node. This is enforced by database constraints.

- There are uniqueness constraints to prevent creating duplicate (holder, custom_action, operation_id) entries for Experiments and Assistants.

- The operation schema is persisted to the CustomActionOperation only when the operation is part of a versioned object (i.e., when a version is created). Working versions compute the schema dynamically from the parent CustomAction.

- The system supports typical OpenAPI features, but there are limitations:
  - Only HTTPS base URLs are allowed (URLField validation).
  - The platform expects standard OpenAPI operation definitions; highly dynamic or non-standard schemas may not parse correctly.
  - Authentication is handled via the configured AuthProvider integration; custom or non-standard auth flows may require building a corresponding AuthProvider.

## Testing and debugging

- If requests are failing, check that the schema's operation_id values are present and unique, the base URL is correct and reachable, and that an appropriate Authentication Provider is configured if required.

- Look at server logs (ocs.custom_actions) for warnings about missing operation_schema on versioned models or OpenAPI parsing errors.

## Versioning behavior

- CustomActionOperation implements Versioning: when you create a new Experiment/Assistant version the operation_schema is snapshot into the versioned CustomActionOperation so the execution will not be affected by future edits to the CustomAction's OpenAPI schema.

---

(Technical reference derived from the open-chat-studio codebase: apps/custom_actions/models.py, forms.py, schema_utils.py, and README.)
