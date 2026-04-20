from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message):
    """Simple echo for testing. Will be replaced with real estate logic later."""
    await message.answer(f"Вы написали: {message.text}\n\n(Это тестовый эхо-ответ)")
