from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery, CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command,CommandStart, MagicData
from Bot.Keyboard.keyboards import Clusters, ChoiceCluster, Keyboard_clusters

router = Router()

print()
@router.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(*Clusters)
    builder.adjust(1)
    await message.answer("Здравствуйте! Это бот тех. поддержки, выберите вашу площадку", reply_markup=builder.as_markup())

@router.callback_query(ChoiceCluster.filter())
async def my_callback_foo(callback: CallbackQuery, callback_data: ChoiceCluster):
    builder = InlineKeyboardBuilder()
    builder.add(*Keyboard_clusters[callback_data.cluster_name])
    builder.adjust(1)
    await callback.message.answer(text=f"Вы выбрали Кластер {callback_data.cluster_number}, укажите, пожалуйста, площадку",reply_markup=builder.as_markup())


