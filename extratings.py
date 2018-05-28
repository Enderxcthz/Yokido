import discord
from discord.ext import commands
import asyncio

    def __init__(self, bot):
         self.bot = bot

class countdown:
    """""    
        
        
@bot.command(pass_context=True)
async def countdown(interval, *, msg: str):
        await asyncio.sleep(int(interval))
        await bot.say(msg)

def setup(bot):
    bot.add_cog(countdown(bot))
