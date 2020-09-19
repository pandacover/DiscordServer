import discord, asyncio
from aiohttp import request
from discord.ext import commands

class mainCog(commands.Cog):
  def __init__(self, bot):
    self.bot=bot

  @commands.command()
  async def hug(self, ctx, member:discord.User=None):
    URL="https://some-random-api.ml/animu/hug"
    async with ctx.channel.typing():
      async with request("GET", URL, headers={}) as response:
        if response.status == 200:
          data = await response.json()
          
          if member is not None:
            embed = discord.Embed(color=discord.Color(0x0BB5FF), description=f"**{ctx.message.author.mention} hugged {member.mention}!!**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          elif member is None:
            embed = discord.Embed(color=discord.Color(0x0BB5FF), description=f"**{ctx.message.author.mention} hugged themself!! Why so lonely?**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          
        else:
          await ctx.send("Uh-oh! Stinky!!")
      await asyncio.sleep(3)
      await ctx.message.delete()

  @commands.command()
  async def pat(self, ctx, member:discord.User=None):
    URL="https://some-random-api.ml/animu/pat"
    async with ctx.channel.typing():
      async with request("GET", URL, headers={}) as response:
        if response.status == 200:
          data = await response.json()
          
          if member is not None:
            embed = discord.Embed(color=discord.Color(0x0BB5FF), description=f"**{ctx.message.author.mention} pats {member.mention}. There there.**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          elif member is None:
            embed = discord.Embed(color=discord.Color(0x0BB5FF), description=f"**{ctx.message.author.mention} pats themself. Why so lonely?**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          
        else:
          await ctx.send("Uh-oh! Stinky!!")
      await asyncio.sleep(3)
      await ctx.message.delete()

def setup(bot):
    bot.add_cog(mainCog(bot)) 