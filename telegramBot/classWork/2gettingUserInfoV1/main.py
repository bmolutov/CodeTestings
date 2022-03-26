import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object


@bot.message_handler(commands=['start'])  # decorator that specifies a handler
# Message is an object of Bot API, it contains info about the message
def start(message):
    bot.send_message(message.chat.id, f'I know everything about you:\n\nChat ID: {message.chat.id}\nUser ID: {message.from_user.id}\nName: {message.from_user.first_name}\nSurname: {message.from_user.last_name}\nUsername: {message.from_user.username}\n\nMessage text: {message.text}')


# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
