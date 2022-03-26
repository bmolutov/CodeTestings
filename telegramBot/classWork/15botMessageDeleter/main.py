import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object


@bot.message_handler(func=lambda x: True)
def deleter(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'I have deleted your message!')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
