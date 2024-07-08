import os
from discord.ext import commands

class BotCogLoader():
    def __init__(self, bot: commands.Bot):
        self._bot = bot
        self._cogs = [
            'bot.cogs.default',
            'bot.cogs.list_cogs',
        ]

    async def LoadExtensions(self, manualLoad: bool) -> None:
        """
        Load the cogs into the Discord bot.

        manualLoad: Whether to load the mannually defined cogs or load any cogs in the ./bot/cogs/ folder.
        """
        if manualLoad:
            for cog in self._cogs:
                await self._bot.load_extension(cog)
        else:
            for filename in os.listdir('./bot/cogs'):
                if filename.endswith('.py'):
                    await self._bot.load_extension(f'bot.cogs.{filename[:-3]}')