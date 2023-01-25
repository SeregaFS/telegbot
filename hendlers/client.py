from aiogram import types, Dispatcher
from cret_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# **************************************КЛИЕНТСКАЯ ЧАСТЬ*********************************************************
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выберите интересующую вас информацию', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС:\nhttps://t.me/NormDockBot')

#@dp.message_handler(commands=['Режим_работы_заведения'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

#@dp.message_handler(commands=['Адрес и телефон'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. 50 Лет ВЛКСМ 22 8 8002000600')

#@dp.message_handler(commands=['МЕНЮ'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы_заведения'])
    dp.register_message_handler(pizza_place_command, commands=['Адрес'])
    dp.register_message_handler(pizza_menu_command, commands=['МЕНЮ'])


