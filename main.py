import asyncio
from bot.bot_main import Bot
from utils.credentials_importer import CredentialsImporter

credentials = CredentialsImporter().GetCredentials('credentials')
BOT_TOKEN = credentials["TOKEN"]
LOG_CHANNEL_ID = credentials["LOG_CHANNEL_ID"]
GUILD_ID = credentials["GUILD_ID"]

async def main(): 
    await Bot().RunBot(BOT_TOKEN, LOG_CHANNEL_ID, GUILD_ID)

asyncio.run(main())