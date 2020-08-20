import discord
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title = "Otaku Realm Beta Website!", 
        description = "Website is still under construction!", 
        color = discord.Color(0x000000),
        url = "")
        embed.set_footer(text = 'Created by OR Dev team.')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mainCog(bot))

