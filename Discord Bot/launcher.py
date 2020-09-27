import discord, os
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="/",
                   status=discord.Status.online,
                   activity=discord.Activity(type=discord.ActivityType.playing,
                                             name="/help"))
bot.remove_command('help')
load_dotenv()


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


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 756482714839810108:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if payload.emoji.name == 'tsuakasa':
            role = discord.utils.get(guild.roles, name="He/Him")
        elif payload.emoji.name == 'nene':
            role = discord.utils.get(guild.roles, name="She/Her")
        elif payload.emoji.name == 'shibaheart':
            role = discord.utils.get(guild.roles, name="They/Them")

    if role is not None:
        member = discord.utils.find(lambda m: m.id == payload.user_id,
                                    guild.members)
        if member is not None:
            await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 756482714839810108:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if payload.emoji.name == 'tsuakasa':
            role = discord.utils.get(guild.roles, name="He/Him")
        elif payload.emoji.name == 'nene':
            role = discord.utils.get(guild.roles, name="She/Her")
        elif payload.emoji.name == 'shibaheart':
            role = discord.utils.get(guild.roles, name="They/Them")

    if role is not None:
        member = discord.utils.find(lambda m: m.id == payload.user_id,
                                    guild.members)
        if member is not None:
            await member.remove_roles(role)


bot.load_extension("cogs.modCommands")
bot.load_extension("cogs.miscCommands")
bot.load_extension("cogs.reaction")
bot.load_extension("cogs.updates")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.profile")
bot.load_extension("cogs.play")
bot.load_extension("cogs.help")
bot.load_extension("cogs.bugs")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
