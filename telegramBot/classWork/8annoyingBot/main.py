import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object


@bot.message_handler(func=lambda x: True)  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_photo(message.chat.id, 'https://learning.unv.org/pluginfile.php/243766/mod_page/content/53/Coursera-Logo.jpg', 'I learned to code here - https://www.coursera.org/. Try this!')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
