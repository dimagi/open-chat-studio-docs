[![](docs/assets/logo.png)](https://github.com/dimagi/open-chat-studio)

This repository contains the user documentation for [Open Chat Studio](https://github.com/dimagi/open-chat-studio).

Open Chat Studio is a platform for building, deploying, and evaluating AI-powered chat applications. It provides tools for working with various LLMs (Large Language Models), creating chatbots, managing conversations, and integrating with different messaging platforms.

## Docs Quickstart

Assuming you've already cloned this repository:

1. Install UV

    ```shell
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    
    See https://docs.astral.sh/uv/getting-started/installation/

2. Set up the project
    
    ```shell
    uv venv
    uv sync
    ```

3. Start the project
    
    ```shell
    uv run mkdocs serve
    ```

### Writing

See the [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/) for how to write documentation.


### API docs

API docs are generated automatically based on the OpenAPI schema. This is done using the `src/ocs_docs/openapi_to_docs.py` utility.

```bash
python src/ocs_docs/openapi_to_docs.py https://openchatstudio.com/api/schema -o docs/api
```

This utility is used in the `update-api-docs` GitHub action.

## Chat Widget Docs

Documentation for the embeddable chat widget lives under `docs/chat_widget/` and ships on a different cadence from the rest of Open Chat Studio. To keep those docs aligned with widget releases:

- Start branches from `widget-develop`, and open the pull request against `widget-develop` so updates can be bundled into the next widget release.
- Limit changes to the widget docs (and their assets) when targeting `widget-develop`; broader documentation updates should continue to go to `main`.
- Release managers merge `widget-develop` back into `main` as part of the widget release process, so no extra action is needed once the PR is approved.
