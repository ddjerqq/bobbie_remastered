from __future__ import annotations
import os
from dotenv import load_dotenv
from bot import DiscordBot

load_dotenv()

bot = DiscordBot()
bot.run(os.environ["BOT__TOKEN"])
