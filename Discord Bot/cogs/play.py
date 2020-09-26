import asyncio, json, discord, random
from aiohttp import ClientSession
from discord.ext import commands


class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        url = f"https://8ball.delegator.com/magic/JSON/{question}"
        async with ctx.channel.typing():
            async with ClientSession() as session:
                async with session.get(url, headers={}) as response:
                    data = await response.json()
                    ballResponse = discord.Embed(color=discord.Color.green())
                    ballResponse.add_field(name=":8ball: says:",
                                           value=data["magic"]["answer"],
                                           inline=False)
                    ballResponse.set_footer(
                        text=
                        "Powered by Otaku Realm and https://8ball.delegator.com/."
                    )
                    print(data)
                    await ctx.send(embed=ballResponse)

    @commands.command()
    async def rps(self, ctx, *, input=None):
        rps = ["rock", "paper", "scissors"]
        output = random.choice(rps)
        async with ctx.channel.typing():
            if input is not None:
                input = input.lower()
                if input == "rock":
                    if output == "rock":
                        await ctx.send(f"**{output}**, draw.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, you lose.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, you win.")

                elif input == "paper":
                    if output == "rock":
                        await ctx.send(f"**{output}**, you win.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, draw.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, you lose.")

                elif input == "scissors":
                    if output == "rock":
                        await ctx.send(f"**{output}**, you lose.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, you win.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, draw.")

                else:
                    await ctx.send(
                        f"Wrong input. What the hell is **{input}** anyway!?")
            elif input is None:
                await ctx.send("What do you choose?")
                input = await self.bot.wait_for(
                    'message',
                    check=lambda message: message.author == ctx.author)
                input = str(input.content).lower()
                if input == "rock":
                    if output == "rock":
                        await ctx.send(f"**{output}**, draw.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, you lose.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, you win.")

                elif input == "paper":
                    if output == "rock":
                        await ctx.send(f"**{output}**, you win.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, draw.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, you lose.")

                elif input == "scissors":
                    if output == "rock":
                        await ctx.send(f"**{output}**, you lose.")
                    elif output == "paper":
                        await ctx.send(f"**{output}**, you win.")
                    elif output == "scissors":
                        await ctx.send(f"**{output}**, draw.")

                else:
                    await ctx.send(
                        f"Wrong input. What the hell is **{input}** anyway!?")


def setup(bot):
    bot.add_cog(mainCog(bot))


#sjK1m2M3oX5AR502gPSg6ibKIEdRiWzAyPKko2gh