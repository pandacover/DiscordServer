import discord, json, sqlite3
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title = "Otaku Realm Beta Website!", 
        description = "{}".format("https://pandacover.github.io/DiscordServer/Discord%20WebPage/html%20files/otaku.html"), 
        color = discord.Color(0x000000)
        )
        embed.set_footer(text = 'Created by OR Dev team.')
        await ctx.send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        embed = discord.Embed(title = "Suggestion by {}".format(ctx.author), description = '{}'.format(suggestion), color = discord.Color(0xff0000))
        embed.set_author(name = '{}'.format(ctx.author))
        embed.set_footer(text='Created by OR Dev Team.')
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channel_id = data["suggestion"]
        await self.bot.get_channel(channel_id).send(embed=embed)

    @commands.command()
    @commands.has_any_role('Admin', 'Moderator')
    async def set_suggest(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channels = str(channel_id)
        channels = channels.replace('<','').replace('#','').replace('>','')
        data["suggestion"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')

    @commands.command()
    async def help(self, ctx):
        embed1 = discord.Embed(title = "Miscellaneous Commands", description = "`help`: Need to see commands?\n`suggest`: Have suggestions for server?\n`website`: Check out our website!", color = discord.Color(0x00ffff))
        embed1.set_author(name = "Luv")
        embed1.set_footer(text = "Developed by OR Dev Team.")
        embed2 = discord.Embed(title = "", description = "`kick`: Someone's bugging the server? Yeet them.\n`ping`: Checkout the latency of the trashy bot!\n`purge`: Tired of deleting messages one by one? Well you know what to do!\n`set_log`: Set the log channel!\n`set_suggest`: Set the suggestion channel!", color = discord.Color(0xff0000))
        embed2.set_author(name = "Luv")
        embed2.set_footer(text = "Developed by OR Dev Team.")
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

    
    @commands.group(invoke_without_command=True)
    async def welcome(self, ctx):
        await ctx.send('Available Setup Commands: \nwelcome channel <#channel>\nwelcome text <message>')
    
    @welcome.command()
    async def channel(self, ctx, channel:discord.TextChannel):
        if ctx.message.author.guild_permissions.manage_messages:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT channel_id FROM main WHERE row = {1}')
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO main(guild_id, channel_id, row) VALUES(?,?,?)")
                val = (ctx.guild.id, channel.id, 1)
                await ctx.send(f"Channel has been set to {channel.mention}")
            
            elif result is not None:
                sql = ("UPDATE main  SET channel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f"Channel has been updated to {channel.mention}")
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
        
    @welcome.command()
    async def text(self, ctx, *, text):
        if ctx.message.author.guild_permissions.manage_messages:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT msg FROM main WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO main(guild_id, msg) VALUES(?,?)")
                val = (ctx.guild.id, text)
                await ctx.send(f"Message has been set to `{text}`")
            
            elif result is not None:
                sql = ("UPDATE main  SET msg = ? WHERE guild_id = ?")
                val = (text, ctx.guild.id)
                await ctx.send(f"Message has been updated to `{text}`")
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()   


def setup(bot):
    bot.add_cog(mainCog(bot))

