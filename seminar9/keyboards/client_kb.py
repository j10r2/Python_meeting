from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove
from seminar9.data_base import sqlite_db
from aiogram import types
import string

b1 = KeyboardButton('меню')
b2 = KeyboardButton('адрес')
b3 = KeyboardButton('режим работы')
b4 = KeyboardButton('погода')
b5 = KeyboardButton('оформить заказ')
buttons = sqlite_db.sql_read3()
mb1 = KeyboardButton(buttons[0] if len(buttons) > 0 else "")
mb2 = KeyboardButton(buttons[1] if len(buttons) > 1 else "")
mb3 = KeyboardButton(buttons[2] if len(buttons) > 2 else "")
mb4 = KeyboardButton(buttons[3] if len(buttons) > 3 else "")
mb5 = KeyboardButton(buttons[4] if len(buttons) > 4 else "")
mb6 = KeyboardButton(buttons[5] if len(buttons) > 5 else "")



# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить местоположение', request_location=True)
# reply_markup=ReplyKeyboardRemove() - удаляет клавиатуру

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(b1, b2, b3).row(b4, b5)
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(mb1, mb2).row(mb3, mb4).row(mb5, mb6)

# add(b1) добавляет с новой строки
# insert(b1) - добавляет в тот же ряд, если есть место
# kb_menu = ReplyKeyboardMarkup(resize_keyboard=True).eval(butts)


