---
title: OAuth2
---

# Getting started with OAuth2

OpenChatStudio supports two OAuth2 grant types:

- **Authorization code flow with PKCE** — for applications that act on behalf of a signed-in user. The user interactively grants permission, and the token acts as that user. See [How OAuth 2.0 works](#how-oauth-20-works) below.
- **Client-credentials flow** — for server-side and automated integrations that call the API without a user present. See [Client-credentials flow (machine-to-machine)](#client-credentials-flow-machine-to-machine).

## How OAuth 2.0 works

For a detailed explanation of the OAuth 2.0 authorization code flow, see [OAuth 2 Simplified](https://aaronparecki.com/oauth-2-simplified/#authorization). OpenChatStudio follows this standard flow, with specific endpoints documented below.

## OpenChatStudio OAuth Endpoints

| Endpoint | URL | Notes |
|----------|-----|-------|
| Authorization | `https://www.openchatstudio.com/o/authorize/` | |
| Token | `https://www.openchatstudio.com/o/token/` | |
| UserInfo | `https://www.openchatstudio.com/o/userinfo/` | Requires `openid` scope |

## Step 1: Register your application with OpenChatStudio

OAuth applications belong to a team, and you register them from that team's admin page. Team Admins and Super Admins can register and manage OAuth applications for their own team; the application belongs to whichever team's admin page you registered it from — there's no separate field to choose the team.

If you need a **global** application that isn't tied to any single team, a Super Admin can register one instead from the site-admin page. Global applications only support the authorization code flow described below — see [Client-credentials flow](#client-credentials-flow-machine-to-machine) for why client-credentials isn't available for them.

You'll receive:

- **Client ID**: A public identifier for your application
- **Client secret**: A confidential secret used for token exchange (keep this secure and server-side only!)

## Step 2: Initiate the authorization call

Your application should redirect the user to OpenChatStudio's authorization endpoint to request permission.

### PKCE Setup (Required)

For security, you must implement PKCE:

1. Generate a random `code_verifier` (43-128 characters, unreserved characters)
2. Create a `code_challenge` by SHA256 hashing the verifier and base64url encoding it
3. Include the `code_challenge` in your authorization request

Here's example Python code to generate PKCE parameters:

```python
import secrets
import string
import base64
import hashlib

# Generate a random code verifier (43-128 characters)
characters = string.ascii_letters + string.digits + '-._~'
code_verifier = ''.join(secrets.choice(characters) for _ in range(128))

# Create the code challenge by hashing and encoding the verifier
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).decode().rstrip('=')
```

### Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `response_type` | Yes | Must be `code` |
| `client_id` | Yes | Your client ID |
| `redirect_uri` | Yes | The URL where you want to receive the authorization code. Must match a registered URI for your application |
| `code_challenge` | Yes | The PKCE code challenge (base64url-encoded SHA256 hash of your code_verifier) |
| `code_challenge_method` | Yes | Must be `S256` (SHA256) |
| `state` | Recommended | Random string to prevent CSRF attacks. Store this and validate the response |
| `scope` | No | Space-separated list of scopes. See available scopes in the [API docs](https://openchatstudio.com/api/docs/). If omitted, defaults to all scopes |
| `team` | No | Only relevant for **global** (team-less) applications — lets the user pick which of their teams the token is scoped to. For an application registered under a team's admin page, the token is always scoped to that team, the user isn't asked to choose, and this parameter has no effect. If the authorizing user isn't a member of the application's team, authorization is refused |

### Example Request

```uri
https://www.openchatstudio.com/o/authorize/?response_type=code&client_id=${CLIENT_ID}&redirect_uri=https://your-server/callback/&code_challenge=${CHALLENGE}&code_challenge_method=S256&scope=chatbot:read+session:read&state=random_state_string
```

## Step 3: Handle the authorization response

After the user grants permission, OpenChatStudio redirects them to your `redirect_uri` with the authorization code in the query string:

```uri
https://your-server/callback/?code=auth_code_here&state=random_state_string
```

**Important validations:**

1. Verify the `state` parameter matches the one you sent in Step 1 (protects against CSRF attacks)
2. Extract the `code` parameter
3. Handle errors if present (user denied, invalid client, etc.)

### Error Responses

If an error occurs, the redirect will include error parameters:

```uri
https://your-server/callback/?error=access_denied&error_description=The+user+denied+the+request&state=random_state_string
```

Common error codes:

- `access_denied`: User rejected the authorization request, or (for a team-owned application) the authorizing user isn't a member of the application's team
- `invalid_request`: Missing or invalid parameters
- `unauthorized_client`: Client not authorized to use this flow
- `server_error`: Authorization server encountered an error

## Step 4: Exchange the authorization code for an access token

Your server must send a POST request to OpenChatStudio's token endpoint.

### Required POST Parameters

| Parameter | Description |
|-----------|-------------|
| `grant_type` | Must be `authorization_code` |
| `code` | The authorization code |
| `client_id` | Your client ID |
| `client_secret` | Your client secret (keep this server-side!) |
| `code_verifier` | The PKCE code verifier you generated in Step 1 |
| `redirect_uri` | Must match the redirect_uri used in Step 1 |

### Example Request

```bash
curl -X POST https://www.openchatstudio.com/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=auth_code_here" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "code_verifier=${PKCE_CODE}" \
  -d "redirect_uri=https://your-server/callback/"
```

### Response

A successful response returns a JSON object with the access token:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "chatbot:read session:read",
  "refresh_token": "1p1mG5sD2k4PCdILM9qLYB..."
}
```

**Key fields:**

- `access_token`: Use this in the `Authorization: Bearer` header for API requests
- `token_type`: Always `Bearer` for this flow
- `expires_in`: Seconds until token expiration
- `scope`: The actual scopes granted
- `refresh_token`: Use this to get a new access token when the current one expires (see Step 6)

## Step 5: Use the access token

Include the access token in the Authorization header when making API requests:

```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  https://www.openchatstudio.com/api/...
```

## Step 6: Get a new access token using the refresh token

When your access token expires, use the refresh token to get a new one without requiring the user to re-authenticate. Send a POST request to the token endpoint with the refresh token grant type.

**Token endpoint:** `https://www.openchatstudio.com/o/token/`

### Required POST Parameters

| Parameter | Description |
|-----------|-------------|
| `grant_type` | Must be `refresh_token` |
| `refresh_token` | The refresh token received in Step 4 |
| `client_id` | Your client ID |
| `client_secret` | Your client secret |

### Example Request

```bash
curl -X POST https://www.openchatstudio.com/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=${REFRESH_TOKEN}" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret={$CLIENT_SECRET}"
```

### Response

A successful response returns a new access token:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "chatbot:read session:read",
  "refresh_token": "new_refresh_token_here..."
}
```

**Important:** Save the new `refresh_token` returned in the response, as it replaces your previous refresh token. Use this new token for future refresh requests.

## OpenID Connect (OIDC)

OpenChatStudio supports OpenID Connect, which extends OAuth 2.0 to provide identity information about authenticated users. This is particularly useful for applications that need to identify which team the authenticated user has access to.

### The `openid` Scope

To use OpenID Connect features, include the `openid` scope in your authorization request (Step 2). You can combine it with other scopes as needed:

```uri
https://www.openchatstudio.com/o/authorize/?response_type=code&client_id=${CLIENT_ID}&redirect_uri=https://your-server/callback/&code_challenge=${CHALLENGE}&code_challenge_method=S256&scope=openid+chatbot:read+session:read&state=random_state_string
```

### ID Token in Token Response

When you request the `openid` scope, the token endpoint response (Step 4) will include an additional `id_token` field:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "openid chatbot:read session:read",
  "refresh_token": "1p1mG5sD2k4PCdILM9qLYB...",
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

The `id_token` is a JSON Web Token (JWT) that contains identity claims about the authenticated user, including:

- `sub`: The user's email address
- `name`: The user's full name
- `is_active`: Whether the user account is active
- `team`: The team slug for the team associated with this token

You can decode this JWT to extract user identity information without making additional API calls.

**Security Note:** When using the `id_token`, always verify its signature using a JWT library before trusting its contents. This ensures the token hasn't been tampered with and was actually issued by OpenChatStudio. Most JWT libraries can handle signature verification automatically using OpenChatStudio's public keys from the OIDC discovery endpoint.

### UserInfo Endpoint

Alternatively, you can retrieve user information by calling the UserInfo endpoint with your access token:

**Endpoint:** `https://www.openchatstudio.com/o/userinfo/`

**Method:** GET or POST

**Authentication:** Include the access token in the Authorization header

**Note:** The access token must have been issued with the `openid` scope to access this endpoint.

```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  https://www.openchatstudio.com/o/userinfo/
```

**Response:**

```json
{
  "sub": "user@example.com",
  "name": "John Doe",
  "is_active": true,
  "team": "team-slug"
}
```

The UserInfo endpoint returns the same claims as the `id_token`, providing a standard way to retrieve user identity information when needed.

## Client-credentials flow (machine-to-machine)

The client-credentials flow lets a server-side integration call the OpenChatStudio API directly, without a user signing in or granting consent. There is no `/authorize` step and no refresh token — your application authenticates directly with the token endpoint using its client ID and secret, and requests a new token whenever the current one expires.

Use this flow for automated integrations, backend jobs, or any service that calls the API on its own behalf rather than a user's.

### How it's different from the authorization code flow

- **No user.** The resulting access token carries no user identity. It cannot be used to sign in as, or act on behalf of, a specific person.
- **Team is fixed by where you registered.** A client-credentials application has no user to pick a team interactively, so it must belong to a team, and every token it issues is scoped to that team. The team comes from **which team's admin page you registered the application on** — there's no separate team field to fill in, and it can't be changed later without registering a new application under the correct team. One application maps to exactly one team — register a separate application for each team you need to integrate with.
- **Global applications can't use this flow.** An application registered from the site-admin page (rather than a team's admin page) has no team, so it supports the authorization code flow only — there's no team to scope a client-credentials token to.
- **No `/authorize` step, no consent screen, and no refresh token.** Request a token directly from the token endpoint whenever you need one, or when your current token expires.

### Step 1: Register a client-credentials application

From your team's admin page, register an OAuth application and select the client-credentials grant type. The application is automatically pinned to that team — this can't be changed later without registering a new application from the correct team's admin page.

You'll receive:

- **Client ID**: A public identifier for your application
- **Client secret**: A confidential secret used to request tokens (keep this secure and server-side only!)

### Step 2: Request an access token

Send a POST request to the token endpoint with your client credentials.

**Token endpoint:** `https://www.openchatstudio.com/o/token/`

#### Required POST Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `grant_type` | Yes | Must be `client_credentials` |
| `client_id` | Yes | Your client ID |
| `client_secret` | Yes | Your client secret (keep this server-side!) |
| `scope` | No | Space-separated list of scopes to request. See [Scopes](#scopes) below |

#### Example Request

```bash
curl -X POST https://www.openchatstudio.com/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "scope=chatbot:read session:read"
```

#### Response

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "chatbot:read session:read"
}
```

There is no `refresh_token` and no `id_token` in this response. When the access token expires, repeat this request to get a new one.

### Step 3: Use the access token

Use the access token exactly as you would with the authorization code flow — include it in the `Authorization` header:

```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  https://www.openchatstudio.com/api/...
```

Every request made with this token resolves to the team the application was pinned to at registration.

### Scopes

Machine tokens can only be granted **API resource scopes**. User-identity scopes (`openid`, `profile`) are never granted to a client-credentials token — requesting them fails when you request the token. See the available API scopes in the [API docs](https://openchatstudio.com/api/docs/).

!!! warning "Authorization is entirely scope-based"
    A machine token has no user, so it has none of the permissions that normally come from a user's team membership. The token's scope, together with the team it's pinned to, is the **entire** authorization decision — anything not explicitly granted by scope is denied. Requesting a broad scope such as `chatbot:write` is equivalent to granting your integration full write access to that resource across the pinned team, so scope each application to the narrowest set of permissions the integration actually needs.

### Limitations

- **User-only endpoints don't work.** Endpoints that require a signed-in user, such as `/me`, or any endpoint gated on a user permission, refuse or ignore machine tokens.
- **No user is recorded as the actor.** Records created or modified using a machine token leave "created by" / "added by" / "cancelled by" style fields empty, since there is no user behind the token.
- **Chat participants come from the request body, not the token.** For chat interactions (`chatbots:interact`), the participant is identified using the OpenAI-standard `user` field in the request body, rather than from the token.
- **An application with no team can't issue usable tokens.** If a client-credentials application has no team (for example, an older application from before applications were team-scoped), token requests won't resolve to any team's data. Ask a Super Admin to assign the application to a team from the site-admin page.

### Best practices

- Keep the client secret server-side; never embed it in a browser, mobile app, or other client the end user can inspect.
- Register a dedicated application per integration so you can revoke or rotate its credentials independently of other integrations.
- Scope each application to the narrowest set of scopes the integration needs.
