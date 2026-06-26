# v2

**Open Chat Studio** API version `v2`.

Build, deploy and monitor chatbots.

## LLM Docs

Simplified per-tag references for LLM consumption:

* [Chatbots](./chatbots.txt){:target="_blank"} — List, retrieve and inspect chatbots (v2; formerly 'experiments').
* [Me](./me.txt){:target="_blank"} — Information about the authenticated user and the team the token is scoped to.

## Endpoints

### Chatbots

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/chatbots/` | List Chatbots |
| GET | `/api/v2/chatbots/{id}/` | Retrieve Chatbot |
| GET | `/api/v2/chatbots/{id}/inspect/` | Inspect Chatbot |

### Me

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v2/me/` | Current User |
