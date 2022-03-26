from multiprocessing.dummy import current_process
import telebot  # importing our main library pyTelegramBotAPI for creating bot

bot = telebot.TeleBot('5235401470:AAF19nx1kXfZF99nbD3YkIDR9zZSfVJ_lFY')  # creating a new object

@bot.message_handler(commands=['change'])
def change(message):
    edited_message = bot.edit_message_text(chat_id=message.chat.id, message_id=prev_message.id, text='Hey Admin!')
    bot.send_message(message.chat.id, edited_message.text)

@bot.message_handler(commands=['start'])
def start(message):
    global prev_message
    prev_message = bot.send_message(message.chat.id, 'Hey User!')

# checks user input and gives specific answer
# gives all user input to handlers for further processing
# depending on user input only one function is chosed for executing line in if/elif/else structure
# it checks commands, and depending on them it chooses specific function for executing
# it checks from upside to downside
bot.polling()
