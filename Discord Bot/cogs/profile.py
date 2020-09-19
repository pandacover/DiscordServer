import discord
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member:discord.Member=None):
        async with ctx.channel.typing():
            roleList = ""
            flag = -1
            embed = discord.Embed(color=discord.Color(0xf1c40f))
            if member is not None and not member.bot:
                embed.set_author(name=member.name, icon_url=member.avatar_url)
                embed.add_field(name="User ID", value=member.id, inline=False)
                for role in member.roles:
                    roleList = roleList + role.name
                embed.add_field(name="Roles", value=roleList, inline=False)
                embed.add_field(name="Status", value=member.status, inline=False)
                embed.add_field(name="Joined Server At", value=member.joined_at, inline=False)
                embed.add_field(name="Joined Discord At", value=member.created_at, inline=False)
                flag = 0
            elif member is None and not ctx.author.bot:
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name="User ID", value=ctx.author.id, inline=False)
                for role in ctx.author.roles:
                    roleList = roleList + role.name
                embed.add_field(name="Roles", value=roleList, inline=False)
                embed.add_field(name="Status", value=ctx.author.status, inline=False)
                embed.add_field(name="Joined Server At", value=ctx.author.joined_at, inline=False)
                embed.add_field(name="Joined Discord At", value=ctx.author.created_at, inline=False)
                flag = 0    
            
            if flag == -1:
                embed.add_field(name="Stupid!", value="Bot don't need profile!")
            embed.set_thumbnail(url=ctx.author.guild.icon_url)
            embed.set_footer(text = 'Created by OR Dev Team.')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def serverinfo(self, ctx):
        async with ctx.channel.typing():
            rolesList = ""
            emojiList = ""
            memberList = 0
            humanList = 0
            guild = ctx.author.guild
            embed = discord.Embed(color=discord.Color(0x7289da))
            embed.set_author(name=f"{guild.name}'s information.",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=guild.icon_url)
            embed.add_field(name="Owner:", value=guild.owner)
            embed.add_field(name="Region:", value=guild.region)
            for role in guild.roles:
                if role.name != "@everyone":
                    rolesList = rolesList + role.mention + " "
                else:
                    rolesList = rolesList + role.name + " "
            embed.add_field(name="Roles:", value=rolesList)
            for emoji in guild.emojis:
                emojiList = emojiList + f"<:{emoji.name}:{emoji.id}>"
            embed.add_field(name="Emoji:", value=emojiList)
            for member in guild.members:
                memberList = memberList + 1
                if not member.bot:
                    humanList = humanList + 1
            embed.add_field(name="Total Members:", value=memberList)
            embed.add_field(name="Total Humans:", value=humanList)
            embed.add_field(name="Created at:", value=guild.created_at)
            embed.set_footer(text = 'Created by OR Dev Team.')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mainCog(bot))