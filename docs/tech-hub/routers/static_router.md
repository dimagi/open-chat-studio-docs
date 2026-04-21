# Static Router Configuration

The Static Router directs messages based on specific data values stored in your system. Unlike the LLM Router, it does not use an AI model; it simply looks up a "fact" about the user and follows the matching path.

## Supported Data Sources

The Router can inspect "fact" information from three primary sources:

* [Participant Data](../../concepts/participant_data.md) - Persistent data stored with the participant (e.g., language)
* [Session State](../python_node.md#session-state) - Data stored for the current chat session
* [Temporary State](../python_node.md#temporary-state) - Transient data that only exists for the duration of the current pipeline execution.

## Configuration: Keys and Paths
You manage your Router Node through the Advanced Settings.

### 1. The Key (The "What")
The Key is the specific field name you want the router to check. The key should be the name of a field path within one of the supported data sources: Participant Data, Session State, or Temporary State.

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

- key of `user.name` resolves to `"John"`
- key of `user.language` resolves to `"EN"`

### 2. The Matching Path (The "Where")
Once the Key is resolved, the Router looks for a linked downstream node whose output label matches that value.

- If `user.language` is `EN`, the conversation will switch to English.
- Note: If the specified Key is missing or the value does not match any path, the Router follows the Default Output (marked with a blue *).

## Route Tagging

See [Route Tagging details](index.md#route-tagging-observability)

