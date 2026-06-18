# Static Router Configuration

The Static Router directs messages using specific data values already stored in your system. Unlike the LLM Router, it does not use an AI model. It resolves a value from your data and follows the route whose output keyword matches that value.

## Supported Data Sources

The router can inspect data from three primary sources:

* [Participant Data](../../concepts/participant_data.md) - Persistent data stored with the participant (for example, language)
* [Session State](../../tech-hub/python_node.md#session-state) - Data stored for the current chat session
* [Temporary State](../../tech-hub/python_node.md#temporary-state) - Data that exists only for the current pipeline execution

## Configuration: Keys and Paths
You manage your router node through the Advanced Settings.

### 1. The Key (The "What")
The key is the field name in the data source you want the router to check. The key must be from one of the supported data sources: Participant Data, Session State, or Temporary State.

OCS supports selecting nested fields via dotted path notation, for example `your_field.your_subfield`.

For example, given the following participant data in JSON format:

```json
{
    "user": {
        "name": "John",
        "language": "EN"
    }
}
```

- key `user.name` resolves to the value of `"John"`
- key `user.language` resolves to `"EN"` as the value

### 2. Configure route output keywords (Where to go)
For each downstream path from this router, set an **output keyword**.

At runtime:

- OCS resolves the configured key to a value.
- OCS compares that value to **output keywords** on downstream paths.
- If a keyword matches, OCS follows that path.
- If no keyword matches, OCS follows the Default Output (blue asterisk).

Example:

- Configured key: user.language
- Path A output keyword: EN
- Path B output keyword: FR
- Resolved value: EN
Result: the router follows Path A

#### Keyword Case Behavior
To ensure technical consistency, OCS handles keywords with the following rules:
- Automatic Uppercase: All keywords are stored in uppercase. While matching is case-insensitive (for example, `Help` matches `HELP`), we recommend using uppercase during configuration for clarity.


### 3. Matching behavior and fallback
- If the key is missing, routing falls back to Default Output.
- If the key resolves but no output keyword matches, routing falls back to Default Output.
- If part of a nested path is missing (for example, user.profile.language when profile does not exist), routing falls back to Default Output.


## Route Tagging

See [Route Tagging details](index.md#route-tagging-observability)
