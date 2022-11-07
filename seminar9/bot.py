from aiogram.utils import executor
from create_bot import dp
from handlers import other, admin, client
from data_base import sqlite_db

async def on_startup(_):
    print('bot is online')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)





# Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
