import discord, json, asyncio
from aiohttp import request
from discord.ext import commands
from discord.ext.commands import Greedy

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title = "Otaku Realm Beta Website!", 
        description = "{}".format("Website is created by Luv and is under construction"), url = "https://pandacover.github.io/DiscordServer/Discord%20WebPage/" , 
        color = discord.Color(0x000000)
        )
        embed.set_footer(text = 'Created by OR Dev team.')
        await asyncio.sleep(0.5)
        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        embed = discord.Embed(title = "Suggestion by {}".format(ctx.author), description = '{}'.format(suggestion), color = discord.Color(0xff0000))
        embed.set_author(name = '{}'.format(ctx.author))
        embed.set_footer(text='Created by OR Dev Team.')
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channel_id = data["suggestion"]
        await self.bot.get_channel(channel_id).send(embed=embed)
        await ctx.message.add_reaction(emoji = "\U0001F44D")
        await asyncio.sleep(5)
        await ctx.message.delete()

    @commands.command()
    @commands.has_any_role('Owner', 'Moderators')
    async def set_suggest(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channels = str(channel_id)
        channels = channels.replace('<','').replace('#','').replace('>','')
        data["suggestion"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
      async with ctx.channel.typing():
        embed1 = discord.Embed(title = "Miscellaneous Commands", description = "`help`: Need to see commands?\n`suggest`: Have suggestions for server?\n`website`: Check out our website!\n`greetings <@user>`: Welcome a new member!\n`fun` : Fun commands! Type `/help fun`.", color = discord.Color(0x00ffff))
        embed1.set_author(name = "Luv")
        embed1.set_footer(text = "Developed by OR Dev Team.")
        embed2 = discord.Embed(title = "", description = "`kick`: Someone's bugging the server? Yeet them.\n`ping`: Checkout the latency of the trashy bot!\n`purge`: Tired of deleting messages one by one? Well you know what to do!\n`set_log`: Set the log channel!\n`set_suggest`: Set the suggestion channel!", color = discord.Color(0xff0000))
        embed2.set_author(name = "Luv")
        embed2.set_footer(text = "Developed by OR Dev Team.")
        await asyncio.sleep(0.5)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
      await asyncio.sleep(3)
      await ctx.message.delete()

    @help.command()
    async def fun(self, ctx):
      embed=discord.Embed(color=discord.Color(0x00C78C),
      description="`hug` : Hug someone, because why not!\n`pat` : Pat the head. Yeah, just like that!\n`kiss(under construction)` : Wanna give a kiss? Sure, it's free!\n`tickle(under construction)` : Make them laugh until they cry!\n`slap(under construction)` : Serious damage. Speech 0, Destruction 100!\n`cat` : Daily does of cats!\n`dog` : Daily does of dogs!")
      embed.set_author(name="All the fun commands are listed below:")
      await ctx.send(embed=embed)
      await asyncio.sleep(3)
      await ctx.message.delete()

    @commands.command()
    async def greetings(self, ctx, targets: Greedy[discord.Member]):
      embed = discord.Embed(title="Welcome New Member", 
      description="**We hope you enjoy your stay here!**\nSince you're new here I recommend you checking out the following channels listed below:\n- <#744601957347360768>\n- <#744612149300822066>\n*Thank you for joining the server!*", color = discord.Color(0x00ffff))
      embed.set_author(name="Staff Team")
      embed.set_footer(text="Developed by OR Dev Team.")
      for target in targets:
        embed.set_thumbnail(url=target.avatar_url)
      await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(mainCog(bot))

