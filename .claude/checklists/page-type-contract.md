# Page-Type Contract

| Page type | Folder | Audience | Must include | Must not include | Example |
|---|---|---|---|---|---|
| Concepts | `concepts/` | End users, advanced users, developers | High-level "why"/"what" explanation, simple language | Jargon, API instructions, code examples — link to Tech Hub/How-To instead | `concepts/sessions.md` |
| How-To Guide | `how-to/` | End users, advanced users, developers | Prerequisites, numbered steps (imperative verbs), prose example use cases, expected outcomes, brief common-issues list | Code snippets, in-depth troubleshooting/diagnostics — link to Tech Hub instead | `how-to/adjust_llm_node_model_parameters.md` |
| Tech Hub | `tech-hub/` | Advanced users, developers | Code examples with expected output, API references, in-depth troubleshooting, architecture/implementation detail | Repeating Concepts/How-To content — link to it instead | `tech-hub/template_and_email_nodes.md` |
| Tutorial | `tutorials/` | End users (first-time) | Numbered steps (imperative verbs), simple real-world application | Advanced features, complex config, code, API references, common pitfalls — write a How-To Guide instead | `tutorials/configure_llm_node.md` |
| Chat Widget | `chat_widget/` | Developers | Prerequisites, code examples, API references, troubleshooting | General OCS/end-user content | `chat_widget/reference.md` |

Diagrams and flowcharts (e.g. mermaid) are useful on any page type to illustrate concepts or steps — use sparingly on Tutorials, which should stay simple for first-time users.
