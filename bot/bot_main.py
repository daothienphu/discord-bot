import discord
from discord.ext import commands
from bot.bot_cog_loader import BotCogLoader

class Bot():
    def __init__(self):
        intents = discord.Intents.all()
        self._bot = commands.Bot(command_prefix=".", intents=intents)

    async def RunBot(self, BOT_TOKEN: str, LOG_CHANNEL_ID: str, GUILD_ID: str) -> None:
        """Run the bot with the given BOT_TOKEN, and outputs some logs into the channel with the given LOG_CHANNEL_ID.
        
        BOT_TOKEN: The bot token, acquired at https://discord.com/developers/applications -> [Bot Name] -> Bot tab -> TOKEN.
        LOG_CHANNEL_ID: The ID of channel that the bot should output its logs into, acquired by right-clicking on the channel and selecting [Copy Channel ID] (Developer Mode required).
        GUILD_ID: 
        """

        await BotCogLoader(self._bot).LoadExtensions(manualLoad=False)

        await self._bot.start(BOT_TOKEN)