# Upgrade Guide

## Overview

This guide will help you upgrade from previous versions of the Open Chat Studio Widget to the latest version ({LATEST_VERSION_NUMBER}). Please follow these steps carefully to ensure a smooth transition.

## 🚀 Quick Upgrade Steps

### 1. Update the script tags

**Update your script tags to use the latest version:**
```bash
<script type="module" src="https://unpkg.com/open-chat-studio-widget@latest/dist/open-chat-studio-widget/open-chat-studio-widget.esm.js"></script>
<script nomodule src="https://unpkg.com/open-chat-studio-widget{LATEST_VERSION_NUMBER}/dist/open-chat-studio-widget/open-chat-studio-widget.js"></script>
```

### 2. Review Your Implementation
Check your current HTML implementation and compare it with the updated properties below.

## 📋 Properties Reference

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `chatbot-id` | `string` | ✅ | - | Your chatbot ID |
| `api-base-url` | `string` | ❌ | `"https://chatbots.dimagi.com"` | API base URL |
| `button-text` | `string` | ❌ | `"Chat"` | Button display text |
| `visible` | `boolean` | ❌ | `false` | Show widget on load |
| `expanded` | `boolean` | ❌ | `false` | Initial expanded state |
| `position` | `string` | ❌ | `"right"` | Widget position (`"left"` \| `"center"` \| `"right"`) |
| `icon-url` | `string` | ❌ | `undefined` | URL to button icon overriding defult OCS logo |
| `button-shape` | `string` | ❌ | `undefined` | Button Shape (`"round"` \| `"square"`) |
| `welcome-messages` | `string` | ❌ | `undefined` | JSON array of welcome messages |
| `starter-questions` | `string` | ❌ | `undefined` | JSON array of clickable starter questions |

**Example Implementation**
```bash
<open-chat-studio-widget
  chatbot-id="your-chatbot-id-here"
  api-base-url="https://your-api-url.com"
  button-text="Let's Chat"
  visible="false"
  expanded="false"
  position="right"
  welcome-messages='["Welcome to our chat!", "How can we help you today?"]'
  starter-questions='["I need help with my account", "Tell me about your services"]'
></open-chat-studio-widget>
```


### Migration Checklist
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

**Position Values:** Ensure position values are one of: "left", "center", or "right"

**Boolean Properties:** Use string values for boolean properties:
```bash
<!-- ✅ Correct -->
visible="true"
expanded="false"

<!-- ❌ Incorrect -->
visible={true}
expanded={false}
```


### New Features
#### Enhanced Mobile Experience

Improved responsive design for mobile devices
Better touch interactions and scrolling

#### Draggable Chat Window

Desktop users can now drag the chat window to reposition it
Automatic position constraints to keep the widget within the viewport

#### Welcome Messages & Starter Questions

Display welcome messages when the chat opens
Provide clickable starter questions to help users get started
Both support rich markdown formatting

#### Improved Message Handling

Better typing indicators
Enhanced message polling
Improved error handling and recovery

#### Markdown Support

Full markdown support in messages
Syntax highlighting for code blocks
Safe HTML sanitization for security

### Troubleshooting

####Common Issues

Widget Not Displaying:

- Verify the chatbot-id is valid
- Check that the API base URL is accessible
- Ensure the widget scripts are loaded properly

Styling Issues:

- Clear browser cache after updating
- Check for CSS conflicts with existing styles
- Verify CSS custom properties are properly applied

JSON Parsing Errors:

- Ensure JSON strings are properly escaped
- Use double quotes inside JSON arrays
- Validate JSON syntax using online tools

API Connection Issues:

- Verify the API base URL is correct and accessible
- Monitor browser console for network errors
