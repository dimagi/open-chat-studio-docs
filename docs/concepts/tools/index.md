# Tools

Tools allow LLMs to affect change in the real world. An LLM on its own can only produce intentions, but it is not able to execute those intentions. *Tools* are a way of telling the LLM what requests it can make and of executing that request when it is made.

Open Chat Studio provides a number of built-in tools as well as the ability to add your own tools in the form of [Custom Actions](../custom_actions.md).

The current set of built-in tools are listed below. If you need to refer to the tool in a prompt, use the tool's name directly e.g. `increment-participant-data`.

Recurring reminders
: Allows the bot to schedule recurring reminders for the participant.
: Name: `recurring-reminder`

One-off Reminder
: Allows the bot to schedule once-off reminders for the participant.
: Name: `one-off-reminder`

Delete Reminder
: Allows the bot to delete existing reminders (either once-off or recurring)
: Name: `delete-reminder`

Move Reminder Date
: Allows the bot to update the reminder date
: Name: `move-scheduled-message-date`

Update Participant Data
: Allows the bot to make changes to the [participant data](../participant_data.md)
: Name: `update-user-data`

Append to Participant Data
: Allows the bot to append a value to a specified key in the [participant data](../participant_data.md)
: Name: `append-to-participant-data`

Increment Participant Data
: Allows the bot to increment the value at a specified key in the [participant data](../participant_data.md)
: Name: `increment-participant-data`

End Session
: Allows the bot to end the current [session](../sessions.md)
: Name: `end-session`

## System tools

Attach Media
: Allows the bot to attach media when a media collection is configured.
: Name: `attach-media`

File Search
: Allows the bot to search indexed collections when a collection is configured.
: Name: `file-search`
