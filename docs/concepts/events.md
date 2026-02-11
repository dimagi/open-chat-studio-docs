# Events

Open Chat Studio provides an event system that allows you to define actions triggered by specific events within a chat session. This functionality enables you to automate responses, manage session states, and enhance user interactions effectively.

## Overview

Events in Open Chat Studio are categorized into two types:

1. **Static Events**: Triggered by specific actions or occurrences within the chat session.
2. **Timeout Events**: Triggered after a specified duration of inactivity following the last interaction.

Each event has one action associated with it that is executed when the event occurs.

## Static Events

Static events are predefined triggers that occur based on specific actions or conditions within the chat session. The available static events are:

- **Conversation End**: A catch-all trigger that fires whenever any conversation ends, regardless of how it ended. This trigger is always fired alongside any of the specific conversation end sub-triggers listed below. Use this trigger when you want to perform an action for all conversation endings, or use the sub-triggers when you need to respond to specific end conditions.
    - **The Conversation is Ended by the Participant**: Triggered when the participant explicitly ends the conversation.
    - **The Conversation is Ended by the Bot**: Triggered when the bot ends the conversation.
    - **The Conversation is Ended via the API**: Triggered when the conversation ends via an API call.
    - **The Conversation is Ended by an Event**: Triggered when the conversation ends due to an event.
    - **The Conversation is manually ended by an Admin**: Triggered when an admin manually ends the conversation.

    !!! note "How Sub-triggers Work"
        When a specific end condition occurs (e.g., participant ends conversation), both the specific sub-trigger AND the generic "Conversation End" trigger will fire. This allows you to create both targeted events (using sub-triggers) and catch-all events (using the generic trigger) that respond to any conversation ending.

- **Last Timeout**: Triggered when the last timeout of any configured timeout events occur.
- **Human Safety Layer Triggered**: Triggered when the safety layer is activated by a message from the user.
- **Bot Safety Layer Triggered**: Triggered when the safety layer is activated by a response from the bot.
- **Conversation Start**: Triggered when a new conversation is started.
- **New Human Message**: Triggered when a new human message is received.
- **New Bot Message**: Triggered when a new bot message is received.
- **Participant Joined Experiment**: Triggered when a participant starts interacting with the bot for the very first time.

## Event Actions

Each event is associated with one action. The available actions are:

