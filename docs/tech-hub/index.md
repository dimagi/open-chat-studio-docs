---
title: Tech Hub
description: Technical guides for developers and administrators configuring Open Chat Studio
---

# Tech Hub

The Tech Hub contains in-depth technical documentation for advanced users and developers. Topics here cover configuration, code examples, and API references that go beyond standard chatbot setup.

You need Super Admin, Pipeline, Experiment, or Team Administrator roles to access most of these features.

## What's covered here

- **[Local Index Optimization](local-index-optimization.md)** — Advanced configuration for [indexed collections](../concepts/collections/indexed.md): embedding model selection, chunk size, chunk overlap, and per-document-type tuning guidance.
- **[Custom Actions](custom_action/index.md)** — Integrate external services into chatbots via OpenAPI schemas. Covers configuration, health monitoring, and testing of Custom Actions.
- **[Calling External APIs](external-api-calls/index.md)** — Use the built-in HTTP client inside Python nodes to securely call third-party APIs from a Pipeline workflow.
- **[Python Node](python_node.md)** — Write custom Python code inside a Pipeline to perform logic, process data, manage session state, and make HTTP requests to external services.
- **[Render a Template and Send an Email Nodes](template_and_email_nodes.md)** — Full Jinja2 variable reference, recipient field syntax, and examples for the Render a Template and Send an Email pipeline nodes.
- **[Tools Reference](tools.md)** — Full argument reference for all built-in tools and the LLM provider tools supported. For a conceptual overview, see [Tools Concepts](../concepts/tools/index.md).
- **[Evaluations](evaluations/index.md)** — Reference for advanced features of Evaluations — a testing system for measuring chatbot performance against different metrics.
- **[OCS API Access](api_access.md)** — Interact with OCS chatbots programmatically using the REST API. Useful for third-party integrations and automated evaluation.
- **[Migrate a Team to Another Instance](migrate_team.md)** — Move a team's chatbots, configuration, and chat history from one OCS instance to another.
