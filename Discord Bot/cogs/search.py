import discord, json, requests, asyncio
from discord.ext import commands
from aiohttp import ClientSession

class searchCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    def createEmbed(self, data):
        index=0
        emojiNumber = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
        embed=discord.Embed(color=discord.Color.orange())
        embed.set_author(name="AL search result", icon_url="https://imgur.com/rqXGU3P.png")
        while index < len(data):
            embed.add_field(name=f'{emojiNumber[index]} {data[index]["title"]["romaji"]}', value=data[index]["title"]["native"], inline=False)
            index += 1
        return embed

    @commands.command()
    async def anime(self, ctx, *, anime, page:int=1):
        url='https://graphql.anilist.co'
        emojiList = ["\U000023EE","\U0000274E","\U000023ED"]
        query = '''
               query ($id: Int, $page: Int, $perPage: Int, $search: String) {
                        Page (page: $page, perPage: $perPage) {
                            media (id: $id, search: $search) {
                                id
                                title {
                                    romaji
                                    english
                                    native
                                }
                            }
                        }
                    }
                '''
        variables = {
                'search':anime,
                'page':page,
                'perPage':9
        }
        response = requests.post(url, json={'query': query, 'variables': variables})
        data = response.json()
        embed = self.createEmbed(data["data"]["Page"]["media"])
        print(data)
        if page == 1:
            embed.set_footer(text="Type `next` or `close`.", icon_url=ctx.author.avatar_url)
        elif page > 1:
            embed.set_footer(text="Type `next`, `previous` or `close`.", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
        try:
            msg = await self.bot.wait_for('message', timeout=60.0,check=lambda message: message.author==ctx.author)

            if msg.content.lower() == "next":
                await ctx.channel.purge(limit=2)
                await self.anime(ctx, anime=anime, page=page+1)
                
            elif page > 1 and msg.content.lower() == "previous":
                await ctx.channel.purge(limit=2)
                await self.anime(ctx, anime=anime, page=page-1)
                
            elif msg.content.lower() == "close":
                await ctx.channel.purge(limit=2)
            
            else:
                await ctx.channel.purge(limit=2)
                await ctx.send("> Next time enter a correct input. Closed due to wrong input.")

        except asyncio.TimeoutError:    
            await ctx.channel.purge(limit=1)
            await ctx.send("> What a dip shit!")

       
    @commands.command()
    async def urban(self, ctx, *, query):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': "115fc09313mshd9c24e1a7ab2a73p136f87jsn55e74e86f499"
        }
        querystring = {"term":query}

        async with ctx.channel.typing():
            async with ClientSession() as session:
                async with session.get(url, headers=headers, params=querystring) as r:
                    data = await r.json()
                    data = data["list"][0]
                    meaning=discord.Embed(color=discord.Color.orange(), description=data["definition"])
                    meaning.set_author(name=f'{data["word"]} by {data["author"]}', icon_url='https://androidgozar.com/wp-content/uploads/2019/05/urban-dictionary-icon-.png')
                    meaning.add_field(name="Example(s)", value=data["example"], inline=False)
                    meaning.add_field(name="Thumb rating", value=f':thumbsup:{data["thumbs_up"]} | :thumbsdown:{data["thumbs_down"]}', inline=False)
                    meaning.add_field(name="Link", value=data["permalink"], inline=False)
                    meaning.set_footer(text="https://www.urbandictionary.com", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=meaning)


def setup(bot):
    bot.add_cog(searchCog(bot))