- **End the conversation**: Ends the conversation with the user. See [Resetting Sessions](sessions.md#resetting-sessions).
- **Prompt the bot to message the user**: Prompts the bot to message the user.
- **Trigger a schedule**: This will create a once off or recurring schedule. Each time the schedule is triggered, the bot will be prompted to message the user.
- **Start a pipeline**: This will run the given pipeline when the event triggers. The input to the pipeline can be configured.

## System Notification Events

Open Chat Studio provides comprehensive system notification events that allow you to monitor and respond to operational failures across your chatbot infrastructure. These events are designed for system monitoring, alerting, and debugging purposes, helping you maintain reliable chatbot operations.

!!! note "Purpose of Notification Events"
    Unlike the static events and timeout events described above (which respond to user interactions), notification events are triggered by system-level failures and operational issues. Use these events to integrate with monitoring systems, send alerts to administrators, or trigger automated recovery procedures.

### Custom Action Notifications

These events monitor the health and operation of your external service integrations:

- **Health Check Failures**: Triggered when a custom action's health check fails, indicating the external service may be unreachable or not responding correctly.
    - **When it triggers**: Occurs during automatic health monitoring (every 5 minutes) or manual health checks when the target service fails to respond or returns an error
    - **Information included**:
        - Custom action name and identifier
        - Detailed failure reason (connection timeout, HTTP error code, etc.)
        - Timestamp of the failed check
        - Base URL that was checked
    - **Use case**: Alert administrators when critical external services become unavailable, trigger failover procedures, or log service outages

- **API Failures**: Triggered when an HTTP API call to a custom action endpoint fails during bot operation.
    - **When it triggers**: Occurs when the bot attempts to call a custom action endpoint and receives an error response or connection failure
    - **Information included**:
        - HTTP method (GET, POST, etc.)
        - Operation/endpoint that failed
        - Error response details
        - Custom action identifier
    - **Use case**: Monitor API reliability, identify frequently failing endpoints, and debug integration issues

- **Unexpected Errors**: Triggered when unexpected exceptions or errors occur during custom action execution.
    - **When it triggers**: Catches runtime errors, exceptions, or unexpected conditions during custom action processing
    - **Information included**:
        - Error message and stack trace
        - Custom action context
        - Operation being performed when the error occurred
    - **Use case**: Identify code bugs, catch edge cases, and monitor for unexpected system behavior

### Chat and Pipeline Operation Notifications

These events monitor the core chatbot execution pipeline:

- **Pipeline Execution Failures**: Triggered when a chatbot's pipeline fails to execute for a user interaction.
    - **When it triggers**: Occurs when a pipeline encounters an error during execution, preventing the bot from generating a response
    - **Information included**:
        - Participant/user identifier
        - Session details
        - Pipeline configuration
        - Error details describing the failure
    - **Use case**: Alert when users experience conversation failures, track pipeline reliability metrics, and identify problematic pipeline configurations

- **LLM Errors**: Triggered when Large Language Model service calls fail.
    - **When it triggers**: Occurs when requests to LLM providers (OpenAI, Anthropic, etc.) fail due to API errors, timeouts, rate limits, or service outages
    - **Information included**:
        - LLM provider name
        - Error context and message
        - Request details (model, parameters)
        - User session information
    - **Use case**: Monitor LLM provider availability, track API quota consumption, and detect rate limiting issues

- **Tool Execution Errors**: Triggered when pipeline tools encounter execution failures.
    - **When it triggers**: Occurs when tools within a pipeline (search tools, data retrieval, etc.) fail to execute properly
    - **Information included**:
        - Tool name and type
        - Error message
        - Tool configuration
        - Pipeline context
    - **Use case**: Debug tool configurations, monitor tool reliability, and identify missing dependencies or permissions

### Media and File Handling Notifications

These events monitor audio and file processing operations:

- **Audio Synthesis Failures**: Triggered when text-to-speech or voice response generation fails.
    - **When it triggers**: Occurs when the system fails to generate audio responses for voice-enabled chatbots
    - **Information included**:
        - Text that failed to synthesize
        - Audio provider details
        - Error reason
        - Session context
    - **Use case**: Monitor voice bot reliability, detect audio service outages, and identify problematic text content

- **Audio Transcription Failures**: Triggered when speech-to-text processing of voice messages fails.
    - **When it triggers**: Occurs when the system cannot transcribe user voice messages to text
    - **Information included**:
        - Audio file details
        - Transcription service provider
        - Error message
        - User session information
    - **Use case**: Track transcription service availability, identify audio quality issues, and monitor voice input reliability

- **File Delivery Failures**: Triggered when file attachments fail to deliver to users.
    - **When it triggers**: Occurs when the system cannot send file attachments (images, documents, etc.) to users through messaging platforms
    - **Information included**:
        - File type and size
        - Delivery channel
        - Error details
        - Recipient information
    - **Use case**: Monitor file delivery reliability, identify file size or format issues, and track platform-specific limitations

### Message Delivery Notifications

These events monitor message delivery across all supported platforms:

- **Platform Delivery Failures**: Triggered when messages fail to send through messaging platforms.
    - **When it triggers**: Occurs when the system cannot deliver bot responses to users through platforms like WhatsApp, Telegram, Slack, Facebook Messenger, or other channels
    - **Information included**:
        - Platform/channel name
        - Message content (or reference)
        - Delivery error details
        - User identifier
        - Platform-specific error codes
    - **Use case**: Monitor multi-channel delivery reliability, identify platform outages, detect user blocking or opt-out scenarios, and track messaging API quota issues

### Configuring Notification Events

To set up system notifications:

1. Navigate to your chatbot's **Events** configuration
2. Create a new event and select the appropriate notification event type from the dropdown
3. Configure the event action to respond to the notification:
    - **Start a pipeline**: Process the error data and send alerts to external monitoring systems
    - **Trigger a schedule**: Set up follow-up actions or retry mechanisms
    - **Prompt the bot to message the user**: Send user-facing error messages when appropriate (use with caution)

!!! tip "Best Practices for Notification Events"
    - **Don't overwhelm users**: Notification events are primarily for system monitoring. Avoid sending technical error details directly to end users
    - **Integrate with monitoring tools**: Use pipelines to send notifications to Slack, PagerDuty, email, or logging systems
    - **Set up aggregation**: For high-volume events, consider aggregating multiple failures before alerting
    - **Monitor trends**: Track notification patterns over time to identify systemic issues
    - **Test your notifications**: Regularly verify that your notification pipelines are working correctly

!!! warning "Privacy and Sensitive Data"
    Notification events may include user identifiers and message context. Ensure your notification handling complies with privacy policies and data protection regulations. Avoid logging or transmitting sensitive personal information unnecessarily.
