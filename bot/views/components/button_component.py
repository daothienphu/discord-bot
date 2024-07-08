import discord 
from discord import ButtonStyle

class ButtonComponent(discord.ui.Button):
    def __init__(self, *, style: discord.ButtonStyle = ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None):
        super().__init__(style=style, label=label, disabled=disabled, url=url, emoji=emoji)