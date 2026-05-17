# Send an Email from a Pipeline

The Send an Email node lets your chatbot trigger an email at any point in a pipeline — without stopping or altering the conversation. Use it to notify an administrator, send a summary to a participant, or alert your team when something important happens.

!!! note

    This node is a **passthrough**: its output is identical to its input. The email is sent, and the pipeline continues as normal.

## Prerequisites

- A pipeline with at least one node before the Send an Email node to provide input.
- If you plan to address emails dynamically (e.g. to the participant's own address), the participant's email must already be stored in [participant data](../concepts/participant_data.md).

## Add and configure the node

1. Open your pipeline in the pipeline editor.
2. Add a **Send an Email** node at the point in the flow where the email should be triggered.
3. Connect it to the upstream node that provides the content you want to send.
4. Fill in the **Subject**, **Recipient**, and optionally the **Body** fields (see below).
5. Connect the node's output to the next step in your pipeline.

## Field reference

### Subject

Accepts a plain string or a [Jinja2 template](../tech-hub/template_and_email_nodes.md). Use template variables to personalize the subject line.

**Examples:**

| Goal | Value |
|------|-------|
| Fixed subject | `Weekly check-in summary` |
| Include participant identifier | `Update for {{ participant_details.identifier }}` |
| Include a value from participant data | `Report for {{ participant_data.name }}` |

### Recipient

Accepts a comma-separated list of email addresses. See the [Recipient Field Syntax](../tech-hub/template_and_email_nodes.md#recipient-field-syntax) reference for advanced usage. 

### Body

Optional. Accepts a plain string or a [Jinja2](https://jinja.palletsprojects.com/en/stable/templates/) template.

When left blank, the node's input is used as the email body. This is useful when the previous node in the pipeline has already produced the text you want to send.

**Example — personalize body with dynamic content:**

**Subject:** `Update for {{ participant_details.identifier }}`

**Body:**
```
Hello {{ participant_data.name }},

Here is your update: {{ input }}
```

## Template variables

The variables available for the Subject, Recipient, and Body fields are [listed here.](../tech-hub/template_and_email_nodes.md#shared-template-variable-context)

## Example use cases

**Notify an administrator when a session ends**

Place the node just before an [End Session](../concepts/tools/index.md) tool call. Set the recipient to your team address and leave the body blank — the final LLM response becomes the email body automatically.

**Send a participant their session summary**

After an LLM node generates a summary, add the Send an Email node with the recipient set to `{{ participant_data.email }}` and the body set to `{{ input }}`.

**Alert your team when a threshold is reached**

After an [Increment counter](../concepts/tools/index.md) tool updates a counter in participant data, use a router to check the value. When the threshold is met, route to the Send an Email node to trigger an alert.
