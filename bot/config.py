# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# Load .env from the current working directory
load_dotenv()

def get_env(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"❌ Missing secret: {key}. Please upload a .env file.")
    return value

BOT_TOKEN = get_env("BOT_TOKEN")
WEBHOOK_URL = get_env("WEBHOOK_URL")
WEBHOOK_SECRET = get_env("WEBHOOK_SECRET")