# Collections

!!! info "Collections are only supported with pipeline bots"
!!! info "Collections are currently behind a Feature Flag that can be enabled for your team on request"

A collection in OCS refers to a collection of files. There are two types of collections:

- [Media collection](#media-collections)
- [Indexed Collection (for RAG applications)](#collection-indexes-for-rag-applications)

## Media collections

### When should I use this?
When you want your bot to be able to send multimedia files to users.

### Currently supported file types

**Documents**
.txt, .pdf, .doc, .docx, .xls, .xlsx, .csv

**Images**
.jpg, .jpeg, .png, .gif, .bmp, .webp, .svg

**Video**
.mp4, .mov, .avi

**Audio**
.mp3, .wav

Once a collection is linked, your bot will be able to send one or more files from it to users—either as a download link or directly—depending on the specific channel’s support for the file type and file size.

### How does it work?
#### How does the bot know when to attach a file?

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


## Collection Indexes (for RAG applications)
### When should I use this?
When you want your bot's responses to be grounded in your uploaded documents.

!!! note "Definition"
    **Retrieval-Augmented Generation** (RAG) is a technique where a language model retrieves relevant information from a set of documents to ground its answers in real data. Instead of relying solely on its built-in knowledge, the model uses indexes—specialized databases that store document content as vectors (numerical representations of meaning). This makes it easy for the model to find and use the most relevant parts of your uploaded files when answering questions.

!!! warning "Indexed collections will replace OpenAI Assistants in the future"

If you’ve used the OpenAI Assistants’ [file search][file-search] capability in OCS, you’ve already interacted with an index behind the scenes.

In OCS, indexed collections are managed through LLM services like OpenAI. When creating an indexed collection, you’ll select the LLM provider responsible for hosting and querying that index.


### Currently supported providers
- OpenAI


### Chunking and Optimization
When you upload a document to an index, it’s broken up into smaller parts called chunks. These chunks are then converted into vectors and stored in the index. Chunking is a key part of how RAG works, as it affects how accurately the model can retrieve relevant information.

In most cases, it will not be necessary to have to change the default chunking strategy, but you’ll have the option to customize the chunking strategy for each set of uploaded files:

- Chunk size – how large each chunk is (in tokens)
- Chunk overlap – how much each chunk overlaps with the next, to preserve context

Choosing the right chunking strategy can improve retrieval accuracy, especially for technical documents.

!!! info "This flexibility helps tailor the index to your use case—whether it’s short notes or long, complex reports."

### Supported file types
Supported files are dictated by the select provider:

- OpenAI - See the [OpenAI docs](https://platform.openai.com/docs/assistants/tools/file-search/supported-files#supported-files)



## Adding a collection to a bot

Navigate to the **Collections** section in the sidebar and click "Add new". Once the collection is created, you will be able to upload files to it.

After your collection has been created and populated with files, you can link it to any [LLM node][llm_node].


## How are attachments sent?
When a bot referenced a particular file or document, it will be sent to the user as an attachment. Depending on the channel, attachments are delivered in different ways.

### Web channels
Attachments are directly downloadable by clicking on them.

### Multimedia-unsupported channels
By default, attachments are sent as download links appended to the bot's message. The user will see the file name and a corresponding download link at the end of the message. These channels do not yet support sending multimedia files:

* Telegram
* WhatsApp (Turn.io provider)
* SureAdhere
* Facebook Messenger
* Slack

### Multimedia-supported channels
Channels that support sending multimedia files will receive each attachment as a separate message, following the bot's initial response. If a file type is not supported by the channel, or the file size exceeds the allowed limit, a download link will be appended to the bot's message instead. These channels support sending multimedia files:

* API - See the [API documentation](https://chatbots.dimagi.com/api/docs/#tag/Channels/operation/new_api_message) for more information
* WhatsApp (Twilio Provider) - Consult the [Twilio docs][twilio_docs] for supported file types.


[llm_node]: ./pipelines/nodes.md
[twilio_docs]: https://www.twilio.com/docs/whatsapp/guidance-whatsapp-media-messages
[file-search]: ./experiment/index.md#file-search