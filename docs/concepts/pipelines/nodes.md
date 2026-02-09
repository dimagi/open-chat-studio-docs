# Node Types

!!! note Examples

    See [cookbook](../../how-to/workflow_cookbook.md) for example usage. 

## LLM
Use an LLM to respond to the node input. This node can be configured with a prompt to give the LLM instructions on how to respond. It can also be configured to use [tools](../tools/index.md) which enable it to perform additional actions.

## Routers

Router nodes allow you to route the input to one of the linked nodes. This is useful if you want your bot to behave
differently depending on the input or some persistent context. For example, you might want to route the input to a different node if the user is asking for help with a specific topic.

Router nodes share some common configuration such as the list of route options. Router nodes can also be configured to
tag the output message with the selected route. This is useful for debugging and for tracking the flow of messages through the pipeline.
The format of the tag is `<node_name>:<route_name>` where `<route_name>` is the name of the route selected by the router node.

!!! info "Router Keywords Are Uppercase"

    All router keywords are automatically converted to uppercase. When configuring router outputs, use uppercase keywords to match this behavior. Keyword matching is case-insensitive, so "HELP", "Help", and "help" will all match the same route.

### LLM Router
Routes the input to one of the linked nodes using an LLM. In this case, the LLM acts as a classifier using the prompt provided to classify an incoming message into a set of discrete categories that allow messages to be routed.

The `outputs` listed by the node are the available classification labels. These should match the classification categories specified in your prompt. They can be adjusted through the `Advanced` settings for the node. The top output, which is prepended by a blue `*` is the default label. In the event that the LLM generates a response outside of the specified `outputs`, the route with the default label will be taken.

