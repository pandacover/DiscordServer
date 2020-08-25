import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Online!')

bot.load_extension("cogs.Api")
token = 'NzQ0MDk2ODc4OTU3NjkwOTEw.XzeQOA.MVnT7pF5NHOhTEfs_FZGBQ3Ai3s'
bot.run(token)