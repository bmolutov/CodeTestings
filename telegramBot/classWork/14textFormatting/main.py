import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object


@bot.message_handler(commands=['start'])  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_message(message.chat.id, 'Text formatting')
    bot.send_message(message.chat.id, '<b>Bold text</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<i>Italic text</i>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<u>Underlined text</u>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<s>Striked text</s>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<a href="https://www.coursera.org/">HyperLink</a>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<code>print(\'I will do my best!\')</code>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<tg-spoiler>Spoiler text</tg-spoiler>', parse_mode='HTML')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
