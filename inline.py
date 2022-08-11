from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot('TOKEN')
dp = Dispatcher(bot)

answ = dict()


#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://www.google.com/search?gs_ssp=eJzj4tFP1zc0NC5MysouT1JgNGB0YPDiudh_Ye-FLRe2Xth1sREArswNrA&q=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&oq=&aqs=chrome.0.46i39i199i362i465j35i39i362l7.28787906j0j7&sourceid=chrome&ie=UTF-8')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://yandex.ru/')
x = [InlineKeyboardButton(text='ссылка3', url='https://yandex.ru/images/?utm_source=main_stripe_big'),\
     InlineKeyboardButton(text='ссылка4', url='https://yandex.ru/images/?utm_source=main_stripe_big'),\
     InlineKeyboardButton(text='ссылка5', url='https://yandex.ru/images/?utm_source=main_stripe_big')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка2', url='https://yandex.ru/news/?utm_source=main_stripe_big'))

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='Like_1'),\
                                             InlineKeyboardButton(text='Не Like', callback_data='Like_-1'))

@dp.message_handler(commands='test')
async def url_command(message : types.Message):
    await message.answer('За видио про деплой бота, reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(collback : types.CallbackQuery):
    res = int(collback.data.split('_')[1])
    if f'{collback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await collback.answer('Вы проголосовали')
    else:
        await collback.answer('Вы уже проголосовали', show_alert=True)




executor.start_polling(dp, skip_updates=True)