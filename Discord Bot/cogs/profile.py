import discord, asyncio
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def profile(self, ctx, member:discord.Member=None):
        monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        async with ctx.channel.typing():
            embed = discord.Embed(color=discord.Color(0xf1c40f))
            if member is not None and not member.bot:
              embed.set_author(name=member.name, icon_url=member.avatar_url)
              embed.add_field(name="User ID", value=member.id, inline=False)
              embed.add_field(name="Top Role", value=member.top_role, inline=False)
              embed.add_field(name="Status", value=member.status, inline=False)
              embed.add_field(name="Joined Server At", value=f"{monthList[member.joined_at.month-1]} {member.joined_at.day}, {member.joined_at.year}", inline=False)
              embed.add_field(name="Joined Discord At", value=f"{monthList[member.created_at.month-1]} {member.created_at.day}, {member.created_at.year}", inline=False)
      
            elif member is None and not ctx.author.bot:
              embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
              embed.add_field(name="User ID", value=ctx.author.id, inline=False)
              embed.add_field(name="Top Role", value=ctx.author.top_role, inline=False)
              embed.add_field(name="Status", value=ctx.author.status, inline=False)
              embed.add_field(name="Joined Server At", value=f"{monthList[ctx.author.joined_at.month-1]} {ctx.author.joined_at.day}, {ctx.author.joined_at.year}", inline=False)
              embed.add_field(name="Joined Discord At", value=f"{monthList[ctx.author.created_at.month-1]} {ctx.author.created_at.day}, {ctx.author.created_at.year}", inline=False)  
            
            if ctx.author.bot:
              embed.add_field(name="Stupid!", value="Bot don't need profile!")
            embed.set_thumbnail(url=ctx.author.guild.icon_url)
            embed.set_footer(text = 'Created by OR Dev Team.')
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()
    
    @commands.command()
    async def serverinfo(self, ctx):
        monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        async with ctx.channel.typing():
            rolesList = 0
            emojiList = 0
            memberList = 0
            humanList = 0
            guild = ctx.author.guild
            embed = discord.Embed(color=discord.Color(0x7289da))
            embed.set_author(name=f"{guild.name}'s information.",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=guild.icon_url)
            embed.add_field(name="Owner:", value=guild.owner)
            embed.add_field(name="Region:", value=guild.region)
            for role in guild.roles:
                rolesList = rolesList + 1
            embed.add_field(name="Roles:", value=rolesList)
            for emoji in guild.emojis:
                emojiList = emojiList + 1
            embed.add_field(name="Emoji:", value=emojiList)
            for member in guild.members:
                memberList = memberList + 1
                if not member.bot:
                    humanList = humanList + 1
            embed.add_field(name="Total Members:", value=memberList)
            embed.add_field(name="Total Humans:", value=humanList)
            embed.add_field(name="Created at:", value=f"{monthList[guild.created_at.month-1]} {guild.created_at.day}, {guild.created_at.year}")
            embed.set_footer(text = 'Created by OR Dev Team.')
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(mainCog(bot))