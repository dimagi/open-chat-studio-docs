# Custom Actions

Custom Actions let your assistant call external HTTP APIs during a conversation. Use them to extend the assistant with real-world capabilities: lookup databases, place orders, fetch documents, control devices, or trigger workflows in other systems.

This guide explains what Custom Actions are from a user perspective, how to register an API, attach actions to your assistants or experiments, how the assistant uses operations in conversations, how versioning works, and common limitations and troubleshooting tips.

Key points
- Custom Actions are defined by an OpenAPI (Swagger) document that describes the external API.
- Each operation (an endpoint + HTTP method) in the OpenAPI spec becomes a callable operation your assistant can use.
- You can attach selected operations to an Assistant or to an Experiment so the assistant can call them at runtime.
- If the API requires authentication, attach an Authentication Provider (configured in Team Settings) to the Custom Action.
- Only HTTPS base URLs are supported and the OpenAPI schema is validated when saved.

What is a Custom Action and why use one?
- A Custom Action is a connection to a remote HTTP API described by an OpenAPI schema. Instead of hard-coding integrations, you upload the API schema and the platform exposes the API operations as tools your assistant can call.
- Use cases: fetch user-specific data, submit forms, create tickets, query product catalogs, retrieve files, or integrate any REST/HTTP service your team uses.

Registering an API (creating a Custom Action)
1. Prepare an OpenAPI document (JSON or YAML). The document should describe the API base URL and include operation IDs for the endpoints you want to expose. Many frameworks (FastAPI, Django Rest Framework, etc.) can emit an OpenAPI spec.
2. In the Custom Actions UI, create a new Custom Action and provide:
   - A descriptive name for the action (e.g., "Orders API").
   - Base URL (the root of the API, e.g., https://api.example.com) — HTTPS only.
   - The OpenAPI schema (paste JSON/YAML or upload a file).
   - (Optional) An Authentication Provider if the API requires credentials. Authentication Providers are configured in Team Settings.
3. Save. The platform validates the OpenAPI schema immediately. If validation fails (invalid JSON/YAML, missing required fields, or unsupported constructs) you will see an error and need to fix the schema.

Authentication
- If the API requires authentication, create an Authentication Provider in Team Settings and attach it to the Custom Action. The platform will use the provider to sign/authorize requests when the assistant calls the operation.
- If no Authentication Provider is attached the assistant will call the API anonymously (no special credentials).

Selecting operations to expose
- After saving the OpenAPI schema, the platform lists the available operations (each operation is an endpoint+method). Pick the specific operations you want the assistant to be able to call.
- You can attach operations to an Assistant or to an Experiment. Attaching limits which operations the assistant can call and is how you grant the assistant access to that API.

Attaching Custom Actions to Assistants and Experiments
- Assistant-level attachment: attach selected operations to an Assistant to make those tools available whenever that Assistant runs.
- Experiment-level attachment: you can attach operations in an Experiment (useful for testing different operation sets or temporary configurations).
- Common workflow: register the API, choose operations, attach them to your Assistant, then run or test the Assistant in an Experiment.

How operations are used in conversations (runtime behavior)
- During a conversation, the assistant's reasoning engine may decide to call an operation when it needs external data or to perform an action.
- When an operation is called the system constructs an HTTP request from the operation definition and the inputs provided by the assistant (or user). The request is sent to the configured base URL using the chosen auth provider if any.
- The API response is returned to the assistant as text (or file when the response indicates a downloadable attachment). The assistant can then continue the conversation using the response.
- You should design operations with clear inputs and outputs (parameters and response schemas) so the assistant can use them reliably.

Versioning (user-facing explanation)
- When you create a version of an Assistant or an Experiment (to freeze a configuration or publish a release), the platform snapshots the operation definitions used by that version. That means the version will continue to use the same operation schema even if you later edit the Custom Action's OpenAPI document.
- The Custom Action itself (the central API definition) remains editable. New changes to the Custom Action affect only new working versions or future attachments — existing published versions keep their snapshot.
- Practical consequence: you can safely update an API schema for future work without breaking previously published assistant versions.

Limitations and important rules
- HTTPS only: base URLs must use HTTPS. HTTP is not supported.
- Valid OpenAPI required: the uploaded schema must be a valid OpenAPI document. Non-standard or highly dynamic schemas may fail validation.
- Operation IDs: operations should have unique operationId values to avoid ambiguity.
- Auth providers: if the API uses a custom or non-standard authentication flow that the platform doesn't support, you may need to adapt the API or create a suitable Authentication Provider.
- Request size and timeouts: APIs that return extremely large payloads or stream indefinite content may be truncated or treated as errors depending on system limits — design responses for concise, machine-parsable results when possible.

Troubleshooting tips
- Validation errors when saving the OpenAPI schema: check JSON/YAML validity, confirm required OpenAPI fields are present, and ensure operationId values are unique.
- Operations not appearing for an Assistant: confirm you selected and attached the operations to the Assistant or Experiment. Also check that the Custom Action was saved successfully.
- Authentication failures: verify your Authentication Provider configuration and credentials in Team Settings. Test the API externally (curl/postman) with the same credentials to confirm they work.
- Unexpected response formats: prefer APIs that return JSON and follow consistent response schemas. If the API returns files, ensure the Content-Disposition header is present so the system can treat it as a downloadable attachment.
- Logs and debugging: when an operation call fails at runtime, check the assistant/experiment run logs in the platform UI for request/response details and error messages. If you need deeper diagnostics, consult platform server logs (ask your admin) which include OpenAPI parsing warnings and HTTP request errors.

Best practices
- Limit operations: only expose the operations an assistant truly needs — smaller, focused sets are easier to test and secure.
- Use clear operation summaries and parameter descriptions in your OpenAPI docs so the assistant and human reviewers can understand intent.
- Keep responses concise and machine-readable (JSON with a predictable schema) so the assistant can parse and use results reliably.
- Use versioning: create a published version of an Assistant/Experiment before making major API or configuration changes so you can roll back if needed.

If you need more help
- See Team Settings -> Authentication Providers to configure auth.
- If you encounter errors you can't resolve, gather the OpenAPI file, the failing operationId, and any run logs and contact your platform administrator or the support channel.

This documentation is focused on user-facing behavior. For implementation details, internal data models, and developer-focused references, see the developer docs (if available to you).
