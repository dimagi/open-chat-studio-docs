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

The Python node provides an `http` global that enables secure HTTP requests to external APIs. This client includes built-in security features to protect against common vulnerabilities and supports automatic credential injection through Authentication Providers.

#### Overview

The `http` is available as a global variable in your Python node code and can be used to make HTTP requests without importing external libraries. It provides a safe, team-aware way to interact with external APIs.

```python
def main(input, **kwargs) -> str:
    # Make a GET request
    response = http.get("https://api.example.com/data")

    # Process the response
    return f"Retrieved {len(response['json'])} items"
```

#### Available Methods

The `http` supports the following HTTP methods:

- `get(url, **kwargs)` - Send a GET request
- `post(url, **kwargs)` - Send a POST request
- `put(url, **kwargs)` - Send a PUT request
- `patch(url, **kwargs)` - Send a PATCH request
- `delete(url, **kwargs)` - Send a DELETE request

All methods accept the following keyword-only parameters:

- `headers` - Dictionary of HTTP headers
- `params` - URL query parameters
- `json` - JSON data to send in the request body (mutually exclusive with `data` and `files`)
- `data` - Form data (dict) or raw body content (str/bytes). Can be combined with `files` for multipart form uploads
- `timeout` - Request timeout in seconds (automatically clamped between 1s and the system maximum)
- `files` - File upload data. See [File Uploads](#file-uploads) for details
- `auth` - Name of an [Authentication Provider](../../team/authentication_providers.md) to inject credentials. This is a string, not a credentials tuple

#### Response Structure

All HTTP methods return a dictionary containing the response data:

```python
{
    "status_code": 200,
    "headers": {...},
    "text": "body as text",  # this is always present
    "json": {"body": "as json"},  # this is `None` if the response was not JSON
    "is_success": 200 <= status_code < 300,
    "is_error": status_code >= 400,
}
```

Access response data using dictionary keys:

```python
response = http.get("https://api.example.com/data")
status = response["status_code"]
data = response["json"]
text_content = response["text"]
```

#### Security Features

The HTTP client includes several built-in security protections:

**SSRF Prevention**: Blocks requests to private IP addresses, localhost, and other internal network resources to prevent Server-Side Request Forgery attacks.

**Request/Response Size Limits**: Enforces maximum size limits on both requests and responses to prevent memory exhaustion.

**Timeout Clamping**: Automatically limits request timeouts to prevent indefinite hanging.

**Blocked Headers**: Certain sensitive headers are blocked to prevent security issues.

**Automatic Retries**: Requests that receive a `429`, `502`, `503`, or `504` status code are automatically retried up to 3 times with exponential backoff. The client also respects the `Retry-After` header when present. Connection errors and timeouts are also retried.

**No Redirect Following**: The HTTP client does not follow redirects automatically. If a request returns a `3xx` redirect status, you will receive the redirect response directly and must handle it in your code.

**Request Count Limit**: There is a maximum number of HTTP requests that can be made per pipeline run. Exceeding this limit will raise an error.

#### Exceptions

The HTTP client raises exceptions for infrastructure-level errors. You should handle these in your code if you need custom error handling:

| Exception | When it's raised |
|-----------|-----------------|
| `http.RequestLimitExceeded` | Maximum number of requests per pipeline run exceeded |
| `http.RequestTooLarge` | Request body or file upload exceeds the size limit |
| `http.ResponseTooLarge` | Response body exceeds the size limit |
| `http.ConnectionError` | Connection failed after all retries exhausted |
| `http.TimeoutError` | Request timed out after all retries exhausted |
| `http.InvalidURL` | URL blocked by SSRF protection (private IPs, localhost, etc.) |
| `http.AuthProviderError` | Auth provider not found or not available |

!!! note
    HTTP error status codes like `400`, `401`, `404`, or `500` do **not** raise exceptions. These are returned as normal response dicts. Always check `response["status_code"]` or `response["is_error"]` to detect HTTP-level errors.

##### Handling Exceptions

Use `try`/`except` blocks to catch infrastructure-level errors and provide user-friendly responses. Since the exception classes cannot be imported directly, reference them from the `http` global:

```python
def main(input, **kwargs) -> str:
    try:
        response = http.get("https://api.example.com/data", timeout=10)
    except http.TimeoutError:
        return "The request timed out. Please try again later."
    except http.ConnectionError:
        return "Could not connect to the server. Please try again later."
    except http.InvalidURL:
        return "The request was blocked for security reasons."
    except http.RequestLimitExceeded:
        return "Too many requests have been made. Please try again later."

    # HTTP error status codes (4xx, 5xx) don't raise exceptions,
    # so check the response directly
    if response["is_error"]:
        return f"Request failed with status {response['status_code']}"

    return f"Got data: {response['json']}"
```

You can also catch multiple exceptions at once:

```python
def main(input, **kwargs) -> str:
    try:
        response = http.post(
            "https://api.example.com/submit",
            json={"query": input},
            auth="my-api",
            timeout=15,
        )
    except (http.TimeoutError, http.ConnectionError) as e:
        return f"Network error: {e}"
    except (http.RequestTooLarge, http.ResponseTooLarge):
        return "The request or response was too large."
    except http.AuthProviderError:
        return "Authentication is not configured correctly."

    if response["is_success"]:
        return f"Result: {response['json']}"
    else:
        return f"API error (status {response['status_code']}): {response['text']}"
```

#### Using Authentication Providers

The `http` can automatically inject credentials from your team's [Authentication Providers](../../team/authentication_providers.md) into HTTP requests. This provides a secure way to manage API credentials without hardcoding them in your code. To use a configured Authentication Provider, pass the name of the provider to the request method using the `auth` keyword:

```python
http.get("https://example.com", auth="my auth provider")
```

#### Complete Examples

##### Example 1: Fetching Data from a Public API

```python
def main(input, **kwargs) -> str:
    """Fetch weather data from a public API"""
    response = http.get(
        "https://api.weather.gov/gridpoints/TOP/31,80/forecast",
        timeout=10
    )

    if response["status_code"] == 200:
        data = response["json"]
        forecast = data["properties"]["periods"][0]
        return f"Weather: {forecast['shortForecast']}, Temp: {forecast['temperature']}°F"
    else:
        return f"Error: Unable to fetch weather (status {response['status_code']})"
```

##### Example 2: Posting Data with Authentication

```python
def main(input, **kwargs) -> str:
    """Submit form data to an external API"""
    # Parse user input
    user_data = {
        "message": input,
        "timestamp": "2024-01-01T12:00:00Z"
    }

    # Post to API with authentication
    response = http.post(
        "https://api.example.com/submissions",
        json=user_data,
        auth="my-api-key",
        timeout=15
    )

    if response["status_code"] == 201:
        result = response["json"]
        return f"Submission successful! ID: {result['id']}"
    else:
        return f"Submission failed with status {response['status_code']}"
```

##### Example 3: Working with Query Parameters

```python
def main(input, **kwargs) -> str:
    """Search an API with query parameters"""
    # Build query parameters from user input
    params = {
        "q": input,
        "limit": 10,
        "format": "json"
    }

    response = http.get(
        "https://api.example.com/search",
        params=params,
        auth="search-api"
    )

    if response["status_code"] == 200:
        results = response["json"]
        count = len(results["items"])
        return f"Found {count} results for '{input}'"
    else:
        return "Search failed"
```

##### Example 4: Handling Different Response Types

```python
def main(input, **kwargs) -> str:
    """Handle both JSON and text responses"""
    response = http.get(
        "https://api.example.com/data",
        auth="api-provider"
    )

    # Check content type
    content_type = response["headers"].get("Content-Type", "")

    if "application/json" in content_type:
        data = response["json"]
        return f"JSON data: {data}"
    else:
        text = response["text"]
        return f"Text data: {text[:100]}..."  # First 100 chars
```

#### File Uploads

The `files` parameter allows you to upload files as part of a multipart form request. It accepts either a dictionary or a list of tuples mapping field names to file values.

Each file value can be one of:

- An `Attachment` object from the temporary state `attachments` list
- A tuple of `(filename, data, content_type)` where `data` is bytes
- Raw `bytes` (the field name is used as the filename with `application/octet-stream` content type)

!!! note
    The `json` parameter cannot be combined with `files`. Use `data` (dict) alongside `files` if you need to send additional form fields with your file upload.

##### Example 5: Uploading User Attachments to an External API

```python
def main(input, **kwargs) -> str:
    """Forward all user attachments to an external API"""
    attachments = get_temp_state_key("attachments")

    if not attachments:
        return "No files were uploaded"

    # Pass attachments directly — the HTTP client handles them
    files = [("files", attachment) for attachment in attachments]

    response = http.post(
        "https://api.example.com/upload",
        files=files,
        auth="upload-api",
        timeout=30
    )

    if response["is_success"]:
        return f"Successfully uploaded {len(attachments)} file(s)"
    else:
        return f"Upload failed with status {response['status_code']}"
```

##### Example 6: Uploading a Single Attachment with Form Data

```python
def main(input, **kwargs) -> str:
    """Upload the first attachment with additional metadata"""
    attachments = get_temp_state_key("attachments")

    if not attachments:
        return "Please upload a file"

    attachment = attachments[0]

    response = http.post(
        "https://api.example.com/documents",
        files={"document": attachment},
        data={"description": input, "source": "chatbot"},
        auth="doc-api",
        timeout=30
    )

    if response["is_success"]:
        result = response["json"]
        return f"Uploaded '{attachment.name}' — Document ID: {result['id']}"
    else:
        return f"Upload failed: {response['text']}"
```

##### Example 7: Uploading Raw Bytes

```python
def main(input, **kwargs) -> str:
    """Generate a CSV and upload it"""
    csv_content = "name,email\nAlice,alice@example.com\nBob,bob@example.com\n"
    csv_bytes = csv_content.encode("utf-8")

    response = http.post(
        "https://api.example.com/import",
        files={"file": ("contacts.csv", csv_bytes, "text/csv")},
        auth="import-api"
    )

    if response["is_success"]:
        return "CSV uploaded successfully"
    else:
        return f"Upload failed: {response['status_code']}"
```

##### Example 8: Filtering Attachments by Type Before Uploading

```python
def main(input, **kwargs) -> str:
    """Upload only image attachments"""
    attachments = get_temp_state_key("attachments")

    images = [a for a in attachments if a.content_type.startswith("image/")]

    if not images:
        return "No images found in attachments"

    files = [("images", img) for img in images]

    response = http.post(
        "https://api.example.com/gallery",
        files=files,
        auth="gallery-api",
        timeout=30
    )

    if response["is_success"]:
        return f"Uploaded {len(images)} image(s)"
    else:
        return f"Upload failed: {response['text']}"
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

1. **Check status codes**: HTTP error status codes (4xx, 5xx) do not raise exceptions — they are returned as normal response dicts. Always check `response["status_code"]` or use `response["is_success"]` and `response["is_error"]` to detect HTTP-level errors. Infrastructure errors like connection failures, timeouts, and size limit violations **do** raise exceptions (see [Exceptions](#exceptions)).

2. **Set reasonable timeouts**: Specify timeout values to prevent requests from hanging indefinitely.

3. **Use Authentication Providers**: Never hardcode API keys or credentials in your code. Use Authentication Providers instead.

4. **Validate user input**: If using user input in URLs or parameters, validate and sanitize it first.

5. **Limit data size**: Be mindful of the size of data you're requesting or sending.

6. **Cache when appropriate**: If making repeated requests for the same data, consider caching results in session state.

#### Troubleshooting

**"Network access is disabled"**: Network access must be enabled in the pipeline configuration. Contact your team administrator.

**"SSRF protection blocked request"**: The URL you're trying to access is blocked for security reasons (e.g., localhost, private IPs).

**"Authentication provider not found"**: Verify the provider name matches exactly what's configured in your team settings.

**"Request timeout"**: The external API took too long to respond. Try increasing the timeout or check if the API is available.

**"Connection refused"**: The target server is not accepting connections. Verify the URL and check if the service is running.

**"Request limit exceeded"**: You have made too many HTTP requests in a single pipeline run. Reduce the number of requests or restructure your pipeline.

**"Request body exceeds ... bytes"** / **"File upload exceeds ... bytes"**: The data you are sending is too large. Reduce the payload size or split it into multiple requests.

**"Response body exceeds ... bytes"**: The external API returned a response that is too large. Consider requesting a smaller payload (e.g., use pagination or limit fields).

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
