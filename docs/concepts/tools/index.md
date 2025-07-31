# Tools

Tools allow LLMs to affect change in the real world. An LLM on its own can only produce intentions, but it is not able to execute those intentions. *Tools* are a way of telling the LLM what requests it can make and of executing that request when it is made.

Open Chat Studio provides a number of built-in tools as well as the ability to add your own tools in the form of [Custom Actions](../custom_actions.md).

The current set of built-in tools are:

Recurring Reminder
: Allows the bot to schedule recurring reminders for the participant.

One-off Reminder
: Allows the bot to schedule once-off reminders for the participant.

Delete Reminder
: Allows the bot to delete existing reminders (either once-off or recurring)

Move Reminder Date
: Allows the bot to update the reminder date

Update Participant Data
: Allows the bot to make changes to the [participant data](../participant_data.md)

Append to Participant Data
: Allows the bot to append a value to a specified key in the [participant data](../participant_data.md)

Increment Participant Data
: Allows the bot to increment the value at a specified key in the [participant data](../participant_data.md)

End Session
: Allows the bot to end the current [session](../sessions.md)
