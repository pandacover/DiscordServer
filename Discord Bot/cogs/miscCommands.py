import discord, json
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title = "Otaku Realm Beta Website!", 
        description = "Website is still under construction!", 
        color = discord.Color(0x000000),
        url = " ")
        embed.set_footer(text = 'Created by OR Dev team.')
        await ctx.send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        embed = discord.Embed(title = "Suggestion by {}".format(ctx.author), description = '{}'.format(suggestion), color = discord.Color(0xff0000))
        embed.set_author(name = '{}'.format(ctx.author))
        embed.set_footer(text='Created by OR Dev Team.')
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channel_id = data["suggestion"]
        await self.bot.get_channel(channel_id).send(embed=embed)

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def set_suggest(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channels = str(channel_id)
        channels = channels.replace('<','').replace('#','').replace('>','')
        data["suggestion"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')

    @commands.command()
    async def help(self, ctx):
        embed1 = discord.Embed(title = "Miscellaneous Commands", description = "`help`: Need to see commands?\n`suggest`: Have suggestions for server?\n`website`: Check out our website!", color = discord.Color(0x00ffff))
        embed1.set_author(name = "Luv")
        embed1.set_footer(text = "Developed by OR Dev Team.")
        embed2 = discord.Embed(title = "", description = "`kick`: Someone's bugging the server? Yeet them.\n`ping`: Checkout the latency of the trashy bot!\n`purge`: Tired of deleting messages one by one? Well you know what to do!\n`set_log`: Set the log channel!\n`set_suggest`: Set the suggestion channel!", color = discord.Color(0xff0000))
        embed2.set_author(name = "Luv")
        embed2.set_footer(text = "Developed by OR Dev Team.")
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

def setup(bot):
    bot.add_cog(mainCog(bot))

