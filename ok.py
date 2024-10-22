from modules._config import TOKEN, bot
from modules._helpers import load_modules
from modules.custdl import file_server
import asyncio
from web import keep_alive

bot.start(bot_token=TOKEN)

load_modules()
asyncio.ensure_future(file_server())

bot.run_until_disconnected()
if __name__ == "__main__":
    keep_alive()
