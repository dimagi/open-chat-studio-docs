# Participant Data API

Use the participant data API when you need to list participants, inspect their stored data, or sync participant records from an external system.

The API works with participant records for a team and stores separate data entries per chatbot.

## Endpoints

| Endpoint | Purpose | Scope |
| --- | --- | --- |
| `GET /api/participants/` | Lists participants and their per-chatbot data. | `participants:read` |
| `POST /api/participants/` | Creates or updates participant data. | `participants:write` |

## Listing participants

`GET /api/participants/` returns a cursor-paginated list of participants.

Supported query parameters:

* `identifier` - Filter by participant identifier.
* `platform` - Filter by channel platform.
* `chatbot` - Filter by chatbot public id.
* `cursor` - Use the pagination cursor from a previous response.
* `page_size` - Set how many results to return per page.

Each participant response includes a `data` array. Each data entry identifies the chatbot it belongs to with `chatbot` and `chatbot_id`.

## Updating participant data

`POST /api/participants/` creates or updates participant data for a participant.

Use this endpoint when you need to:

* Store participant data from an external system.
* Sync participant records into OCS.
* Update data outside the conversation flow.

For the full request body and response schema, see the generated [API docs](../api/index.md).

## Related docs

* [Participant Data](../concepts/participant_data.md)
* [API docs](../api/index.md)