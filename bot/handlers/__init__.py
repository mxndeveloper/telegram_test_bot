# -*- coding: utf-8 -*-
from aiogram import Dispatcher
from .start import router as start_router
from .help import router as help_router
from .echo import router as echo_router
from .real_estate import router as real_estate_router

def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(echo_router)
    dp.include_router(real_estate_router)