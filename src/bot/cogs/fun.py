from __future__ import annotations

import os
import random

import discord
from discord.ext import commands
from discord.ext.commands import Context
from typing import TYPE_CHECKING

from bot import logger
from bot.views.choice import Choice
from bot.views.rock_paper_scissors import RockPaperScissorsView

if TYPE_CHECKING:
    from bot.discord_bot import DiscordBot


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot: DiscordBot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="coinflip",
        description="Make a coin flip, but give your bet before.",
        guild_id=os.environ["BOT__TESTING_GUILD"],
    )
    async def coinflip(self, context: Context) -> None:
        buttons = Choice()
        embed = discord.Embed(description="What is your bet?", color=0xBEBEFE)
        message = await context.send(embed=embed, view=buttons)

        await buttons.wait()  # We wait for the user to click a button.
        result = random.choice(["heads", "tails"])

        if buttons.value == result:
            embed = discord.Embed(
                description=f"Correct! You guessed `{buttons.value}` and I flipped the coin to `{result}`.",
                color=0xBEBEFE,
            )
        else:
            embed = discord.Embed(
                description=f"Woops! You guessed `{buttons.value}` and I flipped the coin to `{result}`, better luck next time!",
                color=0xE02B2B,
            )
        await message.edit(embed=embed, view=None, content=None)

    @commands.hybrid_command(
        name="rps",
        description="Play the rock paper scissors game against the bot.",
        guild_id=os.environ["BOT__TESTING_GUILD"],
    )
    async def rock_paper_scissors(self, context: Context) -> None:
        view = RockPaperScissorsView()
        await context.send("Please make your choice", view=view)


async def setup(bot) -> None:
    logger.info("Loading fun cog...")
    await bot.add_cog(Fun(bot))
