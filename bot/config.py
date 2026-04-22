import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug: print all environment variables (remove after testing)
logger.info("=== Environment variables ===")
for key, value in os.environ.items():
    if "TOKEN" in key or "URL" in key or "DOMAIN" in key:
        logger.info(f"{key}={value[:20] if value else ''}...")

# BOT_TOKEN: try multiple possible keys
BOT_TOKEN = (
    os.getenv("BOT_TOKEN") or
    os.getenv("API_TOKEN") or
    os.getenv("TELEGRAM_BOT_TOKEN") or
    os.getenv("TOKEN")
)

# WEBHOOK_URL: construct from DOMAIN if not set directly
domain = os.getenv("DOMAIN")
webhook_url_from_env = os.getenv("WEBHOOK_URL")

if webhook_url_from_env:
    WEBHOOK_URL = webhook_url_from_env
elif domain:
    WEBHOOK_URL = f"https://{domain}/webhook"
else:
    # Fallback to hardcoded domain (last resort)
    WEBHOOK_URL = "https://bot-1776854668-5130-wisdomica-info-gmail.bothost.tech/webhook"

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "my_bot_secret_2026")

# Validation
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not found in environment (tried BOT_TOKEN, API_TOKEN, TELEGRAM_BOT_TOKEN, TOKEN)")
if not WEBHOOK_URL:
    raise RuntimeError("WEBHOOK_URL could not be determined")

logger.info(f"BOT_TOKEN = {BOT_TOKEN[:10]}...")
logger.info(f"WEBHOOK_URL = {WEBHOOK_URL}")
logger.info(f"WEBHOOK_SECRET = {'*' * len(WEBHOOK_SECRET)}")