import discord
from discord.ext import commands
from utils.database import checks


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            status=discord.Status.idle, activity=discord.Game("_help")
        )
        print("We have logged in as {0.user}".format(self.bot))
        await checks.table_check()

def setup(bot):
    bot.add_cog(Ready(bot))
