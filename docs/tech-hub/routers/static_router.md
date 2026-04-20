# Static Router Configuration

The Static Router routes messages based on the value of a key in a data source. No AI model is involved.

## Supported Data Sources

The key can be read from any of the following:

* [Participant Data](../../concepts/participant_data.md) - Persistent data stored with the participant
* [Session State](../python_node.md#session-state) - Data stored for the current chat session
* [Temporary State](../python_node.md#temporary-state) - Transient data for the current pipeline execution

## Key Syntax

The key field accepts dotted path notation to select nested fields. For example, given the following participant data in JSON format:

```json
{
    "user": {
        "name": "John",
        "age": 30
    }
}
```

- key `user.name` resolves to `"John"`
- key `user.age` resolves to `30`

If the specified key is not present in the data source, the router falls back to the default (first linked) output.

## Route Tagging

!!! tip "Tip"

    Use the Output Message [Tagging](../../concepts/tags.md) feature to make it easy to review how messages are flowing through your pipeline. 
