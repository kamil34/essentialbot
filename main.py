import discord
from discord.ext import commands

### BOT SETTINGS
from config.settings import bot as instance
from config.settings import token as token

### FEATURES
instance.load_extension("cogs.welcome")  # welcome event
instance.load_extension("cogs.time")  # time command

instance.run(token)
