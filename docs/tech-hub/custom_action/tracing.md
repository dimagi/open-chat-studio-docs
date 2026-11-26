---
title: Custom Action Tracing
---

# Custom Action Tracing

[Tracing](../../concepts/tracing.md) records each HTTP request a [Custom Action](./index.md) makes during a chatbot turn.
The requests appear in the **Custom Action Requests** section of the [trace detail page](../../concepts/tracing.md#builtin-tracing).
Use this section to debug a Custom Action that returns errors or unexpected data.

## Find the requests

In the [session](../../concepts/sessions.md), hover over the chatbot message and select the Open Chat Studio (OCS) trace icon (:fontawesome-solid-diagram-project:).

If Langfuse is configured and the turn was sampled, the message also has a Langfuse trace icon (![Langfuse](../../assets/images/langfuse.svg){ width="16" }), which opens the trace in Langfuse instead.
Turns that [Langfuse sampling](../../concepts/langfuse_tracing.md#trace-sampling) skips have only the OCS trace icon (:fontawesome-solid-diagram-project:).

The **Custom Action Requests** section is on the trace detail page.

## What each request shows

Each request shows the response status, method, URL, duration, and the Custom Action and operation that made it.
Expand a request to see its headers, bodies, and the error if the call failed.

## Which requests are logged

OCS logs every attempt as a separate request.
This includes retries after a `429` (too many requests) response, and transport errors that produced no response.
Requests from a turn that failed are kept.
A request that returned `200` but whose body could not be read is shown in red with the error.

The **Custom Action Requests** section is hidden when the trace has no Custom Action requests.

If you delete a Custom Action later, its requests stay on the trace page with a fallback label in place of the Custom Action name.

## Credential redaction

OCS redacts the credentials that the Custom Action's authentication provider adds, and headers with credential-like names, before saving the requests:

- Headers added by the Custom Action's [authentication provider](../../concepts/team/authentication_providers.md) show as `[REDACTED]`.
- Any header whose name contains `auth`, `token`, `secret`, `password`, `key`, `cookie`, `session` or `signature` also shows as `[REDACTED]`.
- The authentication provider's credential, as sent in the request header, is replaced with `[REDACTED]` in the URL, the request and response bodies, and the error text.
  An API that echoes that value back does not expose it.
  For Basic authentication, the header carries the Base64-encoded username and password, not the password itself.
  If an API echoes the plain password in a response body, the password stays visible in the request log.

## Body limits

- Bodies longer than 10,000 characters are truncated.
- For a file attachment response, the body shows `[attachment not logged]`.

## Langfuse events

If your team has a [Langfuse tracing provider](../../concepts/langfuse_tracing.md), each request on a sampled turn is also sent to Langfuse as a `custom_action_request` event on the tool span.
The event contains the same redacted record shown on the trace detail page.
Requests on turns that sampling skips are not sent to Langfuse, but still appear on the OCS trace detail page.

## See also

- [Set up a Custom Action](./index.md)
- [Failure notifications](./index.md#failure-notifications)
- [Custom Action Health Monitoring](./health_custom_action.md)
- [Custom Action Testing](./test_custom_action.md)
