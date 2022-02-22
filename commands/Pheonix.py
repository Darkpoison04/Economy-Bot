import discord, json, psutil, os
from discord.ext import commands
tera = {
    "fields": [
        {"inline": False, "name": "> Actions ", "value": "```tickle ```"},
        {"inline": False, "name": "> Fun ", "value": "```rolldice , coinflip ```"},
        {
            "inline": False,
            "name": "> Animals ",
            "value": "```cat , dog , bird , fox , kangaroo , koala , panda , raccoon ```",
        },
        {
            "inline": False,
            "name": "> Moderation",
            "value": "```kick , ban , mute , unmute , clear```",
        },
        {
            "inline": False,
            "name": "> Music",
            "value": "```join , play , skip , disconnect , queue ```",
        },
        {
            "inline": False,
            "name": "> Utility",
            "value": "```botinfo , userinfo , serverinfo , avatar , ping , prefix , calculate , spotify ```",
        },
    ],
    "color": 16760333,
    "type": "rich",
    "title": "<a:heartshade:855323491522576404> HELP PANEL",
}



class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["cmd"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def help_command(self, ctx):
        prefix = await self.bot.get_prefix(ctx.message)
        helpembed = discord.Embed.from_dict(tera)
        helpembed.set_footer(
            text=f"Requested by {ctx.author.name} || Prefix for this server is -> {prefix[2]}",
            icon_url=ctx.author.avatar_url,
        )
        msg = await ctx.send(embed=helpembed)
        await msg.add_reaction("✨")

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def ping(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return
        em = discord.Embed(color=0xFFBE0D)
        em.title = "Pong!"
        em.description = f":green_circle: {round(self.bot.latency * 1000)} ms"
        await ctx.reply(embed=em)

    @commands.command(aliases=["botinfo"])
    async def stats(self, ctx):
        ram_aval = psutil.virtual_memory().available * 1e-09
        ram_total = psutil.virtual_memory().total * 1e-09
        process = psutil.Process(os.getpid())

        embedve = discord.Embed(
            title="<a:heartshade:855323491522576404> Chiggy Stats",
            color=ctx.author.color,
        )
        embedve.add_field(
            name="**Bot Latency**",
            value=f"Bot latency - {round(self.bot.latency * 1000)}ms",
            inline=False,
        )
        embedve.add_field(
            name="**Hosting Stats**",
            value=f"""Cpu usage- {psutil.cpu_percent(1)}%

        Number of Cores - {psutil.cpu_count()}
        Number of Threads- {psutil.cpu_count(logical=False)}

        Ram Usage - {round(process.memory_info().rss * 0.000001, 2)} MB
        Total ram- {round(ram_total, 2)} GB
        Available Ram - {round(ram_aval, 2)} GB""",
        )

        await ctx.send(embed=embedve)


def setup(bot):
    bot.add_cog(Main(bot))
