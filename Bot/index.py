import asyncio
import sys,os
import logging
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from Bot.Handlers.handlers import router
from Bot.Handlers.admins import admin_router
from dotenv import load_dotenv

dp = Dispatcher()

async def main():
    load_dotenv()
    dp.include_router(router)
    dp.include_router(admin_router)
    bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())