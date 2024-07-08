from discord.ext import commands
from discord import app_commands
import discord
from bot.views.blank_view import BlankView
from bot.views.components.dropdown_component import DropdownComponent
from bot.views.components.button_component import ButtonComponent

class LobbyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # @commands.command()
    # async def sync(self, ctx) -> None:
    #     fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    #     await ctx.send(f"Synced {len(fmt)} commands.")

    @app_commands.command(name='ask', description="Answer a question")
    async def start_lobby(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message("The fuck you want me to answer? Your mom?")

    @app_commands.command(name='say_fuck_yeah', description='Says fuck yeah')
    async def cheer(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fuck yeahhh")

    @app_commands.command(name='start', description="Start some shit")
    async def start(self, interaction: discord.Interaction):
        async def dropdownCallback(interaction):
            selectedValue = dropdown.GetSelectedValue()
            await interaction.response.edit_message(content=f"Selected option: {selectedValue[0]}")
        
        async def buttonCallback(interaction):
            selectedValue = dropdown.GetSelectedValue()
            await interaction.response.send_message(f"Option {selectedValue[0]} started.")

        dropdown = DropdownComponent()
        dropdown.add_option(label="O1", description="D1")
        dropdown.add_option(label="O2", description="D2")
        dropdown.add_option(label="O3", description="D3")      
        dropdown.callback = dropdownCallback
        
        confirmButton = ButtonComponent(label="Confirm", style=discord.ButtonStyle.grey)
        confirmButton.callback = buttonCallback
        
        viewModel = BlankView()
        viewModel.add_item(dropdown)
        viewModel.add_item(confirmButton)
    
        await interaction.response.send_message(content="Select some shit", view=viewModel)

async def setup(bot):
    await bot.add_cog(LobbyCog(bot))