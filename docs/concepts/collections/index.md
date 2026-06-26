# Collections

A collection is a group of files you can attach to a chatbot to give it access to content. There are two types of collections:

- [Media collection](./media.md)
- [Indexed Collection (for RAG applications)](./indexed.md)

## Adding a collection to a chatbot

Navigate to the **Collections** section in the sidebar and click "Add new". Once the collection is created, you will be able to upload files to it.

After your collection has been created and populated with files, you can link it to any [LLM node][llm_node].

## Collections and published chatbots

Collection content is a **live shared resource**. When you update the files in a collection — either manually or through a scheduled document-source sync — those changes are reflected in your published chatbot automatically. You do not need to republish to pick up new or updated files.

This means:

- Adding or removing files from a media collection takes effect for users immediately.
- Document-source syncs to a RAG index collection (for example, nightly Confluence or GitHub syncs) are applied to the published chatbot as each sync completes.

The *structure* of a published version — which collections are linked to which pipeline nodes — is still frozen at publish time. To change which collections a chatbot uses, you must publish a new version.

For more detail on how versioning interacts with collections, see [Versioning](../versioning.md#what-is-frozen-and-what-is-live).

## How are attachments sent?
Whenever your chatbot references a particular file or document, it will be sent to the user as an attachment. Depending on the channel, attachments are delivered in different ways.

### Web channels
Attachments are directly downloadable by clicking on them.

### Multimedia-unsupported channels
By default, attachments are sent as download links appended to the chatbot's message. The user will see the file name and a corresponding download link at the end of the message. These channels do not yet support sending multimedia files:

* Telegram
* WhatsApp (Turn.io provider)
* SureAdhere
* Facebook Messenger
* Slack

### Multimedia-supported channels
Channels that support sending multimedia files will receive each attachment as a separate message, following the chatbot's initial response. If a file type is not supported by the channel, or the file size exceeds the allowed limit, a download link will be appended to the chatbot's message instead. These channels support sending multimedia files:

* API - See the [API documentation](https://openchatstudio.com/api/v1/docs/#tag/Channels/operation/new_api_message) for more information
* WhatsApp (Twilio Provider) - Consult the [Twilio docs][twilio_docs] for supported file types.

[llm_node]: ../pipelines/nodes.md
[twilio_docs]: https://www.twilio.com/docs/whatsapp/guidance-whatsapp-media-messages
