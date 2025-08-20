# Tools

Tools allow LLMs to affect change in the real world. An LLM on its own can only produce intentions, but it is not able to execute those intentions. *Tools* are a way of telling the LLM what requests it can make and of executing that request when it is made.

Open Chat Studio provides a number of built-in tools as well as the ability to add your own tools in the form of [Custom Actions](../custom_actions.md).

The current set of built-in tools are listed below. If you need to refer to the tool in a prompt, use the tool's name directly e.g. `update-user-data`.

**Recurring reminders**

Allows the bot to schedule recurring reminders for the participant.

* Name: `recurring-reminder`
* Arguments:
  * `datetime_due`: The first (or only) reminder start date in ISO 8601 format.
  * `every`: Number of 'periods' to wait between reminders.
  * `period`: The time period used in conjunction with 'every'. One of `minutes`, `hours`, `days`, `weeks`, `months`
  * `message`: The reminder message.
  * `schedule_name`: The name for this reminder.
  * `datetime_end`: The date of the last reminder in ISO 8601 format (optional).
  * `repetitions`: The number of messages to send before stopping (optional).

**One-off Reminder**

Allows the bot to schedule once-off reminders for the participant.

* Name: `one-off-reminder`
* Arguments:
  * `datetime_due`: The datetime that the reminder is due in ISO 8601 format
  * `message`: The reminder message
  * `schedule_name`: The name for this reminder

**Delete Reminder**

Allows the bot to delete existing reminders (either once-off or recurring)

* Name: `delete-reminder`
* Arguments:
  * `message_id`: The ID of the scheduled message to delete.

**Move Reminder Date**

Allows the bot to update the reminder date

* Name: `move-scheduled-message-date`
* Arguments:
  * `message_id`: The ID of the scheduled message to update.
  * `weekday`: The new day of the week (1-7 where 1 = Monday).
  * `hour`: The new hour of the day, in UTC.
  * `minute`: The new minute of the hour.
  * `specified_date`: A specific date to re-schedule the message for in ISO 8601 format

**Update Participant Data**

Allows the bot to make changes to the [participant data](../participant_data.md)

* Name: `update-user-data`
* Arguments:
  * `key`: The key in the user data to update.
  * `value`: The new value of the user data.

**Append to Participant Data**

Append a value to [participant data](../participant_data.md) at a specific key. This will convert any existing value to a list and append the new value to the end of the list. Use this tool to track lists of items e.g. questions asked.

* Name: `append-to-participant-data`
* Arguments:
  * `key`: The key in the user data to append to.
  * `value`: The value to append.

**Increment Counter**

Increment the value of a counter. The counter is stored in [participant data](../participant_data.md) with the key `_counter_{counter_name}`.

* Name: `increment-counter`
* Arguments:
  * `counter`: The name of the counter to increment.
  * `value`: Integer value to increment the counter by (defaults to 1).

**End Session**

End the current chat [session](../sessions.md). This will mark the session as completed. New messages will result in a new session being created.

* Name: `end-session`
* Arguments: (none)

## System tools

**Attach Media**

Allows the bot to attach media when a media collection is configured. 

* Name: `attach-media`
* Arguments:
  * `file_id`: The ID of the media file to attach.

**File Search**

Allows the bot to search indexed collections when a collection is configured.

* Name: `file-search`
* Arguments:
  * `query`: A natural language query to search for relevant information in the documents.
