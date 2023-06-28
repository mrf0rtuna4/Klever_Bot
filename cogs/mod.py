import disnake
from disnake.ext import commands

class Mod(commands.Cog, name = "🛠️ Модерация", description = "Страх хадилки брадилки"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = "ban", description = "Забанить кого-то")
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)

    async def ban(self, ctx, user: disnake.User, *, reason = None):

        try:
            await ctx.guild.ban(user,reason = reason)
            await ctx.message.add_reaction("✅")
            if ctx.guild and ctx.guild.get_channel(0):
                embed = disnake.Embed(
                    title = ":hammer: Выдана блокировка",
                    description = f"Пользователь {user.mention} был успешно заблокирован на сервере по причине: **{reason}**",
                    color = 0xFF0600
                )
                embed.set_footer(text = f"Выдал: {ctx.author}")
                await ctx.guild.get_channel(0).send(embed=embed)
            else:
                embed = disnake.Embed(
                    title = "✅ Успешно",
                    description = f"Пользователь {user.mention} успешно забанен по причине **{reason}**!",
                    color = 0x00FF00
                )
                await ctx.reply(embed = embed)
        except disnake.Forbidden:
            await ctx.reply("У меня нет прав заблокировать пользователя.")


def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))
