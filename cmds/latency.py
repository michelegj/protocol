import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['ping'])
    async def latency(self, ctx):
        await ctx.send(f"`[protocol] network status: {round(self.bot.latency * 1000)}ms`", delete_after=30)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Ping(bot))