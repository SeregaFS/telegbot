import telebot
from telebot import types


bot = telebot.TeleBot('5560815511:AAFBhVwafsLWXsGfkzoTTmG0VJ02TYfdEso')

list = ['ТСЖ Сатурн', 'УК перс']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    saturn = types.KeyboardButton()
    list[1] = types.KeyboardButton(list[1])

    markup.add(list[0], list[1])

@bot.message_handler(content_types=['text'])
def start(message):

bot.polling(none_stop=True)