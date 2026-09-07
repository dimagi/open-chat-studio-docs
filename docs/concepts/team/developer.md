# Developers

The **Developers** section of Team Settings groups the tools your team uses to extend and integrate with Open Chat Studio: [Custom actions](#custom-actions) and [OAuth applications](#oauth-applications).
Both are available only to **Team Admins** and **Super Admins** — see [User Groups](groups.md) for what each role can access.

## Custom actions

A [Custom Action](../llm_custom_action.md) lets a chatbot call an external HTTP service during a conversation, using an OpenAPI schema you provide.
The Developers section lists every Custom Action registered for your team, and lets you add, edit, or run a manual health check on one.

For the configuration steps — including how to add an authentication provider and enable actions on a chatbot — see [Custom Actions](custom_actions.md).

## OAuth applications

An OAuth application lets an external system authenticate to Open Chat Studio and read or write your team's data through the [API](../../api/index.md).
The Developers section lists every OAuth application registered for your team, showing its name, client ID, grant type, and when it was created.
From there you can edit an application's settings or delete it.

Registering an application gives you a **client ID** and **client secret**, which the external system uses to request access tokens.

When you register an application, you choose one of two grant types:

- **Authorization code** — for applications that act on behalf of a signed-in user, who interactively grants permission.
- **Client credentials** — for server-side or automated integrations that call the API without a user present. You can also restrict which chatbots a client-credentials application is allowed to access.

!!! note "Global applications"
    Applications registered from Team Settings always belong to your team, and every token they issue is scoped to it.
    A Super Admin can also register a **global** application, not tied to any team, from the site-admin area — but only with the authorization code grant type.

For the full technical integration guide — endpoints, PKCE setup, requesting and refreshing tokens, and available scopes — see [Getting Started with OAuth2](../../api/getting_started_with_oauth.md).

## See also

- [Team Settings](index.md)
- [Custom Actions](custom_actions.md)
- [Getting Started with OAuth2](../../api/getting_started_with_oauth.md)
- [Members & Access](members.md)
- [User Groups](groups.md)
