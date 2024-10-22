import logging
import sqlite3
import time
from logging import INFO, basicConfig, getLogger, handlers
from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from telethon import TelegramClient

basicConfig(
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    level=INFO,
)

handler = handlers.RotatingFileHandler(
    "logs.txt", maxBytes=10 * 1024 * 1024, backupCount=10
)
handler.setLevel(INFO)
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
)
getLogger("").addHandler(handler)


StartTime = time.time()
help_dict = {}

# Load .env file
load_dotenv()

log = getLogger("- valeri ->")
# Environment variables
TOKEN ="1203800025:AAGNkcUH64WACiROGxpnU4YvJNDnVqFb5v0"
API_KEY =2118051
API_HASH ="1d9d2bf8fdbfe48da2daa8ca1de1ee65"
MONGO_DB = "mongodb+srv://21101054:<db_password>@sht.1vfs6.mongodb.net/?retryWrites=true&w=majority&appName=sht"
OWNER_ID =952735084
TMDB_KEY ="e547e17d4e91f3e62a571655cd1ccaff"
OPENAI_API_KEY ="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"

# clients
bot = TelegramClient(
    "bot", api_id=API_KEY, api_hash=API_HASH, device_model="iPhone XS", lang_code="en"
)

if MONGO_DB != "":
    log.info("Using MongoDB database")
    db = MongoClient(MONGO_DB, connect=True)
else:
    log.info("Using SQLite database")
    db = sqlite3.connect("bot.db")
