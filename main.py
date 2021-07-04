import discord
from discord.ext import commands

### BOT SETTINGS
from config.settings import prefix, token

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

### FEATURES
bot.load_extension("cogs.welcome")  # welcome event
bot.load_extension("cogs.time")  # time command
bot.load_extension("cogs.staff_commands")  # staff commands

bot.run(token)
