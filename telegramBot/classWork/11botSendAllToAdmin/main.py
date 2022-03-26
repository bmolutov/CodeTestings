import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object

@bot.message_handler(content_types=['video'])
@bot.message_handler(content_types=['photo'])
def sender(message):
    if message.content_type == 'photo':
        bot.send_photo(1211502998, message.photo[0].file_id)
    else:
        bot.send_video(1211502998, message.video.file_id)
    bot.send_message(message.chat.id, 'Hehehe I forwarded everything to my master!')
# admin chat id: 1211502998
@bot.message_handler(func=lambda x: True)  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_message(message.chat.id, 'Hey, waiting for you to send a photo or video.')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
