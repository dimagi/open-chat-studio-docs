This page provides an overview of how to utilize surveys in your OCS chatbot.

### What are Surveys on Open Chat Studio?

The Surveys feature allows chatbot makers to give users a link to a Google form (or any other link to a survey), both at the start and end of an OCS chatbot web session. 

!!! info "External Channel Survey Limitations & Workarounds"
    Surveys will not be automatically presented to the user before or after the chat if you deploy your chatbot on external channels like WhatsApp or Telegram. If you would still like to capture pre- or post-survey questions using these channels, you can: 

    - Incorporate survey questions in your prompt and structuring the prompt such that the chatbot starts and ends with questions as you would like it to. 
    - Send users links to a Google form or other kind of survey directly, before or after providing them with the link to the chatbot. 



**Example of a pre-survey when using an OCS bot on the web**
![image](../assets/images/survey1.png)


**Example of a post-survey when using an OCS bot on the web**
![image](../assets/images/survey2.png)
![image](../assets/images/survey3.png)

### Create a Survey

The very first step is to create a survey and generate a web link for that survey. For example, you might use [Google forms](#using-google-forms) to create pre- and post-surveys. Once this step is complete, navigate to the "Surveys" option on the left-hand menu on Open Chat Studio and follow the steps given below to add your survey(s) to a chatbot. 

#### Select "Add New". 

Name: This is a name for you or your team members on OCS to identify different surveys.
- URL: Add the URL of your survey. 
- Confirmation text: This is the text a user sees when they see the link to the survey, before they begin to use the chatbot. You can edit this text as you'd like. Here, it's also important to add the following text such that the bot knows to reference the URL you've added: Survey link: {survey_link}. 

**Example**
> Before starting the experiment, we ask that you complete a short survey. Please click on the survey link, fill it out, and, when you have finished, select the checkbox to confirm you have completed it. Survey link: {survey_link}. 

If you would like to include both a pre-survey and a post-survey, repeat the above process for each survey.

### Final Step

Now edit your chatbot and choose which survey to use as the pre- or post survey.



## Using Google Forms
Go to [Google Forms][google_forms] and create your form. In order to link a particular participant, session and experiment with a specific form, you'll need to include questions with the titles "Participant ID", "Session ID" and "Experiment ID".

For example:
![image](../assets/images/survey6.png)

From here, click on the 3 dots in the top right corner and go to "Get Prefilled Link". Now fill in the fields that you want prefilled. In this case, "Participant ID", "Session ID" and "Experiment ID".

![image](../assets/images/survey7.png)
When you click on "Get Link", you'll get a link that looks something like:

> https://docs.google.com/forms/some/uri/viewform?usp=pp_url&entry.1118764343=participant&entry.791635770=session&entry.784126073=experiment

Replace the sections in the URL as follows:

- participant -> {participant_id}
- session -> {session_id}
- experiment -> {experiment_id}

This will result in a link that looks like this:

> https://docs.google.com/forms/some/uri/viewform?usp=pp_url&entry.1118764343={participant_id}&entry.791635770={session_id}&entry.784126073={experiment_id}


This new link should be used for your survey link.


[google_forms]: https://docs.google.com/forms