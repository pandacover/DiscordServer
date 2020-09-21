import discord, asyncio, requests, json, random
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
            embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.message.author.mention} hugged {member.mention}!!**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          elif member is None:
            embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.message.author.mention} hugged themself!! Why so lonely?**")
            embed.set_image(url=data["link"])
            embed.set_footer(text="Created by OR Dev.")
            await asyncio.sleep(1)
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
            embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.message.author.mention} pats {member.mention}. There there.**")
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
          elif member is None:
            embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.message.author.mention} pats themself. Why so lonely?**")
            embed.set_image(url=data["link"])
            embed.set_footer(text="Created by OR Dev.")
            await asyncio.sleep(1)
            await ctx.send(embed=embed)
          
        else:
          await ctx.send("Uh-oh! Stinky!!")
      await asyncio.sleep(3)
      await ctx.message.delete()
  
  @commands.command()
  async def tickle(self, ctx, member:discord.Member=None):
    file = open("./json/fun.json", "r")
    data = json.load(file)
    async with ctx.channel.typing():
      if member is not None:
        embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.author.mention} started tickling {member.mention}.Tickle them until they cry!**")
      elif member is None:
        embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"**{ctx.author.mention} started tickling themself. That's illegal!**")
      embed.set_image(url=random.choice(data["tickle"]))
      embed.set_footer(text="Created by OR Dev.")
      await asyncio.sleep(1)
      await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await ctx.message.delete()


  @commands.command()
  async def slap(self, ctx, member:discord.Member=None):
    file = open("./json/fun.json")
    data = json.load(file)
    async with ctx.channel.typing():
      if member is not None:
        embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"{ctx.author.mention} slapped {member.mention}. Lol, destroyed in seconds!")
      elif member is None:
        embed = discord.Embed(color=discord.Color(0x1abc9c), description=f"{ctx.author.mention} slapped themself. Self abuse? Not very good.")
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
      URL="https://some-random-api.ml/img/dog"
      async with request("GET", URL, headers={}) as response:
        if response.status == 200:
          data = await response.json()
          img = data['link']
        else:
          ctx.send(response.status)
        URL="https://some-random-api.ml/facts/dog"
        async with request("GET", URL, headers={}) as response:
          if response.status == 200:
            data = await response.json()
            fact = data['fact']
          else:
            ctx.send(response.status)

        embed1 = discord.Embed(title = f"{ctx.author.name} did you know?", description = f"{fact}", color = discord.Color(0x00ffff))
        embed2 = discord.Embed(color = discord.Color(0x00ffff))
        embed2.set_footer(text = 'Created by OR Dev Team.')
        embed2.set_image(url = img)
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
      async with request("GET", URL, headers = {}) as response:
        if response.status == 200:
          data = await response.json()
          fact_url = data["fact"]
        else:
          ctx.send(f'{response.status}!')
        URL = "https://some-random-api.ml/img/cat"
        async with request("GET", URL, headers = {}) as response:
          if response.status == 200:
            data = await response.json()
            imageUrl = data["link"]
          else:
            ctx.send(f'{response.status}!')

        embed1 = discord.Embed(title = f"{ctx.author.name} did you know?", description = f"{fact_url}", color = discord.Color(0x00ffff))
        embed2 = discord.Embed(color = discord.Color(0x00ffff))
        embed2.set_footer(text = 'Created by OR Dev Team.')
        embed2.set_image(url = imageUrl)
        await asyncio.sleep(1)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
    await asyncio.sleep(3)
    await ctx.message.delete()

  @commands.command()
  async def rps(self, ctx, *, input):
    rps = ["rock", "paper", "scissors"]
    output = random.choice(rps)
    input = input.lower()
    async with ctx.channel.typing():
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
        await ctx.send(f"Wrong input. What the hell is **{input}** anyway!?")



def setup(bot):
    bot.add_cog(mainCog(bot)) 
