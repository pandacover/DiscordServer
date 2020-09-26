import discord, json, asyncio
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Greedy


class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send_log(self, ctx, message):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channel = data["logs"]
        embed = discord.Embed(title='Admin Command Log',
                              description='{}'.format(message),
                              color=discord.Color(0xff0000))
        embed.set_footer(text='Developed by OR Dev Team.')
        await self.bot.get_channel(channel).send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Bot Latency",
            description=f'{round(self.bot.latency * 1000)}ms',
            color=discord.Color(0xff0000))
        embed.set_footer(text='Created by OR Dev Team.')
        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    @commands.has_any_role('Moderators')
    async def purge(self, ctx, limit=1):
        await ctx.message.channel.purge(limit=int(limit) + 1)
        await self.send_log(
            ctx.author,
            'Purge command was used by {} to purge {} messages'.format(
                ctx.author, limit))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,
                   ctx,
                   targets: Greedy[discord.Member],
                   *,
                   reason: Optional[str] = "No reason provided!"):
        if not len(targets):
            await ctx.send('Please enter a valid username!')
        else:
            for target in targets:
                if target != ctx.author:
                    await target.kick(reason=reason)
                    await self.send_log(
                        'Kick command was used by{}\nTo kick{}.\nReason: {}'.
                        format(ctx.author, target, reason))
                else:
                    await ctx.send('You cannot kick yourself!')
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    @commands.has_any_role('Moderators')
    async def set_logs(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        channels = str(channel_id)
        channels = channels.replace('<', '').replace('#', '').replace('>', '')
        data["logs"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def rules(self, ctx):
        guild = self.bot.get_guild(756865168054681630)
        serverRules = discord.Embed(
            title="Otaku Realm Server Rules",
            color=discord.Color.red(),
            description=
            "• These are the general rules for the **OTAKU REALM** community.\n• Please read [Discord TOS](https://discord.com/terms).\n• Report in <#758631131607334917> and mention <@&747462559485001898> if you see someone breaking the following __rules listed below__."
        )
        serverRules.add_field(
            name="1. Be respectful to everyone.",
            value="Do not show rudeness towards someone, that shit's bad.",
            inline=False)
        serverRules.add_field(
            name="2. Discord Names and Avatar should be appropriate.",
            value=
            "We're a SFW community, and that's what we would expect from you too.",
            inline=False)
        serverRules.add_field(
            name="3. Do not spam.",
            value=
            "No spam of any kind will be tolerated. Instant mute is the punishment.",
            inline=False)
        serverRules.add_field(
            name="4. Do not advertise w/o permission.",
            value="Annoying invite links are not allowed in the chat.",
            inline=False)
        serverRules.add_field(
            name="5. Do not try to find loop holes in the rules.",
            value=
            "All the rules are supposed to be understand by people having common sense.",
            inline=False)
        serverRules.add_field(
            name="5. Do not mention/ping staff w/o any legitimate reason.",
            value="We also have work to do, so please don't ping w/o reason.",
            inline=False)
        serverRules.add_field(
            name="6. Controversial/sensitive topics are not allowed.",
            value=
            "This includes political topics too. Please refrain from bringing any trouble to yourself.",
            inline=False)
        serverRules.set_thumbnail(url=guild.icon_url)
        serverRules.set_footer(
            text=
            f"Note: Server rules are made by {guild.owner.name} and are subjected to changes anytime."
        )
        serverRules.set_image(
            url="https://media.giphy.com/media/qd5HiIDqq2pNFeqjpV/giphy.gif")
        await ctx.send(embed=serverRules)


def setup(bot):
    bot.add_cog(mainCog(bot))
