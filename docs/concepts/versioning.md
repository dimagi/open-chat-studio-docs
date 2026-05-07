# Versioning

Versioning keeps your live chatbot stable while you make changes. You can edit and test your chatbot without impacting your users. For more details, see the tutorial on [creating and publishing versions](../tutorials/versioning_steps.md).

Versioning tracks the history of your chatbot's configuration so you can review what changed, and roll back to a previous version if needed.


## Terminology

* *Unreleased Version*. This is the version of the chatbot you are currently editing. It is a draft that has not been versioned or published.

* *Published Version*. This is the version that users will interact with — through the web, WhatsApp, or any other channel you have set up, including the public link.

## What is a Chatbot Version?

Once a version is created, it cannot be edited or modified. This ensures that the users' experience remains stable even if chatbot editors are changing the unreleased version.

## Chatting to the unreleased version
For testing, if you want to chat with the unreleased draft chatbot, go to the chatbot home page and click the speech bubble icon in the top-right corner. In the dropdown, select "Unreleased Version" instead of "Published Version" to open a web chat. 

When chatting with an unpublished version, a banner will appear indicating that it is not the published version and showing the version number.

![Web chat unpublished version banner](images/version_web_chat.png)

Only bot editors can chat with the unreleased version because it is not available through [channels](channels.md). 

!!! note "Behavior before versioning"
    Previously, all channels always used the unreleased version.

## Changing the Published Version
The published version can be selected from any of the Chatbot versions, enabling rollback to a previous version.
Only one version can be the published version at a time.

To publish a version, follow the tutorial on [creating and publishing versions](../tutorials/versioning_steps.md).


## Versioning for OpenAI Assistants

!!! info "Versioning chatbots that use OpenAI Assistants"
    Yes, this is supported. When a new version is saved for a chatbot that uses an OpenAI Assistant, a snapshot copy of that assistant is automatically created — no extra setup needed. The original assistant remains available and can still be updated in the unreleased version.

!!! warning "Modifying Assistants in OpenAI referenced by released versions"

    As mentioned above, the copied assistant will be read-only in OCS, however, in OpenAI changes can still be made to that copy of the assistant. *We recommend advising your team to not modify this assistant if it references a released version.* This can cause unexpected behavior to the version and to its end users. To ensure that the released version acts as expected this assistant should remain as-is.
