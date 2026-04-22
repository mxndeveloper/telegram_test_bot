from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "��� Добро пожаловать в Moscow Real Estate Bot!\n\n"
        "Я помогаю находить недвижимость в Москве.\n"
        "Напишите /help для списка команд."
    )
