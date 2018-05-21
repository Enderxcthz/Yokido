# Yokido by Enderxcthz#1181

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='_')

@bot.event
async def on_ready():
    print ("OOMPH! I am a-ready! (loading awesome genji sound effects...)")
    print ("Booting up stupidity- " + bot.user.name)
    print ("With the random numberz: " + bot.user.id)

@bot.command(pass_context=True)
async def introduction(ctx):
    await bot.say("Konichi- ugh forget, was never an A* even at my own language! HOI OVER THERE! :wave: I am **Yokido**! The bot of all bots! (-i think, das is vat my creator told meh!) I am an *EXCULSIVE* (well not rlly :joy:) bot in EXTREME EARLY ACCESS! But judging by your facial expression, you don't care, cya bub! :wink:")
    await bot.say("Use '_help' for a list of current commands and other stuffs.")
    await bot.say("Made and scripted by Enderxcthz#1181. All rights reserved©")
    print ("User (input) Introduction Command.")

@bot.command(pass_context=True)
async def getdiscordinfo(ctx, user: discord.Member):
    await bot.say("ya boi's name is... **{}**".format(user.name))
    await bot.say("The users ID is: **{}**".format(user.id))
    await bot.say("The user's status is: **{}**".format(user.status))
    await bot.say("The user's current role is: **{}**".format(user.top_role))
    await bot.say("The user joined the fam at: **{}**".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("You kicked us {}, Now we kick you :pensive:".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def version(ctx):
    await bot.say ("Current Bot version is: `Unofficial, Still early access.`")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("You broke the rules {}, now get banned fool! :scream:".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def unban(ctx, user: discord.Member): 
    await bot.say("{} was unbanned successfully! Your welcome. :smile:".format(user.name))
    await bot.unban(user)
    
@bot.command(pass_context=True)
async def roast(ctx, user: discord.Member):
    messages = ['foo', 'bar', 'baz', 'bork']
    await bot.say(random.choice(messages))

@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(ctx.author, 'You need help? Cash me outside, HOW ABOU- no im just kidding :persevere:')
    await bot.send_message(ctx.author, 'https://hastebin.com/jazipaxeke.vbs')
    
    bot.remove_command('help')
    
    bot.run(os.environ["TOKEN"])
