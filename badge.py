import nextcord
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption, Member
from nextcord.ui import Button, View, Select
from nextcord.ext import commands


intents = Intents.all()

intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.slash_command()
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello user !")











































bot.run("OTMwODIyOTQwNTkxODEyNjE5.GoW9Ja.2B3l2FtJ0Qr1_ALoek8a7ETNt_vj6fCvT3BB24")