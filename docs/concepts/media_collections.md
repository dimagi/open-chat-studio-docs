# Media Collections

!!! info "Collections are only supported with pipeline bots"
!!! info "Collections are currently behind a Feature Flag that can be enabled for your team on request"

If you want your bot to send multimedia files to users, you’ll need to link a collection to your bot. A collection refers to a set of multimedia files you’ve uploaded to OCS.

## Currently supported file types

**Documents**
.txt, .pdf, .doc, .docx, .xls, .xlsx, .csv

**Images**
.jpg, .jpeg, .png, .gif, .bmp, .webp, .svg

**Video**
.mp4, .mov, .avi

**Audio**
.mp3, .wav

Once a collection is linked, your bot will be able to send one or more files from it to users—either as a download link or directly—depending on the specific channel’s support for the file type and file size.

## How does it work?
### How does the bot know when to attach a file?

When you create a collection and upload files to it, you'll be prompted to add a summary for each file. These summaries are included in the system prompt when you link a collection to your bot. This allows the bot to accurately determine when a particular file is relevant to a conversation.

Additionally, OCS automatically provides the bot with a tool that enables it to attach files to its responses.

The location in the prompt where these summaries are included is defined by the [{media} prompt variable](./prompt_variables.md).

Here’s an example of how file details appear in the system prompt:
```
You are a friendly assistant. Here's some files that you can attach to your responses when you think the user will benefit from it:
{media}
```
becomes

```
You are a friendly assitant. Here's some files that you can attach to your responses when you think the user will benefit from it:
* File (id=22, content_type=image/png): This is an image of a border collie
* File (id=23, content_type=application/pdf): This file contains information about the behaviours of border collies
```

### How are attachments sent?
#### Web channels
Attachments are directly downloadable by clicking on them.

#### Multimedia-unsupported channels
By default, attachments are sent as download links appended to the bot's message. The user will see the file name and a corresponding download link at the end of the message. These channels do not yet support sending multimedia files:

* Telegram
* WhatsApp (Turn.io provider)
* SureAdhere
* Facebook Messenger
* Slack

#### Multimedia-supported channels
Channels that support sending multimedia files will receive each attachment as a separate message, following the bot's initial response. If a file type is not supported by the channel, or the file size exceeds the allowed limit, a download link will be appended to the bot's message instead. These channels support sending multimedia files:

* API (See the [API documentation](https://chatbots.dimagi.com/api/docs/#tag/Channels/operation/new_api_message) for more information)
* WhatsApp (Twilio Provider)



## Adding a collection to a bot

Navigate to the **Manage Files** section in the sidebar, then go to the **Collections** tab to create a new collection.

Once the collection is created, switch to the **Files** tab to upload files to it. Be sure to add a summary for each uploaded file—this helps the bot understand when a file is relevant.

After your collection has been created and populated with files, you can link it to any [LLM node][llm_node].


[llm_node]: ./pipelines/nodes.md
