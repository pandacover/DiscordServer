import discord, json, asyncio
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Greedy


class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit=1):
        file = open("./json/channels.json", "r")
        data = json.load(file)
        if not str(ctx.guild.id) in data:
            await ctx.send(
                "Please set a log channel using `/set_logs #channel_name`")

        elif data[str(ctx.guild.id)]['logs'] == 0:
            await ctx.send(
                "Please set a log channel using `/set_logs #channel_name`")

        else:
            await ctx.message.channel.purge(limit=int(limit) + 1)
            await self.send_log(
                ctx.message,
                f"Purge command was used by {ctx.author} to purge {limit} messages"
            )

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,
                   ctx,
                   targets: Greedy[discord.Member],
                   *,
                   reason: Optional[str] = "No reason provided!"):
        file = open("./json/channels.json", "r")
        data = json.load(file)
        if str(ctx.guild.id) in data:
            if not len(targets):
                await ctx.send('Please enter a valid username!')
            else:
                for target in targets:
                    if target != ctx.author:
                        await target.kick(reason=reason)
                        await self.send_log(
                            ctx.message,
                            f'Kick command was used by{ctx.author}\nTo kick{target}.\nReason: {reason}'
                        )
                    else:
                        await ctx.send('You cannot kick yourself!')
            await asyncio.sleep(3)
            await ctx.message.delete()

        else:
            await ctx.send(
                "Please set a log channel using `/set_logs #channel_name`")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def set_logs(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)

        if not str(ctx.guild.id) in data:
            data[str(ctx.guild.id)] = {}
            data[str(ctx.guild.id)]['logs'] = 0
            data[str(ctx.guild.id)]['suggest'] = 0

        channels = str(channel_id)
        channels = channels.replace('<', '').replace('#', '').replace('>', '')
        data[str(ctx.guild.id)]["logs"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')
        await asyncio.sleep(3)
        await ctx.message.delete()

    @commands.Cog.listener()
    async def send_log(self, message, log):
        embed = discord.Embed(color=discord.Color.red(), description=log)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Created by OR Dev")
        with open("./json/channels.json", "r") as f:
            data = json.load(f)
        await message.guild.get_channel(data[str(message.guild.id)]["logs"]
                                        ).send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def rules(self, ctx):
        guild = self.bot.get_guild(744590909852876810)
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
            f"Note: Server rules and gif are made by {guild.owner.name}, please do not steal. Rules are subjected to changes anytime."
        )
        serverRules.set_image(
            url="https://media.giphy.com/media/qd5HiIDqq2pNFeqjpV/giphy.gif")
        await ctx.send(embed=serverRules)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def set_suggest(self, ctx, *, channel_id):
        file = open('./json/channels.json', 'r')
        data = json.load(file)
        if not str(ctx.guild.id) in data:
            data[str(ctx.guild.id)] = {}
            data[str(ctx.guild.id)]['logs'] = 0
            data[str(ctx.guild.id)]['suggestion'] = 0

        channels = str(channel_id)
        channels = channels.replace('<', '').replace('#', '').replace('>', '')
        data[str(ctx.guild.id)]["suggestion"] = int(channels)
        with open('./json/channels.json', 'w') as tf:
            json.dump(data, tf)
        await ctx.send('Channel set successfully!')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member=None, *, reason="no specific reason"):
        roleList = ctx.guild.roles
        if member is None:
            await ctx.send(f"{ctx.author} type `/mute @user_you_want_to_mute reason(optional but recommended)`.")
        for role in roleList:
            if role.name == "muted":
                await member.add_roles(role)
                await ctx.send(f"{member.mention} was muted by {ctx.author.mention} for **{reason}**.")
                await asyncio.sleep(1)
                await ctx.message.delete()
                return
        await ctx.guild.create_role(name="muted", permissions=discord.Permissions(permissions=0), color=discord.Color.default())
        await self.mute(ctx, member, reason=reason)
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member:discord.Member=None, *, reason="no specific reason"):
        if member is None:
            await ctx.send(f"{ctx.author} type `/unmute @user_you_want_to_unmute reason(optional but recommended)`.")
        for role in member.roles:
            if role.name == "muted":
                await member.remove_roles(role)
                await ctx.send(f"{member.mention} was unmuted by {ctx.author.mention} for **{reason}**.")
                return
        await ctx.send(f"{member.mention} is not muted!")
        await asyncio.sleep(1)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(mainCog(bot))