import discord
from discord.ext import commands
import datetime

datetime = datetime.datetime.now()
date = datetime.strftime("%m/%d/%Y")
clock = (datetime.strftime("%l:%M %p").replace('AM', 'a.m.').replace('PM', 'p.m.'))


class Time(commands.Cog):
    @commands.command()
    @commands.guild_only()
    async def time(self, ctx):
        message = discord.Embed(
            title="The time information",
            description=f"The current server time is: {clock}\nThe current server date is: {date}.",
            color=0x0066ff
        )
        await ctx.send(embed=message)


def setup(client):
    client.add_cog(Time(client))
