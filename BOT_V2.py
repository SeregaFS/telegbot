import telebot
from telebot import types

a = ['СП 11-103-97']

bot = telebot.TeleBot('5560815511:AAFBhVwafsLWXsGfkzoTTmG0VJ02TYfdEso')


bot.message_handler()
def website(message):
    if message.text(a):
        marckap.types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, "Искомый документ", url="https://docs.cntd.ru/document/901704792")
        bot.send_message(message.chat.id, 'ddfgh')
















bot.polling(none_stop=True)