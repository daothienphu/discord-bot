import discord
import random
from discord.ext import commands
from art.art_loader import ArtPathLoader
from utils.name_formatter import NameFormatter

class BonkCog(commands.Cog):
    def __init__(self, bot):
        self._bot = bot

    @commands.command(name='bonk')
    async def bonk(self, ctx, username: str):
        author = ctx.message.author

        member = None
        nameFormatter = NameFormatter()
        formatedUsername = nameFormatter.FormatName(username)
        for m in ctx.guild.members:
            formatedMemberName = nameFormatter.FormatName(m.name)
            if formatedMemberName.startswith(formatedUsername) or formatedMemberName.endswith(formatedUsername):
                member = m
                break
    
        #imagePaths = ArtPathLoader.LoadArtByNamesInFolder("bonkCog", ["bonk1", "bonk2", "bonk3", "bonk4", "bonk5"])
        #randomimage = imagePaths[random.randint(0, len(imagePaths) - 1)]        
        #print(imagePaths)
        #print(randomimage)
        
        if member:
            await ctx.send(f"{author.mention} bonked {member.mention}!")
        else:
            await ctx.send(f"{author.mention} bonked {username}!")

async def setup(bot):
    await bot.add_cog(BonkCog(bot))
