[![](docs/assets/logo.png)](https://github.com/dimagi/open-chat-studio)

This repository contains the user documentation for [Open Chat Studio](https://github.com/dimagi/open-chat-studio).

Open Chat Studio is a platform for building, deploying, and evaluating AI-powered chat applications. It provides tools for working with various LLMs (Language Learning Models), creating chatbots, managing conversations, and integrating with different messaging platforms.

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
