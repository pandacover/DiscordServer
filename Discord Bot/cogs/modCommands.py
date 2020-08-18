import discord
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = "Bot Latency", description = f'{round(self.bot.latency * 1000)}ms', color = discord.Color(0xff0000))
        embed.set_footer(text = 'Created by OR Dev Team.')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def purge(self, ctx, limit=1):
        await ctx.message.channel.purge(limit=int(limit) + 1)

def setup(bot):
    bot.add_cog(mainCog(bot))
