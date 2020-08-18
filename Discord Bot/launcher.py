import discord, json, random
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
        await ctx.send('Command not found!')
    
    elif hasattr(exc, "original"):
        raise exc.original

@bot.command()
async def echo(ctx, *, content):
    await ctx.send(content)

bot.load_extension("cogs.modCommands") 
bot.load_extension("cogs.miscCommands")   
bot.run(token)