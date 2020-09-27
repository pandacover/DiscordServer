import discord, asyncio
from discord.ext import commands


class bugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 300.0, type=commands.BucketType.guild)
    async def reportbug(self, ctx, *, bug):
        bugReport = discord.Embed(color=discord.Color.red())
        bugReport.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
        bugReport.add_field(name="Guild member",
                            value=ctx.author,
                            inline=False)
        bugReport.add_field(name="Channel ID",
                            value=ctx.channel.id,
                            inline=False)
        bugReport.add_field(name="Bug Reported", value=bug, inline=False)
        bugReport.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
        bugReport.set_footer(text="Created by OR Dev Team.")
        for guild in self.bot.guilds:
            if guild.id == 744590909852876810:
                await guild.get_channel(759377020936650792).send(
                    embed=bugReport)
        await ctx.message.add_reaction(emoji="\U00002705")
        await asyncio.sleep(5)
        embed = discord.Embed(color=discord.Color.red(),
                              description="We have received your bug report!")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Created by OR Dev Team.")
        await ctx.send(embed=embed)

    @commands.command()
    async def answerbug(self, ctx, guild_id, channel_id, *, answer):
        answerReport = discord.Embed(color=discord.Color.green(),
                                     description=answer)
        answerReport.set_author(name=ctx.author.name,
                                icon_url=ctx.author.avatar_url)
        answerReport.set_footer(text="Created by OR Dev Team.")
        await ctx.send("Do you want to send the message? Yes or No.")
        msg = await self.bot.wait_for(
            'message', check=lambda message: ctx.author == message.author)
        if str(msg.content).lower() == "yes":
            for guild in self.bot.guilds:
                if guild.id == int(guild_id):
                    await guild.get_channel(int(channel_id)
                                            ).send(embed=answerReport)
            await ctx.message.add_reaction(emoji="\U00002705")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=3)
            await ctx.send(embed=answerReport)
        elif str(msg.content).lower() == "no":
            await ctx.send("Message was not sent.")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=4)
        else:
            await ctx.send(
                f"You were supposed to answer Yes or No not `{msg.content}`. Please run the whole command again."
            )
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=4)


def setup(bot):
    bot.add_cog(bugCog(bot))
