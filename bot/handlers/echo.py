# -*- coding: utf-8 -*-
from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

# This will be overridden by start.py's catch‑all, but kept for consistency
@router.message(F.text, ~Command("start", "help", "test"))
async def echo_all(message: types.Message):
    await message.reply(f"Эхо: {message.text}")