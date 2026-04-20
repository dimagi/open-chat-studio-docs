# LLM Router Configuration

The LLM Router uses an AI model to classify incoming messages into one of the defined output categories.

## Outputs and Default Route

The `outputs` listed on the node are the available classification labels. These should match the categories described in your prompt. They can be adjusted through the **Advanced** settings for the node.

The top output — marked with a blue `*` — is the **default** label. If the model generates a response that does not match any of the defined outputs, the message is routed along the default path.

## Prompt Design

Your prompt should clearly describe each category and give the model enough context to classify reliably. Ambiguous or overlapping categories will reduce accuracy.


!!! info "Keyword matching is case-insensitive"

    Route names are not case-sensitive. "HELP", "Help", and "help" all refer to the same route.



## History Mode

It is strongly advisable to use [Node history mode](../../concepts/pipelines/history.md#node) for an LLM Router. Without this, the model may receive previous conversation turns as few-shot examples, which can include earlier classification outputs and cause the model to reproduce them incorrectly in a new context.
