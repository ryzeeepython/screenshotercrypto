from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from dispatcher import dp
from aiogram import types


@dp.message_handler(Command('start'))
async def on_start_test(message: types.Message):
    list_button_name = ['Сделать скрин', '🚨 Инфо']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
    keyboard.add(*list_button_name)
    await message.answer('Привет, ' + str(message.from_user.full_name) + '\nЭто бот для генерации скриншотов с профитами с биржи Binance \nПросто напиши /make_screen', reply_markup=keyboard)
    