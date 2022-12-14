from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from seminar9.create_bot import bot, dp
from seminar9.data_base import sqlite_db
from seminar9.keyboards import admin_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None
admin = 326826129

class FSM_admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def admin_check(message: types.message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "чё хочу?", reply_markup=admin_kb.button_case_admin)
    await message.delete()

async def admin_start(message: types.message):
    if message.from_user.id == ID:
        await FSM_admin.photo.set()
        await message.reply('загрузи фото')

async def cancel_handler(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state == None:
            return

        await state.finish()
        await message.reply('ok')

async def load_photo(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSM_admin.next()
        await message.reply('Введите название')

async def set_name(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSM_admin.next()
        await message.reply('Введите описание')

async def set_description(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSM_admin.next()
        await message.reply('Укажите цену')

async def set_price(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()

async def del_callback(callback: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback.data.replace('del ', ''))
    await callback.answer(text=f'{callback.data.replace("del ", "")} удалена.', show_alert=True)

async def delete_item(message: types.Message):
    # if message.from_user.id == ID:
    read = await sqlite_db.sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup()\
                               .insert(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, lambda message: "Загрузить" in message.text, state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM_admin.photo)
    dp.register_message_handler(set_name, state=FSM_admin.name)
    dp.register_message_handler(set_description, state=FSM_admin.description)
    dp.register_message_handler(set_price, state=FSM_admin.price)
    dp.register_message_handler(admin_check, commands='admin', is_chat_admin=True)
    dp.register_message_handler(delete_item, lambda message: 'Удалить' in message.text)
    dp.register_callback_query_handler(del_callback, lambda x: x.data and x.data.startswith('del '))

