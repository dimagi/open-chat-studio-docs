# Render a Template and Send an Email Nodes

The Render a Template and Send an Email nodes both use [Jinja2](https://jinja.palletsprojects.com/en/stable/templates/) templates to produce dynamic text from pipeline state. This page is the complete reference for the shared template variable context, field behaviour, and syntax examples for both nodes.

For a plain-English introduction to these nodes, see [Node Types](../concepts/pipelines/nodes.md).

## Shared Template Variable Context

Both nodes evaluate templates against the same context dictionary. All keys listed below are available in every template field.

| Key                     | Type            | Description                                                                    |
|-------------------------|-----------------|--------------------------------------------------------------------------------|
| `input`                 | String          | The current input to the node                                                  |
| `node_inputs`           | List of strings | All inputs to the node — same as `[input]` except in [parallel branches](../concepts/pipelines/parallel.md) |
| `temp_state`            | Dict            | Temporary state for this pipeline run — reset on each new message              |
| `session_state`         | Dict            | State scoped to the participant's current session                               |
| `participant_details`   | Dict            | Contains `identifier` and `platform` for the current participant               |
| `participant_data`      | Dict            | Persistent key-value data stored against the participant                       |
| `participant_schedules` | List            | Scheduled messages associated with the participant                             |

!!! note "Session-dependent keys"

    `participant_details`, `participant_data`, and `participant_schedules` are only populated when the pipeline is running inside an active session. They are empty when the pipeline is tested in isolation without a session context.

!!! warning "Strict variable resolution"

    Templates use strict undefined behaviour. Referencing a variable that does not exist in the context will raise an error at runtime. Use Jinja2's `default` filter to provide fallback values: `{{ participant_data.name | default('there') }}`.

## Render a Template Node

### Template Field

The **template** field is a single Jinja2 template string. The node renders it against the context and passes the result to the next node.

**Example — building a prompt for a downstream LLM node:**

```jinja
You are helping {{ participant_details.identifier }}.

Their question: {{ input }}

Relevant context from their profile:
- Preferred language: {{ participant_data.language | default('English') }}
- Account tier: {{ participant_data.tier | default('standard') }}
```

**Example — combining parallel branch inputs:**

```jinja
Summary from branch A: {{ node_inputs[0] }}
Summary from branch B: {{ node_inputs[1] }}
```

### Syntax Validation

The template string is validated for correct Jinja2 syntax when you save the node. An invalid template prevents saving and displays the line and column of the error.

## Send an Email Node

### Fields

| Field         | Required | Accepts Jinja2 | Notes                                                                                   |
|---------------|----------|----------------|-----------------------------------------------------------------------------------------|
| `recipient`   | Yes      | Yes            | Comma-separated email addresses or a Jinja2 expression that resolves to them            |
| `subject`     | Yes      | Yes            | Newlines are stripped from the rendered subject                                         |
| `body`        | No       | Yes            | When left blank, the node input is used as the body                                     |

The node output is always the unmodified node input, regardless of the email content. This means you can insert the node anywhere in a pipeline without breaking the data flow.

### Recipient Field Syntax

The recipient field must resolve to a comma-separated list of valid email addresses after rendering.

| Use case                                | Template                                           |
|-----------------------------------------|----------------------------------------------------|
| Single static address                   | `ops@example.com`                                  |
| Single address from participant data    | `{{ participant_data.email }}`                     |
| Multiple addresses from a list          | `{{ participant_data.emails \| join(',') }}`        |
| Addresses stored as a delimited string  | `{{ participant_data.emails \| split(';') \| join(',') }}` |
| Mix of static and dynamic              | `ops@example.com,{{ participant_data.manager_email }}` |

!!! warning "Validation at render time"

    If the recipient field contains a Jinja2 expression, email address validation runs after rendering, not when you save the node. An invalid address discovered at runtime will cause the pipeline step to fail. Test your recipient expressions before deploying.

### Body Field Behaviour

When the **body** field is blank, the node sends the pipeline input as the email body. This is the backwards-compatible default and is appropriate when an upstream node (such as an LLM node) has already produced the text you want to send.

When the **body** field contains a template, the node renders it and uses the result as the email body. The pipeline input is still passed through to the next node unchanged.

### Example — Dynamic Subject and Personalised Body

**Subject:**
```jinja
Update for {{ participant_details.identifier }}
```

**Body:**
```jinja
Hello {{ participant_data.name | default('there') }},

Here is your update: {{ input }}

To unsubscribe, reply STOP.
```

## Related Pages

- [Node Types](../concepts/pipelines/nodes.md) — plain-English overview of all pipeline nodes
- [Parallel Branches](../concepts/pipelines/parallel.md) — how `node_inputs` behaves when multiple branches converge
- [Participant Data](../concepts/participant_data.md) — what is stored in `participant_data` and how to manage it
