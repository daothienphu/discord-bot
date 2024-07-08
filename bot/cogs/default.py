from discord.ext import commands
from datetime import datetime

class DefaultCog(commands.Cog):
    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{self._bot.user} is online at {currentTime}")
        try:
            synced = await self._bot.tree.sync()
            print(f"Synced {len(synced)} command(s).")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(DefaultCog(bot))