import discord
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['clear'])
    @commands.has_any_role("-", "bar", "perms", "boss", "admin")
    async def purge(self, ctx, amount : int):
        if amount > 300:
            await ctx.send(f"`[protocol] limit of 300 messages exided`", delete_after=20)
        elif amount <= 300:
            await ctx.channel.purge(limit=amount+1)
            logChannel = self.bot.get_channel("channel id here")
            await logChannel.send(f"`[protocol] {ctx.author.name}#{ctx.author.discriminator} purged {amount} messages in {ctx.channel.name}`")
            await ctx.send(f"`[purge] removed {amount} messages - {round(self.bot.latency * 1000)}ms`", delete_after=20)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Purge(bot))