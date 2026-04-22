# -*- coding: utf-8 -*-
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📋 Доступные команды:\n"
        "/start – главное меню\n"
        "/help – эта справка\n"
        "/test – тест скорости\n\n"
        "Также вы можете нажимать инлайн-кнопки."
    )