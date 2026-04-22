# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# Load .env only if it exists (local development)
load_dotenv()

def get_env(key: str, required: bool = True) -> str:
    """Get environment variable, first from os.environ, then from .env."""
    value = os.environ.get(key) or os.getenv(key)
    if required and not value:
        raise ValueError(f"{key} is not set in environment or .env file")
    return value

BOT_TOKEN = get_env("BOT_TOKEN")
WEBHOOK_URL = get_env("WEBHOOK_URL")
WEBHOOK_SECRET = get_env("WEBHOOK_SECRET", required=False)  # optional

# Optional: set a default secret if missing
if not WEBHOOK_SECRET:
    WEBHOOK_SECRET = "default_insecure_secret_change_me"