from discord.ext import commands
import utils.MessageProcessor as MessageProcessor
import requests,json


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel.type) == "private" or message.author.bot:
            return
        await MessageProcessor.react(self.bot, message)
        if "pheonix-ai" in message.channel.name:
           await MessageProcessor.react(self.bot, message)
           


def setup(bot):
    bot.add_cog(Messages(bot))
