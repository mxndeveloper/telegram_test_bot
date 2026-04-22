# -*- coding: utf-8 -*-
import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("API_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # this is the user-defined one that persists

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment")
if not WEBHOOK_URL:
    raise ValueError("WEBHOOK_URL not found in environment")
if not WEBHOOK_SECRET:
    # optional, but you set it, so it should exist
    print("Warning: WEBHOOK_SECRET not set")