from utils.singleton import BorgSingleton
from discord.ext import commands

class BotLogger(BorgSingleton):
    def __init__(self, bot: commands.Bot, LOG_CHANNEL_ID: str):
        self._bot = bot
        self._channelID = LOG_CHANNEL_ID

    async def Log(self, message):
        await self._bot.send(message)

    async def LogWarning(self, message):
        await self._bot.send(message)

    async def LogError(self, message):
        await self._bot.send(message)