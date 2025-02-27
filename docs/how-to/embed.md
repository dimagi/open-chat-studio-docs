# Embedding a Bot

## Overview

Open Chat Studio provides two methods for embedding a chatbot into your website: using the Chat Component or an iframe. This guide covers both approaches.

Here is a demo of using the chat component:

<open-chat-studio-widget visible="false" bot-url="https://chatbots.dimagi.com/a/dimagi/experiments/e/dc2c0c98-d655-4042-b184-7a7a2ecb2954/embed/start/" button-text="Chat Demo"></open-chat-studio-widget>

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
        expanded="false">
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
