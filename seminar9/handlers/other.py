from seminar9.create_bot import dp
from aiogram import types, Dispatcher
import json, string

@dp.message_handler()
async def mat_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('filter.json')))) != set():
        await message.delete()
        await message.reply("А ну не матерись, сучара!")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_filter)