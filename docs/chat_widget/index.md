# Open Chat Studio Widget

The Open Chat Studio Widget is a customizable chat component that allows you to easily embed conversational AI bots into any website. Create engaging user experiences with minimal setup and extensive customization options.

## Features

- **Easy Integration**: Add to any website with just a few lines of code
- **Flexible Embedding**: Choose between widget component or iframe methods
- **Custom Styling**: Match your brand with CSS variables and custom themes
- **Welcome Messages**: Greet users with personalized messages
- **Starter Questions**: Guide users with pre-defined clickable questions
- **Responsive Design**: Works seamlessly across desktop and mobile devices

<div class="grid cards" markdown>

-   :octicons-gear-16:{ .lg .middle } [View the reference docs](reference.md)
-   ::octicons-list-unordered-16:{ .lg .middle } [Changelog and upgrade info](changelog.md)

</div>

## Getting Started

Before embedding, you must create a bot in Open Chat Studio.

1. Add the widget script to your site's `<head>` section:
   
      ```html
      <script type='module' src='https://unpkg.com/open-chat-studio-widget@0.4.1/dist/open-chat-studio-widget/open-chat-studio-widget.esm.js' async></script>
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

## Test the Chatbot

1. Open your website in a web browser.
2. Ensure the chatbot appears and functions as expected.
3. Try sending a message to confirm it responds correctly.

## Troubleshooting

If the chatbot does not appear:

- Ensure you copied and pasted the embed code correctly.
- Clear your browser cache and refresh the page.
- Check that your website allows embedding external scripts.
