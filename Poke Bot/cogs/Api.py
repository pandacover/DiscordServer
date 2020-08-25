import discord, json
from aiohttp import request
from random import randint
from discord.ext import commands
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk import Card

class mainCog(commands.Cog):
    def __init__(self, bot, response_dict = {}):
        self.bot = bot
        self.image_url = response_dict.get('imageUrl')
    


    @commands.command()
    async def meme(self, ctx):
        URL = "https://some-random-api.ml/meme"
        async with ctx.channel.typing():
            async with request("GET", URL, headers=[]) as response:
                if response.status == 200:
                    data = await response.json()
                    embed = discord.Embed(title = "", description = data["caption"], color = discord.Color(0x00ffff))
                    embed.set_footer(text = "Created by OR Dev Team.")
                    embed.set_image(url=data["image"])
                    embed.set_author(name = "Meme")
                    await ctx.send(embed=embed)
                
                else:
                    await ctx.send('API returned a {response.status} status.')

    @commands.command()
    async def card(self, ctx):
        url = Card.image_url
        async with ctx.channel.typing():
            embed = discord.Embed(title = "", description = '', color = discord.Color(0x00ffff))
            embed.set_footer(text = "Created by OR Dev Team.")
            embed.set_image(url=url)
            embed.set_author(name = "Meme")
            await ctx.send(embed=embed)   

    @commands.command()
    async def test(self, ctx):
        URL = "https://api.pokemontcg.io/v1/cards"
        async with ctx.channel.typing():
            async with request("GET", URL, headers = []) as response:
                if response.status == 200:
                    data = await response.json()
                    embed = discord.Embed(title = "", description = "", color = discord.Color(0x00ffff))
                    embed.set_footer(text = "Created by OR Dev Team.")
                    embed.set_image(url=data['cards'][0]['imageUrl'])
                    embed.set_author(name = "")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('API returned {response.status} status!')

    @commands.command()
    async def spawn(self, ctx):
        URL = "https://api.pokemontcg.io/v1/cards"
        async with ctx.channel.typing():
            async with request("GET", URL, headers=[]) as response:
                if response.status == 200:
                    data = await response.json()
                    flag = randint(0, 100)
                    title = data["cards"][flag]["name"]
                    embed = discord.Embed(title=title, description = '', color =  discord.Color(0x00ffff))
                    embed.set_author(name = "Luv")
                    embed.set_image(url = data["cards"][flag]["imageUrl"])
                    id = data["cards"][flag]["id"]
                    embed.set_footer(text = 'Created by OR Dev Team. id = {}'.format(id))
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(response.status)
                


def setup(bot):
    bot.add_cog(mainCog(bot))