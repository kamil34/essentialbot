import discord
from discord.ext import commands
import datetime
import config.settings

get_time = datetime.datetime.now()
@config.settings.bot.command()
async def time(ctx):
    await ctx.send('Current time is: {}'.format(get_time))