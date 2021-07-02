import discord
from discord.ext import commands

## discord intents settings
intents = discord.Intents.default()
intents.members = True

# SETTINGS YOU NEED TO CHANGE
bot = commands.Bot(command_prefix='.', intents=intents)  # prefix
token = "YOUR TOKEN HERE"  # token
