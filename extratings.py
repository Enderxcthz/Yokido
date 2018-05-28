import discord
from discord.ext import commands
import asyncio

class Countdown:
         def __init__(self, bot):
                self.bot = bot
         
         @commands.command(pass_context=True)
         async def countdown(self, ctx, interval, *, msg: str):
                  await asyncio.sleep(int(interval))
                  e = discord.Embed(color=0x123456, title='some title', description=msg)
                  e.set_footer(text='some text')
                  await bot.say(embed=e)

def setup(bot):
    bot.add_cog(Countdown(bot))
