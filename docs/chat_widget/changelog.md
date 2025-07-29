# Changelog

## General upgrade guide

This guide will help you upgrade from previous versions of the Open Chat Studio Widget to the latest version. Please follow these steps carefully to ensure a smooth transition and also review any changes and upgrade steps between your current version and the latest version.

## :octicons-rocket-24: Quick Upgrade Steps

### 1. Update the script tags

**Update your script tags to use the latest version:**
```bash
<script 
  src="https://unpkg.com/open-chat-studio-widget{LATEST_VERSION_NUMBER}/dist/open-chat-studio-widget/open-chat-studio-widget.js"
  type="module"
  async
  ></script>
```

### 2. Review Your Implementation
Check your current HTML implementation and compare it with the [latest properties reference](reference.md#properties-reference).

## Changelog

### v0.4.0

!!! warning

    This is a full rebuild of the widget and includes breaking changes. See the [updgrade guide](#upgrading-from-03x) for details.

#### Updates

* Enhanced Mobile Experience
    * Improved responsive design for mobile devices
    * Better touch interactions and scrolling
* Draggable Chat Window
    * Desktop users can now drag the chat window to reposition it
* [Button Customization](reference.md#button-customization)
    * You can now set a button icon and change the button shape
* [Welcome Messages](reference.md#welcome-messages) & [Starter Questions](#starter-questions)
    * Display welcome messages when the chat opens
    * Provide clickable starter questions to help users get started
    * Both support rich markdown formatting
* Persistent sessions
    * Store session data in browser local storage to allow resuming sessions across page loads. 

#### Upgrading from 0.3.x

The minimal steps required to upgrade are to replace the `bot-url` attribute with the `chatbot-id` attribute:

``` { .diff .annotate }
  <open-chat-studio-widget
-     bot-url=".../experiments/e/{CHATBOT_ID}/embed/start/"
+     chatbot-id="{CHATBOT_ID}"
  </open-chat-studio-widget>
```

The `chatbot_id` can be extracted from the `bot-url` by copying the UUID from the URL as shown above.


## Upgrade Checklist
✅ Check These Items

**Property Names:** Ensure all property names use kebab-case (e.g., chatbot-id, not chatbotId)
**JSON Properties:** Verify that welcome-messages and starter-questions are properly formatted
**JSON strings:**
```bash
<!-- ✅ Correct -->
welcome-messages='["Message 1", "Message 2"]'

<!-- ❌ Incorrect -->
welcome-messages="Message 1, Message 2"
```

**API Base URL:** If you were using a custom API URL, ensure the api-base-url property is set correctly

**Boolean Properties:** Use string values for boolean properties:
```bash
<!-- ✅ Correct -->
visible="true"
expanded="false"

<!-- ❌ Incorrect -->
visible={true}
expanded={false}
```
