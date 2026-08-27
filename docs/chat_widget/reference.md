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

### Button Text

- When button-text is provided, the button displays both icon and text
- When button-text is empty or not provided, only an icon is shown

### Button Shape

- **round** - Circular button
- **square** - Rectangular button with rounded corners

### Icon URL

If no icon-url is provided, the default Open Chat Studio avatar is used.

### Button position

Customize the button position using CSS variables or a CSS class attached to the widget element:

```css
open-chat-studio-widget {
    position: fixed;
    right: 20px;
    bottom: 20px;
}
```

!!! tip "Drag the button"

    The button can be dragged by the user to anywhere on the screen. This allows the user to move the button
    if it is obstructing other page content. The button will return to its original position on the next page load.

<div class="grid cards" markdown>
-   :simple-css:{ .sm .middle } See [CSS Styling](styling.md) for more customization options.
</div>

## :material-shield-key: Embed Authentication {#embed-authentication}
Secure your embedded widgets with authentication keys for controlled access to specific channels.

### Overview
The embed authentication feature allows you to:

- Restrict widget access to authorized embeddings only
- Authenticate specific embedded channel instances
- Provide secure access control for sensitive or premium content
- Track and manage different embedded deployments

Two authentication mechanisms are available, depending on how the channel is configured on the server:

