
from aiogram import types


class Keyboard:

    def startmenu(self):
        list_button_name = ['Сделать скрин', '🚨 Инфо']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(*list_button_name)

        return keyboard


