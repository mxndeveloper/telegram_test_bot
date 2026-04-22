# -*- coding: utf-8 -*-
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

router = Router()

WELCOME_TEXT = (
    "🏠 Добро пожаловать в Moscow Real Estate Bot!\n\n"
    "🇬🇧 Welcome to Moscow Real Estate Bot!\n\n"
    "Я тестовый помощник по недвижимости в Москве.\n"
    "Нажмите кнопку ниже или отправьте любое сообщение, чтобы проверить скорость ответа.\n\n"
    "📌 Команды:\n"
    "/start – показать это меню\n"
    "/help – список команд\n"
    "/test – измерить задержку"
)

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔍 Квартиры", callback_data="show_flats"),
            InlineKeyboardButton(text="💰 Цены", callback_data="prices")
        ],
        [
            InlineKeyboardButton(text="⏱ Тест скорости", callback_data="speed_test"),
            InlineKeyboardButton(text="📞 Контакты", callback_data="contact")
        ]
    ])

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(WELCOME_TEXT, reply_markup=get_main_keyboard())

@router.message(Command("test"))
async def cmd_test(message: types.Message):
    start = time.time()
    await message.reply("⏳ Измеряю задержку...")
    elapsed = (time.time() - start) * 1000
    await message.answer(f"✅ Ответ через {elapsed:.0f} мс")

@router.callback_query(F.data == "show_flats")
async def show_flats(callback: types.CallbackQuery):
    await callback.answer("🔍 Загружаю...")
    await callback.message.answer(
        "📍 Примеры квартир в Москве:\n"
        "• 1-к., 45 м², м. Новослободская – 15 млн ₽\n"
        "• 2-к., 68 м², м. Фили – 22 млн ₽\n"
        "• Студия, 28 м², м. Дмитровская – 8.5 млн ₽\n\n"
        "Тестовые данные – скорость ответа ~0.2 сек"
    )

@router.callback_query(F.data == "prices")
async def show_prices(callback: types.CallbackQuery):
    await callback.answer("💰 Цены")
    await callback.message.answer(
        "💰 Средние цены на жильё в Москве (апрель 2026):\n"
        "• Эконом: 250–350 тыс. ₽/м²\n"
        "• Бизнес: 400–600 тыс. ₽/м²\n"
        "• Элитная: от 800 тыс. ₽/м²"
    )

@router.callback_query(F.data == "speed_test")
async def speed_test_callback(callback: types.CallbackQuery):
    start = time.time()
    await callback.answer("⏱ Тест...")
    elapsed = (time.time() - start) * 1000
    await callback.message.answer(f"⚡️ Время ответа: {elapsed:.0f} мс (отлично)")

@router.callback_query(F.data == "contact")
async def contact(callback: types.CallbackQuery):
    await callback.answer("📞 Связь")
    await callback.message.answer(
        "📞 Связь с агентом: @your_support_bot\n"
        "☎️ Телефон: +7 (495) 123-45-67"
    )

# Echo for any text (proves bot is alive)
@router.message(F.text)
async def echo_message(message: types.Message):
    await message.reply(
        f"✅ Вы написали: «{message.text[:50]}»\n"
        "Используйте /start для меню."
    )