- **Embed key** (default) — a static key sent as an `X-Embed-Key` header. See [Implementation](#implementation) below.
- **OAuth credential mode** — a bearer token supplied by your own backend via the `authTokenProvider` JS property. See [OAuth Credential Mode](#oauth-credential-mode) below.

### Implementation

```html
<open-chat-studio-widget
  chatbot-id="your-chatbot-id"
  embed-key="your-secure-embed-key">
</open-chat-studio-widget>
```

When an embed key is provided, it's automatically sent as an `X-Embed-Key` header with all API requests to authenticate the widget instance.

### OAuth Credential Mode

!!! note "Not yet configurable in Open Chat Studio"
    OAuth credential mode is a setting on the "Chat Widget & API" channel itself, and the channel
    configuration screen does not yet offer a control for it. Widget support has landed ahead of that
    control, so for now you cannot switch a channel into OAuth mode. Setting `authTokenProvider` on a
    channel using the default embed-key mode has no effect, and existing embeds are unaffected.

When a channel is configured for OAuth credential mode, the widget must present an OAuth bearer token to start a chat session. You provide that token by setting the `authTokenProvider` JS property on the widget element:

```javascript
document.querySelector('open-chat-studio-widget').authTokenProvider = async ({ forceRefresh }) => {
  const response = await fetch(`/api/get-widget-token?force_refresh=${forceRefresh}`, { credentials: 'include' });
  const { token } = await response.json();
  return token;
};
```

`authTokenProvider` is a **JS property only** — there is no HTML attribute equivalent, because its value is a function and HTML attributes can only hold strings. A copy-paste HTML embed snippet cannot use OAuth mode on its own; the host page needs a small `<script>` block, like the one above, that selects the widget element and assigns the property.

#### How it works

- The widget calls `authTokenProvider` at the start of every session and sends the returned token as an `Authorization: Bearer <token>` header on the `chat/start/` request only. The header is **not** sent on message-send, poll, or upload requests.
- The widget passes a single options object to the function — `{ forceRefresh: boolean }` — described in [The `forceRefresh` argument](#the-forcerefresh-argument) below.
- The function can return a token string directly, or a `Promise` that resolves to one.
- The widget never stores or caches the token itself. It calls the provider every time it starts a session — including when a previous session expires and the widget starts a new one automatically. The widget does not run a refresh timer; `forceRefresh` is the only signal it gives the host page about token freshness.
- If `authTokenProvider` returns a falsy value (`undefined`, `null`, or an empty string), the widget sends the request with no `Authorization` header. On an OAuth-mode channel the server will then refuse to start the session.
- If `authTokenProvider` **throws**, the widget does *not* fall back to an unauthenticated request — session start fails and the widget shows "Could not obtain an authentication token". The thrown error's own text is deliberately not surfaced in the chat (it is logged to the browser console instead), so that a message quoting a token is never written to the persisted transcript.

#### The `forceRefresh` argument

Your provider is allowed to cache tokens — on your backend, or in the browser for the lifetime of the page. `forceRefresh` tells you when a cached token is acceptable and when it is not:

| `forceRefresh` | When the widget passes it | What your provider should do |
|----------------|---------------------------|------------------------------|
| `false`        | The first call for a given session start | Return a token. An existing cached token is fine, as long as it is still valid. |
| `true`         | The retry call, after `chat/start/` came back `401` with the previous token | Bypass your cache and mint a genuinely new token. |

```javascript
let cached;

document.querySelector('open-chat-studio-widget').authTokenProvider = async ({ forceRefresh }) => {
  if (cached && !forceRefresh) {
    return cached;
  }
  const response = await fetch('/api/get-widget-token', { credentials: 'include' });
  cached = (await response.json()).token;
  return cached;
};
```

!!! warning "Returning the same token for `forceRefresh: true` cancels the retry"
    The widget only resends `chat/start/` if the refreshed token **differs** from the one that
    was just rejected (see [Retry behavior on 401](#retry-behavior-on-401)). A provider that
    ignores `forceRefresh` and returns its cached value again — or returns a falsy value — gets no
    retry, and the session start fails with the original `401`.

Because the argument is an object, a zero-argument provider such as `async () => token` is still valid JavaScript and works for the initial call — but it can never distinguish the retry, so it forfeits the behavior above. Read `forceRefresh` if you cache anything.

#### Mint tokens on your server, not in the browser

Minting an OAuth token uses a client-credentials flow, which requires a client secret. That secret must never be exposed in a web page. `authTokenProvider` should call an endpoint on your own backend — one that holds the secret, talks to Open Chat Studio to obtain a token, and returns just the token to the browser. The example above shows this pattern: the browser calls your `/api/get-widget-token` endpoint, and your server does the actual client-credentials exchange with Open Chat Studio.

#### Retry behavior on 401

If Open Chat Studio rejects the token with an `HTTP 401` on `chat/start/`, the widget calls `authTokenProvider` again — this time with `{ forceRefresh: true }` — and retries the session-start request **exactly once**, but only if the newly returned token is different from the one that was just rejected. `chat/start/` is rate-limited, so the widget avoids resending an identical request that would waste your quota for no benefit.

!!! note "401 vs. 403"
    A `401` means the token itself was refused (missing, expired, or invalid), which triggers the retry described above. A `403` means the session or resource is forbidden for an otherwise-valid caller — this is a distinct case and does not trigger a token refresh or retry.

#### Version requirement

OAuth credential mode support requires widget version **0.12.0** or later. See [Widget Version](#widget-version) for how to check the version running on a page.

## :material-account: User Identification {#user-identification}
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

- Example: `ocs:550e8400-e29b-41d4-a716-446655440000`

!!! note
    Widget versions before **0.12.0** generated IDs in an older `ocs:1703123456789_a7x9k2m8f` (timestamp + random suffix) format. This is not a breaking change — IDs already stored in a visitor's browser keep working, and only newly generated IDs use the UUID format.

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

## :material-hand-wave: Welcome Messages {#welcome-messages}

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

## :material-folder-question: Starter Questions {#starter-questions}

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

## :material-lock: Read-Only Mode {#read-only-mode}

Put the widget into a read-only state when your team is unavailable to respond, during maintenance windows, or whenever you need to pause conversations without hiding the widget entirely. Read-only mode is ideal for:

- Enforcing business hours or on-call availability
- Pausing conversations during scheduled maintenance
- Temporarily suspending a chatbot without removing it from the page

When enabled:

- Chat history remains visible and scrollable, so users can still review past messages
- The message composer and send button stay visible, but disabled
- Sending is blocked entirely — even programmatic `sendMessage` calls return early, so the restriction cannot be bypassed from the host page
- Starter questions are hidden

```html
<open-chat-studio-widget
 chatbot-id="your-chatbot-id"
 disabled="true">
</open-chat-studio-widget>
```

!!! tip "Tell users why"
    Pair `disabled` with a [banner](#banner) so users understand why they can't send messages, for example to display your support hours or an outage notice.

## :material-bullhorn: Banner {#banner}

Display an always-visible notice above the chat history to communicate information that shouldn't scroll away with the conversation. Banners are useful for:

- Announcing maintenance windows or outages
- Sharing business hours or expected response times
- Displaying compliance, legal, or privacy notices
- Explaining why the chat is in [read-only mode](#read-only-mode)

Set `banner-message` to show the banner. Use `banner-style` to match the tone of the notice, and `banner-position` to control where it appears.

```html
<open-chat-studio-widget
 chatbot-id="your-chatbot-id"
 banner-message="We're currently offline. We'll be back during business hours."
 banner-style="warning"
 banner-position="top">
</open-chat-studio-widget>
```

### Banner Styles

- **default** - Neutral notice styling
- **info** - Informational notice
- **warning** - Cautionary notice
- **error** - Critical or urgent notice

### Banner Position

- **top** (default) - Displayed above the chat history
- **bottom** - Displayed directly above the message input area

The banner works on its own, or together with `disabled` to explain a read-only state:

```html
<open-chat-studio-widget
 chatbot-id="your-chatbot-id"
 disabled="true"
 banner-message="This chat is temporarily unavailable. Please email support@example.com for help."
 banner-style="error"
 banner-position="bottom">
</open-chat-studio-widget>
```

## :material-paperclip: File Attachments {#file-attachments}
Enable users to send files along with their messages. This feature is perfect for support scenarios where users need to share screenshots, documents, or other files.

```html
<open-chat-studio-widget
 allow-attachments="true">
</open-chat-studio-widget>
```

### Supported File Types

#### Documents:
- Text files: All text/* types (including .txt, .csv, .log, .md, and more)
- PDF documents: .pdf
- Microsoft Word: .doc, .docx
- Microsoft Excel: .xls, .xlsx

#### Images:
- Supported formats: .jpg, .jpeg, .png, .gif, .webp
- `.bmp` and `.svg` are **not** supported and are rejected at upload

!!! note
    Image support varies slightly by the chatbot's LLM provider. Most providers accept PNG, JPEG, GIF, and WEBP. Google Gemini models accept PNG, JPEG, WEBP, HEIC, and HEIF, but not GIF.

#### Media:
- Video files: .mp4, .mov, .avi
- Audio files: .mp3, .wav

### How Files Are Processed

When attachments are sent to the LLM:

- **PDFs and images** are sent directly to the LLM API as native file attachments (where supported by the model).
- **Word (.doc, .docx) and Excel (.xls, .xlsx) documents** are automatically converted to plain text before being sent to the LLM.
- **Text files and CSVs** are sent as plain text content.

Files are validated on upload by their contents, not just their extension — if a file's contents don't match its extension (for example, SVG data renamed to `photo.jpg`), the upload is rejected. Attachments are never silently dropped: if an image reaches the LLM in a format that provider doesn't support, the whole message fails with a clear error naming the file and the formats that provider accepts, rather than a raw provider error.

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

## :material-translate: Internationalization {#internationalization}

The chat widget supports multiple languages and custom translations for all UI text elements.

### Built-in Language Support

The widget includes built-in translations for the following languages:

- **English** (`en`) - Default
- **Spanish** (`es`)
- **French** (`fr`)
- **Arabic** (`ar`)
- **Hindi** (`hi`)
- **Italian** (`it`)
- **Portuguese** (`pt`)
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

By default, the widget will save the chat messages and the widget's open/closed state in the browser local storage. This allows users to continue sessions after reloading the page or navigating to a new page. If the user had the chat widget open when navigating to a new page, it will automatically reopen. In addition to automatic session expiration, the user can also use the 'new chat' button to start a new session.

To disable this feature, set the `persistent-session="false"` attribute on the widget element.

!!! note "Single-tab persistence"
    Requires widget **0.12.0+**. Set `persistent-session="tab"` to scope persistence to a single browser tab: the widget keeps the session in `sessionStorage` instead of `localStorage`, so the conversation survives a reload of that tab but is forgotten as soon as the tab is closed. This differs from the default `true`, which persists across tabs and browser restarts via `localStorage`. Clearing a session only clears the storage the current widget instance is using, so a `"tab"` widget on one page can't clear a session held by a `true` widget on another page at the same origin, or vice versa.

!!! note

    The session persistence is associated with the `chatbot-id`. If the `chatbot-id` changes, any previous session data will be ignored.

The session data is set to expire after 24 hours. This is also configurable by using the `persistent-session-expire` attribute. The value is interpreted as *"the number of minutes since the last message before the session expires"*. Setting this attribute to `0` will disable the expiration entirely. This still applies to `persistent-session="tab"` sessions, so a tab-scoped session left open (rather than closed) is reaped on the same schedule as any other.

!!! note

    Session persistence works in conjunction with [User Identification](#user-identification). Different users will have separate persistent sessions.

## :material-clock-outline: Browser Timezone {#browser-timezone}

When a chat session starts, the widget automatically detects the visitor's browser timezone (for example `America/New_York`) and sends it to Open Chat Studio, which stores it on the participant. This lets the chatbot refer to dates and times in the user's local time. No attribute or configuration is needed to enable this — it happens automatically for every session start.

## :material-lightbulb: Page Context {#page-context}

Pass page-specific context to the bot with each message to enable more personalized and relevant responses. The context is automatically included with every user message and helps the bot understand the current page state and user environment.

### Use Cases

Page context is ideal for:

- Providing current user role or permissions to the bot
- Sharing page URL, document name, or current section information
- Passing feature flags or configuration state
- Including product/service information relevant to the page

### Basic Implementation

Context must be set using JavaScript with a plain object:

```javascript
const widget = document.querySelector('open-chat-studio-widget');

widget.pageContext = {
  user_role: 'admin',
  page_location: 'dashboard'
};
```

### Dynamic Context Management

Update context dynamically using JavaScript when page state changes:

```javascript
const widget = document.querySelector('open-chat-studio-widget');

// Set initial context
let pageContext = {
  user_role: 'customer',
  page_location: 'product-listing',
  product_category: 'electronics'
};

widget.pageContext = pageContext;

// Update context when user navigates
document.addEventListener('navigate', (event) => {
  let newContext = {
    ...pageContext,
    page_location: event.detail.location
  };
  widget.pageContext = newContext;
});
```

### Context Object Structure

The `pageContext` property accepts a plain JavaScript object (not a JSON string). Each property is included in the context sent to the bot:

```javascript
widget.pageContext = {
  // User information
  user_role: 'support_agent',
  user_department: 'technical_support',

  // Page information
  page_location: 'help-center',
  page_title: 'Troubleshooting Guide',

  // Application state
  session_type: 'trial',
  account_status: 'active',

  // Custom data
  feature_flags: ['new_ui', 'beta_features'],
  request_context: 'urgent'
};
```

!!! note

    The page context is persisted in the session state on the server side and is accessible via `session_state.remote_context`. See [accessing remote context](../concepts/prompt_variables.md#accessing-remote-context) for more details.

## :material-lightning-bolt: Events {#events}

The widget dispatches custom events on the `<open-chat-studio-widget>` host element. All events are dispatched with `bubbles: true` and `composed: true`, so they escape the shadow DOM and are catchable anywhere on the host page using standard `addEventListener`.

### Event Reference

| Event | Fired when | `event.detail` |
|---|---|---|
| `ocs:open` | Widget becomes visible | — |
| `ocs:close` | Widget is hidden | — |
| `ocs:message:before-send` | Before a message is sent to the API | `{ message, sessionId }` |
| `ocs:message:sent` | Message dispatched to the API | `{ message, sessionId }` |
| `ocs:message:received` | Bot reply delivered | `{ message: { content: string, role: string }, sessionId }` |
| `ocs:session:started` | New session created | `{ sessionId }` |
| `ocs:session:ended` | Server ended the session | `{ sessionId }` |

!!! note "`ocs:message:received`"
    This event fires only for non-`user` roles (bot, assistant, and system replies). It does not fire for the participant's own messages.

### `ocs:message:before-send`

`ocs:message:before-send` fires **synchronously** before the API call. A handler can update the `pageContext` property and the new value is picked up in that same send. This is the recommended pattern for lazily refreshing page context just before each message.

### Usage Example

```javascript
const widget = document.querySelector('open-chat-studio-widget');

// Lazy pageContext update just before send
widget.addEventListener('ocs:message:before-send', () => {
  widget.pageContext = getClientPageContext(); // your own function
});

// Track bot replies
widget.addEventListener('ocs:message:received', (e) => {
  console.log('Bot said:', e.detail.message.content);
});
```

## :material-information-outline: Widget Version {#widget-version}

The widget stamps its build version onto the `<open-chat-studio-widget>` host element, so you can confirm which release is running on a deployed page without checking the CDN URL.

### `data-widget-version` attribute

Read the version straight from the DOM with `getAttribute`. This is the quickest way to check the version in the browser DevTools:

```javascript
document.querySelector('open-chat-studio-widget').getAttribute('data-widget-version');
// "0.12.0"
```

!!! note
    `data-widget-version` is set as soon as the widget script loads, even if `chatbot-id` is missing or invalid. You can rely on it to confirm the widget script itself loaded correctly, independent of chatbot configuration.

### `getVersion()` method

For programmatic access, call `getVersion()` on the element. Like other widget methods, it returns a `Promise`:

```javascript
const widget = document.querySelector('open-chat-studio-widget');
const version = await widget.getVersion();
console.log(version); // "0.12.0"
```

## :material-clipboard-list: Properties Reference {#properties-reference}

### Core Configuration

| Property | Type | Required | Default | Description | Example |
|----------|------|----------|---------|-------------|---------|
| `chatbot-id` | `string` | **REQUIRED** | - | Your chatbot ID from Open Chat Studio | `"183312ac-cbe5-4c91-9e7b-d9df96b088e4"` |
| `api-base-url` | `string` | Optional | `"https://openchatstudio.com"` | API base URL for your Open Chat Studio instance | `"https://your-domain.com"` |
| `embed-key` | `string` | Optional | `undefined` | Authentication key for embedded channels | `"your-embed-auth-key"` |
| `authTokenProvider` | `function` | Optional | `undefined` | **JS property only — no HTML attribute.** Function (or async function) returning an OAuth bearer token string, called fresh at the start of every session. Used for [OAuth credential mode](#oauth-credential-mode). Requires widget **0.12.0+** | `() => fetchTokenFromMyBackend()` |

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
| `user-id` | `string` | Optional | Auto-generated | None | Unique user identifier for session continuity<br/>**Auto-format:** `ocs:<uuid v4>`, e.g. `ocs:550e8400-e29b-41d4-a716-446655440000` | `"user_12345"` or `"customer@email.com"` |
| `user-name` | `string` | Optional | `undefined` | Max 200 chars | Display name sent to chat API for personalization | `"John Smith"` or `"Customer #12345"` |

### Chat Behavior & Sessions

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `pageContext` | `object` | Optional | `undefined` | Plain JS object | Optional context data to send with each message for personalization<br/>**Note:** Context is cleared after each message | `{"user_role": "admin", "page_location": "dashboard"}` |
| `persistent-session` | `boolean \| "tab"` | Optional | `true` | `true` \| `false` \| `"tab"` | Save chat history in browser localStorage. `"tab"` scopes persistence to the current browser tab via sessionStorage instead — see [Persistent Sessions](#persistent-sessions). Requires widget **0.12.0+** for `"tab"` | `"false"` to disable session saving, `"tab"` to persist only for the current tab |
| `persistent-session-expire` | `number` | Optional | `1440` (24 hours) | 0-43200 (30 days) | Minutes before session expires | `720` for 12 hours, `0` for never expire |
| `allow-full-screen` | `boolean` | Optional | `true` | `true` \| `false` | Enable fullscreen mode button | `"false"` to hide fullscreen option |
| `allow-attachments` | `boolean` | Optional | `false` | `true` \| `false` | Enable file upload functionality<br/>**Limits:** 50MB per file, 50MB total per message | `"true"` to enable file uploads |
| `disabled` | `boolean` | Optional | `false` | `true` \| `false` | Puts the widget into [read-only mode](#read-only-mode): history stays visible, but the composer, send controls, and starter questions are disabled or hidden | `"true"` to make the widget read-only |

### Banner Notice

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `banner-message` | `string` | Optional | `undefined` | - | Notice text shown in an always-visible [banner](#banner). The banner only displays when this is set | `"We're currently offline."` |
| `banner-style` | `string` | Optional | `"default"` | `"default"` \| `"info"` \| `"warning"` \| `"error"` | Visual style of the banner | `"warning"` for a cautionary notice |
| `banner-position` | `string` | Optional | `"top"` | `"top"` \| `"bottom"` | Where the banner appears. The bottom position sits directly above the input area | `"bottom"` to anchor above the composer |

### Messages & Content

| Property | Type | Required | Default | Validation | Description | Example |
|----------|------|----------|---------|------------|-------------|---------|
| `welcome-messages` | `string` | Optional | `undefined` | Valid JSON array<br/>**Max:** 5 messages, 500 chars each | Welcome messages shown when chat opens<br/>**Format:** `'["Message 1", "Message 2"]'` | `'["Welcome!", "How can I help?"]'` |
| `starter-questions` | `string` | Optional | `undefined` | Valid JSON array<br/>**Max:** 6 questions, 100 chars each | Clickable question buttons to start conversation<br/>**Format:** `'["Question 1", "Question 2"]'` | `'["Check my order", "Technical support"]'` |
| `typing-indicator-text` | `string` | Optional | `"Preparing response"` | Max 50 chars | **⚠️ DEPRECATED:** Text shown while bot is typing. Use `status.typing` in translations instead | `"AI is thinking..."` |
| `new-chat-confirmation-message` | `string` | Optional | `"Starting a new chat will clear your current conversation. Continue?"` | Max 200 chars | **⚠️ DEPRECATED:** Confirmation dialog text for new chat button. Use `modal.newChatBody` in translations instead | `"Start over? Your current chat will be lost."` |

### Internationalization & Translations

| Property | Type | Required | Default | Validation | Description                                                      | Example |
|----------|------|----------|---------|------------|------------------------------------------------------------------|---------|
| `language` | `string` | Optional | `"en"` | Valid language code | Language code for widget UI (en, es, fr, ar, hi, it, pt, sw, uk) | `"es"` for Spanish |
| `translations-url` | `string` | Optional | `undefined` | Valid URL | URL to custom JSON translations file for widget strings          | `"https://yoursite.com/translations.json"` |
