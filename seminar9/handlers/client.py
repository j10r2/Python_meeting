from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from seminar9.create_bot import bot
from aiogram import types, Dispatcher
from seminar9.keyboards.client_kb import kb_client, kb_menu
from seminar9.data_base import sqlite_db
import requests
from aiogram.dispatcher.filters import Text
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from seminar9.handlers.admin import admin

async def cmd_start(message: types.Message):
    await message.answer("выберите действие", reply_markup=kb_client)

async def cmd_adress(message: types.Message):
    await message.answer("магазин располагается по адресу ул. Мира 9")

async def cmd_work_time(message: types.Message):
    await message.answer("пн-пт 10:00-20:00, сб-вс 9:00-21:00")#

    #https: // random - d.uk / api / random

class FSM_client(StatesGroup):
        city = State()
        order = State()
        order_name = State()
        order_num = State()
        order_repeat = State()

async def set_city(message: types.message):
    await FSM_client.city.set()
    await message.reply('введите название города: \n*для выхода наберите "отмена"')

async def cancel_handler(message: types.message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == None:
        return
    await state.finish()
    await message.reply('ok')

async def get_city(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = str(message.text)
        try:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={data['city']}\
                &appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
            weather = response.json()['weather'][0]['description']
            temp = response.json()['main']['temp']
            temp_feeling = response.json()['main']['feels_like']
            weather_message = f'погода в городе {data["city"]}:\n{weather}, температура воздуха: {temp}\
            , ощущается как: {temp_feeling}'
        except:
            weather_message = 'нет такой буквы в этом слове'
    await message.answer(weather_message)
    await state.finish()

async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

async def name_accept(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        if await name_check(message):
            data['name'] = str(message.text)
            await FSM_client.order_num.set()
            await message.answer("выберите количество")
        else:
            await message.answer('такого товара нет')

async def num_accept(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        if await num_check(message):
            data['num'] = int(message.text)
            await state.finish()
            await message.answer('заказ принят', reply_markup=ReplyKeyboardRemove())
            await bot.send_message(admin, f'поступил заказ: {data["name"]}, количество {data["num"]}, заказчик - {message.from_user.username}')
        else:
            await message.answer('введено неверное количество')


        # if repeat_check(message):
        # await message.answer(data['order'])
        # await state.finish()

async def name_check(message: types.Message):
    if message.text in sqlite_db.sql_read3():
        return True
    else: return False

async def num_check(message: types.Message):
    try:
        if int(message.text) > 0:
            return True
        else:
            return False
    except:
        return False

async def menu_sent(message: types.Message):
    await FSM_client.order_name.set()
    await message.answer('"выберите пиццу"\n*для выхода наберите "отмена"', reply_markup=kb_menu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_adress, lambda message: "адрес" in message.text)
    dp.register_message_handler(cmd_work_time, lambda message: "режим работы" in message.text)
    dp.register_message_handler(menu_command, lambda message: "меню" in message.text)
    dp.register_message_handler(set_city, lambda message: "погода" in message.text)
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(get_city, state=FSM_client.city)
    dp.register_message_handler(menu_sent, lambda message: 'оформить заказ' in message.text)
    dp.register_message_handler(name_accept, state=FSM_client.order_name)
    dp.register_message_handler(name_check, state=FSM_client.order_name)
    dp.register_message_handler(num_accept, state=FSM_client.order_num)
    dp.register_message_handler(num_check, state=FSM_client.order_num)

