# Embedding a Bot

## Overview

Open Chat Studio provides two methods for embedding a chatbot into your website: using the Chat Component or an iframe. This guide covers both approaches.

Here is a demo of using the chat component:

<open-chat-studio-widget visible="false" bot-url="https://chatbots.dimagi.com/a/dimagi/experiments/e/dc2c0c98-d655-4042-b184-7a7a2ecb2954/embed/start/" button-text="Chat Demo" welcome-messages="['Hi! Welcome to our support chat.']"
 starter-questions="['Tell me about pricing', 'Schedule a demo']"></open-chat-studio-widget>

## Prerequisites

Before embedding, you must create a bot in Open Chat Studio.

## Method 1: Using the Chat Component

### Installation Steps

1. Add the widget script to your site's `<head>` section:
   
      ```html
      <script type='module' src='https://unpkg.com/open-chat-studio-widget@0.3.1/dist/open-chat-studio-widget/open-chat-studio-widget.esm.js' async></script>
      ```

2. Obtaining Embed Code

      1. **Log in** to Open Chat Studio.
      2. Navigate to the **Experiment** you wish to embed.
      3. Click on the :fontawesome-regular-window-maximize: **Web** channel and select :fontawesome-solid-share-nodes: **Share**
      4. Copy the provided embed code snippet.

3. Insert the widget where you want the chat button.

      The embed code snippet should look something like this:

      ```html
      <open-chat-studio-widget
        visible="false"
        bot-url="https://chatbots.dimagi.com/...."
        button-text="Let's Chat"
        position="right"
        expanded="false"
        welcome-messages="['Hi! Welcome to our support chat.']"
        starter-questions="['Tell me about pricing', 'Schedule a demo']">
      </open-chat-studio-widget>
      ```

### Customization

Customize the widget using CSS and CSS variables:

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
```

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

To see how this feature looks, follow the demo presented outlined on this page.

## Method 2: Embedding via iframe

1. Get Your Embed Code

      1. **Log in** to Open Chat Studio.
      2. Navigate to the **Experiment** you want to embed.
      3. Click on the :fontawesome-regular-window-maximize: **Web** channel and select :fontawesome-solid-share-nodes: **Share**
      4. Copy the provided embed code snippet.

2. Add the Embed Code to Your Website

      **If You Have a Website Builder (e.g., Wix, WordPress, Squarespace)**
      
      1. Open your website editor.
      2. Find the option to add an **HTML or Code Block**.
      3. Paste the embed code into the block.
      4. Save and publish your changes.
   
      **If You Have a Static HTML Website**
   
      1. Open the HTML file of your website in a text editor.
      2. Locate the `<body>` section where you want the chat widget to appear.
      3. Paste the embed code just before the closing `</body>` tag.
      4. Save the file and upload it to your web hosting service.

## Test the Chatbot

1. Open your website in a web browser.
2. Ensure the chatbot appears and functions as expected.
3. Try sending a message to confirm it responds correctly.

## Troubleshooting

If the chatbot does not appear:

- Ensure you copied and pasted the embed code correctly.
- Clear your browser cache and refresh the page.
- Check that your website allows embedding external scripts.
