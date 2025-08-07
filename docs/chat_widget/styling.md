---
render_macros: true
---
# :simple-css: CSS Styling

{% macro color_swatch(value) -%}
    <span style="font: monospace"><span style="background-color: {{ value }}; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; border-radius: 4px;"></span> ({{value}})</span>
{%- endmacro %}


Customization of the widget appearance can be done using CSS variables as follows:

```css
open-chat-studio-widget {
    --button-background-color: #d1d5db;
}
```

The following tables contain the full list of CSS variables that are available.

## Launch button

Customize the button position using CSS variables or a CSS class attached to the widget element:

```css
open-chat-studio-widget {
    position: fixed;
    right: 20px;
    bottom: 20px;
}
```

Use the following CSS variables to style the appearance of the button.

| Name                              | Description                                                    |
|-----------------------------------|----------------------------------------------------------------|
| `--button-background-color`       | Button background color {{ color_swatch('#ffffff') }}          |
| `--button-background-color-hover` | Button background color on hover {{ color_swatch('#f3f4f6') }} |
| `--button-border-color`           | Button border color {{ color_swatch('#6b7280') }}              |
| `--button-border-color-hover`     | Button border color on hover {{ color_swatch('#374151') }}     |
| `--button-font-size`              | Button text font size (0.875rem)                               |
| `--button-icon-height`            | Button icon height (1.5rem)                                    |
| `--button-icon-width`             | Button icon width (1.5rem)                                     |
| `--button-padding`                | Button padding (0.75rem)                                       |
| `--button-padding-sm`             | Small button padding (0.375rem)                                |
| `--button-text-color`             | Button text color {{ color_swatch('#111827') }}                |
| `--button-text-color-hover`       | Button text color on hover {{ color_swatch('#1d4ed8') }}       |

## Chat Window

| Name                         | Description                                                |
|------------------------------|------------------------------------------------------------|
| `--chat-window-bg-color`     | Chat window background color {{ color_swatch('#ffffff') }} |
| `--chat-window-border-color` | Chat window border color {{ color_swatch('#d1d5db') }}     |
| `--chat-window-font-size`    | Default font size for text in the chat window (0.875rem)   |
| `--chat-window-font-size-sm` | Font size for small text in the chat window (0.75rem)      |
| `--chat-window-shadow-color` | Chat window shadow color (rgba(0, 0, 0, 0.1))              |
| `--container-padding`        | General container padding (1rem) Button Variables          |

## Header

| Name                             | Description                                                     |
|----------------------------------|-----------------------------------------------------------------|
| `--header-bg-color`              | Header background color (transparent)                           |
| `--header-bg-hover-color`        | Header background color on hover {{ color_swatch('#f9fafb') }}  |
| `--header-border-color`          | Header border color {{ color_swatch('#f3f4f6') }}               |
| `--header-button-bg-hover-color` | Header button background on hover {{ color_swatch('#f3f4f6') }} |
| `--header-button-text-color`     | Header button text color {{ color_swatch('#6b7280') }}          |
| `--header-padding`               | Header padding (0.5rem)                                         |

### Messages

| Name                                  | Description                                                      |
|---------------------------------------|------------------------------------------------------------------|
| `--message-assistant-bg-color`        | Assistant message background color {{ color_swatch('#e5e7eb') }} |
| `--message-assistant-text-color`      | Assistant message text color {{ color_swatch('#1f2937') }}       |
| `--message-padding-x`                 | Message horizontal padding (1rem)                                |
| `--message-padding-y`                 | Message vertical padding (0.5rem)                                |
| `--message-system-bg-color`           | System message background color {{ color_swatch('#f3f4f6') }}    |
| `--message-system-text-color`         | System message text color {{ color_swatch('#4b5563') }}          |
| `--message-timestamp-assistant-color` | Assistant message timestamp color (rgba(75, 85, 99, 0.7))        |
| `--message-timestamp-color`           | User message timestamp color (rgba(255, 255, 255, 0.7))          |
| `--message-user-bg-color`             | User message background color {{ color_swatch('#3b82f6') }}      |
| `--message-user-text-color`           | User message text color {{ color_swatch('#ffffff') }}            |

## Starter question

