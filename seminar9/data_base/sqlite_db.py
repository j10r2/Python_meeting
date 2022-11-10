import sqlite3 as sq
import string
from aiogram.types import message
from seminar9.create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def sql_start():
    global base, cur
    base = sq.connect('flowers.db')
    cur = base.cursor()
    if base:
        print('есть контакт')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        print('данные добавлены')
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
    await bot.send_message(reply_markup=InlineKeyboardMarkup()\
                               .insert(InlineKeyboardButton(f'оформить заказ', callback_data='заказать')))

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()

def sql_read3():
    base = sq.connect('flowers.db')
    cur = base.cursor()
    read = cur.execute('SELECT name FROM menu').fetchall()
    buttons = [i.translate(str.maketrans('', '', string.punctuation)) for i in str(read).split(",), (")]
    return buttons
