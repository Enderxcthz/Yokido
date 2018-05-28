import discord
from discord.ext import commands
import asyncio

class Countdown:
         def __init__(self, bot):
                self.bot = bot
         
         @commands.command(pass_context=True)
         async def countdown(self, ctx, interval, *, msg: str):
                  await asyncio.sleep(int(interval))
                  e = discord.Embed(color=7289da, title='Countdown', description=msg)
                  e.set_footer(text='Command in BETA')
                  await bot.say(embed=e)

def setup(bot):
    bot.add_cog(Countdown(bot))
