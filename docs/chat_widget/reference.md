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

- When button-text is provided, the button displays both an icon and text
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


### Custom Icon
Replace the default chat icon with your own:
```html
<open-chat-studio-widget
  icon-url="https://your-domain.com/custom-chat-icon.svg">
</open-chat-studio-widget>
```

If no icon-url is provided, the default Open Chat Studio logo is used

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

## :simple-css: CSS Styling

### Colors and Appearance

Customize the widget using CSS variables:

```css
open-chat-studio-widget {
    position: fixed;
    right: 20px;
    bottom: 20px;
    --button-background-color: blue;
    --button-background-color-hover: black;
    --button-text-color: white;
    --button-text-color-hover: yellow;
}
```

### Z-Index

If the chatbot appears below other elements on the page you can increase the `z-index` of the chatbot by setting the `--chat-z-index` CSS variable. The default value is `50`.

```css
open-chat-studio-widget {
    --chat-z-index: 100;
}
```

In some cases, it may also be necessary to reduce the z-index of other elements on the page.

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
| `expanded`                  | `boolean` | `false`                         | Initial expanded state                                                                                                            |
| `position`                  | `string`  | `"right"`                       | Initial widget position (`"left"` \| `"center"` \| `"right"`)                                                                     |
| `welcome-messages`          | `string`  | `undefined`                     | JSON array of welcome messages                                                                                                    |
| `starter-questions`         | `string`  | `undefined`                     | JSON array of clickable starter questions                                                                                         |
| `persistent-session`        | `boolean` | `true`                          | Whether to persist session data to local storage to allow resuming previous conversations after page reload.                      |
| `persistent-session-expire` | `number`  | `1440` (24 hours)               | Minutes since the most recent message after which the session data in local storage will expire. Set this to `0` to never expire. |
