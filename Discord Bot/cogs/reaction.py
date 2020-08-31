import discord, asyncio, random, json
from discord.ext import commands
from discord.ext.commands import has_permissions, bot_has_permissions, Greedy

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        file = open('./json/channels.json')
        data = json.load(file)
        channel_id = data["suggestion"]
        if message.channel.id == channel_id:
            if message.author == self.bot.user:
                await message.add_reaction(emoji = "\U00002705")
                await message.add_reaction(emoji = "\U0000274E")

        query_channel = 749311952819585124
        if message.channel.id == query_channel and message.author != self.bot.user:
            await message.channel.send("<@&747462559485001898>")
            


def setup(bot):
    bot.add_cog(mainCog(bot))
