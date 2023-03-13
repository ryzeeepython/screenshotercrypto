from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from main.main import DrawScreen
from dispatcher import dp
from aiogram import types
from main.users import Users
from states.add_member_states import add_member_states

users = Users()

@dp.message_handler(Command('add_members'))
async def on_start_test(message: types.Message):
    if users.check_is_admin(message.from_user.id):
        await message.answer('Введи user_id')
        await add_member_states.Q1.set()
    else:
        await message.answer('Ты не админ')

@dp.message_handler(state=add_member_states.Q1)
async def main(message: types.Message, state: FSMContext):
    answer = message.text
    if not(answer.startswith('/')):
        await state.finish()
        await message.answer('Все, добавил')
        users.add_member(str(answer))
        await message.answer(f'Пользователи бота:\n{users.get_members}')
    else:
        await state.finish()

