from imaplib import IMAP4
import sqlite3
from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery, CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command,CommandStart, MagicData
from Bot.Keyboard.keyboards import Clusters, ChoiceCluster, Keyboard_clusters, ChoiceStructure, json_data
from Bot.Database.database import add_data_db

router = Router()
user_message = {}
Flag = False


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
async def platform_callback(callback: CallbackQuery, callback_data: ChoiceStructure):
    await callback.message.answer(text="Вы выбрали платформу, опишите Вашу проблему и отправьте сообщение боту")
    user_message.update(
        {"address": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["address"],
         "name": json_data[f"cluster{callback_data.cluster_number}"][callback_data.structure_number]["name"],}
    )


@router.message()
async def report(message: Message):
    if len(user_message) == 2:
        user_message.update({"message": message.text})
        await message.answer("Ваше сообещение передано в тех. поддержку")
        await add_data_db(user_message)
        user_message.clear()
    else:
        await message.answer("Вы не выбрали адрес")
