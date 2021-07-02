import discord
from discord.ext import commands
import datetime

datetime = datetime.datetime.now()
date = datetime.strftime("%m/%d/%Y")
clock = (datetime.strftime("%H:%M:%S %p").replace('AM', 'a.m.').replace('PM', 'p.m.'))


class Time(commands.Cog):
    @commands.command()
    @commands.guild_only()
    async def time(self, ctx):
        # await ctx.send('Current date is: {}'.format(date))
        # await ctx.send('Current time is: {}'.format(clock))
        message = discord.Embed(
            title="The time information",
            description="The current server time is: {}\nThe current server date is: {}.".format(clock, date),
            color=0x0066ff
        )
        await ctx.send(embed=message)


def setup(client):
    client.add_cog(Time(client))
