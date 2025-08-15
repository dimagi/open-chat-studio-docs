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

This project includes a plugin for generating API docs from the OCS OpenAPI schema.

See `src/ocs_docs/api_docs_plugin.py`.

The plugin will rebuild the docs when there is a change to the API schema downloaded from the schema URL. To force a rebuild, delete the `api_schema.yml` file.
