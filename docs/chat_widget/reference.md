# Reference Docs

Learn how to customize the Open Chat Studio widget to match your brand and improve user experience.

## Button Customization

The widget button can be customized using the following properties:

```html
<open-chat-studio-widget
  button-text="Chat with us"
  button-shape="round"
  icon-url="https://your-domain.com/custom-chat-icon.svg">
</open-chat-studio-widget>
```

**Button Text**

- When button-text is provided, the button displays both icon and text
- When button-text is empty or not provided, only an icon is shown

**Button Shape**

- **round** - Circular button
- **square** - Rectangular button with rounded corners

**Icon URL**

If no icon-url is provided, the default Open Chat Studio logo is used.

### Button position

Customize the button position using CSS variables or a CSS class attached to the widget element:

```css
open-chat-studio-widget {
    position: fixed;
    right: 20px;
    bottom: 20px;
}
```

<div class="grid cards" markdown>
-   :simple-css:{ .sm .middle } See [CSS Styling](styling.md) for more customization options.
</div>

## :material-shield-key: Embed Authentication
Secure your embedded widgets with authentication keys for controlled access to specific channels.

### Overview
The embed authentication feature allows you to:

- Restrict widget access to authorized embeddings only
- Authenticate specific embedded channel instances
- Provide secure access control for sensitive or premium content
- Track and manage different embedded deployments

### Implementation
```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id"
  embed-key="your-secure-embed-key">
</open-chat-studio-widget>
```

When an embed key is provided, it's automatically sent as an `X-Embed-Key` header with all API requests to authenticate the widget instance.

## :material-account: User Identification
Control how users are identified across chat sessions to enable personalized experiences and session continuity.
### Overview
The chat widget uses user identification to:

- Maintain chat history across page reloads and different visits
- Separate conversations for different users on shared devices
- Personalize interactions with user names and context
- Enable analytics and user tracking in your chat system

### Basic Implementation
Anonymous Users (Default)
```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id">
</open-chat-studio-widget>
```
Identified Users
```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id"
  user-id="user_12345"
  user-name="Sarah Johnson">
</open-chat-studio-widget>
```
### Auto-Generated User IDs

When no user-id is provided, the widget automatically creates a unique identifier:

- Example: ocs:1703123456789_a7x9k2m8f

Persistence Behavior:

- Same browser/device: ID persists across sessions
- Different browser/device: Gets new auto-generated ID
- Incognito mode: New ID that's cleared when session ends


### Dynamic User Management
Update user identification when authentication state changes:
```javascript
function updateChatUser(user) {
  const widget = document.querySelector('open-chat-studio-widget');

  if (user) {
    widget.userId = user.id;
    widget.userName = user.name;
  }
}
```

## :material-hand-wave: Welcome Messages

Enhance user experience by displaying personalized greeting messages when the chat opens. These messages appear as bot messages at the beginning of the conversation. Welcome messages are perfect for:

- Greeting users and introducing your bot's capabilities
- Providing context about what kind of help is available
- Creating a warm, engaging first impression

Pass welcome messages as a JSON array string. Each message appears as a separate message bubble.

```html
<open-chat-studio-widget
 welcome-messages="['Hi! Welcome to our support chat.', 'How can I assist you today?']"
>
</open-chat-studio-widget>
```

## :material-folder-question: Starter Questions

Accelerate user engagement with pre-defined clickable questions that address common queries. These starter questions help users quickly find what they're looking for without having to type, which improves the user experience. Starter questions are ideal for:

- Highlighting your most frequently asked questions
- Guiding users toward key features or information
- Improving accessibility for users who prefer clicking to typing

These questions appear as blue-outlined buttons aligned to the right (similar to user messages), making it clear that they are user actions. When clicked, they automatically send that question as a user message, initiating the conversation flow. The starter questions disappear after the user clicks one or starts typing their own message.

```html
<open-chat-studio-widget
 starter-questions="[
   'I need technical support',
   'Tell me about pricing',
   'Schedule a demo',
   'Contact sales team'
 ]">
</open-chat-studio-widget>
```

## :material-paperclip: File Attachments
Enable users to send files along with their messages. This feature is perfect for support scenarios where users need to share screenshots, documents, or other files.

```html
<open-chat-studio-widget
 allow-attachments="true">
</open-chat-studio-widget>
```
### Supported File Types

#### Documents:
- Text files: .txt
- PDF documents: .pdf
- Microsoft Word: .doc, .docx
- Microsoft Excel: .xls, .xlsx
- Spreadsheets: .csv

#### Images:
- Common formats: .jpg, .jpeg, .png, .gif, .bmp, .webp
- Vector graphics: .svg

#### Media:
- Video files: .mp4, .mov, .avi
- Audio files: .mp3, .wav

### File Size Limits

- Maximum file size: 50MB per individual file
- Maximum total size: 50MB for all files combined in a single message
- Multiple files: Users can attach multiple files as long as the total doesn't exceed 50MB

### User Experience

