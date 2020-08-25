import discord, sqlite3
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def update(self, ctx):
        embed = discord.Embed(
            title="Bot Updates", 
            color=discord.Color(0xff0000),
            description= "Available commands are:\n1: channel #channel_name\n2: announce"
        )
        embed.set_author(name="Luv")
        embed.set_footer(text="Developed by OR Dev Team.")
        await ctx.send(embed=embed)

    @update.command()
    async def channel(self, ctx, channel:discord.TextChannel):
        if ctx.message.author.id == ctx.guild.owner_id:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT channel_id FROM main WHERE row = {2}')
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO main(guild_id, channel_id, row) VALUES(?,?,?)")
                val = (ctx.guild.id, channel.id, 2)
                await ctx.send(f'Updates channel has been set to {channel.mention}')

            elif result is not None:
                sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f'Updates channel has been updated to {channel.mention}')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    @update.command()
    async def text(self, ctx, *, text):
        if ctx.message.author.id == ctx.guild.owner_id:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT msg FROM main WHERE row = {2}')
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO main(guild_id, msg, row) VALUES(?,?,?)")
                val = (ctx.guild.id, text, 2)
                await ctx.send(f"Updates text has been set to `{text}`")

            elif result is not None:
                sql = ("UPDATE main SET msg = ? WHERE guild_id = ?")
                val = (text, ctx.guild.id)
                await ctx.send(f"Updates text has been updated to `{text}`")
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

def setup(bot):
    bot.add_cog(mainCog(bot))