import discord , random
from discord.ext import commands
import asyncio
from utils.database import checks, functions

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx, *args):
        await checks.user_check(ctx.author.id)
        bet = 1
        heads = ["h","heads","head","H"]
        tails = ["t","tail","tails","T"]
        if len(args) > 2:
            return await ctx.send(f"❗Invalid arguments **{ctx.author.name}**|Please include the betting amount and the choice[optional]. ")
        if args:
            for amt in args:
                if amt.isdigit():
                    bet = int(amt)
                    break
            for choi in args:
                if choi.lower() in tails:
                    choice = "Tails"
                elif choi.lower() in heads:
                    choice = "Head"
                else:
                    choice = random.choice(['Tails','Head'])
        else:
            choice = random.choice(['Tails','Head'])

        
        win_condition = random.choice(['Tails','Head'])
        win_amount = bet*2
       
        if bet < 1: await ctx.send(f"**{ctx.author.name}** you can't bet that...")
        else:
            if await functions.check_balance(ctx.author.id) <bet:
               await ctx.send(f"**{ctx.author.name}** you don't even have that much chigs... " )
            else: 
            
                message=await ctx.send(f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins... <a:cf:939070721504706572>")
                if choice==win_condition:
                   await asyncio.sleep(2)
                   await message.edit(content=f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins...and you won {win_amount} <:chigs:937640062332571699> !! ")
                   await functions.add_balance(ctx.author.id,bet)
            
                if choice!=win_condition:
                   await asyncio.sleep(2)
                   await message.edit(content=f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins...and you lost it...")
                   await functions.remove_balance(ctx.author.id,bet)




    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["rd"])
    async def rolldice(self, ctx):
        htembed = discord.Embed(title="__ROLLING A DICE__ 🎲", color=ctx.author.color)
        htembed.add_field(name="And you got:", value=str(random.randint(1, 6)))
        await ctx.reply(embed=htembed)


def setup(bot):
    bot.add_cog(Gamble(bot))
