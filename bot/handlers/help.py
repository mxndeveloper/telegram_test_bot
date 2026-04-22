from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "��� Доступные команды:\n\n"
        "/start — Приветствие\n"
        "/help — Это сообщение\n\n"
        "Просто напишите текст — я отвечу (тестовый режим)."
    )