1. Users click the paperclip icon next to the send button to select files
2. Selected files appear in a preview area above the input field
3. Files show name, size, and upload status
4. Users can remove files before sending by clicking the X button
5. Error messages appear for unsupported file types or files exceeding size limits
6. Files are uploaded when the message is sent


See [CSS Styling](styling.md#file-attachments) for customization options

## :material-translate: Internationalization

The chat widget supports multiple languages and custom translations for all UI text elements.

### Built-in Language Support

The widget includes built-in translations for the following languages:

- **English** (`en`) - Default
- **Spanish** (`es`)
- **French** (`fr`)
- **Arabic** (`ar`)
- **Hindi** (`hi`)
- **Italian** (`ita`)
- **Portuguese** (`por`)
- **Swahili** (`sw`)
- **Ukrainian** (`uk`)

```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id"
  language="es">
</open-chat-studio-widget>
```

### Custom Translations

You can provide custom translations using a JSON file hosted on your server:

```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id"
  translations-url="https://yoursite.com/custom-translations.json">
</open-chat-studio-widget>
```

#### Translation File Format

Provide translations as a flat JSON object that uses dot-notation keys. These keys loosely group strings by the part of the widget they affect:

```json
{
  "launcher.open": "Open chat",
  "window.close": "Close",
  "window.newChat": "Start new chat",
  "window.fullscreen": "Enter fullscreen",
  "window.exitFullscreen": "Exit fullscreen",
  "attach.add": "Attach files",
  "attach.remove": "Remove file",
  "attach.success": "File attached",
  "status.starting": "Starting chat...",
  "status.typing": "Preparing response",
  "status.uploading": "Uploading",
  "modal.newChatTitle": "Start New Chat",
  "modal.newChatBody": "Starting a new chat will clear your current conversation. Continue?",
  "modal.cancel": "Cancel",
  "modal.confirm": "Confirm",
  "composer.placeholder": "Type a message...",
  "composer.send": "Send message",
  "error.fileTooLarge": "File too large",
  "error.totalTooLarge": "Total file size too large",
  "error.unsupportedType": "Unsupported file type",
  "error.connection": "Connection error. Please try again.",
  "error.sessionExpired": "Session expired. Please start a new chat.",
  "branding.poweredBy": "Powered by",
  "branding.buttonText": "",
  "branding.headerText": "",
  "content.welcomeMessages": [],
  "content.starterQuestions": []
}
```

#### Translation Key Reference

Use the following reference when creating or updating translation bundles (mirrors the widget's `en.json`):

- **launcher**
  - `launcher.open` — Launcher button label, aria-label, and tooltip.
- **window**
  - `window.close` — Closes the chat window.
  - `window.newChat` — Menu item to start a new chat.
  - `window.fullscreen` — Enters fullscreen mode.
  - `window.exitFullscreen` — Leaves fullscreen mode.
- **attach**
  - `attach.add` — Adds file attachments.
  - `attach.remove` — Removes a pending attachment.
  - `attach.success` — Upload queued confirmation.
- **status**
  - `status.starting` — Shown while the session initializes.
  - `status.typing` — Typing indicator text (previously `typingIndicatorText`).
  - `status.uploading` — Attachment upload in progress.
- **modal**
  - `modal.newChatTitle` — "Start new chat" dialog title.
  - `modal.newChatBody` — Dialog body text.
  - `modal.cancel` — Dialog cancel button.
  - `modal.confirm` — Dialog confirmation button.
- **composer**
  - `composer.placeholder` — Message composer placeholder text.
  - `composer.send` — Send button text.
- **error**
  - `error.fileTooLarge` — Single file size violation.
  - `error.totalTooLarge` — Combined size violation.
  - `error.unsupportedType` — Unsupported file format.
  - `error.connection` — Generic connection failure.
  - `error.sessionExpired` — Session expiration prompt.
- **branding**
  - `branding.poweredBy` — Footer "Powered by" label.
  - `branding.buttonText` — Optional launcher text override; leave blank to use widget props.
  - `branding.headerText` — Optional header title override; leave blank to use widget props.
- **content**
  - `content.welcomeMessages` — Array of initial bot messages (empty array falls back to props).
  - `content.starterQuestions` — Array of starter questions (empty array falls back to props).

#### Customizable Content

You can override specific widget content through translations.

If you only want to override some text, include just those keys in your custom translation file. The widget will use the values from the default language file for provided languages or fall back to English. Arrays must remain arrays, and null values in `branding.buttonText` defer to the runtime HTML attribute or prop.

### Translation Priority

The widget uses the following priority order for text content:

1. **Custom translations from `translations-url`** (highest priority)
2. **Built-in language translations** (if `language` is specified)
3. **Widget props / HTML attributes** (used when translation keys are null or missing - ⚠️ **DEPRECATED** for long-term use)
4. **English defaults** (lowest priority)

!!! warning "Deprecation Notice"
    HTML attributes for text content (`header-text`, `typing-indicator-text`, `new-chat-confirmation-message`) are deprecated and will be removed in a future major release. Please migrate to using the translations system for better internationalization support. Leave translation values blank when you want the widget props to supply the text instead of duplicating it.

## Persistent Sessions

By default, the widget will save the chat messages in the browser local storage. This allows users to continue sessions after reloading the page or navigating to a new page. In addition to automatic session expiration, the user can also use the 'new chat' button to start a new session.

To disable this feature, set the `persistent-session="false"` attribute on the widget element.

!!! note

    The session persistence is associated with the `chatbot-id`. If the `chatbot-id` changes, any previous session data will be ignored.

The session data is set to expire after 24 hours. This is also configurable by using the `persistent-session-expire` attribute. The value is interpreted as *"the number of minutes since the last message before the session expires"*. Setting this attribute to `0` will disable the expiration entirely.

!!! note

    Session persistence works in conjunction with [User Identification](#user-identification). Different users will have separate persistent sessions.

## :material-clipboard-list: Properties Reference

### Core Configuration

| Property | Type | Required | Default | Description | Example |
|----------|------|----------|---------|-------------|---------|
| `chatbot-id` | `string` | **REQUIRED** | - | Your chatbot ID from Open Chat Studio | `"183312ac-cbe5-4c91-9e7b-d9df96b088e4"` |
| `api-base-url` | `string` | Optional | `"https://chatbots.dimagi.com"` | API base URL for your Open Chat Studio instance | `"https://your-domain.com"` |
| `embed-key` | `string` | Optional | `undefined` | Authentication key for embedded channels | `"your-embed-auth-key"` |

### Button & UI Customization

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `button-text` | `string` | Optional | `undefined` | Max 50 chars | Button display text. If empty, shows icon only | `"Need Help?"` |
| `button-shape` | `string` | Optional | `"square"` | `"round"` \| `"square"` | Button shape style | `"round"` for circular button |
| `icon-url` | `string` | Optional | OCS default logo | Valid URL | Custom icon for the chat button | `"https://yoursite.com/chat-icon.svg"` |
| `visible` | `boolean` | Optional | `false` | `true` \| `false` | Show widget immediately on page load | `"true"` to auto-open |
| `position` | `string` | Optional | `"right"` | `"left"` \| `"center"` \| `"right"` | Initial widget position on screen | `"left"` for left side placement |
| `header-text` | `string` | Optional | `undefined` | Max 100 chars | **⚠️ DEPRECATED:** Text displayed in chat window header. Use `branding.headerText` in translations instead | `"Customer Support"` |

### User Management

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `user-id` | `string` | Optional | Auto-generated | Alphanumeric + underscore/dash | Unique user identifier for session continuity<br/>**Auto-format:** `ocs:1703123456789_a7x9k2m8f` | `"user_12345"` or `"customer@email.com"` |
| `user-name` | `string` | Optional | `undefined` | Max 200 chars | Display name sent to chat API for personalization | `"John Smith"` or `"Customer #12345"` |

### Chat Behavior & Sessions

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `persistent-session` | `boolean` | Optional | `true` | `true` \| `false` | Save chat history in browser localStorage | `"false"` to disable session saving |
| `persistent-session-expire` | `number` | Optional | `1440` (24 hours) | 0-43200 (30 days) | Minutes before session expires | `720` for 12 hours, `0` for never expire |
| `allow-full-screen` | `boolean` | Optional | `true` | `true` \| `false` | Enable fullscreen mode button | `"false"` to hide fullscreen option |
| `allow-attachments` | `boolean` | Optional | `false` | `true` \| `false` | Enable file upload functionality<br/>**Limits:** 50MB per file, 50MB total per message | `"true"` to enable file uploads |

### Messages & Content

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `welcome-messages` | `string` | Optional | `undefined` | Valid JSON array<br/>**Max:** 5 messages, 500 chars each | Welcome messages shown when chat opens<br/>**Format:** `'["Message 1", "Message 2"]'` | `'["Welcome!", "How can I help?"]'` |
| `starter-questions` | `string` | Optional | `undefined` | Valid JSON array<br/>**Max:** 6 questions, 100 chars each | Clickable question buttons to start conversation<br/>**Format:** `'["Question 1", "Question 2"]'` | `'["Check my order", "Technical support"]'` |
| `typing-indicator-text` | `string` | Optional | `"Preparing response"` | Max 50 chars | **⚠️ DEPRECATED:** Text shown while bot is typing. Use `status.typing` in translations instead | `"AI is thinking..."` |
| `new-chat-confirmation-message` | `string` | Optional | `"Starting a new chat will clear your current conversation. Continue?"` | Max 200 chars | **⚠️ DEPRECATED:** Confirmation dialog text for new chat button. Use `modal.newChatBody` in translations instead | `"Start over? Your current chat will be lost."` |

### Internationalization & Translations

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `language` | `string` | Optional | `"en"` | Valid language code | Language code for widget UI (en, es, fr, ar, hi, ita, por, sw, uk) | `"es"` for Spanish |
| `translations-url` | `string` | Optional | `undefined` | Valid URL | URL to custom JSON translations file for widget strings | `"https://yoursite.com/translations.json"` |
