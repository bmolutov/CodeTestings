import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object


@bot.message_handler(content_types=['text'])
def text(message):
    bot.reply_to(message, "This is a text!")

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.reply_to(message, "This is a sticker!")

@bot.message_handler(content_types=['audio'])
def audio(message):
    bot.reply_to(message, "This is an audio!")

@bot.message_handler(content_types=['document'])
def document(message):
    bot.reply_to(message, "This is a document!")

@bot.message_handler(content_types=['video'])
def video(message):
    bot.reply_to(message, "This is a video!")

@bot.message_handler(content_types="photo")
def image(message):
    bot.reply_to(message, "This is a photo!")

@bot.message_handler(commands=['start'])  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_message(message.chat.id, 'I will do my best!')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
