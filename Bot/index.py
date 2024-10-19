import asyncio
import sys
import logging
import json
from Bot.Keyboard.keyboards import Keyboard_cluster1, Clusters
from Keyboard import keyboards
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder

from config import TOKEN



dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(*Clusters)
    builder.adjust(1)
    await message.answer("Здравствуйте! Это бот тех. поддержки, выберите вашу площадку", reply_markup=builder.as_markup())



@dp.callback_query(F.data == "cl1")
async def my_callback_foo(callback: CallbackQuery, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(*Keyboard_cluster1)
    await callback.message.answer(text="Вы выбрали Кластер 1, укажите, пожалуйста, площадку",reply_markup=builder.as_markup())



@dp.message(Command('test'))
async def cmd_start(message: Message):
    await message.answer("Привет")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())