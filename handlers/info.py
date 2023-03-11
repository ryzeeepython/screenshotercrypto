from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from dispatcher import dp
from aiogram import types


@dp.message_handler(Text(equals='🚨 Инфо'))
@dp.message_handler(Command('info'))
async def on_start_test(message: types.Message):  
    await message.answer('Other Projects: GitHub: https://github.com/ryzeeepython \n По всем вопросам  - @s_ryzeee')