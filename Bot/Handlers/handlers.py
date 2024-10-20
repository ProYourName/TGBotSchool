from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command,CommandStart
from Bot.Keyboard.keyboards import Clusters,Keyboard_cluster1

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(*Clusters)
    builder.adjust(1)
    await message.answer("Здравствуйте! Это бот тех. поддержки, выберите вашу площадку", reply_markup=builder.as_markup())

@router.callback_query(F.data == "cl1")
async def my_callback_foo(callback: CallbackQuery, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(*Keyboard_cluster1)
    await callback.message.answer(text="Вы выбрали Кластер 1, укажите, пожалуйста, площадку",reply_markup=builder.as_markup())

@router.message(Command('test'))
async def cmd_start(message: Message):
    await message.answer("Привет")
