import telebot
from telebot import types


bot = telebot.TeleBot('5466784826:AAHtQMhMk4P-vH5qCaks8QPmhKO2P6eX3f0')

@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    vladikawkaz = types.KeyboardButton('Владикавказ')
    georgievsk = types.KeyboardButton('Георгиевск')
    stavropol = types.KeyboardButton('Ставрополь')
    doc = types.KeyboardButton('Документация')
    nevinnomissk = types.KeyboardButton('Невинномысск')
    vopros_jndtn = types.KeyboardButton('Вопрос ответ')
    markup.add(vladikawkaz, georgievsk, stavropol, doc, nevinnomissk, vopros_jndtn)

    bot.send_message(message.chat.id, 'Нажмите на интересующюю вас кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Владикавказ':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.avito.ru/vladikavkaz/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg?cd=1"))
        bot.send_message(message.chat.id, 'Результат', reply_markup=markup)
    elif message.text == 'Владикавказ':
        bot.send_message(message.chat.id, 'Работай кнопками')

    if message.text == 'Георгиевск':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.avito.ru/georgievsk/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg?cd=1"))
        bot.send_message(message.chat.id, 'Результат', reply_markup=markup)

    if message.text == 'Ставрополь':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.avito.ru/stavropol/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg?cd=1"))
        bot.send_message(message.chat.id, 'Результат', reply_markup=markup)

    if message.text == 'Невинномысск':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.avito.ru/nevinnomyssk/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg?q=%D0%BD%D0%B5%D0%B2%D0%B8%D0%BD%D0%BD%D0%BE%D0%BC%D1%8B%D1%81%D1%81%D0%BA"))
        bot.send_message(message.chat.id, 'Результат', reply_markup=markup)

    if message.text == "Документация":
        bot.send_message(message.chat.id, 'Документация по боту')
        dock = open('doc_bot.txt', 'rb')
        bot.send_document(message.chat.id, dock)



bot.polling(none_stop=True)
