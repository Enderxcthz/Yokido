import asyncio
import contextlib
import inspect
import io
import json
import logging
import sys
import traceback

import discord
from discord.ext import commands


logging.basicConfig(level='INFO')




class Typing:
    """Keeps the bot "typing" until we leave the context."""
    def __init__(self, client, channel):
        self.client, self.channel = client, channel
        self.task = None
    
    def __enter__(self):
        if self.task:
            raise RuntimeError('Already typing')
        self.task = self.client.loop.create_task(self.talking_task())
    
    def __exit__(self, *_):
        try:
            self.task and self.task.cancel()
        except:
            traceback.print_exc()
        finally:
            self.task = None
            
    async def talking_task(self):
        while True:
            await asyncio.sleep(5)
            await self.client.send_typing(channel)
