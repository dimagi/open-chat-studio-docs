# Open Chat Studio Widget

The Open Chat Studio Widget is a customizable chat component that allows you to easily embed conversational AI bots into any website. Create engaging user experiences with minimal setup and extensive customization options.

## Features

- **Easy Integration**: Add to any website with just a few lines of code
- **Flexible Embedding**: Choose between widget component or iframe methods
- **Custom Styling**: Match your brand with CSS variables and custom themes
- **Welcome Messages**: Greet users with personalized messages
- **Starter Questions**: Guide users with pre-defined clickable questions
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## Quick Demo

<open-chat-studio-widget visible="false" bot-url="https://chatbots.dimagi.com/a/dimagi/experiments/e/dc2c0c98-d655-4042-b184-7a7a2ecb2954/embed/start/" button-text="Chat Demo" welcome-messages="['Hi! Welcome to our support chat.']" starter-questions="['Tell me about pricing', 'Schedule a demo']"></open-chat-studio-widget>

## Getting Started

### 1. Embed Your Bot
Learn how to add the chat widget to your website using either the component method or iframe approach.

[**→ How to Embed Guide**](../../how-to/embed.md)

### 2. Customize Your Widget
Personalize the appearance and behavior of your chat widget to match your brand and improve user experience.

[**→ Widget Customization Guide**](./widget_customization.md)

## Quick Start

1. **Create a bot** in Open Chat Studio
2. **Add the script** to your website's `<head>`:
   ```html
   <script type='module' src='https://unpkg.com/open-chat-studio-widget@0.3.1/dist/open-chat-studio-widget/open-chat-studio-widget.esm.js' async></script>
