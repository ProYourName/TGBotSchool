import os
from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery, CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command, CommandStart, MagicData, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.Keyboard.keyboards import Clusters, ChoiceCluster, Keyboard_clusters, ChoiceStructure, json_data, department, \
    ChoiceDep
from Bot.Database.database import database
from dotenv import load_dotenv

admin_router = Router()
admins = [int(x) for x in os.getenv("ADMINS").split(",")]
load_dotenv()

@admin_router.message(F.from_user.id.in_(admins) and Command("show_status"))
async def test(message: Message, command: CommandObject):
    print(command.args)
    if command.args is None:
        await message.answer("Не заданы нужные аргументы")
    elif " " in command.args:
        await message.answer("Слишком много аргументов")
    else:
        db_info = database.get_data_by_id(str(command.args))
        if not db_info:
            await message.answer("Такой заявки не существует")
        else:
            await message.answer(f"Номер заявки - {db_info[0][0]}\nОтдел - {db_info[0][3]}\nАдрес - {db_info[0][4]}\nНомер аудитории - {db_info[0][2]}\nСообщение - {db_info[0][5]}\nСтутус - {db_info[0][6]}")




