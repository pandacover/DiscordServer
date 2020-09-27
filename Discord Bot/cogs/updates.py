import discord
from discord.ext import commands


class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def updates(self, ctx, *, update):
        embed = discord.Embed(title="Otaku - 0.1v stable",
                              description=update,
                              color=discord.Color(0xff0000))
        embed.set_author(name="Dev Team")
        embed.set_footer(text="Developed by OR Dev Team.")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        channel = 746693072456253461
        await ctx.guild.get_channel(channel).send(embed=embed)
        await ctx.message.add_reaction(emoji="\U00002705")


def setup(bot):
    bot.add_cog(mainCog(bot))