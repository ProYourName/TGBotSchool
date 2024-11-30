from email.policy import default
from idlelib.undo import Command
from pyexpat.errors import messages

from aiogram import Router,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.Keyboard.keyboards import Clusters, ChoiceCluster, Keyboard_clusters, ChoiceStructure, json_data, department, \
    ChoiceDep, BackButton
from Bot.Database.database import Database
from dotenv import load_dotenv

router = Router()
load_dotenv()
user_message = {}
database = Database("reports.db")

class Form(StatesGroup):
    admin = State()
    await_pass = State()
    choose_class = State()
    write_phone = State()
    write_FIO = State()
    write_message = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Form.await_pass)
    await message.answer("Здравствуйте! Это бот тех. поддержки сотрудников. Чтобы продолжить введите код доступа")


@router.message(Form.await_pass)
async def pass_check(message: Message, state: FSMContext):
    if message.text == "1337":
        await state.clear()
        await message.answer("Вы успешно авторизовались")
    else:
        await message.answer("Ваш пароль неверный! Повторите попытку")


@router.message(Command("report"))
async def report(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(*department)
    builder.adjust(1)
    await message.answer("Заполните данные заявки",reply_markup=builder.as_markup())

@router.callback_query(ChoiceDep.filter())
async def department_callback(callback: CallbackQuery,callback_data: ChoiceDep):
    user_message.update({"department":callback_data.department_choice})
    builder = InlineKeyboardBuilder()
    builder.add(*Clusters)
    builder.adjust(1)
    await callback.message.edit_text("Выберите вашу площадку",
                         reply_markup=builder.as_markup())

@router.callback_query(ChoiceCluster.filter())
async def cluster_callback(callback: CallbackQuery, callback_data: ChoiceCluster):
    builder = InlineKeyboardBuilder()
    builder.add(*Keyboard_clusters[callback_data.cluster_name])
    builder.adjust(1)
    user_message.update({"cluster": callback_data.cluster_number})
    await callback.message.edit_text(text=f"Вы выбрали Кластер {callback_data.cluster_number}, укажите, пожалуйста, площадку",reply_markup=builder.as_markup())

@router.callback_query(ChoiceStructure.filter())
async def platform_callback(callback: CallbackQuery, callback_data: ChoiceStructure,state: FSMContext):
    await callback.message.edit_text(text="Вы выбрали платформу, напишите Ваше ФИО")
    await state.set_state(Form.write_FIO)
    user_message.update(
        {"address": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["address"],
         "name": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["name"],
         "tg_id": callback.from_user.id,
         "cluster_number": callback_data.cluster_number}
    )


@router.callback_query(BackButton.filter())
async def back_handler(callback: CallbackQuery, callback_data: BackButton):
    if callback_data.stage == "1":
        builder = InlineKeyboardBuilder()
        builder.add(*department)
        builder.adjust(1)
        await callback.message.edit_text("Заполните данные заявки", reply_markup=builder.as_markup())
    elif callback_data.stage == "2":
        builder = InlineKeyboardBuilder()
        builder.add(*Clusters)
        builder.adjust(1)
        await callback.message.edit_text("Выберите вашу площадку",
                                         reply_markup=builder.as_markup())



@router.message(Form.write_FIO)
async def get_class(message: Message,state: FSMContext):
    user_message.update({"FIO": message.text})
    await message.answer("Напишите Ваш номер телефона")
    await state.set_state(Form.write_phone)

@router.message(Form.write_phone)
async def get_class(message: Message,state: FSMContext):
    user_message.update({"phone": message.text})
    await message.answer("Напишите номер аудитории")
    await state.set_state(Form.choose_class)

@router.message(Form.choose_class)
async def get_class(message: Message,state: FSMContext):
    user_message.update({"class_number": message.text})
    await message.answer("Напишите Ваше сообщение")
    await state.set_state(Form.write_message)


@router.message(Form.write_message)
async def report(message: Message,bot: Bot, state: FSMContext):
    user_message.update({"message": message.text})
    try:
        database.add_data(user_message)
        db_info = database.get_newest()
        await bot.send_message(chat_id=json_data[f"cluster{user_message["cluster_number"]}"][
            len(json_data[f"cluster{user_message["cluster_number"]}"]) - 1][user_message["department"]],
                            text=f"По Вашему кластеру получена новая заявка!\nНомер заявки - {db_info[0][0]}\nНомер телефона - {db_info[0][2]}\nФИО - {db_info[0][3]}\nОтдел - {db_info[0][5]}\nЗдание - {db_info[0][6]}\nАдрес - {db_info[0][7]}\nНомер аудитории - {db_info[0][8]}\nСообщение - {db_info[0][9]}\nСтатус - {db_info[0][10]}")
        await message.answer("Ваше сообещение передано в тех. поддержку")
    finally:
        user_message.clear()
        await state.clear()
        #await bot.send_message(chat_id="-4503968763",text=f"Получена новая заявка!\nОтдел - {db_info[0][3]}\nАдрес - {db_info[0][5]}\nНомер аудитории - {db_info[0][2]}\nСообщение - {db_info[0][5]}")

