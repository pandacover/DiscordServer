import discord, asyncio
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        async with ctx.channel.typing():
            embed = discord.Embed(color=discord.Color(0x00ffff))
            embed.set_author(name="Command list.")
            embed.add_field(name="utility",
                            value="Utility commands. `/help utility`",
                            inline=False)
            embed.add_field(name="fun",
                            value="Fun commands. `/help fun`",
                            inline=False)
            embed.add_field(name="games",
                            value="Games command. `/help games`",
                            inline=False)
            embed.set_footer(text="Created by OR Dev.")
            embed.add_field(name="mod",
                            value="Mod commands. `/help mod`, inline=False")
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)

    @help.command()
    async def utility(self, ctx):
        utilityHelp = discord.Embed(color=discord.Color.green())
        utilityHelp.add_field(name="suggest",
                              value="Send some suggestions for the server.",
                              inline=True)
        utilityHelp.add_field(name="status",
                              value="Check the bot status.",
                              inline=True)
        utilityHelp.add_field(name="ping",
                              value="Check the bot's latency",
                              inline=True)
        utilityHelp.add_field(name="website",
                              value="Check the server's official website.",
                              inline=True)
        utilityHelp.add_field(
            name="greetings",
            value="Welcome a new member. Make sure to mention them.",
            inline=True)
        utilityHelp.add_field(name="reportbug",
                              value="Report a bug to the help server.",
                              inline=True)
        utilityHelp.add_field(name="purge",
                              value="*Delete a certain number of messages.",
                              inline=True)
        utilityHelp.add_field(name="set_logs",
                              value="*Set the log channel.",
                              inline=True)
        utilityHelp.add_field(name="set_suggest",
                              value="*Set the suggestion channel.",
                              inline=True)
        utilityHelp.set_footer(
            text=
            "* implies to commands that can be only used by guild Moderators.")
        await asyncio.sleep(0.5)
        await ctx.send(embed=utilityHelp)

    @help.command()
    async def mod(self, ctx):
        modHelp = discord.Embed(color=discord.Color(0xff0000))
        modHelp.add_field(
            name="kick",
            value="Kick a guild member. Make sure to add the reason.",
            inline=True)
        modHelp.add_field(
            name="ban",
            value=
            "Ban a guild member. Make sure to add reason.[Under construction]",
            inline=True)
        modHelp.add_field(
            name="mute",
            value=
            "Mute a guild member. Make sure to add reason.[Under construction]",
            inline=True)
        modHelp.add_field(
            name="answerbug",
            value=
            "Answer the bug reprot if not answered to.\nHow to use:\n`/answerbug guild_id channel_id your_answer`.",
            inline=True)
        await asyncio.sleep(0.5)
        await ctx.send(embed=modHelp)

    @help.command()
    async def fun(self, ctx):
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name="hug",
                        value="Hug someone, because why not!",
                        inline=True)
        embed.add_field(name="pat",
                        value="Pat the head. Yeah, just like that!",
                        inline=True)
        embed.add_field(name="kiss",
                        value="Wanna give a kiss? Sure, it's free!",
                        inline=True)
        embed.add_field(name="tickle",
                        value="Make them laugh until they cry!",
                        inline=True)
        embed.add_field(name="slap",
                        value="Serious damage. Speech 0, Destruction 100!",
                        inline=True)
        embed.add_field(name="dog", value="Daily does of dogs!", inline=True)
        embed.add_field(name="cat", value="Daily does of cats!", inline=True)
        embed.add_field(name="memes",
                        value="Check out some memes coz why not.",
                        inline=True)
        embed.add_field(name="dadjoke",
                        value="Not funny at all but.",
                        inline=True)
        embed.set_author(name="All the fun commands are listed below:")
        await asyncio.sleep(0.5)
        await ctx.send(embed=embed)

    @help.command()
    async def games(self, ctx):
        game = discord.Embed(color=discord.Color.green())
        game.add_field(name="rps",
                       value="Play rock paper scissors with our sensei.",
                       inline=True)
        game.add_field(name="8ball",
                       value="Ask 8ball to predict something.",
                       inline=True)
        game.set_author(name="All the games command are listed below:")
        await asyncio.sleep(0.5)
        await ctx.send(embed=game)


def setup(bot):
    bot.add_cog(Help(bot))
