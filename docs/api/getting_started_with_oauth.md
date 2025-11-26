---
title: OAuth2
---

# Getting started with OAuth2

OpenChatStudio uses OAuth2 with the Authorization Code Flow with PKCE (Proof Key for Code Exchange) to enable secure third-party integrations. This guide walks you through the implementation.

## Terminology

- **Authorization server**: The server that issues access tokens e.g. OpenChatStudio
- **Client application**: Your server — requests tokens on behalf of users
- **Authorization code**: Short-lived, one-time-use code exchanged for an access token
- **Access token**: Credential used to access protected resources
- **PKCE**: Security mechanism that protects against authorization code interception attacks
- **Scopes**: Permissions granted to the access token. The available scopes and scopes required by each endpoint are shown in the [API docs](https://chatbots.dimagi.com/api/docs/).

## Overview of the authorization flow

```mermaid
sequenceDiagram
    participant User as User<br/>(Browser)
    participant Client as Your Client<br/>(Server)
    participant OCS as OpenChatStudio<br/>(Authorization Server)
    
    User->>Client: 1. Click button that starts the authorization flow
    Client->>Client: 2. Generate code_challenge from code_verifier
    Client->>OCS: 3. Redirect to /o/authorize/<br/>with client_id, redirect_uri,<br/>code_challenge, scope
    OCS->>User: 4. Show login & consent screen
    User->>OCS: 5. Authenticate & grant permission
    OCS->>Client: 6. Redirect to redirect_uri<br/>with authorization code
    Client->>OCS: 7. POST to /o/token/<br/>with code, code_verifier,<br/>client_id, client_secret
    OCS->>OCS: 8. Validate code_verifier against<br/>code_challenge & verify client
    OCS->>Client: 9. Return access token
```


## Step 1: Register your application with OpenChatStudio

Contact the OpenChatStudio team to register your application. During registration, you must provide one or more **redirect URIs** where you'll receive authorization codes. OpenChatStudio will only redirect to URIs that match exactly what you registered.

You'll receive:

- **Client ID**: A public identifier for your application
- **Client secret**: A confidential secret used for token exchange (keep this secure and server-side only!)

## Step 2: Initiate the authorization call

Your application should redirect the user to OpenChatStudio's authorization endpoint to request permission.

**Authorization endpoint:** `https://www.openchatstudio.com/o/authorize/`

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
| `scope` | No | Space-separated list of scopes (defaults to all scopes if omitted) |
| `team` | No | Specific team to scope the token to |

### Example Request

```uri
https://www.openchatstudio.com/o/authorize/?response_type=code&client_id=TkojUzrbS4nOUeF3deQ0uFwpNNH1kYjYFTisfEIC&redirect_uri=https://your-server/callback/&code_challenge=E9Mrozoa2owUzb1iCHFpQwbi6E3MwMZLvDu0mkMksYI&code_challenge_method=S256&scope=chatbot:read+session:read&state=random_state_string
```

## Step 2: Handle the authorization response

After the user grants permission, OpenChatStudio redirects them to your `redirect_uri` with the authorization code in the query string:

```
https://your-server/callback/?code=auth_code_here&state=random_state_string
```

**Important validations:**

1. Verify the `state` parameter matches the one you sent in Step 1 (protects against CSRF attacks)
2. Extract the `code` parameter
3. Handle errors if present (user denied, invalid client, etc.)

## Step 3: Exchange the authorization code for an access token

Your server must send a POST request to OpenChatStudio's token endpoint.

**Token endpoint:** `https://www.openchatstudio.com/o/token/`

### Required POST Parameters

| Parameter | Description |
|-----------|-------------|
| `grant_type` | Must be `authorization_code` |
| `code` | The authorization code received in Step 2 |
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
  -d "client_id=TkojUzrbS4nOUeF3deQ0uFwpNNH1kYjYFTisfEIC" \
  -d "client_secret=your_client_secret" \
  -d "code_verifier=random_string_used_for_pkce" \
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
}
```

**Key fields:**

- `access_token`: Use this in the `Authorization: Bearer` header for API requests
- `token_type`: Always `Bearer` for this flow
- `expires_in`: Seconds until token expiration
- `scope`: The actual scopes granted

## Step 4: Use the access token

Include the access token in the Authorization header when making API requests:

```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  https://www.openchatstudio.com/api/...
```
