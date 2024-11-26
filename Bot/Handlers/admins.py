import os
from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command,CommandObject
from Bot.Database.database import database
from dotenv import load_dotenv

admin_router = Router()
admins = [int(x) for x in os.getenv("ADMINS").split(",")]
load_dotenv()

@admin_router.message(F.from_user.id.in_(admins) and Command("show"))
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
async def test(message: Message):
    await message.answer("Список доступных команд:\n"
                        "/show id - показывает заявку по её номеру\n"
                        "/set id status - уставить статус для заявки по id")