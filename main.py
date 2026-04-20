import os
import logging
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI, Request, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.exceptions import TelegramAPIError

# Load environment
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("BOT_TOKEN and WEBHOOK_URL are required in .env file")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize Bot and Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Import handlers (they will register themselves)
from bot.handlers import start, echo, real_estate, register_handlers
register_handlers(dp)

# Lifespan for clean startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("��� Bot starting...")
    # Delete old webhook and set new one
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(
        url=WEBHOOK_URL,
        secret_token=WEBHOOK_SECRET,
        drop_pending_updates=True
    )
    logger.info(f"✅ Webhook successfully set to: {WEBHOOK_URL}")
    yield
    # Shutdown
    logger.info("��� Shutting down bot...")
    await bot.session.close()

# Create FastAPI app
app = FastAPI(title="Moscow Real Estate Bot", lifespan=lifespan)

# Webhook endpoint
@app.post("/webhook")
async def telegram_webhook(request: Request):
    if WEBHOOK_SECRET:
        secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret != WEBHOOK_SECRET:
            logger.warning("Invalid webhook secret received")
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