!!! info "Best practices for configuring a LLM Router"

    It is advisable to use the [Node history mode](history.md#node) for an LLM Router to avoid unintentionally supplying few-shot examples to the node with an incorrect output format.

### Static Router
The Static Router node allows you to route the input to one of the linked nodes based on the value of a specific key in the data source. This is useful if you want your bot to behave differently depending on the value of a specific key in the data source.

The data source can be any of the following:

* [Participant Data](../participant_data.md)
* [Session State](#session-state)
* [Temporary State](#temporary-state)

The key should be a name of a field in the data source and supports selecting nested fields via the `<field>.<subfield>` syntax. For example, if the data source is a JSON object with the following structure:

```json
{
    "user": {
        "name": "John",
        "age": 30
    }
}
```

You can select the `name` field using the key `user.name` and the `age` field using the key `user.age`.

If the field is not present in the data source, the router will not route the input to the first linked node.

## Assistant
Use an OpenAI assistant to respond to the input.

## Python Node
The Python node allows the bot builder to execute custom Python code to perform logic, data processing, or other tasks.

The code **must** define a `main` function which takes the node input as a string and returns a string to pass to the next node.
The `main` function must also accept arbitrary keyword arguments to support future features. Here is an example of what the code might look like:

```python
def main(input, **kwargs) -> str:
    # Put your code here
    return input
```

The `input` parameter is a string that contains the input to the node. The return value of the function is a string that will be passed to the next node in the pipeline.

### Additional Keyword Arguments

The following additional arguments are provided:

* `node_inputs: list[str]` - A list of all the inputs to the node at the time of execution. This will be the same as `[input]` except when the node is part of a workflow with [parallel branches](./index.md#parallel-nodes).

!!! warning

    All the code must be encapsulated in a `main` function. You can write other functions but they must be within the scope of the `main` function. For example:

    ``` py
    def main(input, **kwargs):
        def important(arg):
            return arg + "!"

        return important(input)
    ```

### Utility Functions

The Python node provides a set of utility functions that can be used to interact with the user's data and the pipeline state.

#### ::: python_node.get_participant_data
#### ::: python_node.set_participant_data
#### ::: python_node.set_participant_data_key
#### ::: python_node.append_to_participant_data_key
#### ::: python_node.increment_participant_data_key
#### ::: python_node.get_participant_schedules
#### ::: python_node.get_temp_state_key
#### ::: python_node.set_temp_state_key
#### ::: python_node.get_session_state_key
#### ::: python_node.set_session_state_key
#### ::: python_node.get_selected_route
#### ::: python_node.get_node_path
#### ::: python_node.get_all_routes
#### ::: python_node.add_message_tag
#### ::: python_node.add_session_tag
#### ::: python_node.get_node_output
#### ::: python_node.require_node_outputs
#### ::: python_node.wait_for_next_input
#### ::: python_node.abort_with_message

### HTTP Client

The Python node provides an `http_client` global that enables secure HTTP requests to external APIs. This client includes built-in security features to protect against common vulnerabilities and supports automatic credential injection through Authentication Providers.

#### Overview

The `http_client` is available as a global variable in your Python node code and can be used to make HTTP requests without importing external libraries. It provides a safe, team-aware way to interact with external APIs.

```python
def main(input, **kwargs) -> str:
    # Make a GET request
    response = http_client.get("https://api.example.com/data")

    # Process the response
    data = response.json()
    return f"Retrieved {len(data)} items"
```

#### Available Methods

The `http_client` supports the following HTTP methods:

- `get(url, **kwargs)` - Send a GET request
- `post(url, **kwargs)` - Send a POST request
- `put(url, **kwargs)` - Send a PUT request
- `patch(url, **kwargs)` - Send a PATCH request
- `delete(url, **kwargs)` - Send a DELETE request

All methods accept the same parameters as Python's `requests` library, including:

- `headers` - Dictionary of HTTP headers
- `params` - URL query parameters
- `json` - JSON data to send in the request body
- `data` - Form data or raw body content
- `timeout` - Request timeout (automatically clamped to safe limits)

#### Security Features

The HTTP client includes several built-in security protections:

**SSRF Prevention**: Blocks requests to private IP addresses, localhost, and other internal network resources to prevent Server-Side Request Forgery attacks.

**Request/Response Size Limits**: Enforces maximum size limits on both requests and responses to prevent memory exhaustion.

**Timeout Clamping**: Automatically limits request timeouts to prevent indefinite hanging.

**Blocked Headers**: Certain sensitive headers are blocked to prevent security issues.

**Automatic Retries**: Failed requests are automatically retried with exponential backoff for improved reliability.

!!! warning "Network Access Toggle"

    Network access must be explicitly enabled for the pipeline. If disabled, any attempt to use `http_client` will raise an error. Contact your team administrator if you need network access enabled.

#### Using Authentication Providers

The `http_client` can automatically inject credentials from your team's [Authentication Providers](../../team/authentication_providers.md) into HTTP requests. This provides a secure way to manage API credentials without hardcoding them in your code.

##### Basic Usage with Authentication

To use an Authentication Provider, specify the `auth_provider` parameter:

```python
def main(input, **kwargs) -> str:
    # Use the configured authentication provider
    response = http_client.get(
        "https://api.example.com/protected/resource",
        auth_provider="my-api-provider"
    )
    return response.text
```

##### Authentication Provider Types

The HTTP client supports all Authentication Provider types configured in Open Chat Studio:

**API Key**: Automatically adds the API key to the specified header.

```python
# Authentication Provider configured with:
# - Type: API Key
# - Header: X-API-Key
# - Value: your-api-key

response = http_client.get(
    "https://api.example.com/data",
    auth_provider="api-key-provider"
)
# Request will include: X-API-Key: your-api-key
```

**Bearer Token**: Automatically adds the token to the Authorization header.

```python
# Authentication Provider configured with:
# - Type: Bearer Token
# - Token: your-bearer-token

response = http_client.post(
    "https://api.example.com/create",
    json={"name": "example"},
    auth_provider="bearer-provider"
)
# Request will include: Authorization: Bearer your-bearer-token
```

**Basic Auth**: Automatically adds HTTP Basic Authentication.

```python
# Authentication Provider configured with:
# - Type: Basic Auth
# - Username: user
# - Password: pass

response = http_client.get(
    "https://api.example.com/resource",
    auth_provider="basic-provider"
)
# Request will include appropriate Authorization header
```

**CommCare**: Supports CommCare-specific authentication schemes.

```python
response = http_client.get(
    "https://commcarehq.example.com/api/v0.5/case/",
    auth_provider="commcare-provider"
)
```

##### Setting Up an Authentication Provider

To use authentication providers with the HTTP client:

1. Navigate to your team settings
2. Create a new Authentication Provider with the appropriate type
3. Configure the credentials (API key, token, username/password, etc.)
4. Reference the provider name in your Python node code

See [Authentication Providers](../../team/authentication_providers.md) for detailed setup instructions.

#### Complete Examples

##### Example 1: Fetching Data from a Public API

```python
def main(input, **kwargs) -> str:
    """Fetch weather data from a public API"""
    try:
        response = http_client.get(
            "https://api.weather.gov/gridpoints/TOP/31,80/forecast",
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            forecast = data["properties"]["periods"][0]
            return f"Weather: {forecast['shortForecast']}, Temp: {forecast['temperature']}°F"
        else:
            return f"Error: Unable to fetch weather (status {response.status_code})"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
```

##### Example 2: Posting Data with Authentication

```python
def main(input, **kwargs) -> str:
    """Submit form data to an external API"""
    try:
        # Parse user input
        user_data = {
            "message": input,
            "timestamp": "2024-01-01T12:00:00Z"
        }

        # Post to API with authentication
        response = http_client.post(
            "https://api.example.com/submissions",
            json=user_data,
            auth_provider="my-api-key",
            timeout=15
        )

        if response.status_code == 201:
            result = response.json()
            return f"Submission successful! ID: {result['id']}"
        else:
            return f"Submission failed with status {response.status_code}"

    except Exception as e:
        return f"Error submitting data: {str(e)}"
```

##### Example 3: Working with Query Parameters

```python
def main(input, **kwargs) -> str:
    """Search an API with query parameters"""
    try:
        # Build query parameters from user input
        params = {
            "q": input,
            "limit": 10,
            "format": "json"
        }

        response = http_client.get(
            "https://api.example.com/search",
            params=params,
            auth_provider="search-api"
        )

        if response.status_code == 200:
            results = response.json()
            count = len(results["items"])
            return f"Found {count} results for '{input}'"
        else:
            return "Search failed"

    except Exception as e:
        return f"Search error: {str(e)}"
```

##### Example 4: Handling Different Response Types

```python
def main(input, **kwargs) -> str:
    """Handle both JSON and text responses"""
    try:
        response = http_client.get(
            "https://api.example.com/data",
            auth_provider="api-provider"
        )

        # Check content type
        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type:
            data = response.json()
            return f"JSON data: {data}"
        else:
            text = response.text
            return f"Text data: {text[:100]}..."  # First 100 chars

    except Exception as e:
        return f"Error: {str(e)}"
```

#### Error Handling

Always wrap HTTP requests in try-except blocks to handle potential errors gracefully:

```python
def main(input, **kwargs) -> str:
    try:
        response = http_client.get("https://api.example.com/data")
        response.raise_for_status()  # Raises error for 4xx/5xx status codes
        return response.json()
    except http_client.exceptions.ConnectionError:
        return "Unable to connect to the API"
    except http_client.exceptions.Timeout:
        return "Request timed out"
    except http_client.exceptions.HTTPError as e:
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

#### Common Status Codes

When checking response status codes:

- `200` - OK (successful GET)
- `201` - Created (successful POST)
- `204` - No Content (successful DELETE)
- `400` - Bad Request (client error)
- `401` - Unauthorized (authentication required)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `429` - Too Many Requests (rate limited)
- `500` - Internal Server Error
- `503` - Service Unavailable

#### Best Practices

1. **Always handle errors**: Network requests can fail for many reasons. Always use try-except blocks.

2. **Check status codes**: Don't assume a request succeeded. Check `response.status_code` or use `response.raise_for_status()`.

3. **Set reasonable timeouts**: Specify timeout values to prevent requests from hanging indefinitely.

4. **Use Authentication Providers**: Never hardcode API keys or credentials in your code. Use Authentication Providers instead.

5. **Validate user input**: If using user input in URLs or parameters, validate and sanitize it first.

6. **Limit data size**: Be mindful of the size of data you're requesting or sending.

7. **Cache when appropriate**: If making repeated requests for the same data, consider caching results in session state.

#### Troubleshooting

**"Network access is disabled"**: Network access must be enabled in the pipeline configuration. Contact your team administrator.

**"SSRF protection blocked request"**: The URL you're trying to access is blocked for security reasons (e.g., localhost, private IPs).

**"Authentication provider not found"**: Verify the provider name matches exactly what's configured in your team settings.

**"Request timeout"**: The external API took too long to respond. Try increasing the timeout or check if the API is available.

**"Connection refused"**: The target server is not accepting connections. Verify the URL and check if the service is running.

### Temporary State
The Python node can also access and modify the temporary state of the pipeline. The temporary state is a dictionary that is unique to each run of the pipeline (each new message from the user) and is not stored between sessions.

The temporary state can be accessed and modified using the [get_temp_state_key](#python_node.get_temp_state_key) and [set_temp_state_key](#python_node.set_temp_state_key) utility functions.

Temporary state contains the following keys by default. These keys can not be modified or deleted:

| Key           | Description                                                                  |
|---------------|------------------------------------------------------------------------------|
| `user_input`  | The message sent by the user                                                 |
| `outputs`     | The outputs generated by the previous node                                   |
| `attachments` | A list of attachments passed in by the user. See [Attachments](#attachments) |

In addition to these keys, the temporary state can also contain custom key-value pairs that can be set and accessed by the Python node and by the [Static Router](#static-router) node.

Here is an example of a temporary state dictionary:

```python
{
    "user_input": "Please help me with my problem",
    "outputs": {
        "Assistant": "I'm here to help! What can I do for you?"
    },
    "attachments": [
        Attachment(...),
    ],
    "my_custom_key": "my_custom_value",
}
```

### Session State
The Python node can also access and modify the state of the participant's session. This state is a dictionary that is scoped to each session that the user might have with the bot.

The session state can be accessed and modified using the [get_session_state_key](#python_node.get_session_state_key) and [set_session_state_key](#python_node.set_session_state_key) utility functions.

### Attachments

Part of the temporary state is a list of attachments. Attachments are files that the user has uploaded to the bot. Each attachment has the following fields:

| Field                 | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `name`                | The name of the file                                                  |
| `size`                | The size of the file in bytes                                         |
| `content_type`        | The MIME type of the file                                             |
| `upload_to_assistant` | Whether the file should be uploaded to the assistant as an attachment |
| `read_bytes()`        | Reads the attachment content as bytes.                                |
| `read_text()`         | Reads the attachment content as text.                                 |

Here is an example of an attachment object:

```python
attachment = Attachment(
    name="proposal.pdf",
    size=1234,
    content_type="application/pdf",
    upload_to_assistant=False,
)
content = attachment.read_text()
```

#### Supported File Types
The Python node currently only supports reading the contents of the following file types:

- Text-based formats (TXT, CSV, HTML, JSON, XML, etc.)
- PDF
- DOCX
- XLSX
- XLS
- Outlook
- PPTX

Other file types can still be uploaded to assistants but the Python Node is not able to read the file contents using the `read_text()` method on the attachment.

## Template
Renders a [Jinja](https://jinja.palletsprojects.com/en/stable/templates/) template.

## Available Template Variables
The following variables are available in the template context:

| Key                     | Description                                                          | Type            |
|-------------------------|----------------------------------------------------------------------|-----------------|
| `input`                 | The input to the node                                                | String          |
| `node_inputs`           | The list of all inputs to the node in the case of parallel workflows | List of strings |
| `temp_state`            | Pipeline temporary state                                             | Dict            |
| `session_state`         | Session state                                                        | Dict            |
| `participant_details`   | Participant details (`identifier`, `platform`)                       | Dict            |
| `participant_data`      | Participant data                                                     | Dict            |
| `participant_schedules` | Participant schedule data                                            | List            |

### Sample Template
```
Input: {{ input }}
Node Inputs: {{ node_inputs }}
Temp State Key: {{ temp_state.my_key }}
Participant ID: {{ participant_details.identifier }}
Participant Platform: {{ participant_details.platform }}
Participant Data: {{ participant_data.custom_key }}
Schedules: {{ participant_schedules }}
```

## Email
Send the input to the specified list of email addresses. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Extract Structured Data
Extract structured data from the input. This node acts as a passthrough, meaning the output will be identical to the input, allowing it to be used in a pipeline without affecting the conversation.

## Update Participant Data
Extract structured data and save it as participant data.
