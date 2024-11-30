import os
import openpyxl
from aiogram import Router,F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command,CommandObject
from Bot.Database.database import Database
from dotenv import load_dotenv
from Bot.Keyboard.keyboards import department

admin_router = Router()
admins = [int(x) for x in os.getenv("ADMINS").split(",")]
load_dotenv()
database = Database("reports.db")

@admin_router.message(F.from_user.id.in_(admins) and Command("show"))
async def test(message: Message, command: CommandObject):
    print(command.args)
    if command.args is None:
        await message.answer("Не заданы нужные аргументы")
    elif " " in command.args:
        await message.answer("Слишком много аргументов")
    else:
        db_info = database.get_data_by_id(str(command.args))
        print(db_info)
        if not db_info:
            await message.answer("Такой заявки не существует")
        else:
            await message.answer(f"Номер заявки - {db_info[0][0]}\nНомер телефона - {db_info[0][2]}\nФИО - {db_info[0][3]}\nОтдел - {db_info[0][5]}\nЗдание - {db_info[0][6]}\nАдрес - {db_info[0][7]}\nНомер аудитории - {db_info[0][8]}\nСообщение - {db_info[0][9]}\nСтатус - {db_info[0][10]}")

@admin_router.message(F.from_user.id.in_(admins) and Command("set"))
async def test(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer("Не заданы нужные аргументы")
    elif " " not in command.args:
        await message.answer("Слишком мало аргументов")
    else:
        index,status = command.args.split(" ")
        database.update_status(index,status)

@admin_router.message(F.from_user.id.in_(admins) and Command("showcommands"))
async def show_commands(message: Message):
    await message.answer("Список доступных команд:\n"
                        "/show id - показывает заявку по её номеру\n"
                        "/set id status - уставить статус для заявки по id")


