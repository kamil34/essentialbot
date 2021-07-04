import discord
from discord.ext import commands


class StaffCommands(commands.Cog):
    @commands.command()
    @commands.guild_only()
    # @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason is not None:
            await member.kick(reason=reason)

            message = f"{member.mention} has been kicked with the following reason: {reason}"
            await member.guild.system_channel.send(embed=discord.Embed(
                title="Ugh... Someone in here literally overdid with something! What a shame!",
                description=message,
                color=0xff0000
            ))
        else:
            await member.kick(reason=reason)

            message = f"{member.mention} has been kicked with no reason. What a surprise!"
            await member.guild.system_channel.send(embed=discord.Embed(
                title="Ugh... Someone in here literally overdid with something! What a shame!",
                description=message,
                color=0xff0000
            ))

    @kick.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Sorry, I couldn't find the user.")


def setup(client):
    client.add_cog(StaffCommands(client))
