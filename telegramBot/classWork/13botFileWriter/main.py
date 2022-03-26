import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object

@bot.message_handler(commands=['start'])  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_message(message.chat.id, 'Hey, how is it going?')

@bot.message_handler(content_types=['text'])
def writer(message):
    with open('inputMessage.txt', 'w') as f:
        f.write(message.text)
    with open('inputMessage.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)
    # bot.send_message(message.chat.id, message.text)

# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
