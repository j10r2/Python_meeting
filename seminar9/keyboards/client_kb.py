from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove

b1 = KeyboardButton('меню')
b2 = KeyboardButton('адрес')
b3 = KeyboardButton('режим работы')
b4 = KeyboardButton('погода')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить местоположение', request_location=True)
# reply_markup=ReplyKeyboardRemove() - удаляет клавиатуру

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# add(b1) добавляет с новой строки
# insert(b1) - добавляет в тот же ряд, если есть место
kb_client.row(b1, b2, b3).add(b4)
