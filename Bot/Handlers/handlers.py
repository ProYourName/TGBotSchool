from email.policy import default
from imaplib import IMAP4
import sqlite3
from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery, CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command,CommandStart, MagicData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.Keyboard.keyboards import Clusters, ChoiceCluster, Keyboard_clusters, ChoiceStructure, json_data
from Bot.Database.database import add_data_db

router = Router()
user_message = {}

class Form(StatesGroup):
    choose_class = State()
    write_message = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(*Clusters)
    builder.adjust(1)
    await message.answer("Здравствуйте! Это бот тех. поддержки, выберите вашу площадку", reply_markup=builder.as_markup())

@router.callback_query(ChoiceCluster.filter())
async def cluster_callback(callback: CallbackQuery, callback_data: ChoiceCluster):
    builder = InlineKeyboardBuilder()
    builder.add(*Keyboard_clusters[callback_data.cluster_name])
    builder.adjust(1)
    await callback.message.answer(text=f"Вы выбрали Кластер {callback_data.cluster_number}, укажите, пожалуйста, площадку",reply_markup=builder.as_markup())

@router.callback_query(ChoiceStructure.filter())
async def platform_callback(callback: CallbackQuery, callback_data: ChoiceStructure,state: FSMContext):
    await callback.message.answer(text="Вы выбрали платформу, напишите номер аудитории")
    await state.set_state(Form.choose_class)
    user_message.update(
        {"address": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["address"],
         "name": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["name"],}
    )

@router.message(Form.choose_class)
async def get_class(message: Message,state: FSMContext):
    user_message.update({"class_number": message.text})
    await message.answer("Теперь опишите вашу проблему")
    await state.set_state(Form.write_message)

@router.message(Form.write_message)
async def report(message: Message,bot: Bot):
    user_message.update({"message": message.text})
    await message.answer("Ваше сообещение передано в тех. поддержку")
    #await add_data_db(user_message)
    await bot.send_message(chat_id="-4503968763",text=f"Получена новая заявка!\nАдрес - {user_message["address"]}\nНомер аудитории - {user_message["class_number"]}\nСообщение - {user_message["message"]}")
    user_message.clear()

