# -*- coding: utf-8 -*-
from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "🏠 Добро пожаловать в Moscow Real Estate Bot!\n\n"
        "✅ Бот работает через webhook на Python 3.12.\n"
        "Отправьте любое сообщение для теста скорости."
    )

@router.message()
async def echo(message: types.Message):
    await message.reply(f"Эхо: {message.text}")