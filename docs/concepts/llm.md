---
title: Large Language Model
---

# Large Language Models (LLMs)

!!! note "Definition"
    A Large Language Model (or LLM) is a type of artificial intelligence software that is trained on a vast amount of text data. Its
    primary function is to understand, interpret, and generate human language. This training allows it to produce text-based
    responses, answer questions, translate between languages, and perform various other language-related tasks. 
    
    The term "large" in its name refers to the extensive volume of data it has been trained on and the complexity of its design, enabling it to handle complex language tasks.

<small>The definition above was authored by the famous LLM that powers ChatGPT: GPT-4 developed by OpenAI.</small>

When building chatbots, an LLM powers the chatbot's ability to understand and respond to user inputs, effectively acting as the brain behind the chatbot.

## Which Large Language Models are supported by Open Chat Studio?

Open Chat Studio is developed to support a range of LLMs. The platform is designed to be flexible and can work with any
LLM that has an API. The platform currently supports all the models provided by the following APIs:

* [OpenAI](https://platform.openai.com/docs/models)
* [Azure OpenAi](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure%2Cglobal-standard%2Cstandard-chat-completions)
* [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models_)
* [Groq](https://console.groq.com/docs/models)
* [Perplexity](https://docs.perplexity.ai/guides/model-cards)
* [Deepseek](https://api-docs.deepseek.com/quick_start/pricing)

## Model Configuration Parameters

### Temperature
Temperature controls the creativity or randomness of the chatbot's responses.

- A low temperature (e.g., 0.1) makes the chatbot more deterministic, providing straightforward and predictable answers.
- A high temperature (e.g., 0.9) makes responses more creative, varied, or even surprising.

#### Example:
- Low temperature: *What's a dog?* → A dog is a domesticated animal.
- High temperature: *What's a dog?* → A dog is a loyal companion, a furry friend who fills your life with wagging tails and boundless joy.

The default temperature of 0.7 is a balanced choice designed to provide responses that are both varied and  interesting, while still being coherent.

---

### Prompt
A prompt is the input or instructions given to the LLM to guide its response. It sets the context for the chatbot. Prompts can be as simple as a user question or as detailed as a conversation framework or role-play setup.

#### Example:
You are a helpful assistant. Answer questions clearly and concisely.


### Tokens
Tokens are the building blocks of text that the LLM processes. A token might be a word, a part of a word, or even just punctuation.

#### Example:
The sentence *"Chatbots are cool."* is broken into 4 tokens:
`Chatbots | are | cool | .`

Tokens are important because they determine the cost and the processing complexity of an LLM's response.

---

### Max Token Limit
The max token limit is the maximum number of tokens the LLM can handle in a single interaction, including both the input (prompt) and output (response).

#### Example:
If the max token limit is 4096 tokens:
- A long prompt with 2000 tokens leaves 2096 tokens available for the response.

Understanding the token limit helps you create effective prompts without truncating responses.

---

## Model-Specific Features

Different LLM providers offer unique capabilities and features. This section documents provider-specific features that are available in Open Chat Studio.

### Claude Opus 4.6 (Anthropic)

Claude Opus 4.6 is Anthropic's most advanced model, featuring adaptive thinking capabilities and exceptional performance on complex reasoning tasks. This model is particularly well-suited for:

- **Agentic coding**: Building sophisticated AI agents that can write, debug, and refactor code
- **Long-context retrieval**: Processing and extracting information from large documents
- **Complex reasoning**: Tackling multi-step problems that require deep analysis

#### Key Specifications

| Specification | Value |
|--------------|-------|
| Model ID | `claude-opus-4-6` |
| Context Window | 200,000 tokens |
| Max Output Tokens | 128,000 tokens |
| Release Date | February 5, 2026 |

#### Adaptive Thinking

Claude Opus 4.6 introduces **adaptive thinking**, a feature that allows the model to engage in extended reasoning before generating responses. This is particularly valuable for complex tasks that benefit from careful analysis and planning.

The adaptive thinking feature is controlled by the **effort parameter**, which determines how much computational resources the model dedicates to reasoning about your request before responding.

##### Effort Levels

You can configure the effort level when using Claude Opus 4.6 in your chatbot or pipeline:

| Effort Level | Description | Best For |
|-------------|-------------|----------|
| **Low** | Minimal extended thinking | Simple queries, quick responses, straightforward tasks |
| **Medium** | Moderate extended thinking | Tasks requiring some analysis, balanced performance |
| **High** (default) | Substantial extended thinking | Complex reasoning, multi-step problems, detailed analysis |
| **Max** | Maximum extended thinking | Highly complex tasks, critical decision-making, thorough analysis |

!!! tip "Choosing the Right Effort Level"
    Start with the **high** effort level (default) for most use cases. Increase to **max** for particularly challenging problems, or reduce to **medium** or **low** for simpler tasks where speed is more important than depth of reasoning.

##### How to Configure Effort Level

When configuring a chatbot or LLM node with Claude Opus 4.6:

1. Select "claude-opus-4-6" as your model
2. Look for the **Effort** parameter in the model configuration
3. Choose from: `low`, `medium`, `high`, or `max`
4. The default setting is `high` if not specified

!!! note "Effort Parameter Compatibility"
    The effort parameter is only available for Claude Opus 4.6. Other Claude models (such as Claude 3.5 Sonnet or Claude 3 Haiku) do not support this feature and will use their standard reasoning capabilities.

##### Use Cases for Different Effort Levels

**Low Effort**
```
- Simple fact retrieval
- Basic translations
- Straightforward summarization
- Quick responses to common questions
```

**Medium Effort**
```
- Content creation and editing
- Basic code review
- Moderate complexity analysis
- Multi-turn conversations
```

**High Effort (Default)**
```
- Complex problem solving
- Detailed code generation and debugging
- In-depth document analysis
- Strategic planning and decision support
```

**Max Effort**
```
- Research and analysis requiring extreme thoroughness
- Critical code review for production systems
- Complex mathematical or logical proofs
- High-stakes decision-making scenarios
```

#### Performance Benchmarks

Claude Opus 4.6 achieves state-of-the-art performance on several industry benchmarks:

- **Terminal-Bench 2.0**: Advanced agentic coding evaluation
- **Humanity's Last Exam**: Complex reasoning and knowledge assessment
- **GDPval-AA**: Economic and analytical reasoning
- **BrowseComp**: Web browsing and information retrieval tasks

For the latest benchmark results and detailed performance comparisons, visit [Anthropic's model documentation](https://docs.anthropic.com/en/docs/about-claude/models).

---
