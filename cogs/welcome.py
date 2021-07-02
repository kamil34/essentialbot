import discord
from discord.ext import commands


class Greetings(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.system_channel:
            message = discord.Embed(
                title="Hello there!",
                description=f"Welcome and hello {member.mention} to our wonderful Discord community!",
                color=0x0066ff
            )
            await member.guild.system_channel.send(embed=message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.system_channel:
            message = discord.Embed(
                title="See ya!",
                description=f"{member.mention}, we feel sorry for leaving us. We wish you the best for the future.",
                color=0x0066ff
            )
            await member.guild.system_channel.send(embed=message)


def setup(client):
    client.add_cog(Greetings(client))
