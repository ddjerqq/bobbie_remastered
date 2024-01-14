import os
from dotenv import load_dotenv
from bot import DiscordBot

load_dotenv()

bot = DiscordBot()
bot.run(os.environ["TOKEN"])
