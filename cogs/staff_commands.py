import discord
from discord.ext import commands


class Staff_commands(commands.Cog):
    @commands.command()
    @commands.guild_only()
    # @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason=None):
        if reason != "None":
            await member.kick(reason=reason)
            message = discord.Embed(
                title="Ugh... Someone literally overdid something!",
                description=f"{member.mention} has been kicked with the following reason: {reason}",
                color=0xff0000
            )
            await member.guild.system_channel.send(embed=message)
        else:
            message = discord.Embed(
                title="Ugh... Someone literally overdid something!",
                description=f"{member.mention} has been kicked with no reason. What a surprise!",
                color=0xff0000
            )
            await member.kick(reason=reason)
            await member.guild.system_channel.send(embed=message)

    @kick.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Sorry, I couldn't find the user.")


def setup(client):
    client.add_cog(Staff_commands(client))
