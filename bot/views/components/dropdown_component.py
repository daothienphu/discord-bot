import discord

class DropdownComponent(discord.ui.Select):
    def __init__(self, placeholder:str = None):
        super().__init__(placeholder=placeholder)

    def GetSelectedValue(self):
        return self.values