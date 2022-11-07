from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5543712114:AAG1J6jmyPoHNZ2URRdZXsT34EdosszGIAU")
dp = Dispatcher(bot, storage=storage)