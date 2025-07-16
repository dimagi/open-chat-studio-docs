# Widget Customization

Learn how to customize the Open Chat Studio widget to match your brand and improve user experience.

## Basic Styling

### Colors and Appearance

Customize the widget using CSS variables:

```html
<style>
  open-chat-studio-widget {
    position: fixed;
    right: 20px;
    bottom: 20px;
    --button-background-color: blue;
    --button-background-color-hover: black;
    --button-text-color: white;
    --button-text-color-hover: yellow;
  }
</style>
<open-chat-studio-widget
  visible="false"
  bot-url="...."
  button-text="👋">
</open-chat-studio-widget>

#### Z-Index

If the chatbot appears below other elements on the page you can increase the `z-index` of the chatbot by setting the `--chat-z-index` CSS variable. The default value is `50`.

```html
<style>
  open-chat-studio-widget {
    --chat-z-index: 1000;
  }
</style>
```

In some cases it may also be necessary to reduce the z-index of other elements on the page.

For more details, see [Open Chat Studio Widget on npm](https://www.npmjs.com/package/open-chat-studio-widget)

#### Welcome Messages and Starter Questions
```html
<open-chat-studio-widget
 welcome-messages="['Hi! Welcome to our support chat.', 'How can I assist you today?']"
 starter-questions="[
   'I need technical support',
   'Tell me about pricing',
   'Schedule a demo',
   'Contact sales team'
 ]">
</open-chat-studio-widget>
```
**Welcome Messages**: Enhance user experience by displaying personalized greeting messages when the chat opens. These messages appear as bot messages at the beginning of the conversation. Welcome messages are perfect for:
- Greeting users and introducing your bot's capabilities
- Providing context about what kind of help is available
- Creating a warm, engaging first impression

Pass welcome messages as a JSON array string. Each message appears as a separate bot message bubble.

**Starter Questions**: Accelerate user engagement with pre-defined clickable questions that address common queries. These starter questions help users quickly find what they're looking for without having to type which improves the user experience. Starter questions are ideal for:
- Highlighting your most frequently asked questions
- Guiding users toward key features or information
- Improving accessibility for users who prefer clicking over typing

These questions appear as blue-outlined buttons aligned to the right (similar to user messages), making it clear they're user actions. When clicked, they automatically send that question as a user message, initiating the conversation flow. The starter questions disappear after the user clicks one or starts typing their own message, keeping the interface clean and focused.



#### Attributes List

| Attribute | Description | Required |
|-----------|-------------|----------|
| `bot-url` | URL to your chatbot | Yes |
| `visible` | Initial visibility state | No |
| `button-text` | Text on chat button | No |
| `position` | Widget position | No |
| `expanded` | Initial expanded state | No |
| `welcome-messages` | JSON array of welcome messages | No |
| `starter-questions` | JSON array of starter questions | No |
