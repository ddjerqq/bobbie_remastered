import os
import random
from typing import TYPE_CHECKING

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

if TYPE_CHECKING:
    from src.bot import DiscordBot


class General(commands.Cog, name="general"):
    def __init__(self, bot: DiscordBot) -> None:
        self.bot = bot
        self.context_menu_user = app_commands.ContextMenu(
            name="Grab ID",
            callback=self.grab_id
        )
        self.bot.tree.add_command(self.context_menu_user)

    async def grab_id(
            self,
            interaction: discord.Interaction,
            user: discord.User
    ) -> None:
        embed = discord.Embed(
            description=f"The ID of {user.mention} is `{user.id}`.",
            color=0xBEBEFE,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="help", description="List all commands the bot has loaded."
    )
    async def help(self, context: Context) -> None:
        prefix = os.environ["BOT__PREFIX"]
        embed = discord.Embed(
            title="Help",
            description="List of available commands:",
            color=0xBEBEFE
        )

        for name, cog in self.bot.cogs.items():
            help_text = "\n".join(
                f"{prefix}{command.name} - {command.description}"
                for command in cog.get_commands()
            )

            embed.add_field(
                name=name.capitalize(),
                value=f"```{help_text}```",
                inline=False,
            )

        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="Check if the bot is alive.",
    )
    async def ping(self, context: Context) -> None:
        embed = discord.Embed(
            title="Pong!",
            description=f"Websocket latency: {round(self.bot.latency * 1000)}ms.",
            color=0xBEBEFE,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="8ball",
        description="Ask any question to the bot.",
    )
    @app_commands.describe(question="The question you want to ask.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Ask any question to the bot.

        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "You may rely on it.",
            "Without a doubt.",
            "Yes - definitely.",
            "As I see, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again later.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{random.choice(answers)}",
            color=0xBEBEFE,
        )
        embed.set_footer(text=f"The question was: {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Get the current price of bitcoin.",
    )
    async def bitcoin(self, context: Context) -> None:
        """
        Get the current price of bitcoin.

        :param context: The hybrid command context.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript"
                    )  # For some reason the returned content is of type JavaScript
                    embed = discord.Embed(
                        title="Bitcoin price",
                        description=f"The current price is {data['bpi']['USD']['rate']} :dollar:",
                        color=0xBEBEFE,
                    )
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)


async def setup(bot) -> None:
    await bot.add_cog(General(bot))
