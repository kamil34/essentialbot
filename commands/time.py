import discord
from discord.ext import commands
import datetime
import config.settings

datetime = datetime.datetime.now()
date = datetime.strftime("%m/%d/%Y")
clock = (datetime.strftime("%H:%M:%S %p").replace('AM', 'a.m.').replace('PM', 'p.m.'))


@config.settings.bot.command()
async def time(ctx):
    #await ctx.send('Current date is: {}'.format(date))
    #await ctx.send('Current time is: {}'.format(clock))
    message = discord.Embed(
        title="The time information",
        description="The current server time is: {} \n The current server date is: {}.".format(clock, date),
        color=0x0066ff
    )
    await ctx.send(embed=message)