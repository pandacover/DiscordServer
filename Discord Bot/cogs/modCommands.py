import discord, json, asyncio
from typing import Optional
from discord.ext import commands
from discord.ext.commands import has_permissions, bot_has_permissions, Greedy

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send_log(self, ctx, message):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channel = data["logs"]
        embed = discord.Embed(title = 'Admin Command Log', description = '{}'.format(message), color = discord.Color(0xff0000))
        embed.set_footer(text='Developed by OR Dev Team.')
        await self.bot.get_channel(channel).send(embed=embed) 

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = "Bot Latency", description = f'{round(self.bot.latency * 1000)}ms', color = discord.Color(0xff0000))
        embed.set_footer(text = 'Created by OR Dev Team.')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def purge(self, ctx, limit=1):
        await ctx.message.channel.purge(limit=int(limit) + 1)
        await self.send_log(ctx.author, 'Purge command was used by {} to purge {} messages'.format(ctx.author, limit))

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def kick(self, ctx, targets: Greedy[discord.Member], *, reason: Optional[str] = "No reason provided!"):
        if not len(targets):
            await ctx.send('Please enter a valid username!')
        else:
            for target in targets:
                    if target != ctx.author:
                        await target.kick(reason=reason)
                        await self.send_log(ctx.author, 'Kick command was used by{}\nTo kick{}'.format(ctx.author, target))
                    else:
                        await ctx.send('You cannot kick yourself!')

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def set_logs(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channels = str(channel_id)
        channels = channels.replace('<','').replace('#','').replace('>','')
        data["logs"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')    

def setup(bot):
    bot.add_cog(mainCog(bot))
