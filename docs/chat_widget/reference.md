# Reference Docs

Learn how to customize the Open Chat Studio widget to match your brand and improve user experience.

## Button Customization

### :material-text: Button Text

Control whether your chat button displays text alongside an icon:

```html
<open-chat-studio-widget
  button-text="Chat with us">
</open-chat-studio-widget>
```
Behavior:

- When button-text is provided, the button displays both icon and text
- When button-text is empty or not provided, only an icon is shown

### :material-shape: Button Shape
Customize the shape of your chat button:
```html
<open-chat-studio-widget
  button-shape="round">
</open-chat-studio-widget>
```
Available Shapes:

- **round** - Circular button
- **square** - Rectangular button with rounded corners

For further customization of the appearance, see [CSS Styling](styling.md)

### Custom Icon
Replace the default chat icon with your own:
```html
<open-chat-studio-widget
  icon-url="https://your-domain.com/custom-chat-icon.svg">
</open-chat-studio-widget>
```

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


### Session Impact

| Scenario                        | Behavior   |
|---------------------------------|-----------|
| Same `user-id`                 | Restores previous chat history |
| Different `user-id`                 | Starts fresh session for new user |
| No `user-id` (auto-generated)          | Restores on same browser only |
| `user-id` changes                 | Switches to different user's session |

### Dynamic User Management
Update user identification when authentication state changes:
```javascript
function updateChatUser(user) {
  const widget = document.querySelector('open-chat-studio-widget');

  if (user) {
    widget.setAttribute('user-id', user.id);
    widget.setAttribute('user-name', user.name);
  } else {
    widget.removeAttribute('user-id');
    widget.removeAttribute('user-name');
  }
}
```

!!! warning "Privacy Best Practices"
	- Use internal user IDs rather than emails or sensitive data
	- Auto-generated IDs are not personally identifiable
	- Consider your privacy policy for chat data retention
	- Allow users to clear their data if required by regulations

	Recommended:
	```html
		<!-- ✅ Good: Internal database ID -->
		user-id="user_12345"
		user-name="John Doe"
		<!-- ❌ Avoid: Sensitive information -->
		user-id="john.doe@company.com"
	```


### Troubleshooting
Chat history not restoring:

- Ensure user-id is consistent across sessions
- Check that localStorage is not being cleared
- Verify persistent-session="true" is set (default)

Multiple users seeing each other's chats:

- Always provide unique user-id for each user
- Clear session data when users switch:


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

Accelerate user engagement with pre-defined clickable questions that address common queries. These starter questions help users quickly find what they're looking for without having to type which improves the user experience. Starter questions are ideal for:

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

## :material-chat-plus: New Chat Confirmation
When users have an active conversation and click the "new chat" button, a confirmation dialog appears to prevent accidental loss of conversation history. You can customize the message displayed in this confirmation dialog:

```html
<open-chat-studio-widget
 new-chat-confirmation-message="Are you sure you want to start a new conversation?">
</open-chat-studio-widget>
```

Default behavior:

- Shows confirmation dialog with the message: "Starting a new chat will clear your current conversation. Continue?"
- Users can either "Cancel" to keep their current chat or "Continue" to start fresh
- The dialog only appears when there's an existing conversation with messages

Customization options:

- Customize the confirmation message text to match your brand voice
- Style the dialog appearance using CSS variables (see CSS Styling)


## :material-robot-excited: Typing Indicator

Customize the message displayed while the assistant is preparing a response. This helps set user expectations and can match your brand's personality.

```html
<open-chat-studio-widget
     typing-indicator-text="AI is thinking">
</open-chat-studio-widget>
```

The typing indicator appears with animated dots and a progress bar to provide visual feedback during response generation.

Styling:
- Text color is controlled by `--loading-text-color`
- Font size uses `--chat-window-font-size-sm`
- See [CSS Styling](styling.md#loading-indicators) for customization options


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

### Button & UI Customization

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `button-text` | `string` | Optional | `undefined` | Max 50 chars | Button display text. If empty, shows icon only | `"Need Help?"` |
| `button-shape` | `string` | Optional | `"square"` | `"round"` \| `"square"` | Button shape style | `"round"` for circular button |
| `icon-url` | `string` | Optional | OCS default logo | Valid URL | Custom icon for the chat button | `"https://yoursite.com/chat-icon.svg"` |
| `visible` | `boolean` | Optional | `false` | `true` \| `false` | Show widget immediately on page load | `"true"` to auto-open |
| `position` | `string` | Optional | `"right"` | `"left"` \| `"center"` \| `"right"` | Initial widget position on screen | `"left"` for left side placement |
| `header-text` | `string` | Optional | `undefined` | Max 100 chars | Text displayed in chat window header | `"Customer Support"` |

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
| `typing-indicator-text` | `string` | Optional | `"Preparing response"` | Max 50 chars | Text shown while bot is typing | `"AI is thinking..."` |
| `new-chat-confirmation-message` | `string` | Optional | `"Starting a new chat will clear your current conversation. Continue?"` | Max 200 chars | Confirmation dialog text for new chat button | `"Start over? Your current chat will be lost."` |
