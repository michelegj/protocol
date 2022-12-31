import discord
from discord.ext import commands
import os 

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loaded = []
        self.unloaded = []
        self.slash = "\n"

        for filename in os.listdir('./cogs'):
            if filename.endswith('py'):
                self.loaded.append(f'cogs.{filename[:-3]}')
        for filename in os.listdir('./cmds'):
            if filename.endswith('py'):
                self.loaded.append(f'cmds.{filename[:-3]}')
    
    
    @commands.group(invoke_without_command=True)
    @commands.is_owner()
    async def cog(self, ctx):
        await ctx.send(
            "\n`cogs help menu"
            "\n- !cog list <l/u>"
            "\n- !cog reload <cog>"
            "\n- !cog load <cog>"
            "\n- !cog unload <cog>`"
            , delete_after=20)
        await ctx.message.delete()

    @cog.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            await self.bot.load_extension(f"{cog}")
        except Exception as e:
            await ctx.send(f"`[cogs] error: {type(e).__name__} - {e}`", delete_after=20)
        else:
            await ctx.send(f"`[cogs] loaded '{cog}' cog`", delete_after=20)
            try:
                self.loaded.append(cog)
                self.unloaded.remove(cog)
            except:
                print("error - load cogs")
        await ctx.message.delete()

    @cog.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            await self.bot.unload_extension(f"{cog}")
        except Exception as e:
            await ctx.send(f"`[cogs] error: {type(e).__name__} - {e}`", delete_after=20)
        else:
            await ctx.send(f"`[cogs] unloaded '{cog}' cog`", delete_after=20)
            try:
                self.loaded.append(cog)
                self.unloaded.remove(cog)
            except:
                print("error - unload cogs")
        await ctx.message.delete()

    @cog.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            await self.bot.unload_extension(f"{cog}")
            await self.bot.load_extension(f"{cog}")
        except Exception as e:
            await ctx.send(f"`[cogs] error: {type(e).__name__} - {e}`", delete_after=20)
        else:
            await ctx.send(f"`[cogs] reloaded '{cog}' cog`", delete_after=20)
        await ctx.message.delete()

    @cog.command()
    @commands.is_owner()
    async def list(self, ctx, check : str):
        if check == "l" or check == "loaded":
            if len(self.loaded) != 0:  
                await ctx.send(f"`[loaded cogs list]\n -{f'{self.slash} -'.join(map(str, self.loaded))}`", delete_after=20)
            else:
                await ctx.send(f"`[cogs] there are no loaded cogs`", delete_after=20)
        if check == "u" or check == "unloaded":
            if len(self.unloaded) != 0: 
                await ctx.send(f"`[unloaded cogs list]\n -{f'{self.slash} -'.join(map(str, self.unloaded))}`", delete_after=20)
            else:
                await ctx.send(f"`[cogs] there are no unloaded cogs`", delete_after=20)
        await ctx.message.delete()
        
async def setup(bot):
    await bot.add_cog(OwnerCog(bot))
