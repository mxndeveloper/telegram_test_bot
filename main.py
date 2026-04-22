# -*- coding: utf-8 -*-
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from bot.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_SECRET
from bot.handlers import register_handlers

# ====================== LOGGING ======================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ====================== BOT & DISPATCHER ======================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
register_handlers(dp)

# ====================== LIFESPAN ======================
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Moscow Real Estate Bot...")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(
        url=WEBHOOK_URL,
        secret_token=WEBHOOK_SECRET,
        drop_pending_updates=True
    )
    logger.info(f"Webhook set successfully -> {WEBHOOK_URL}")
    yield
    logger.info("Shutting down bot...")
    await bot.session.close()

# ====================== FASTAPI APP ======================
app = FastAPI(title="Moscow Real Estate Bot", lifespan=lifespan)

@app.post("/webhook")
async def telegram_webhook(request: Request):
    # Verify secret token
    if WEBHOOK_SECRET:
        secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret != WEBHOOK_SECRET:
            logger.warning("Invalid webhook secret")
            raise HTTPException(status_code=403, detail="Forbidden")

    try:
        update_data = await request.json()
        update = Update.model_validate(update_data)
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return {"ok": False}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)