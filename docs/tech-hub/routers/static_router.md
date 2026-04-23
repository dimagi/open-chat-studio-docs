# Static Router Configuration

The Static Router directs messages using specific data values already stored in your system. Unlike the LLM Router, it does not use an AI model. It looks up a value about the user and follows the matching path.

## Supported Data Sources

The router can inspect data from three primary sources:

* [Participant Data](../../concepts/participant_data.md) - Persistent data stored with the participant (for example, language)
* [Session State](../python_node.md#session-state) - Data stored for the current chat session
* [Temporary State](../python_node.md#temporary-state) - Data that exists only for the current pipeline execution

## Configuration: Keys and Paths
You manage your router node through the Advanced Settings.

### 1. The Key (The "What")
The key is the field name you want the router to check. The key should be a field path from one of the supported data sources: Participant Data, Session State, or Temporary State.

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

- key `user.name` resolves to `"John"`
- key `user.language` resolves to `"EN"`

### 2. The Matching Path (The "Where")
Once the key is resolved, the router looks for a linked downstream node whose output label matches that value.

- If `user.language` is `EN`, the conversation will switch to English.
- Note: If the specified key is missing, or the value does not match any path, the router follows the Default Output (marked with a blue *).

## Route Tagging

See [Route Tagging details](index.md#route-tagging-observability)

