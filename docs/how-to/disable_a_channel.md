# Disable a channel

Instead of deleting a channel, you can pause it with the **Enabled** toggle in the channel's configuration dialog. This keeps the channel's settings in place so you can turn it back on later. See [Disabling a channel][disabling-concept] for what this does and why you might use it.

To disable a channel:

1. Navigate to the **Chatbot** the channel is linked to.
2. Open the channel from the list and switch off **Enabled**.
3. Optionally, enter a **Disabled message** — a static reply sent to any participant who messages the channel, or tries to start a chat on it, while it's off. The field appears once **Enabled** is switched off. Leave it blank to keep the channel silent instead.
4. Click **Save**.

Disabled channels are highlighted in the chatbot's channel list, so you can see at a glance which ones are off.

## What participants and admins see

What happens depends on where they try to reach the disabled channel:

| Entry point | What happens |
|---|---|
| Chat widget, and `POST /api/chat/start/` | Starting a chat is refused. The widget currently shows a generic "Failed to start chat session" error rather than your configured disabled message. |
| Public web chat link (consent/start page) | The page shows your disabled message instead of starting the conversation. |
| OCS console (starting a chat from the chatbot management pages) | A generic error is shown in place of the chat; your disabled message isn't used here. |
| Slack | If a disabled message is set, it's sent back; otherwise the channel stays silent with no visible error. |
| Messaging an already-disabled channel on any platform | The message isn't processed or recorded. If a disabled message is set, it's sent back as the reply; otherwise the bot stays silent. |

## Known limitations

Two API endpoints still open a session on a disabled channel:

- `POST /api/sessions/` succeeds as normal. Only messages sent afterwards on that session are blocked.
- The OpenAI-compatible chat completions endpoint also opens the session, then returns your disabled message as the assistant's reply — or an empty reply if you haven't set one. Callers see it in place of the model's answer.

`POST /api/chat/start/`, which the chat widget uses, *is* refused — see the table above.

Evaluation runs and pipeline test runs are unaffected by a channel's disabled state and continue to work as normal.

## Re-enabling a channel

Switch **Enabled** back on and click **Save**. The channel resumes straight away — new conversations can start again, and scheduled messages send as normal from their next trigger.

Nothing that happened while the channel was off is replayed:

- Messages participants sent were never recorded, so the chatbot won't answer them later.
- Scheduled and event messages that came due were **skipped, not queued**. Each one still counts as a trigger, so a schedule with a fixed number of repeats has fewer left, and one that reached its last repeat while disabled is marked complete without ever having sent.

## See also
- [Channels][disabling-concept] — what disabling does and why you might use it
- [Deploying your chatbot to different channels][deploy]

[disabling-concept]: ../concepts/channels.md#disabling-a-channel
[deploy]: ./deploy_to_different_channels.md
