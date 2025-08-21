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
     typing-indicator-text="AI is thinking...">
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

The session data is set to expire after 24 hours. This is also configurable by using the `persistent-session-expire` attribute. The value is interpreted as *"the number of minutes since the last message before the session expires"*. Setting this attribute to `0` will disable the expiration entirely.

!!! note

    The session persistence is associated with the `chatbot-id`. If the `chatbot-id` changes, any previous session data will be ignored.

## :material-clipboard-list: Properties Reference

| Property                    | Type      | Default                         | Description                                                                                                                       |
|-----------------------------|-----------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `chatbot-id`                | `string`  | -                               | Your chatbot ID (required)                                                                                                        |
| `api-base-url`              | `string`  | `"https://chatbots.dimagi.com"` | API base URL                                                                                                                      |
| `button-text`               | `string`  | `"Chat"`                        | Button display text                                                                                                               |
| `button-shape`              | `string`  | `square`                        | Button Shape (`"round"` \| `"square"`)                                                                                            |
| `icon-url`                  | `string`  | The OCS logo                    | URL to button icon                                                                                                                |
| `visible`                   | `boolean` | `false`                         | Show widget on load                                                                                                               |
| `position`                  | `string`  | `"right"`                       | Initial widget position (`"left"` \| `"center"` \| `"right"`)                                                                     |
| `header-text`               | `string`  | `undefined`                     | Text to place in the window header                                                                                                |
| `welcome-messages`          | `string`  | `undefined`                     | JSON array of welcome messages                                                                                                    |
| `starter-questions`         | `string`  | `undefined`                     | JSON array of clickable starter questions                                                                                         |
| `new-chat-confirmation-message` | `string` | `"Starting a new chat will clear your current conversation. Continue?"` | The message to display in the new chat confirmation dialog |
| `persistent-session`        | `boolean` | `true`                          | Whether to persist session data to local storage to allow resuming previous conversations after page reload.                      |
| `persistent-session-expire` | `number`  | `1440` (24 hours)               | Minutes since the most recent message after which the session data in local storage will expire. Set this to `0` to never expire. |
| `allow-full-screen`         | `boolean` | `true`                          | Allow the user to make the chat window full screen.                                                                               |
| `typing-indicator-text`         | `string`  | `"Preparing response"`          | Text displayed while the assistant is typing/preparing a response    |