| Name                                    | Description                                                        |
|-----------------------------------------|--------------------------------------------------------------------|
| `--starter-question-bg-color`           | Starter question background color (transparent)                    |
| `--starter-question-bg-hover-color`     | Starter question background on hover {{ color_swatch('#eff6ff') }} |
| `--starter-question-border-color`       | Starter question border color {{ color_swatch('#3b82f6') }}        |
| `--starter-question-border-hover-color` | Starter question border on hover {{ color_swatch('#2563eb') }}     |
| `--starter-question-padding`            | Starter question padding (0.75rem)                                 |
| `--starter-question-text-color`         | Starter question text color {{ color_swatch('#3b82f6') }}          |

## Input bar

| Name                          | Description                                                |
|-------------------------------|------------------------------------------------------------|
| `--input-bg-color`            | Input area background color (transparent)                  |
| `--input-border-color`        | Input field border color {{ color_swatch('#d1d5db') }}     |
| `--input-outline-focus-color` | Input field focus ring color {{ color_swatch('#3b82f6') }} |
| `--input-placeholder-color`   | Input placeholder text color {{ color_swatch('#6b7280') }} |
| `--input-text-color`          | Input text color {{ color_swatch('#111827') }}             |
| `--input-textarea-padding-x`  | Input textarea horizontal padding (0.75rem)                |
| `--input-textarea-padding-y`  | Input textarea vertical padding (0.5rem)                   |

## Send button

| Name                                | Description                                                        |
|-------------------------------------|--------------------------------------------------------------------|
| `--send-button-bg-color`            | Send button background color {{ color_swatch('#3b82f6') }}         |
| `--send-button-bg-disabled-color`   | Send button background when disabled {{ color_swatch('#d1d5db') }} |
| `--send-button-bg-hover-color`      | Send button background on hover {{ color_swatch('#2563eb') }}      |
| `--send-button-padding-x`           | Send button horizontal padding (1rem)                              |
| `--send-button-padding-y`           | Send button vertical padding (0.5rem)                              |
| `--send-button-text-color`          | Send button text color {{ color_swatch('#ffffff') }}               |
| `--send-button-text-disabled-color` | Send button text when disabled {{ color_swatch('#6b7280') }}       |

## Loading indicators

| Name                            | Description                                                        |
|---------------------------------|--------------------------------------------------------------------|
| `--loading-spinner-fill-color`  | Loading spinner fill color {{ color_swatch('#3b82f6') }}           |
| `--loading-spinner-size`        | Loading spinner size (1.25rem)                                     |
| `--loading-spinner-track-color` | Loading spinner track color {{ color_swatch('#e5e7eb') }}          |
| `--loading-text-color`          | Loading text color {{ color_swatch('#6b7280') }}                   |
| `--typing-progress-bg-color`    | Typing progress bar background color {{ color_swatch('#ade3ff') }} |

## Markdown code


| Name                            | Description                                                                    |
|---------------------------------|--------------------------------------------------------------------------------|
| `--code-bg-assistant-color`     | Code background in assistant messages {{ color_swatch('#ffffff') }}            |
| `--code-bg-user-color`          | Code background in user messages {{ color_swatch('rgba(59, 130, 246, 0.3)') }} |
| `--code-border-assistant-color` | Code border in assistant messages {{ color_swatch('#d1d5db') }}                |
| `--code-border-user-color`      | Code border in user messages {{ color_swatch('rgba(59, 130, 246, 0.6)') }}     |
| `--code-text-assistant-color`   | Code text color in assistant messages {{ color_swatch('#1f2937') }}            |
| `--code-text-user-color`        | Code text color in user messages {{ color_swatch('#dbeafe') }}                 |

## Error message

| Name                      | Description                                    |
|---------------------------|------------------------------------------------|
| `--error-message-padding` | Error message padding (0.5rem)                 |
| `--error-text-color`      | Error text color {{ color_swatch('#ef4444') }} |


## Z-Index

If the chatbot appears below other elements on the page you can increase the `z-index` of the chatbot by setting the `--chat-z-index` CSS variable. The default value is `50`.

```css
open-chat-studio-widget {
    --chat-z-index: 100;
}
```

In some cases, it may also be necessary to reduce the z-index of other elements on the page.
