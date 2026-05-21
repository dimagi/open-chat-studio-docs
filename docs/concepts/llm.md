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

Different models expose different knobs for shaping their behaviour. The most common
are **temperature**, **effort**, and **reasoning / adaptive thinking**. Not every model
supports every parameter — when you select a model in Open Chat Studio, the configuration
panel only shows the parameters that model actually supports, so you won't accidentally
set one that has no effect.

### Temperature
Temperature controls the creativity or randomness of the chatbot's responses.

- A low temperature (e.g., 0.1) makes the chatbot more deterministic, providing straightforward and predictable answers.
- A high temperature (e.g., 0.9) makes responses more creative, varied, or even surprising.

#### Example:
- Low temperature: *What's a dog?* → A dog is a domesticated animal.
- High temperature: *What's a dog?* → A dog is a loyal companion, a furry friend who fills your life with wagging tails and boundless joy.

The default temperature of 0.7 is a balanced choice designed to provide responses that are both varied and  interesting, while still being coherent.

Temperature is supported by most "general-purpose" chat models (e.g. GPT-4o, Claude Sonnet/Opus
without thinking enabled, Gemini, Groq, Perplexity, Deepseek). It is **not** available on
reasoning-first models that use effort instead — see below.

---

### Effort
Effort (sometimes called **reasoning effort**) controls how much internal "thinking" the
model does before answering. It's used by **reasoning models** — models that are designed
to work through problems step-by-step before producing a final response.

Effort is set as a level rather than a number:

| Level    | What it does                                                                                          |
|----------|-------------------------------------------------------------------------------------------------------|
| `low`    | Fastest and cheapest. Short reasoning before answering — good for routine questions.                  |
| `medium` | A balanced default for most tasks.                                                                    |
| `high`   | More thorough reasoning — useful for complex analysis, multi-step problems, or careful code review.   |
| `max`    | Maximum reasoning budget. Slowest and most expensive, but produces the most considered answers.       |

Higher effort levels generally produce better answers on hard problems but cost more
(both in tokens and latency). For simple conversational tasks, low or medium is almost
always enough — turning the knob up doesn't make a friendly chitchat bot friendlier, just
slower.

#### When effort is set, temperature is ignored
On models that use effort, OpenAI and Anthropic do not allow temperature or `top_p` to be
configured at the same time — the reasoning loop manages randomness internally. Open Chat
Studio reflects this by hiding the temperature field on these models so you don't have to
think about it.

Models that use effort include OpenAI's GPT-5 / GPT-5.2 series and Anthropic's Claude Opus
4.6 and Sonnet 4.6 with thinking enabled.

---

### Reasoning and adaptive thinking
"Reasoning" is the broader name for the same idea as effort: letting the model spend extra
tokens *thinking* before it produces the answer the user sees. Different providers expose
this slightly differently:

- **OpenAI** calls it `reasoning_effort` and uses the level system above.
- **Anthropic** offers **adaptive thinking** on its Claude 4.6 models. Adaptive thinking
  lets the model decide how much to think on a per-message basis, guided by the effort
  level you set. Easy turns finish quickly; hard turns get more thinking budget.
- **Google Gemini** exposes a thinking budget on some Gemini 2.5+ models.

You normally don't need to think about these provider-level differences — Open Chat Studio
abstracts them into the same effort levels (low/medium/high/max) wherever the model supports
them.

---

### Choosing between temperature and effort

These two knobs do very different things, so it's worth being clear about when each one
helps:

| If you want to…                                                  | Reach for…  |
|------------------------------------------------------------------|-------------|
| Make answers more or less creative / varied / unpredictable      | Temperature |
| Make answers more or less rigorous / careful / well-reasoned     | Effort      |
| Get more diverse phrasing for a friendly conversational bot      | Temperature |
| Solve a harder problem (analysis, coding, multi-step reasoning)  | Effort      |
| Reduce hallucinations on a factual Q&A bot                       | Lower temperature, or switch to a reasoning model and raise effort |
| Make a strict classifier / extractor more deterministic          | Temperature → 0 (or use a reasoning model with low effort) |
| Speed things up / cut costs on an over-engineered setup          | Lower effort (if set), or stick with a non-reasoning model |

A simple rule of thumb:

- **Temperature** is for *style*.
- **Effort** is for *substance*.

If you find yourself wanting both — for example, a creative writing assistant that also
needs to follow complex constraints — pick a reasoning model with medium-to-high effort.
You won't be able to set temperature on it, but the model's own randomness is usually
enough for natural-sounding text.

#### Quick decision guide

1. Is this a conversational, creative, or stylistic task? → Use a general-purpose model and
   tune **temperature**.
2. Is this a logic, analysis, math, or coding task? → Use a reasoning model and tune **effort**.
3. Not sure? → Start with the default model and default settings. Adjust only if the output
   is consistently too random, too bland, too shallow, or too slow.

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

For reasoning models, note that the model's *internal* thinking tokens count toward your
max output token budget. If you set effort to `high` or `max` on a complex task and set the
max output low, the model may run out of room before it produces a visible answer. If you
see truncated or empty responses from a high-effort run, raise the max output token limit.

---

## Model Lifecycle and Deprecation

AI providers regularly update their model offerings, which means models available on Open Chat Studio may occasionally be deprecated or removed over time.

- **Deprecation**: If a model you are using is deprecated, you will receive an in-app notification recommending that you switch to a replacement model. Your chatbots and pipelines continue to work during this period, but you should update your configuration at your earliest convenience.
- **Removal**: If a model is fully removed from the platform, Open Chat Studio automatically removes all references in your chatbots and pipelines. Where there is a clear replacement model, Open Chat Studio will migrate usages of the old model to the recommended replacement model. You will receive an in-app notification confirming that the removal or migration has taken place.

No manual action is required when a model is removed — the platform handles the transition for you.
