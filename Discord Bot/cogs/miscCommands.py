import discord, json, asyncio, datetime
from aiohttp import ClientSession
from discord.ext import commands
from discord.ext.commands import Greedy


class mainCog(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(
            title="Otaku Realm Beta Website!",
            description="{}".format(
                "Website is created by Luv and is under construction"),
            url="https://pandacover.github.io/DiscordServer/Discord%20WebPage/",
            color=discord.Color(0x000000))
        embed.set_footer(text='Created by OR Dev team.')
        await asyncio.sleep(0.5)
        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        file = open("./json/channels.json", "r")
        data = json.load(file)
        if not str(ctx.guild.id) in data:
            await ctx.send(
                "Please set a log channel using `/set_logs #channel_name`")

        elif data[str(ctx.guild.id)]['suggestion'] == 0:
            await ctx.send(
                "Please set a Suggestion channel using `/set_suggest #channel_name`"
            )

        else:
            embed = discord.Embed(title="Suggestion by {}".format(ctx.author),
                                  description='{}'.format(suggestion),
                                  color=discord.Color(0xff0000))
            embed.set_author(name='{}'.format(ctx.author))
            embed.set_footer(text='Created by OR Dev Team.')
            file = open('./json/channels.json', 'r')
            data = json.load(file)
            channel_id = data[str(ctx.guild.id)]["suggestion"]
            await self.bot.get_channel(channel_id).send(embed=embed)
            await ctx.message.add_reaction(emoji="\U0001F44D")
            await asyncio.sleep(5)
            await ctx.message.delete()

    @commands.command()
    async def greetings(self, ctx, targets: Greedy[discord.Member]):
        embed = discord.Embed(
            title="Welcome New Member",
            description=
            "**We hope you enjoy your stay here!**\nSince you're new here I recommend you checking out the following channels listed below:\n- <#744601957347360768>\n- <#744612149300822066>\n*Thank you for joining the server!*",
            color=discord.Color(0x00ffff))
        embed.set_author(name="Staff Team")
        embed.set_footer(text="Developed by OR Dev Team.")
        for target in targets:
            embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if isinstance(message.channel, discord.DMChannel):
                if len(message.content) < 10:
                    await message.channel.send(
                        "Your query/report should be at least of 10 characters."
                    )
                else:
                    embed1 = discord.Embed(
                        color=discord.Color(0xa84300),
                        description=
                        "We have received your message. Please wait until our staff team reach you!"
                    )
                    embed1.set_author(name=message.author.name,
                                      icon_url=message.author.avatar_url)
                    embed2 = discord.Embed(title="Modmail",
                                           color=discord.Color(0xa84300),
                                           description=message.content,
                                           timestamp=datetime.datetime.utcnow)
                    embed2.set_author(name=message.author.name,
                                      icon_url=message.author.avatar_url)
                    await message.add_reaction(emoji="\U00002705")
                    await asyncio.sleep(1)
                    await message.channel.send(embed=embed1)
                    await self.bot.get_guild(756865168054681630).get_channel(
                        756865168499015684).send(embed=embed2)

    @commands.command()
    async def search(self, ctx, *, search=None):
        api_key="AIzaSyDwVYQrQ45qIzpHJ23qWDUCxZ46b_pBkVs"
        url=f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx=ccf6cea7f214e3d0c&q={search}'
        if search is not None:
            async with ClientSession() as session:
                async with session.get(url, headers={}) as r:
                    data = await r.json()
                    index=0
                    result=discord.Embed(color=discord.Color.green())
                    
                    while index < len(data):
                        result.add_field(name=f"Search Result {index+1}", value=f'[{data["items"][index]["title"]}]({data["items"][index]["link"]})', inline=False)
                        index += 1
                    result.add_field(name="Caution: Read before clicking any link.", value="The search is powered by `googlesearchapi` but neither they nor us will take any responsibilty for any kind of mishappening. Please click the link only if you trust `Google`. Learn more about [googlesearchapi here](https://developers.google.com/custom-search/docs/overview).")
                    result.set_footer(text="Powered by OR and googleapi.", icon_url=ctx.author.avatar_url)
                    result.set_author(name=f"Search result for {search}.", icon_url="https://bit.ly/3nesR3A")

                    await ctx.send(embed=result)
        else:
            await ctx.send('> Example: `/search Discord` to get details about term Discord.')


def setup(bot):
    bot.add_cog(mainCog(bot))
#AIzaSyDwVYQrQ45qIzpHJ23qWDUCxZ46b_pBkVs
