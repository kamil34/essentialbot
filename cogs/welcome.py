import discord
from discord.ext import commands


class Greetings(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.system_channel:
            message = discord.Embed(
                title="Hello there!",
                description="Welcome and hello <@{}> to our wonderful Discord community!".format(member.id),
                color=0x0066ff
            )
            await member.guild.system_channel.send(embed=message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.system_channel:
            message = discord.Embed(
                title="See ya!",
                description="<@{}>, we feel sorry for leaving us. We wish you the best for the future.".format(member.id),
                color=0x0066ff
            )
            await member.guild.system_channel.send(embed=message)


def setup(client):
    client.add_cog(Greetings(client))