import discord
from discord.ext import commands
import asyncio

async def countdown(interval, *, msg: str):
        await asyncio.sleep(int(interval))
        await bot.say(msg)
