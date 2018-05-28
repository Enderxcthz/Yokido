import discord
from discord.ext import commands
import asyncio

class Countdown:
         def __init__(self, bot):
                self.bot = bot
         
         @commands.command(pass_context=True)
         async def countdown(self, ctx, interval, *, msg: str):
                  await asyncio.sleep(int(interval))
                  await self.bot.say(msg)


def setup(bot):
    bot.add_cog(Countdown(bot))
