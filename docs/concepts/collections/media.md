---
title: Media collections
---

## When should I use this?
When you want your chatbot to be able to send multimedia files to users.

## Currently supported file types

**Documents**
.txt, .pdf, .doc, .docx, .xls, .xlsx, .csv

**Images**
.jpg, .jpeg, .png, .gif, .bmp, .webp, .svg

**Video**
.mp4, .mov, .avi

**Audio**
.mp3, .wav

Once a collection is linked, your chatbot will be able to send one or more files from it to users—either as a download link or directly—depending on the specific channel’s support for the file type and file size.

!!! note "Changes take effect on published chatbots immediately"
    Adding, removing, or replacing files in a media collection is reflected in the published chatbot without requiring a republish. See [Collections and published chatbots](index.md#collections-and-published-chatbots) for more detail.

## How does it work?
### How does the chatbot know when to attach a file?

When you create a collection and upload files to it, you'll be prompted to add a summary for each file. These summaries are included in the system prompt when you link a collection to your chatbot. This allows the chatbot to accurately determine when a particular file is relevant to a conversation.

Additionally, OCS automatically provides the chatbot with a tool that enables it to attach files to its responses.

The location in the prompt where these summaries are included is defined by the [{media} prompt variable](../prompt_variables.md).

Here’s an example of how file details appear in the system prompt:

```text
You are a friendly assistant. Here's some files that you can attach to your responses when you think the user will benefit from it:
{media}
```

becomes

```text
You are a friendly assistant. Here's some files that you can attach to your responses when you think the user will benefit from it:
* File (id=22, content_type=image/png): This is an image of a border collie
* File (id=23, content_type=application/pdf): This file contains information about the behaviours of border collies
```
