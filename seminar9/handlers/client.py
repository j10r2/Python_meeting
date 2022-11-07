from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from seminar9.create_bot import dp
from aiogram import types, Dispatcher
from seminar9.keyboards import kb_client
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from seminar9.data_base import sqlite_db
import requests
from aiogram.dispatcher.filters import Text


# users_lib = [['m_p_EAST', 'botty'],['pnh','lll']]

# @dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    # if message.from_user.username in users_lib[0]:
    #     await message.answer(str(users_lib[1][users_lib[0].index(message.from_user.username)]), reply_markup=kb_client)
    # else: "Приветствую в чате нашего магазина, выберите команду:\n /adress\n /work_time"
    await message.answer("выберите действие", reply_markup=kb_client)

async def cmd_adress(message: types.Message):
    await message.answer("магазин располагается по адресу ул. Мира 9")

async def cmd_work_time(message: types.Message):
    await message.answer("пн-пт 10:00-20:00, сб-вс 9:00-21:00")#, reply_markup=ReplyKeyboardRemove()

# async def cmd_weather(message: types.Message):
#     name = input("Введите название города: ")
#     response = requests.get(
#         f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
#     weather = response.json()['weather'][0]['description']
#     temp = response.json()['main']['temp']
#     temp_feeling = response.json()['main']['feels_like']
#     weather_message = f'погода в городе {name}:\n{weather}, температура воздуха - {temp}, ощущается как {temp_feeling}'
#     print(weather_message)
#     await message.answer("пн-пт 10:00-20:00, сб-вс 9:00-21:00")

    #https: // random - d.uk / api / random

class FSM_weather(StatesGroup):
        city = State()

async def set_city(message: types.message):
    await FSM_weather.city.set()
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
                f"http://api.openweathermap.org/data/2.5/weather?q={data['city']}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
            weather = response.json()['weather'][0]['description']
            temp = response.json()['main']['temp']
            temp_feeling = response.json()['main']['feels_like']
            weather_message = f'погода в городе: {data["city"]}:\n{weather}, температура воздуха: {temp}, ощущается как: {temp_feeling}'
        except:
            weather_message = 'нет такой буквы в этом слове'
    await message.answer(weather_message)
    await state.finish()

    # @dp.message_handler(regexp='привет')
async def msg_handler(message: types.Message):
    await message.answer(f"И вам здравствуйте, {message.from_user.first_name}")

async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_adress, lambda message: "адрес" in message.text)
    dp.register_message_handler(cmd_work_time, lambda message: "режим работы" in message.text)
    dp.register_message_handler(menu_command, lambda message: "меню" in message.text)
    dp.register_message_handler(set_city, lambda message: "погода" in message.text)
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(get_city, state=FSM_weather.city)

