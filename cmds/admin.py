import discord
import random
from discord.ext import commands

class OwnerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['say'])
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, channel : int, *args):
        tempChannel = self.bot.get_channel(channel)
        await tempChannel.send("{}".format(" ".join(args)))
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, reason=None):
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"`[protocol] you've successfully kicked " 
            + f"{str(member.name).lower()}#{member.discriminator}`", delete_after=10)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"`[protocol] you've successfully banned " 
            + f"{str(member.name).lower()}#{member.discriminator}`", delete_after=10)
        await ctx.message.delete()
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, id : int):
        member = await self.bot.fetch_user(id)
        await ctx.guild.unban(member)
        await ctx.send(f"`[protocol] you've successfully unbanned " 
            + f"{str(member.name).lower()}#{member.discriminator}`", delete_after=10)
        await ctx.message.delete()

    @commands.command(aliases=['rank', 'group'])
    @commands.has_permissions(administrator=True)
    async def role(self, ctx, member : discord.Member, role : discord.Role):
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"`[protocol] you've given {str(role.name).lower()} role to " 
                + f"{str(member.name).lower()}#{member.discriminator}`", delete_after=10)
        elif role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"`[protocol] you've removed {str(role.name).lower()} role from " 
                + f"{str(member.name).lower()}#{member.discriminator}`", delete_after=10)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(OwnerCommand(bot))