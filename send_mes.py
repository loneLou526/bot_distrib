import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime
from db import Data_base
import sqlite3 as sl

with open('token.txt', 'r') as f:
    token = f.read()

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=token)
db = Data_base()

@dp.message(Command('start'))
async def hand(message: Message):
    while True:
        await asyncio.sleep(1)
        db.select()
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        if current_time in db.time:
            await bot.send_message(int(db.id[db.time.index(current_time)]), text=db.mes[db.time.index(current_time)])
            await message.answer(db.mes[db.time.index(current_time)])


@dp.message(Command('id'))
async def get_id(message: Message):
    mes = db.insert_db(message.chat.full_name, message.chat.id)
    await message.answer(mes)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())