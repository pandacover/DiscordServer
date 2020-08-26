import discord, json, random, sqlite3
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix = '/')
bot.remove_command('help')

file = open('./json/token.json', 'r')
data  = json.load(file)
token = data["token"]

@bot.event
async def on_ready():
    print('Logged in!')

@bot.event
async def on_error(err, *args, **kwargs):
    if err == "on_command_error":
        await args[0].send('Something went wrong!')

    raise

@bot.event
async def on_command_error(ctx, exc):
    if isinstance(exc, CommandNotFound):
        flag = 0
        list1 = ['website','echo', 'purge','ping', 'set_logs', 'set_suggest', 'kick', 'suggest']
        list2 = []
        music = ['/play', '/join', '/disconnect', '/dc']
        for word in ctx.message.content:
            list2.append(word)
        if ctx.message.content not in music:
            for words in list1:
                if list2[1] == words[:1]:
                    await ctx.send('Did you mean `/' + words + '`?')
                    flag = 1
                    break
        else:
            flag = 1
          
        if flag == 0:
            await ctx.send('Command not found!')

    elif hasattr(exc, "original"):
        raise exc.original

@bot.command()
async def echo(ctx, *, content):
    await ctx.send(content)

bot.load_extension("cogs.modCommands") 
bot.load_extension("cogs.miscCommands")   
bot.load_extension("cogs.reaction")
bot.load_extension("cogs.updates")
bot.run(token)