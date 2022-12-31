import discord
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fun"))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def status(self, ctx, *message : str):
        if len(message) <= 15:
            await ctx.send(f"`[protocol] changed status msg to: "+"{}".format(" ".join(message))+"`", delete_after=30)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="{}".format(" ".join(message))))
        else:
            await ctx.send("`[protocol] limit of 15 chars exceeded!`", delete_after=12)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Ready(bot))
