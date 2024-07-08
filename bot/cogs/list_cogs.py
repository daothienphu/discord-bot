from discord.ext import commands
import os

class ListCogs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cogs = []

    @commands.command()
    async def list_cogs(self, ctx):
        for filename in os.listdir('./bot/cogs'):
            if filename.endswith('.py'):
                self.cogs.append(filename[:-3])
            
        message = "Loaded cogs:\n  " + "\n  ".join(self.cogs)

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(ListCogs(bot))