# Versioning

Versioning is now enabled by default for all projects on Open Chat Studio. This comes with a few important changes that modify the default behavior of the platform.

## Terms
OCS uses the following terms:

* **Working copy**. This is the version of the chatbot that exists when you click the edit button on the experiment. It can also be considered a `draft` or that it has "unsaved changes".

* **Deployed version**. This is the version that users will interact with through the web, WhatsApp or any other configured channel--including the public link.


!!! warning "Chatting to the working copy"

    The only way to chat to the working copy is through the experiment edit screen.
    Only bot authors can chat to the working copy as it is not available through channels.
    This is a change in the default behavior of the platform as prior to versioning, all
    channels chatted to the working copy at all times.

    It is on the near-term roadmap to add support for chatting to a specific version (deployed
    or not), as well as the working copy, through the API to support external evaluation of
    the chatbot.
