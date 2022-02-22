import discord , json
from discord.ext import commands
from utils.database import checks ,functions



class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['bal','balance'])
    async def cash(self, ctx ,user: discord.Member = None):
        if str(ctx.message.channel.type) == "private":
            return
        user = user or ctx.author
        uid = user.id
        await checks.user_check(int(uid))
        cash = await functions.check_balance(int(uid))

        await ctx.reply(f"<:chigs:937640062332571699> **{user.name}** currently has **{cash:,}** chigs.")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name='give',aliases=['send'])
    async def sendchigs(self,ctx,cash,user:discord.Member= None):
        if type(cash) is int:
           await checks.user_check(ctx.author.id)
       
           if cash is None or user is None : await ctx.send(f"❗Invalid arguments **{ctx.author.name}** |Please include cash and the user. ") 
           elif cash < 0: await ctx.send(f"**{ctx.author.name}** Well are you basically trying to rob **{user.name}** _tch tch_...")
           else:

            if await functions.check_balance(ctx.author.id) < cash:
                 await ctx.send(f"**{ctx.author.name}** you cannot send that much chigs... " )
            else:
                 await functions.add_balance(user.id,cash)
                 await functions.remove_balance(ctx.author.id,cash)
                 await ctx.send(f"**{ctx.author.name}** sent {cash} chigs <:chigs:937640062332571699> to **{user.name}**!")
        elif type(cash) is str:
            await ctx.send(f"**{ctx.author.name}** sent {cash} to **{user.name}**!")
        else: 
            await ctx.send(f"❗Invalid arguments **{ctx.author.name}** |Please include cash and the user. ")




def setup(bot):
    bot.add_cog(Bot(bot))
