import discord
from discord.ext import commands

### BOT SETTINGS
import config.settings

### FEATURES
import commands.time # time command

config.settings.bot.run(config.settings.token)
