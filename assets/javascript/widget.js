document$.subscribe(function() {
  const element = document.querySelector('open-chat-studio-widget ');
  if (element) {
    let welcomeMessages = ['Hi! Welcome to our support chat.', '[Learn about this widget.](/chat_widget/)'];
    let starterQuestions = ['How do I create a bot?', 'How do I connect my bot to WhatsApp?']
    element.welcomeMessages = JSON.stringify(welcomeMessages)
    element.starterQuestions = JSON.stringify(starterQuestions)

    // Set page context for the bot
    element.pageContext = {
      page_title: document.title,
      page_path: window.location.pathname
    };
  }
})
