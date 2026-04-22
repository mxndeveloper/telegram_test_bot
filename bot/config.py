import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("API_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "my_bot_secret_2026")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN missing")
if not WEBHOOK_URL:
    raise RuntimeError("WEBHOOK_URL missing")