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

### v0.4.7

* Fix regression in font size consistency.

### v0.4.6

* Add support for sending messages with attachments.
  * Enabled by setting `allow-attachments="true"`
  * * See the [file attachments](styling.md#file-attachments) section in the style guide for available CSS properties.
* Update the 'Start a new session' icon.
* Add a confirmation dialog when starting a new chat.
  * Customize the text using the `new-chat-confirmation-message` attribute.
  * See the [confirmation dialog](styling.md#confirmation-dialog) section in the style guide for available CSS properties.
* Customize the typing indicator text using the `typing-indicator-text` attribute.
* Update message background and text colors.
  * See the [messages](styling.md#messages) section of the style guide.
* Update link CSS styling.
  * New properties `--message-user-link-color`, `--message-assistant-link-color`, `--message-system-link-color`.
* Removed unnecessary CSS properties for padding (`--*-padding*`).
* Added `--success-text-color` CSS property.
* Error handling improvements.
* Fix full screen mode layout.

### v0.4.5

* Internal API changes

### v0.4.4

* Merge width & height vars:
    * `--button-icon-width`, `--button-icon-height` -> `--button-icon-size` 
* Fix launch button styling.
    * Correctly apply font size and borders.
* Add variables to control header font and icon size:
    * `--header-font-size` 
    * `--header-button-icon-size` 
* Support for placing text in the window header using the `header-text`.
    * User `--header-text-font-size` and `--header-text-color` to style it independently of the other header elements. 

### v0.4.3

* Fix markdown styling
* Allow customizing the chat window width and height using the following CSS vars:
    * `--chat-window-width` 
    * `--chat-window-height` 
    * `--chat-window-fullscreen-width`
    * See the [styling guide](./styling.md#chat-window) for details.
* Change size units from `rem` to `em`.

### v0.4.2

* Fully configurable styling via CSS properties.

### v0.4.1

* Improved styling.
* Replaced 'expand' with 'fullscreen' mode.

#### Attribute changes

**Added**

* `allow-full-screen`: Allow the user to make the chat window full screen. 

**Removed**

* `expanded`

### v0.4.0

!!! warning

    This is a full rebuild of the widget and includes breaking changes. See the [upgrade guide](#upgrading-from-03x) for details.

* Enhanced Mobile Experience
    * Improved responsive design for mobile devices
    * Better touch interactions and scrolling
* Draggable Chat Window
    * Desktop users can now drag the chat window to reposition it
* [Button Customization](reference.md#button-customization)
    * You can now set a button icon and change the button shape
* [Welcome Messages](reference.md#welcome-messages) & [Starter Questions](reference.md#starter-questions)
    * Display welcome messages when the chat opens
    * Provide clickable starter questions to help users get started
    * Both support rich markdown formatting
* [Session persistence](reference.md#persistent-sessions) across page loads
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
