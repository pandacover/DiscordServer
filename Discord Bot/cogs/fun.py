import discord, asyncio, json, random
from aiohttp import request, ClientSession
from discord.ext import commands


class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member: discord.User = None):
        URL = "https://some-random-api.ml/animu/hug"
        async with ctx.channel.typing():
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    if member is not None:
                        embed = discord.Embed(
                            color=discord.Color(0x1abc9c),
                            description=
                            f"**{ctx.message.author.mention} hugged {member.mention}!!**"
                        )
                        embed.set_image(url=data["link"])
                        await ctx.send(embed=embed)
                    elif member is None:
                        embed = discord.Embed(
                            color=discord.Color(0x1abc9c),
                            description=
                            f"**{ctx.message.author.mention} hugged themself!! Why so lonely?**"
                        )
                        embed.set_image(url=data["link"])
                        embed.set_footer(text="Created by OR Dev.")
                        await asyncio.sleep(1)
                        await ctx.send(embed=embed)

                else:
                    await ctx.send("Uh-oh! Stinky!!")
            await asyncio.sleep(3)
            await ctx.message.delete()

    @commands.command()
    async def pat(self, ctx, member: discord.User = None):
        URL = "https://some-random-api.ml/animu/pat"
        async with ctx.channel.typing():
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    if member is not None:
                        embed = discord.Embed(
                            color=discord.Color(0x1abc9c),
                            description=
                            f"**{ctx.message.author.mention} pats {member.mention}. There there.**"
                        )
                        embed.set_image(url=data["link"])
                        await ctx.send(embed=embed)
                    elif member is None:
                        embed = discord.Embed(
                            color=discord.Color(0x1abc9c),
                            description=
                            f"**{ctx.message.author.mention} pats themself. Why so lonely?**"
                        )
                        embed.set_image(url=data["link"])
                        embed.set_footer(text="Created by OR Dev.")
                        await asyncio.sleep(1)
                        await ctx.send(embed=embed)

                else:
                    await ctx.send("Uh-oh! Stinky!!")
            await asyncio.sleep(3)
            await ctx.message.delete()

    @commands.command()
    async def tickle(self, ctx, member: discord.Member = None):
        file = open("./json/fun.json", "r")
        data = json.load(file)
        async with ctx.channel.typing():
            if member is not None:
                embed = discord.Embed(
                    color=discord.Color(0x1abc9c),
                    description=
                    f"**{ctx.author.mention} started tickling {member.mention}.Tickle them until they cry!**"
                )
            elif member is None:
                embed = discord.Embed(
                    color=discord.Color(0x1abc9c),
                    description=
                    f"**{ctx.author.mention} started tickling themself. That's illegal!**"
                )
            embed.set_image(url=random.choice(data["tickle"]))
            embed.set_footer(text="Created by OR Dev.")
            await asyncio.sleep(1)
            await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        file = open("./json/fun.json")
        data = json.load(file)
        async with ctx.channel.typing():
            if member is not None:
                embed = discord.Embed(
                    color=discord.Color(0x1abc9c),
                    description=
                    f"{ctx.author.mention} slapped {member.mention}. Lol, destroyed in seconds!"
                )
            elif member is None:
                embed = discord.Embed(
                    color=discord.Color(0x1abc9c),
                    description=
                    f"{ctx.author.mention} slapped themself. Self abuse? Not very good."
                )
            embed.set_image(url=random.choice(data["slap"]))
            embed.set_footer(text="Created by OR Dev.")
            await asyncio.sleep(1)
            await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command(aliases=['pup', 'puppy'])
    async def dog(self, ctx):
        fact = ''
        img = ''
        async with ctx.channel.typing():
            URL = "https://some-random-api.ml/img/dog"
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    img = data['link']
                else:
                    ctx.send(response.status)
                URL = "https://some-random-api.ml/facts/dog"
                async with request("GET", URL, headers={}) as response:
                    if response.status == 200:
                        data = await response.json()
                        fact = data['fact']
                    else:
                        ctx.send(response.status)

                embed1 = discord.Embed(
                    title=f"{ctx.author.name} did you know?",
                    description=f"{fact}",
                    color=discord.Color(0x00ffff))
                embed2 = discord.Embed(color=discord.Color(0x00ffff))
                embed2.set_footer(text='Created by OR Dev Team.')
                embed2.set_image(url=img)
                await asyncio.sleep(1)
                await ctx.send(embed=embed1)
                await ctx.send(embed=embed2)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command(aliases=['neko', 'kitty'])
    async def cat(self, ctx):
        fact_url = ''
        imageUrl = ''
        async with ctx.channel.typing():
            URL = "https://some-random-api.ml/facts/cat"
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    fact_url = data["fact"]
                else:
                    ctx.send(f'{response.status}!')
                URL = "https://some-random-api.ml/img/cat"
                async with request("GET", URL, headers={}) as response:
                    if response.status == 200:
                        data = await response.json()
                        imageUrl = data["link"]
                    else:
                        ctx.send(f'{response.status}!')

                embed1 = discord.Embed(
                    title=f"{ctx.author.name} did you know?",
                    description=f"{fact_url}",
                    color=discord.Color(0x00ffff))
                embed2 = discord.Embed(color=discord.Color(0x00ffff))
                embed2.set_footer(text='Created by OR Dev Team.')
                embed2.set_image(url=imageUrl)
                await asyncio.sleep(1)
                await ctx.send(embed=embed1)
                await ctx.send(embed=embed2)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command(
        name="Meme",
        aliases=["meme", "memes"],
        description="Sends meme to the channel the command was invoked in.")
    async def memes(self, ctx):
        url = "https://some-random-api.ml/meme"
        async with ctx.channel.typing():
            async with ClientSession() as session:
                async with session.get(url, headers={}) as response:
                    data = await response.json()
                    meme = discord.Embed(color=discord.Color.red())
                    meme.set_image(url=data["image"])
                    meme.set_footer(text=f"Caption: {data['caption']}")
                    await ctx.send(embed=meme)

    @commands.command()
    async def dadjoke(self, ctx):
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        async with ctx.channel.typing():
            async with ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    data = await response.json()
                    dadJoke = discord.Embed(color=discord.Color.green(),
                                            description=data["joke"])
                    dadJoke.set_author(name=self.bot.user.name,
                                       icon_url=self.bot.user.avatar_url)
                    dadJoke.set_footer(
                        text=
                        "Powered by OR DEV and https://icanhazdadjoke.com/.")
                    await ctx.send(embed=dadJoke)
                    await asyncio.sleep(3)
                    await ctx.send(f"{ctx.author.mention} was it funny?")


def setup(bot):
    bot.add_cog(mainCog(bot))