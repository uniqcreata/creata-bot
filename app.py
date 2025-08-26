import os
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load local .env when running on your PC (Render will ignore .env and use dashboard vars)
load_dotenv()

app = Flask(__name__)

# Read secrets from environment
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

# Optional (only if you actually use Telegram in this app)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Quick sanity check (helps you catch missing vars locally)
if not BYBIT_API_KEY or not BYBIT_API_SECRET:
    app.logger.warning("BYBIT_API_KEY or BYBIT_API_SECRET is not set.")

@app.get("/health")
def health():
    return jsonify(status="ok")
