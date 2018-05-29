# Yokido by Enderxcthz#1181

import discord
from discord.ext import commands
import asyncio
import os
from discord.utils import find
import random

bot = commands.Bot(command_prefix='_')

@bot.event
async def on_ready():
    print ("OOMPH! I am a-ready! (loading awesome genji sound effects...)")
    print ("Booting up stupidity- " + bot.user.name)
    print ("With the random numberz: " + bot.user.id)

bot.load_extension('extratings')
bot.load_extension('voting')
    

@bot.event
async def on_ready(): 
    await bot.change_presence(game=discord.Game(name=" with over {} servers!".format(len(bot.servers))))
    print("Successfully changed bot status!" + bot.user.name)
   
 
    
@bot.event
async def on_server_join(server):
    try:
        channel = find(lambda x: x.name == 'general',  server.text_channels)
    except:
        channel = server.default_channel
    else:
        print('Can\'t send message in {}. Please send owner error report.'.format(server))
    
    if channel and channel.permissions_for(server.me).send_messages:
        
        await channel.send('Salutations {}! I have been waiting to join you (no not rlly) hehehe. [IF I HAVE BEEN INVITED TO YOUR SERVER THAT MEANS THAT YOUR SERVER IS SPECIAL! :O] But why :thinking: ?'.format(ctx.message.server.name))
        await channel.send('Yokido (MEEE >_<) Is an extremley early alpha access bot, availible only to a few people: -The devs close friends & -The three lucky sponsors.'.format(ctx.message.server.name))
        await channel.send('So wait! What does that mean? IS MY OWNER THE FRIEND OF THE DEV AND I CAN USE HIM TO ACCESS EVERYTHING OMG (answer: no, tbh no-one really cares :joy:)'.format(ctx.message.server.name))
        await channel.send('Slogan: *The bot of all the bots...the bot of the bots!* So! Now that we are done with the formalities, let us begin!'.format(ctx.message.server.name))
        await channel.send('Honourable mentions: Mutxnts & Wiki ~ Without you guys, this could not have happened.'.format(ctx.message.server.name))
        await channel.send('Made and scripted by Enderxcthz#1181 All rights reserved©.'.format(ctx.message.server.name))
        await channel.send('Do "_introduction" to begin! I am allllll yours! (Totally 100% not gei :sweat_smile:)'.format(ctx.message.server.name))
   

        
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
    await bot.say("You kicked us {}, Now we kick you :pensive:".format(user.mention))
    await bot.kick(user)

@bot.command(pass_context=True)
async def version(ctx):
    await bot.say ("Current Bot version is: `Unofficial, Still early access.`")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("You broke the rules {}, now get banned fool! :scream:".format(user.mention))
    await bot.ban(user)

@bot.command(pass_context=True)
async def unban(ctx, user: discord.Member): 
    await bot.say("{} was unbanned successfully! Your welcome. :smile:".format(user.name))
    await bot.unban(user)

@bot.command(pass_context=True)
async def warn(ctx, user: discord.Member, *, reason: str=None):
    await bot.send_message(user, "You were warned for: **{}**, in the *{}* server. This will be added to your record.".format(reason, ctx.message.server.name))
    await bot.say("{} was warned successfully! ✅".format(user.mention))
    
    
@bot.command(pass_context=True)
async def roast(ctx, user: discord.Member):
    messages = ["You're an idiot {}! https://giphy.com/gifs/lulz-users-stans-1ofR3QioNy264"].format(user.mention), ["{} the only way you’ll ever get laid is if you crawl up a chicken’s ass and wait. https://giphy.com/gifs/fandor-movie-scene-film-stroszek-3oEdv5jk7miq98Jv0c"].format(user.mention), ["{} you’re so fat you could sell shade.https://giphy.com/gifs/WxDZ77xhPXf3i"].format(user.mention), ["Your family tree must be a cactus because everyone on it is a prick. https://giphy.com/gifs/cosplay-costume-final-fantasy-P6Pt8lZw7BiQo"].format(user.mention)
    await bot.say(random.choice(messages))
	
@bot.command(pass_context = True)
@commands.check(lambda ctx: ctx.message.author.id == '352461162819878912')
async def dm(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)


bot.remove_command('help')         

@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(ctx.message.author, 'You need help? Cash me outside, HOW ABOU- no im just kidding :persevere:')
    await bot.send_message(ctx.message.author, 'https://hastebin.com/jazipaxeke.vbs')
    await bot.say("{} Check your DM's! :white_check_mark:".format(ctx.message.author.mention))
    
@bot.command(pass_context=True)
@commands.check(lambda ctx: ctx.author.id == '352461162819878912')
async def shutdown(ctx):
    await bot.logout()
                
@bot.command(pass_context=True)
@commands.check(lambda ctx: ctx.message.author.id == '352461162819878912')
async def announce(ctx, *, message):
    await bot.say(message)

@bot.command(pass_context=True)
async def betatest(ctx):
	await bot.say('Congratulations {}! Check your DM\'s! :white_check_mark:'.format(ctx.message.author.mention))
	await bot.send_message(ctx.message.author, 'Thank you for deciding to be a BETA tester! :smiley:')
	await bot.send_message(ctx.message.author, 'Once You have added me to your server, you will automatically be added to the BETA record! This means you will get special perks in the future :ok_hand: :eyes:')
	await bot.send_message(ctx.message.author, 'https://hastebin.com/pejihetuho.pas Here we go {}! Your journey begins now! :thumbsup: :sparkling_heart:'.format(ctx.message.author.mention))
                

    

bot.run(os.environ["TOKEN"])
