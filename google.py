import discord
import asyncio
import re
from discord.ext.commands import Bot
from discord.ext import commands
from google import google

@commands.command(aliases=['google'])
	async def g(self, ctx, *, query):
		num_page = 1
		search_results = google.search(query, num_page)
		em = discord.Embed(title='Google Search', colour=0xff0000)
		em.add_field(name=search_results[0].name, value=search_results[0].description)
		em.add_field(name='Link', value=search_results[0].link)
		msg = await ctx.send(embed=em)
		await msg.add_reaction('◀')
		await msg.add_reaction('▶')
		count = 0
		def check(r, m):
			return m == ctx.author and r.emoji in ["▶", "◀"]
		while True:
			try:
				timeoutlen = 10*60
				reaction, member = await self.bot.wait_for('reaction_add', check=check, timeout=timeoutlen)
			except asyncio.TimeoutError:
				break
			
			if reaction.emoji == '▶':
				count = count + 1
				if count > 6:
					await msg.remove_reaction('▶', ctx.author)
					count = count - 1
				def limit(count, minimum=0, maximum=6):
					return max(min(count, maximum), minimum)
				await msg.remove_reaction('▶', ctx.author)
				em.set_field_at(0, name=search_results[count].name, value=search_results[count].description)
				em.set_field_at(1, name='Link', value=search_results[count].link)
				await msg.edit(embed=em)
			if reaction.emoji == '◀':
				count = count-1
				if count < 0:
					await msg.remove_reaction('◀', ctx.author)
					count = count + 1
				def limit(count, minimum=0, maximum=7):
					return max(min(count, maximum), minimum)
				await msg.remove_reaction('◀', ctx.author)
				em.set_field_at(0, name=search_results[count].name, value=search_results[count].description)
				em.set_field_at(1, name='Link', value=search_results[count].link)
				await msg.edit(embed=em)
                                
