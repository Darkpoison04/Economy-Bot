from discord import guild, Spotify
from discord.ext import commands
import discord
import json


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @commands.command()
    async def prefix(self, ctx, *, prefix):

        with open(r"./utils/resources/prefixes.json") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
        await ctx.send(f"Guild prefix set to '{prefix}' .")

        with open(r"./utils/resources/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
            
def setup(bot):
    bot.add_cog(Utility(bot))
