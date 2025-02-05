# Experiment Sessions

### What are sessions?
Think of a session as a conversation between two people. A session includes all messages exchanged during a conversation. A new message from the participant is interpreted in the context of the current conversation (or session). OCS achieves this by including all previous messages from a particular session in the system prompt as conversation history. This system prompt, along with the participant's message, is sent to the LLM to generate context-appropriate responses.

Participants can have multiple sessions, but depending on the platform they are using, only one can be active at any given time. This is not true for the web and API channels.

#### Web and API channels
For the web channel, a new session can be started simply by opening the chat link in a new tab. The participant can continue chatting with the bot in both tabs.

For API-based sessions, a new API call to the [create experiment session endpoint][create-experiment-session]{target="_blank"} can be made to create a new session. Each API call can initiate a separate session.

#### All other channels
Since these channels are inherently single-threaded, only a single session can be active at any given time. Once a session ends, any new message will start a new session, even though the participant can still see previous messages on their side.

### How sessions are ended
Sessions are ended either manually or automatically using timeout triggers.
<!-- Link timeout triggers to events / timeout_triggers page -->

#### Web channel
The participant can end the session by clicking the "End Experiment" button at the bottom of their chat.

#### All other channels
When the participant sends `/reset`, the current session will be ended and a new one will be started.


[channels]: ../channels.md
[create-experiment-session]: https://chatbots.dimagi.com/api/docs/#tag/Experiment-Sessions/operation/session_create